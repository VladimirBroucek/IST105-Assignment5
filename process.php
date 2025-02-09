<?php
$year = $_GET['year'];
$word = $_GET['word'];

if( !is_numeric($year) || empty($word)) {
    echo "<p>Error: Invalid input</p>";
    exit();
}

$output = shell_exec("python3 process.py year=$year word=$word");
echo $output;

?>
