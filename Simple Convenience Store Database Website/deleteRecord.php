<?php
    // Redirects this page to the more secure HTTPS protocol.
    require_once("httpsRedirection.php");

    // Starts a session for the user.
    session_start();
?>
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Error - Jeremey's Convenience Store</title>
        <link rel="stylesheet" href="Styling/styles.css"/>
    </head>
    <header>
        <h1>Jeremey's Convenience Store</h1>
    </header>
    <body>
        <br><h2>Error</h2><br>
        <?php
            if (isset($_SESSION['valid_user'])) {
                $ItemID = $_POST['ItemID'];
                try {
                    require_once("DBconfig.php");
                    $db = new PDO($dsn, $user, $pass);
                    $query = "UPDATE Items SET Visible = 0 WHERE ItemID = :itemID";
                    $stmt = $db->prepare($query);
                    $stmt->bindParam(':itemID', $ItemID);
                    $stmt->execute();
                    $db = NULL;
                    header("Location: database.php");
                    exit();
                }
                catch (PDOException $e) {
                    echo "Error: ".$e->getMessage();
                    exit;
                }
            }
            else {
                echo '<p id="message">You are not logged in.</p><br>';
                echo '<p id="message">Only logged in users may see this page.</p><br>';
                echo '<a href="index.php"><button>Home</button></a>';
            }
        ?>
    </body>
    <footer>
        <p>Jeremey Larter Inc. 2024</p>
    </footer>
</html>