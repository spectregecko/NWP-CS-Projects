<?php
    // Destroys the session (logs out) if the user was logged in.
    require_once("httpsRedirection.php");
    session_start();
    if (isset($_SESSION['valid_user'])) {
        $old_user = $_SESSION['valid_user'];
        unset($_SESSION['valid_user']);
        unset($_SESSION['privilege']); // It is assumed that if valid_user is set, then privilege would also be set.
    }
    session_destroy();
?>
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Log Out - Jeremey's Convenience Store</title>
        <link rel="stylesheet" href="Styling/styles.css"/>
    </head>
    <header>
        <h1>Jeremey's Convenience Store</h1>
    </header>
    <body>
        <br><h2>Log Out</h2><br>
        <?php
            if (!empty($old_user)) {
                echo '<p id="message">You have been logged out.</p><br>';
            }
            else {
                echo '<p id="message">You were not logged in, and so have not been logged out.</p><br>';
            }
        ?>
        <a href="index.php"><button>Home</button></a>
    </body>
    <footer>
        <p>Jeremey Larter Inc. 2024</p>
    </footer>
</html>