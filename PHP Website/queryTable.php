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
        <title>Catalog Query - Jeremey's Convenience Store</title>
        <link rel="stylesheet" href="Styling/styles.css"/>
        <!--<link rel="stylesheet"href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
        <script src="https://code.jquery.com/jquery-latest.js"></script>-->
    </head>
    <header>
        <h1>Jeremey's Convenience Store</h1>
    </header>
    <body>
        <br><h2>Catalog Query</h2><br>
        <?php
            if (isset($_SESSION['valid_user'])) {
                // Validation for search type and term.
                if (!isset($_POST['searchtype']) || !isset($_POST['searchterm'])) {
                    echo '<p>You have not entered search details.<br/>
                            Please go back and try again.</p>';
                    echo '<p><a href="database.php"><button>Retry</button></a></p>';
                    exit;
                }

                // Retrieves the search type and term from the form in the database.php file.
                $searchtype = $_POST['searchtype'];
                // Partial search term.
                $searchterm = "%{$_POST['searchterm']}%";

                switch ($searchtype) {
                    case 'ItemID': // Do nothing.
                    case 'ItemName': // Do nothing.
                    case 'Price': // Do nothing.
                    case 'UnitsInStock': // Do nothing.
                        break;
                    default:
                        echo '<p>That is not a valid search type.<br/>
                                Please go back and try again.</p>';
                        exit;
                }
                
                try {
                    // Connects to the project database and retrieves the entries requested by the user that are visible.
                    require_once("DBconfig.php");
                    $db = new PDO($dsn, $user, $pass);
                    $query = "SELECT * FROM Items WHERE $searchtype LIKE :searchterm AND Visible = 1";
                    if ($_SESSION['privilege'] == 1) {
                        $query = "SELECT * FROM Items WHERE $searchtype LIKE :searchterm";
                    }
                    $stmt = $db->prepare($query);
                    $stmt->bindParam(':searchterm', $searchterm);
                    $stmt->execute();

                    // Displays the query result to the user.
                    echo '<p id="message">Number of items found: '.$stmt->rowCount()."</p><br>";
                    echo '<fieldset><div id="itemID" class="pk"><strong>Item ID</strong></div>';
                    echo '<div id="itemName"><strong>Item Name</strong></div>';
                    echo '<div id="price"><strong>Price</strong></div>';
                    echo '<div id="unitsInStock"><strong>Units In Stock</strong></div>';
                    if ($_SESSION['privilege'] == 1) {
                        echo '<div id="visible"><strong>Visible</strong></div>';
                    }
                    echo '<div id="option"><strong>Option</strong></div>';
                    echo "<div></div>";
                    while($result = $stmt->fetch(PDO::FETCH_OBJ)) {
                        echo '<div id="itemID">'.$result->ItemID."</div>";
                        echo '<div id="itemName">'.$result->ItemName."</div>";
                        echo '<div id="price">$'.number_format($result->Price, 2)."</div>";
                        echo '<div id="unitsInStock">'.$result->UnitsInStock."</div>";
                        if ($_SESSION['privilege'] == 1) {
                            echo '<div id="visible">'.$result->Visible."</div>";
                        }
                        echo '<div id="option"><a href="editRecord.php?ItemID='.$result->ItemID.'">Edit</a></div>';
                        echo "<div></div>";
                    }
                    echo '</fieldset>';

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