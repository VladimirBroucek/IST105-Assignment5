<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $year = $_POST["year"];
    $word = $_POST["word"];

    if (!is_numeric($year) || empty($word)) {
        echo "<p>Error: Please enter a valid number and a non-empty text.</p>";
    } else {
        header("Location: process.php?year=$year&word=$word");
        exit();
    }
}
?>

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Assignment 5</title>
    </head>
    <body>
        <h1>Assignment #4: Enter Values</h1>
        <form method="post">
            <label for="year">Enter your birth year:</label>
            <input type="number" id="year" name="year" required><br><br>

            <label for="word">Enter your name or secret word:</label>
            <input type="text" id="word" name="word" required><br><br>

            <button type="submit">Solve the puzzle</button>
        </form>
    </body>
</html>
