/* Author: Jeremey Larter
   CS3110 Project (The Bohr Model of an Atom)
   Purpose: To present a functional model of the Bohr Model as my final project to the class, utilizing the concepts learned throughout the semester.
 */

// Vertex shader program.
var VSHADER_SOURCE =
  'attribute vec4 a_Position;\n' +
  'attribute vec2 a_TexCoord;\n' +
  'attribute vec4 a_Color;\n' +
  'attribute vec4 a_Normal;\n' +
  // Flags used to toggle lighting being used in color, as well as textures.
  'attribute float a_Flag;\n' +
  'attribute float a_TexFlag;\n' +
  // Matrix for transformations.
  'uniform mat4 u_ModelMatrix;\n' +
  // Matrix for the camera position.
  'uniform mat4 u_ViewMatrix;\n' +
  // Matrix for the perspective projection.
  'uniform mat4 u_PerspectiveMatrix;\n' +
  // Matrix for normals.
  'uniform mat4 u_NormalMatrix;\n' +
  'uniform vec3 u_DiffuseLight;\n' +
  'uniform vec3 u_LightDirection;\n' +
  'uniform vec3 u_AmbientLight;\n' +
  'varying vec2 v_TexCoord;\n' +
  'varying vec4 v_Color;\n' +
  'varying float v_TexFlag;\n' +
  'void main() {\n' +
  '  gl_Position = u_PerspectiveMatrix * u_ViewMatrix * u_ModelMatrix * a_Position;\n' + // Essentially MVP * a_Position.
  '  v_TexCoord = a_TexCoord;\n' +
  '  v_TexFlag = a_TexFlag;\n' +
	 // Calculates the normal to be fit with a model matrix, and make it 1.0 in length.
  '  vec3 normal = normalize(vec3(u_NormalMatrix * a_Normal));\n' +
	 // Calculates world coordinates of the vertices.
  '  vec4 vertexPosition = u_ModelMatrix * a_Position;\n' +
	 // The dot product of the light direction and the normal.
  '  float nDotL = max(dot(u_LightDirection, normal), 0.0);\n' +
	 // Calculates the colors due to diffuse reflection.
  '  vec3 diffuse = u_DiffuseLight * a_Color.rgb * nDotL;\n' +
	 // Calculates the colors due to ambient reflection.
  '  vec3 ambient = u_AmbientLight * a_Color.rgb;\n' +
  // Shapes are affected by lighting (excited electrons are the exception) while lines are not and only use a set color.
  ' if (a_Flag==0.0)\n' +
  '  v_Color = vec4(diffuse + ambient, a_Color.a);\n' +
  ' else if (a_Flag==1.0)\n' +
  '  v_Color = vec4(0.4, 0.4, 0.4, 1.0);\n' + // Gray.
  ' else\n' +
  '  v_Color = vec4(1.0, 0.6, 0.3, 1.0);\n' + // Orange.
  '}\n';
  
// Fragment shader program.
var FSHADER_SOURCE =
  '#ifdef GL_ES\n' +
  'precision mediump float;\n' +
  '#endif\n' +
  'uniform sampler2D u_Sampler;\n' +
  // Varying variables are passed from the vertex shader.
  'varying vec2 v_TexCoord;\n' +
  'varying float v_TexFlag;\n' +
  'varying vec4 v_Color;\n' +
  'void main() {\n' +
  // Only the background uses textures.
  ' if (v_TexFlag==0.0)\n' +
  '  gl_FragColor = v_Color;\n' +
  ' else\n' +
  '  gl_FragColor = texture2D(u_Sampler, v_TexCoord);\n' +
  '}\n';

// Main function. Sets up the canvas, light source, event handler and animation, as well as initializing the shaders and storage locations.
function main() {
  // Retrieves the <canvas> element.
  var canvas = document.getElementById('webgl');
  // Gets the rendering context for WebGL.
  var gl = getWebGLContext(canvas);
  if (!gl) {
    console.log('Failed to get the rendering context for WebGL');
    return;
  }
  // Sets the canvas color and enable the depth test.
  gl.clearColor(0.05, 0.05, 0.05, 1.0); // Black.
  gl.enable(gl.DEPTH_TEST); // Prevents Z-fighting. Required to make lighting smooth.

  // Initializes the vertex and fragment shaders.
  if (!initShaders(gl, VSHADER_SOURCE, FSHADER_SOURCE)) {
    console.log('Failed to intialize shaders.');
    return;
  }
  
  // Initializes textures for the background.
  if (!initTextures(gl)) {
    console.log('Failed to intialize the texture.');
    return;
  }
  
  // Gets the storage location of the matrices.
  var u_ModelMatrix = gl.getUniformLocation(gl.program, 'u_ModelMatrix');
  var u_ViewMatrix = gl.getUniformLocation(gl.program, 'u_ViewMatrix');
  var u_PerspectiveMatrix = gl.getUniformLocation(gl.program, 'u_PerspectiveMatrix');
  var u_NormalMatrix = gl.getUniformLocation(gl.program, 'u_NormalMatrix');
  var u_DiffuseLight = gl.getUniformLocation(gl.program, 'u_DiffuseLight');
  var u_LightDirection = gl.getUniformLocation(gl.program, 'u_LightDirection');
  var u_AmbientLight = gl.getUniformLocation(gl.program, 'u_AmbientLight');
  if (!u_ModelMatrix || !u_ViewMatrix || !u_PerspectiveMatrix || !u_NormalMatrix || !u_DiffuseLight || !u_LightDirection || !u_AmbientLight) {
    console.log('Failed to get the storage location of the matrices');
    return;
  }
  
  // Sets the light color.
  gl.uniform3f(u_DiffuseLight, 0.8, 0.8, 0.8); // White.
  // Sets the light direction (in the world coordinate).
  var lightDirection = new Vector3([-6.0, 10.0, 7.0]);
  lightDirection.normalize(); // Normalize the elements in the array.
  gl.uniform3fv(u_LightDirection, lightDirection.elements);
  // Sets the ambient light.
  gl.uniform3f(u_AmbientLight, 0.2, 0.2, 0.2);
  
  // Registers the event handler to be called on key press.
  document.onkeydown = function(ev){ keydown(ev); };
  
  // Draws the scene and animates it.
  var currentAngle = 90.0; // Starting angle when the scene first loads.
  var tick = function() {
    currentAngle = animate(currentAngle);  // Updates the rotation angle at a calculated rate, making the animation appear smooth.
    draw(gl, currentAngle, u_ModelMatrix, u_ViewMatrix, u_PerspectiveMatrix, u_NormalMatrix);   // Draws the scene.
    requestAnimationFrame(tick, canvas);   // Requests that the browser calls tick.
  };
  tick();
}

// Calculates a new angle for when the scene is being animated.
var step = -60, backup = 0; // Initial speed and direction. Backup is used for pausing.
// Last time that this function was called.
var g_last = Date.now();
function animate(angle) {
  // Calculates the elapsed time.
  var now = Date.now();
  var elapsed = now - g_last;
  g_last = now;
  // Updates the current rotation angle (adjusted by the elapsed time).
  var newAngle = angle + (step * elapsed) / 1000.0;
  return newAngle %= 360;
}

// Handles key presses and adjusts values accordingly.
function keydown(ev) {
    if(ev.keyCode == 39) { // The right arrow key was pressed.
      eyeX += 1; // Moves the eye ("rotates") right.
    } else 
    if (ev.keyCode == 37) { // The left arrow key was pressed.
      eyeX -= 1; // Moves the eye ("rotates") left.
    } else 
    if (ev.keyCode == 40) { // The down arrow key was pressed.
      if (backup == 0) { // Prevents changing speed while paused.
        step -= 10; // Increases speed clockwise (or decreases speed counterclockwise).
      }
    } else
    if (ev.keyCode == 38) { // The up arrow key was pressed.
      if (backup == 0) {
        step += 10; // Decreases speed clockwise (or increases speed counterclockwise).
      }
    } else 
    if (ev.keyCode == 69) { // The E key was pressed.
      if (excited == 0) {
        excited = 1;
      } else {
        excited = 0;
      }
    } 
    if (ev.keyCode == 32) { // The space key was pressed.
      var temp = step; // Swaps values to "pause" electron rotation.
      step = backup;
      backup = temp;
    } else {
      return;
    }  
}

// Handles browser inputs (ie. buttons and sliders) and adjusts values accordingly.
var atomicNumber = 1, fov = 1; // Initial atomicNumber and fov.
var neutronTable = [0,2,4,5,6,6,7,8,10,10,12,12,14,14,16,16,18,22,20,20,24,26,28,28,30,30,32,31,35,35,39,41,42,45,45,48]; // Neutons don't increase with the atomic number unlike protons and electrons.
var neutrons = neutronTable[0];
function addParticle() {
  if (atomicNumber < 36) {
    atomicNumber += 1;
    neutrons = neutronTable[atomicNumber-1];
  }
  updateValues(-1);
}
function subParticle(fov) {
  if (atomicNumber > 1) {
    atomicNumber -= 1;
    neutrons = neutronTable[atomicNumber-1];
  }
  updateValues(-1);
}
// Sets the values on the browser.
function updateValues(zoom) {
  document.getElementById("protonCount").innerHTML = atomicNumber;
  document.getElementById("neutronCount").innerHTML = neutrons;
  document.getElementById("electronCount").innerHTML = atomicNumber;
  if (zoom != -1) {
    document.getElementById('zoom').innerHTML = zoom;
    fov = 111 - zoom; // Zoom is arbitrary.
  }
}
updateValues(fov);

// Draws the scene.
var eyeX = 0, excited = 0; // EyeX used to change the view while excited is used for the atom state.
function draw(gl, currentAngle, u_ModelMatrix, u_ViewMatrix, u_PerspectiveMatrix, u_NormalMatrix) {
  var levels = 1 + excited; // n=1 has a maximum of 2 electrons.
  if (atomicNumber > 2 && atomicNumber <= 10) { // n=2 has a maximum of 8 electrons.
    levels = 2 + excited;
  }
  if (atomicNumber > 10 && atomicNumber <= 28) { // n=3 has a maximum of 18 electrons.
    levels = 3 + excited;
  }
  if (atomicNumber > 28 && atomicNumber <= 36) { // n=4 has a maximum of 32 electrons, but we are maxing out at 36 elements (first 4 rows of the periodic table).
    levels = 4 + excited;
  }
  
  // Creates the matrices for MVP and lighting.
  var modelMatrix = new Matrix4();
  var viewMatrix = new Matrix4();
  var perspectiveMatrix = new Matrix4();
  var normalMatrix = new Matrix4();
  
  // Sets the matrices for the orbit lines.
  perspectiveMatrix.setPerspective(fov, 1.0, 1.0, 100.0); // fov, scale, near, far
  viewMatrix.setLookAt(eyeX, 0.0, 10.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0); // eyeX, eyeY, eyeZ, referenceX, referenceY, referenceZ, directionX, directionY, directionZ
  modelMatrix.setIdentity();
  normalMatrix.setIdentity(); // The normal matrix is the same as the model matrix for 2D shapes (because of identity matrix).
  gl.uniformMatrix4fv(u_PerspectiveMatrix, false, perspectiveMatrix.elements);
  gl.uniformMatrix4fv(u_ViewMatrix, false, viewMatrix.elements);
  gl.uniformMatrix4fv(u_ModelMatrix, false, modelMatrix.elements);
  gl.uniformMatrix4fv(u_NormalMatrix, false, normalMatrix.elements);
  
  // Clears color and depth buffers.
  gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);
  
  // Gets storage location of a_Flag. This flag is used to enable/disable lighting for colors.
  var a_Flag = gl.getAttribLocation(gl.program, 'a_Flag');
  if (a_Flag < 0) {
    console.log('Failed to get the storage location of a_Flag');
    return -1;
  }
  
  // Gets storage location of a_TexFlag. This flag is used to enable/disable textures.
  var a_TexFlag = gl.getAttribLocation(gl.program, 'a_TexFlag');
  if (a_TexFlag < 0) {
    console.log('Failed to get the storage location of a_TexFlag');
    return -1;
  }
  
  // Sets the vertex information.
  gl.vertexAttrib1f(a_TexFlag, 1.0); // Enable textures for background.
  var n = makeIcon(gl); // Sets the vertex buffer for background textures.
  if (n < 0) {
    console.log('Failed to set the vertex information');
    return;
  }
  
  // Draws the background.
  gl.drawArrays(gl.TRIANGLE_STRIP, 0, n);
  
  // Sets the vertex information.
  gl.vertexAttrib1f(a_TexFlag, 0.0); // Disable textures for background.
  gl.vertexAttrib1f(a_Flag, 1.0); // Disable lighting to affect color.
  n = makeCircleVertices(gl, 0, 0, 2, 360); // Sets the vertex buffer for circles. Set to 256 instead of 360 because firefox freaks out for some reason.
  if (n < 0) {
    console.log('Failed to set the vertex information');
    return;
  }
  
  // Draws the orbit lines.
  for (var i = 1; i <= levels; i++) {
    modelMatrix.setScale(i+2, i+2, i+2);
    gl.uniformMatrix4fv(u_ModelMatrix, false, modelMatrix.elements);
    gl.drawArrays(gl.LINE_LOOP, 0, n);
    
  }
  
  // Changes the matrices for subatomic particles.
  modelMatrix.setScale(0.5, 0.5, 0.5);
  gl.uniformMatrix4fv(u_ModelMatrix, false, modelMatrix.elements);
  // Calculates the matrix to transform the normal based on the model matrix.
  normalMatrix.setInverseOf(modelMatrix);
  normalMatrix.transpose();
  // Passes the transformation matrix for normals to u_NormalMatrix.
  gl.uniformMatrix4fv(u_NormalMatrix, false, normalMatrix.elements);
  
  // Sets the vertex information.
  gl.vertexAttrib1f(a_Flag, 0.0); // Enable lighting to affect color.
  n = initSphereVertexBuffers(gl, 1.0, 0.0, 0.0); // Sets the vertex buffer for red spheres.
  if (n < 0) {
    console.log('Failed to set the vertex information');
    return;
  }

  // Draws the protons of the nucleus.
  gl.drawElements(gl.TRIANGLES, n, gl.UNSIGNED_BYTE, 0); // Nucleus for hydrogen atom is stationary.
  for (var i = 1; i < atomicNumber; i++) {
    modelMatrix.setScale(0.5, 0.5, 0.5);
    modelMatrix.translate((Math.random() * 2 - 1) * 0.6, (Math.random() * 2 - 1) * 0.6, (Math.random() * 2 - 1) * 0.6); // Position is randomized for subsequent protons.
    gl.uniformMatrix4fv(u_ModelMatrix, false, modelMatrix.elements);
    gl.drawElements(gl.TRIANGLES, n, gl.UNSIGNED_BYTE, 0);
  }
  
  // Sets the vertex information.
  n = initSphereVertexBuffers(gl, 0.0, 0.0, 1.0); // Sets the vertex buffer for blue spheres.
  if (n < 0) {
    console.log('Failed to set the vertex information');
    return;
  }
  
  // Draws the neutrons of the nucleus.
  for (var i = 1; i <= neutrons; i++) {
    modelMatrix.setScale(0.5, 0.5, 0.5);
    modelMatrix.translate((Math.random() * 2 - 1) * 0.6, (Math.random() * 2 - 1) * 0.6, (Math.random() * 2 - 1) * 0.6); // Position is randomized for neutrons.
    gl.uniformMatrix4fv(u_ModelMatrix, false, modelMatrix.elements);
    gl.drawElements(gl.TRIANGLES, n, gl.UNSIGNED_BYTE, 0);
  }
  
  // Sets the vertex information.
  n = initSphereVertexBuffers(gl, 0.4, 0.4, 0.4); // Sets the vertex buffer for gray spheres.
  if (n < 0) {
    console.log('Failed to set the vertex information');
    return;
  }
  
  // Draws the electrons.
  var angleOffset = 0, positionOffset = 24; // Angle offset for the angle between electrons. Position offset for the distance between the nucleus and electrons.
  var angleIncrement = 180; // Position of next electron.
  for (var i = 1; i <= atomicNumber; i++) {
    // Corrections for electron positions in levels beyond n=1.
    if (i == 3 || i == 11 || i == 29) {
      positionOffset += 8;
      angleIncrement = 90;
    }
    if (i == 7 || i == 33) {
      angleOffset -= 45;
    }
    if (i == 11) {
      angleOffset += 45;
      angleIncrement = 20;
    }
    
    // Sets the position of the current electron.
    modelMatrix.setScale(0.25, 0.25, 0.25);
    var cosCalculation;
    var sinCalculation = Math.sin((currentAngle + angleOffset) * Math.PI/180);
    if (i <= 2 || (i >= 11 && i <= 28)) { // n=1 and n=3 are clockwise in orbit.
      cosCalculation = Math.cos((currentAngle + angleOffset) * Math.PI/180);
    }
    if ((i >= 3 && i <= 10) || i >= 29) { // n=2 and n=4 are counterclockwise in orbit.
      cosCalculation = Math.cos((currentAngle + angleOffset) * Math.PI/180)*-1;
    }
    modelMatrix.translate(cosCalculation * positionOffset, sinCalculation * positionOffset, 0.0);
    // Sets the position of the excited electron. Excited electron has the same orbit as the level below.
    if (i == atomicNumber && excited == 1) {
      gl.vertexAttrib1f(a_Flag, 2.0); // Disable lighting to affect color.
      modelMatrix.setScale(0.25, 0.25, 0.25);
      modelMatrix.translate(cosCalculation * (positionOffset + 8), sinCalculation * (positionOffset + 8), 0.0); // Moves electron to the next level.
    }
    angleOffset -= angleIncrement; // Changes position for the next electron.
    gl.uniformMatrix4fv(u_ModelMatrix, false, modelMatrix.elements);
    
    // Sets the normal matrix for the electrons so that lighting can affect them.
    normalMatrix.setInverseOf(modelMatrix);
    normalMatrix.transpose();
    gl.uniformMatrix4fv(u_NormalMatrix, false, normalMatrix.elements);
    
    gl.drawElements(gl.TRIANGLES, n, gl.UNSIGNED_BYTE, 0);
  }  
}

// Generates the vertices and texels for the icon in the background.
function makeIcon(gl) {
  var verticesTexCoords = new Float32Array([
    // Vertex coordinates, texture coordinates.
    -14.2, -10.3,  0.0, 0.99,
    -14.2, -14.3,  0.0, 0.00,
    -10.2, -10.3,  1.0, 0.99,
    -10.2, -14.3,  1.0, 0.00,
  ]);
  var n = 4;
  
  // Creates the buffer object.
  var vertexTexCoordBuffer = gl.createBuffer();
  if (!vertexTexCoordBuffer) {
    console.log('Failed to create the buffer object');
    return -1;
  }
  
  // Binds the buffer object to target.
  gl.bindBuffer(gl.ARRAY_BUFFER, vertexTexCoordBuffer);
  gl.bufferData(gl.ARRAY_BUFFER, verticesTexCoords, gl.STATIC_DRAW);
  
  var FSIZE = verticesTexCoords.BYTES_PER_ELEMENT;
  // Gets the storage location of a_Position, assigns and enables the buffer.
  var a_Position = gl.getAttribLocation(gl.program, 'a_Position');
  if (a_Position < 0) {
    console.log('Failed to get the storage location of a_Position');
    return -1;
  }
  gl.vertexAttribPointer(a_Position, 2, gl.FLOAT, false, FSIZE * 4, 0);
  gl.enableVertexAttribArray(a_Position);

  // Gets the storage location of a_TexCoord.
  var a_TexCoord = gl.getAttribLocation(gl.program, 'a_TexCoord');
  if (a_TexCoord < 0) {
    console.log('Failed to get the storage location of a_TexCoord');
    return -1;
  }
  // Assigns the buffer object to a_TexCoord variable.
  gl.vertexAttribPointer(a_TexCoord, 2, gl.FLOAT, false, FSIZE * 4, FSIZE * 2);
  gl.enableVertexAttribArray(a_TexCoord);  // Enable the assignment of the buffer object

  return n;
}

// Generates the vertices for a circle.
function makeCircleVertices(gl, centerX, centerY, radius, vertexCount) {
  var circleData = new Float32Array(vertexCount*2); // Prepares an array with double the vertexCount (for x and y coordinates).
  
  // Using center coordinates, radius and the number of vertices, coordinates of the circle vertices are calculated and stored in the array.
  for (var i = 0; i < vertexCount*2; i++) {
    var angle = i/vertexCount*2*Math.PI;
    if (i % 2 == 0) {
      circleData[i] = centerX+radius*Math.cos(angle); // x coordinate
    }
    else {
      circleData[i] = centerY+radius*Math.sin(angle); // y coordinate
    }
  }
  
  // Creates a buffer object.
  var vertexBuffer = gl.createBuffer();
  if (!vertexBuffer) {
    console.log('Failed to create the buffer object');
    return -1;
  }
  
  gl.bindBuffer(gl.ARRAY_BUFFER, vertexBuffer); // Binds the buffer object to the target.
  gl.bufferData(gl.ARRAY_BUFFER, circleData, gl.STATIC_DRAW); // Writes data into the buffer object.
  
  // Gets the storage location of a_Position.
  var a_Position = gl.getAttribLocation(gl.program, 'a_Position');
  if (a_Position < 0) {
    console.log('Failed to get the storage location of a_Position');
    return -1;
  }
  
  gl.vertexAttribPointer(a_Position, 2, gl.FLOAT, false, 0, 0); // Assigns the buffer object to a_Position variable.
  gl.enableVertexAttribArray(a_Position); // Enable the assignment to a_Position variable.
  
  return vertexCount;
}

// Initializes buffers for drawing a spheres in the scene. Sphere calculation code taken from examples.
function initSphereVertexBuffers(gl, red, green, blue) {
  // Creates a sphere.
  var SPHERE_DIV = 15;

  var i, ai, si, ci;
  var j, aj, sj, cj;
  var p1, p2;

  // Like vectors in C++, these arrays are resizable.
  var positions = [];
  var colors = [];
  var indices = [];

  // Generates the sphere coordinates.
  for (j = 0; j <= SPHERE_DIV; j++) {
    aj = j * Math.PI / SPHERE_DIV;
    sj = Math.sin(aj);
    cj = Math.cos(aj);
    for (i = 0; i <= SPHERE_DIV; i++) {
      ai = i * 2 * Math.PI / SPHERE_DIV;
      si = Math.sin(ai);
      ci = Math.cos(ai);

      positions.push(si * sj); // X
      positions.push(cj);      // Y
      positions.push(ci * sj); // Z
    }
  }
  
  // Pushes colors in conjunction with each coordinate.
  for (j = 0; j <= SPHERE_DIV; j++) {
    for (i = 0; i <= SPHERE_DIV; i++) {
      colors.push(red);   // R
      colors.push(green); // G
      colors.push(blue);  // B
    }
  }
  
  // Generates the indices.
  for (j = 0; j < SPHERE_DIV; j++) {
    for (i = 0; i < SPHERE_DIV; i++) {
      p1 = j * (SPHERE_DIV + 1) + i;
      p2 = p1 + (SPHERE_DIV + 1);

      indices.push(p1);
      indices.push(p2);
      indices.push(p1 + 1);

      indices.push(p1 + 1);
      indices.push(p2);
      indices.push(p2 + 1);
    }
  }
  
  // Converts the flexible arrays to appropriate fixed-size arrays that WebGL can work with.
  var positions = new Float32Array(positions);
  var colors = new Float32Array(colors);
  var indices = new Uint8Array(indices);
  
  // Creates a buffer object for the vertices, writes, and enables them.
  var vertexBuffer = gl.createBuffer();
  if (!vertexBuffer) {
    console.log('Failed to create the buffer object');
    return -1;
  }
  gl.bindBuffer(gl.ARRAY_BUFFER, vertexBuffer);
  gl.bufferData(gl.ARRAY_BUFFER, positions, gl.STATIC_DRAW);
  // Gets the storage location of a_Position.
  var a_Position = gl.getAttribLocation(gl.program, 'a_Position');
  if(a_Position < 0) {
    console.log('Failed to get the storage location of a_Position');
    return -1;
  }
  gl.vertexAttribPointer(a_Position, 3, gl.FLOAT, false, 0, 0);
  gl.enableVertexAttribArray(a_Position);
  // Gets the storage location of a_Normal.
  var a_Normal = gl.getAttribLocation(gl.program, 'a_Normal');
  if(a_Normal < 0) {
    console.log('Failed to get the storage location of a_Normal');
    return -1;
  }
  gl.vertexAttribPointer(a_Normal, 3, gl.FLOAT, false, 0, 0);
  gl.enableVertexAttribArray(a_Normal);
  
  // Creates a buffer object for the colors, writes, and enables them.
  var colorBuffer = gl.createBuffer();
  if (!colorBuffer) {
    console.log('Failed to create the buffer object');
    return -1;
  }
  gl.bindBuffer(gl.ARRAY_BUFFER, colorBuffer);
  gl.bufferData(gl.ARRAY_BUFFER, colors, gl.STATIC_DRAW);
  // Gets the storage location of a_Color.
  var a_Color = gl.getAttribLocation(gl.program, 'a_Color');
  if(a_Color < 0) {
    console.log('Failed to get the storage location of a_Color');
    return -1;
  }
  gl.vertexAttribPointer(a_Color, 3, gl.FLOAT, false, 0, 0);
  gl.enableVertexAttribArray(a_Color);
  
  // Creates a buffer object for the indices and writes them.
  var indexBuffer = gl.createBuffer();
  gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, indexBuffer);
  gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, indices, gl.STATIC_DRAW);

  return indices.length;
}

// Initializes the textures for the background.
function initTextures(gl) {
  var texture = gl.createTexture(); // Creates a texture object.
  if (!texture) {
    console.log('Failed to create the texture object');
    return false;
  }

  // Gets the storage location of u_Sampler.
  var u_Sampler = gl.getUniformLocation(gl.program, 'u_Sampler');
  if (!u_Sampler) {
    console.log('Failed to get the storage location of u_Sampler');
    return false;
  }
  var image = new Image();  // Creates the image object.
  if (!image) {
    console.log('Failed to create the image object');
    return false;
  }
  // Registers the event handler to be called on loading an image.
  image.onload = function(){ loadTexture(gl, texture, u_Sampler, image); };
  // Tells the browser to load an image.
  image.src = 'spectrePFP.jpg';

  return true;
}

// Loads the textures for the background.
function loadTexture(gl, texture, u_Sampler, image) {
  gl.pixelStorei(gl.UNPACK_FLIP_Y_WEBGL, 1); // Flips the image's y-axis.
  // Enables texture unit0.
  gl.activeTexture(gl.TEXTURE0);
  // Binds the texture object to the target.
  gl.bindTexture(gl.TEXTURE_2D, texture);

  // Sets the texture parameters.
  gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR);
  // Sets the texture image.
  gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGB, gl.RGB, gl.UNSIGNED_BYTE, image);
  
  // Sets the texture unit 0 to the sampler.
  gl.uniform1i(u_Sampler, 0);
}