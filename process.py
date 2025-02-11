import sys
import math
import random

def number_puzzle(number):
    if number % 2 == 0:
        result = f"The number {number} is even. Square root: {math.sqrt(number):.2f}"
    else:
        result = f"The number {number} is odd. Cubed: {number ** 3}"
    return result

def text_puzzle(text):
    binary_text = ' '.join(format(ord(char), '08b') for char in text)

    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in text if char in vowels)

    return f"Binary Encoding: {binary_text}\nVowel Count: {vowel_count}"

def treasure_hunt():
    target = random.randint(1, 100)
    attempts = 5
    guess = None

    for _ in range(attempts):
        guess = random.randint(1, 100)  # Simulated guess
        if guess == target:
            return f"You guessed the number {target} correctly in {_+1} attempts! 🎉 You win the treasure!"

    return f"Sorry! The correct number was {target}. Better luck next time! ❌"

def main():
    if len(sys.argv) != 3:
        print("Error: Invalid input")
        return

    try:
        number = int(sys.argv[1])
        text = sys.argv[2]
    except ValueError:
        print("Error: Invalid input values")
        return

    num_result = number_puzzle(number)
    text_result = text_puzzle(text)
    treasure_result = treasure_hunt()

    print("<html>")
    print("<head><title>Puzzle Results</title></head>")
    print("<body style='background-color: #fdf4e3;'>")
    print("<h2>Number Puzzle Result</h2>")
    print(f"<p>{num_result}</p>")
    print("<h2>Text Puzzle Result</h2>")
    print(f"<p>{text_result}</p>")
    print("<h2>Treasure Hunt</h2>")
    print(f"<p>{treasure_result}</p>")
    print("</body>")
    print("</html>")

if __name__ == "__main__":
    main()