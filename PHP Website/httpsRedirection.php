<?php
    // Handles redirection to the HTTPS protocol.
    if (!isset($_SERVER['HTTPS'])) {
        $url = 'https://'.$_SERVER['HTTP_HOST'].$_SERVER['REQUEST_URI'];
        //$url = 'https://localhost:443' . $_SERVER['REQUEST_URI']; // Alternative way.
        header("Location: ".$url); // Redirect - 302
        exit();
    }
?>