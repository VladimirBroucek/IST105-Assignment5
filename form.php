<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Treasure Hunt</title>
</head>
<body>
<h1>Assigment 5 - Treasure Hunt</h1>
<form action="process.php" method="POST">
    <label for="number">Enter a number (e.g., birth year):</label>
    <input type="number" id="number" name="number" required><br><br>

    <label for="text">Enter a text message (e.g., name or secret word):</label>
    <input type="text" id="text" name="text" required><br><br>

    <button type="submit">Solve the Puzzle</button>
</form>
</body>
</html>