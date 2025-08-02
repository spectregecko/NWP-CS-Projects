<?php
    // Redirects this page to the more secure HTTPS protocol.
    require_once("httpsRedirection.php");
    
    // Starts a session for the user.
    session_start();
    // Checks if the user has tried to log in.
    if (isset($_POST['userid']) && isset($_POST['password'])) {
        $userid = $_POST['userid'];
        $password = $_POST['password'];
        require_once('authCookie.php');
    }
    // Checks if the user's browser has login cookies.
    else if(isset($_COOKIE['email']) && isset($_COOKIE['password'])) {
        $userid = $_COOKIE['email'];
        $password = $_COOKIE['password'];
        require_once('authCookie.php');
    }
?>
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Login - Jeremey's Convenience Store</title>
        <link rel="stylesheet" href="Styling/styles.css"/>
    </head>
    <header>
        <h1>Jeremey's Convenience Store</h1>
    </header>
    <body>
        <br><h2>Login</h2><br>
        <?php
            // Checks if the user is valid (logged in).
            if (isset($_SESSION['valid_user'])) {
                header("Location: database.php");
                exit();
            }
            else {
                // Checks if the user has tried and failed to log in (email and password validation).
                if (isset($userid) && !preg_match("/^[a-zA-Z0-9][a-zA-Z0-9_\.]+[a-zA-Z0-9]@[a-zA-Z]+\.[a-zA-Z]{2,3}/", $userid)) {
                    echo '<p id="message"><strong id="error">Please enter a valid email!</strong></p>';
                }
                else if (isset($password) && !preg_match("/^[0-9]?[a-zA-Z]+[0-9]?(-[0-9]?[a-zA-Z]+[0-9]?)+/", $password)) {
                    echo '<p id="message"><strong id="error">Please enter a valid passphrase!</strong><br>';
                }
                else if (isset($userid) && isset($password)) {
                    echo '<p id="message"><strong id="error">Invalid credentials!</strong><br>';
                }
                else {
                    echo '<p id="message">Please log in to access the catalog database.</p>';
                }

                // Login form.
                echo '<script src="Validation/login.js"></script>';
                echo '<form method="post" id="prompt"><fieldset id="promptBody">';
                echo '<p><label>Email</label>';
                echo '<input type="text" name="userid" id="userid"></p>';
                echo '<p><label>Password</label>';
                echo '<input type="password" name="password" id="password"></p>';
                echo '<input type="submit" name="login" value="Login" formaction="index.php"> ';
                echo '<input type="submit" name"register" value="Register" formaction="registration.php" onclick="disableValidation()">';
                echo '</fieldset>';
                echo '</form><br>';
            }
        ?>
    </body>
    <footer>
        <p>Jeremey Larter Inc. 2024</p>
    </footer>
</html>