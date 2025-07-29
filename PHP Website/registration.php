<?php
    // Redirects this page to the more secure HTTPS protocol.
    require_once("httpsRedirection.php");

    // Seession not required.
?>
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Registration - Jeremey's Convenience Store</title>
        <link rel="stylesheet" href="Styling/styles.css"/>
    </head>
    <header>
        <h1>Jeremey's Convenience Store</h1>
    </header>
    <body>
        <br><h2>Registration</h2><br>
        <?php
            try {
                // Connects to the employees database.
                $user = 'root';
                $pass = '';
                $host = 'localhost';
                $db_name = 'employees';
                $dsn = "mysql:host=$host;dbname=$db_name";
                $db = new PDO($dsn, $user, $pass);

                if (isset($_POST['submit'])) {
                    // Retrieves the data from the form below, if applicable.
                    $firstName = $_POST['firstName'];
                    $middleInitial = $_POST['middleInitial'];
                    $lastName = $_POST['lastName'];
                    $email 	= $_POST['email'];
                    $password = $_POST['password'];
                    $confirm = $_POST['confirm'];

                    // Email and password validation.
                    $flag = true;
                    if (!preg_match("/^[a-zA-Z0-9][a-zA-Z0-9_\.]+[a-zA-Z0-9]@[a-zA-Z]+\.[a-zA-Z]{2,3}/", $email)) {
                        echo '<p id="message"><strong id="error">Please enter a valid email!</strong></p>';
                        $flag = false;
                    }
                    else if($password != $confirm) {
                        echo '<p id="message"><strong id="error">Passwords do not match!</strong></p>';
                        $flag = false;
                    }
                    else if (!preg_match("/^[0-9]?[a-zA-Z]+[0-9]?(-[0-9]?[a-zA-Z]+[0-9]?)+/", $password)) {
                        echo '<p id="message"><strong id="error">Please enter a valid passphrase!</strong><br>';
                        $flag = false;
                    }
                    else {
                        // Prevents registering users with an email that already exists in the users database.
                        $query = "SELECT * FROM Users WHERE Email = :userID";
                        $stmt = $db->prepare($query);
                        $stmt->bindParam(':userID', $email);
                        $stmt->execute();
                        if ($stmt->rowCount()) {
                            echo '<p id="message"><strong id="error">User already exists!</strong><br>';
                            $flag = false;
                        }

                        // The new user is added to the users database if their credentials pass validation and doesn't already exist.
                        if ($flag) {
                            // Uses the SHA-256 hash function to store passwords as hashes.
                            $hashPassword = hash('sha256', $password);
                            $query = "INSERT IGNORE INTO Users (FirstName, MiddleInitial, LastName, Email, Password) VALUES (:firstName, :middleInitial, :lastName, :email, :password)";
                            $stmt = $db->prepare($query);
                            $stmt->bindParam(':firstName', $firstName);
                            $stmt->bindParam(':middleInitial', $middleInitial);
                            $stmt->bindParam(':lastName', $lastName);
                            $stmt->bindParam(':email', $email);
                            $stmt->bindParam(':password', $hashPassword);
                            $stmt->execute();

                            // Disconnects from the database.
                            $db = NULL;
                            header("Location: index.php");
                            exit();
                        }
                    }
                }
                else {
                    echo '<p id="message">Please enter the required information.</p>';
                }
                $db = NULL;
            }
            catch (PDOException $e) {
                echo "Error: ".$e->getMessage();
                exit;
            }
        ?>
        <!--Registration form.-->
        <script src="Validation/registration.js"></script>
        <form method="post" id="prompt">
            <fieldset id="promptBody">
                <p><label>First Name</label>
                <input type="text" name="firstName" maxlength="255"></p>
                <p><label>Middle Initial</label>
                <input type="text" name="middleInitial" maxlength="1"></p>
                <p><label>Last Name</label>
                <input type="text" name="lastName" maxlength="255"></p>
                <p><label>Email*</label>
                <input type="text" name="email" maxlength="255"></p>
                <p><label>Password*</label>
                <input type="password" name="password"></p>
                <p><label>Confirm Password*</label>
                <input type="password" name="confirm"></p>
                <input type="submit" name="submit" value="Submit" formaction="registration.php"> 
                <input type="submit" name="back" value="Back" formaction="index.php" onclick="disableValidation()">
            </fieldset>
        </form><br>
    </body>
    <footer>
        <p>Jeremey Larter Inc. 2024</p>
    </footer>
</html>