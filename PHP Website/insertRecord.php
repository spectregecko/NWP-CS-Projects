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
            // If the user is authorized, they can access the database.
            if (isset($_SESSION['valid_user'])) {
                // Retrieves the values from the form in database.php.
                $ItemID = $_POST['ItemID'];
                $ItemName = $_POST['ItemName'];
                $Price = $_POST['Price'];
                $UnitsInStock = $_POST['UnitsInStock'];

                // Handles the insertion of a new record into the database.
                try {
                    // Retrieves the database credentials and connects to it.
                    require_once("DBconfig.php");
                    $db = new PDO($dsn, $user, $pass);

                    // Validates the values from the form in database.php. This isn't really necessary as they can be handled in the form directly.
                    $flag = false;
                    if ($ItemID < 1 || $ItemID > 127) {
                        echo '<p id="message"><strong id="error">The Item ID provided is out of the range [1,127]!</strong></p>';
                        $flag = true;
                    }
                    if ($Price < 0 || $Price > 999.99) {
                        echo '<p id="message"><strong id="error">The Price provided is out of the range [0,999.99]!</strong></p>';
                        $flag = true;
                    }
                    if ($UnitsInStock < 0 || $UnitsInStock > 32767) {
                        echo '<p id="message"><strong id="error">The Unit In Stock provided is out of the range [0,32767]!</strong></p>';
                        $flag = true;
                    }
                    if ($flag) {
                        echo '<br><p id="message">Please go back and try again.</p><br>';
                        echo '<a href="database.php"><button>Retry</button></a>';
                        exit;
                    }

                    // Checks if the new record has an Item ID that already exists in the database.
                    $query = "SELECT * FROM Items WHERE ItemID = :itemID";
                    $stmt = $db->prepare($query);
                    $stmt->bindParam(':itemID', $ItemID);
                    $stmt->execute();
                    if ($stmt->rowCount()) {
                        echo '<p><strong id="error">The Item ID provided already exists!</strong></p>';
                        echo "<p>Please go back and try again.</p>";
                        echo '<a href="database.php"><button>Retry</button></a>';
                        exit;
                    }

                    // Inserts the record into the database.
                    $visible = 1;
                    $query = "INSERT IGNORE INTO Items VALUES ($visible, :itemID, :itemName, :price, :unitsInStock)";
                    $stmt = $db->prepare($query);
                    $stmt->bindParam(':itemID', $ItemID);
                    $stmt->bindParam(':itemName', $ItemName);
                    $stmt->bindParam(':price', $Price);
                    $stmt->bindParam(':unitsInStock', $UnitsInStock);
                    $stmt->execute();

                    // Disconnects from the database.
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