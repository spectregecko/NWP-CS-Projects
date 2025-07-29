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
        <title>Catalog - Jeremey's Convenience Store</title>
        <link rel="stylesheet" href="Styling/styles.css"/>
    </head>
    <header>
        <h1>Jeremey's Convenience Store</h1>
    </header>
    <body>
        <br><h2>Catalog Search</h2><br>
        <?php
            // If the user is authorized, they can access the database.
            if (isset($_SESSION['valid_user'])) {
                // User information and log out.
                echo '<p id="message">You are logged in as '.$_SESSION['valid_user'].' ';
                echo '<a href="logout.php">Logout</a></p>';

                // Catalog search.
                echo '<form action="queryTable.php" method="post"><fieldset id="promptBody">';
                echo '<p><strong>Choose Search Type:</strong><br>';
                echo '<input type="radio" name="searchtype" value="ItemID" required checked>Item ID<br>';
                echo '<input type="radio" name="searchtype" value="ItemName" required>Item Name<br>';
                echo '<input type="radio" name="searchtype" value="Price" required>Price<br>';
                echo '<input type="radio" name="searchtype" value="UnitsInStock" required>Units In Stock</p>';
                echo '<p><label>Enter Search Term</label>';
                echo '<input name="searchterm" type="text" size="40" pattern="[a-zA-Z0-9 ]*"></p>';
                echo '<input type="submit">';
                echo '</fieldset></form>';

                // Insert form.
                echo "<p><details><summary>Insert</summary>";
                if ($_SESSION['privilege'] == 1) {
                    echo '<script src="Validation/record.js"></script>';
                    echo '<form method="post" action="insertRecord.php"><br>';
                    echo    "<fieldset><p>";
                    echo        "<label>Item ID</label>";
                    echo        '<input type="number" name="ItemID" min="0" max="127" step="1">';
                    echo    "</p><p>";
                    echo        "<label>Item Name</label>";
                    echo        '<input type="text" name="ItemName" maxlength="255" required>';
                    echo    "</p><p>";
                    echo        "<label>Price</label>";
                    echo        '<input type="number" name="Price" min="0" max="999.99" step="0.01" pattern="\d*.\d{2}" required>'; // Required because an empty box is considered 0.
                    echo    "</p><p>";
                    echo        "<label>Units In Stock</label>";
                    echo        '<input type="number" name="UnitsInStock" step="1" min="0" max="32767" required>'; // Required because an empty box is considered 0.
                    echo    '</p><p>';
                    echo        '<input type="submit">';
                    echo    "</p></fieldset></form>";
                }
                else {
                    echo '<br><br><p id="message"><strong id="error"> You are not authorized!</strong><p>';
                }
                echo '</details></p>';
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