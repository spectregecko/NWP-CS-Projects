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
        <title>Edit Item - Jeremey's Convenience Store</title>
        <link rel="stylesheet" href="Styling/styles.css"/>
    </head>
    <header>
        <h1>Jeremey's Convenience Store</h1>
    </header>
    <body>
        <br><h2>Edit Item</h2><br>
        <?php
            if (isset($_SESSION['valid_user'])) {
                // Retrieves the shipper ID from the record the user wants to edit.
                $ItemID = $_GET['ItemID'];

                try {
                    // Connects to the database and retrieves the record to be modified.
                    require_once("DBconfig.php");
                    $db = new PDO($dsn, $user, $pass);
                    $query = "SELECT * FROM Items WHERE ItemID = :itemID";
                    $stmt = $db->prepare($query);
                    $stmt->bindParam(':itemID', $ItemID);
                    $stmt->execute();

                    // Displays the record to the user.
                    echo '<p id="message">Item to be edited:</p><br>';
                    echo '<fieldset><div id="itemID" class="pk"><strong>Item ID</strong></div>';
                    echo '<div id="itemName"><strong>Item Name</strong></div>';
                    echo '<div id="price"><strong>Price</strong></div>';
                    echo '<div id="unitsInStock"><strong>Units In Stock</strong></div>';
                    if ($_SESSION['privilege'] == 1) {
                        echo '<div id="visible"><strong>Visible</strong></div>';
                    }
                    echo "<div></div>";
                    $result = $stmt->fetch(PDO::FETCH_OBJ);
                    $ItemName = $result->ItemName;
                    $Price = $result->Price;
                    $UnitsInStock = $result->UnitsInStock;
                    $Visible = $result->Visible;
                    echo '<div id="itemID">'.$ItemID."</div>";
                    echo '<div id="itemName">'.$ItemName."</div>";
                    echo '<div id="price">$'.number_format($Price, 2)."</div>";
                    echo '<div id="unitsInStock">'.$UnitsInStock."</div>";
                    if ($_SESSION['privilege'] == 1) {
                        echo '<div id="visible">'.$Visible."</div>";
                    }
                    echo '</fieldset>';

                    // Allows the user to update or delete the chosen record.
                    echo "<p><details><summary>Update</summary>";
                    echo '<script src="Validation/record.js"></script>';
                    echo '<form method="post" action="updateRecord.php" id="prompt"><br>';
                    echo    '<fieldset id="promptBody"><p>';
                    echo        "<label>Item ID</label>";
                    echo        '<input type="number" name="ItemID" value="'.$ItemID.'" readonly>';
                    echo    "</p><p>";
                    echo        "<label>Item Name</label>";
                    echo        '<input type="text" name="ItemName" maxlength="255" value="'.$ItemName.'" required>';
                    echo    "</p><p>";
                    echo        "<label>Price</label>";
                    echo        '<input type="number" name="Price" min="0" max="999.99" step="0.01" pattern="\d*.\d{2}" value="'.number_format($Price, 2).'" required>'; // Required because an empty box is considered 0.
                    echo    "</p><p>";
                    echo        "<label>Units In Stock</label>";
                    echo        '<input type="number" name="UnitsInStock" min="0" max="32767" step="1" value="'.$UnitsInStock.'" required>'; // Required because an empty box is considered 0.
                    echo    "</p><p>";
                    if ($_SESSION['privilege'] == 1) {
                        echo    "<label>Visible</label>";
                        echo    '<input type="number" name="Visible" min="0" max="1" step="1" value="'.$Visible.'" required>'; // Visible validation is done here.
                        echo    "</p><p>";
                    }
                    echo        '<input type="submit">';
                    echo    "</p></fieldset>";
                    echo '</form></details></p>';
                    echo '<p><form method="post" action="deleteRecord.php">';
                    echo    '<input type="hidden" name="ItemID" value="'.$ItemID.'">';
                    echo    '<input type="submit" value="Delete"></input></form>';
                    echo "</p>";

                    // Disconnects from the database.
                    $db = NULL;

                    echo '<p><a href="database.php"><button>Done</button></a></p>';
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