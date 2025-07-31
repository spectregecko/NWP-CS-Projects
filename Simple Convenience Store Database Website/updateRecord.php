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
                $ItemName = $_POST['ItemName'];
                $Price = $_POST['Price'];
                $UnitsInStock = $_POST['UnitsInStock'];
                try {
                    require_once("DBconfig.php");
                    $db = new PDO($dsn, $user, $pass);
                    $flag = false;
                    if ($Price < 0 || $Price > 999.99) {
                        echo '<p id="message"><strong id="error">The Price provided is out of the range [0,999.99]!</strong></p>';
                        $flag = true;
                    }
                    if ($UnitsInStock < 0 || $UnitsInStock > 32767) {
                        echo '<p id="message"><strong id="error">The Unit In Stock provided is out of the range [0,255]!</strong></p>';
                        $flag = true;
                    }
                    if ($flag) {
                        echo '<br><p id="message">Please go back and try again.</p><br>';
                        echo '<a href="editRecord.php?ItemID='.$ItemID.'"><button>Retry</button></a>';
                        exit;
                    }
                    $Visible = 1;
                    if ($_SESSION['privilege'] == 1) {
                        $Visible = $_POST['Visible'];
                    }
                    $query = "UPDATE Items SET Visible = :visible, ItemName = :itemName, Price = :price, UnitsInStock = :unitsInStock WHERE ItemID = :itemID";
                    $stmt = $db->prepare($query);
                    $stmt->bindParam(':visible', $Visible);
                    $stmt->bindParam(':itemName', $ItemName);
                    $stmt->bindParam(':price', $Price);
                    $stmt->bindParam(':unitsInStock', $UnitsInStock);
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