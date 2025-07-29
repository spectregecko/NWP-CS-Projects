<?php
    try {
        // Connects to the employees database and retrieves the entry of the user.
        $user = 'root';
        $pass = '';
        $host = 'localhost';
        $db_name = 'employees';
        $dsn = "mysql:host=$host;dbname=$db_name";
        $db = new PDO($dsn, $user, $pass);
        $query = "SELECT * FROM Users WHERE Email = :userID";
        $stmt = $db->prepare($query);
        $stmt->bindParam(':userID', $userid);
        $stmt->execute();
        $result = $stmt->fetch(PDO::FETCH_OBJ);

        // Authenticates the user.
        if ($stmt->rowCount() && (hash('sha256', $password) == $result->Password)) {
            //$expiryTime = time() + (60 * 60 * 24); // Cookie is valid for 24 hours.
            $expiryTime = time() + 30; // Cookie is valid for 30 seconds.
            $email = "Email";
            $pass = "Password";
            // Disclaimer: This is not a secure practice to store the userid and password as plaintext in cookies.
            setcookie($email, $userid, $expiryTime);
            setcookie($pass, $password, $expiryTime);
            $_SESSION['valid_user'] = $userid;
            $_SESSION['privilege'] = $result->Privilege;
        }

        // Disconnects from the database.
        $db = NULL;
    }
    catch (PDOException $e) {
        echo "Error: ".$e->getMessage();
        exit;
    }
?>