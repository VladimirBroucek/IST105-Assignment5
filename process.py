import cgi
import math
import random

def number_puzzle(num):
    num = int(num)
    if num % 2 == 0:
        return f"Even number. Square root: {math.sqrt(num):.2f}"
    else:
        return f"Odd number. Cube: {num ** 3}"

def text_puzzle(text):
    binary_text = ' '.join(format(ord(char), '08b') for char in text)
    vowels = sum(1 for char in text.lower() if char in "aeiou")
    return binary_text, vowels

def treasure_hunt():
    treasure_number = random.randint(1, 100)
    attempts = 0
    guessed = False

    while attempts < 5:
        guess = random.randint(1, 100)
        if guess == treasure_number:
            guessed = True
            break
        attempts += 1

    return "You found the treasure!" if guessed else "You failed to find the treasure!"

form = cgi.FieldStorage()
year = form.getvalue("year")
word = form.getvalue("word")

if year is None or word is None:
    print("Content-type: text/html\n")
    print("<p>Error: Missing input values.</p>")
else:
    num_result = number_puzzle(year)
    binary_text, vowel_count = text_puzzle(word)
    treasure_result = treasure_hunt()

    print("Content-type: text/html\n")
    print("<html><head><title>Treasure Hunt Result</title></head><body>")
    print(f"<p>Number Puzzle Result: {num_result}</p>")
    print(f"<p>Binary Text: {binary_text}</p>")
    print(f"<p>Vowel Count: {vowel_count}</p>")
    print(f"<p>{treasure_result}</p>")
    print("</body></html>")
