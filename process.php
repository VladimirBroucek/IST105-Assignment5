<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Puzzle Results</title>
</head>
<body>
<h1>Puzzle Results</h1>
<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $number = escapeshellarg($_POST['number']);
    $text = escapeshellarg($_POST['text']);

    $command = "python3 process.py $number $text";
    $output = shell_exec($command);

    if ($output === null) {
        echo "<p>Error: Unable to execute the Python script.</p>";
    } else {
        echo "<pre>$output</pre>";
    }
} else {
    echo "<p>Error: Invalid request method.</p>";
}
?>
</body>
</html>