import random
import string
from datetime import datetime


def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ""

    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return None

    password = "".join(random.choice(characters) for _ in range(length))
    return password


print("=== Password Generator ===")

length = int(input("Enter password length: "))

print("\nChoose character types:")
print("1 - Letters")
print("2 - Numbers")
print("3 - Symbols")
print("Write choices together (example: 123 or 12): ")

choices = input("Your choice: ")

use_letters = "1" in choices
use_numbers = "2" in choices
use_symbols = "3" in choices

result = generate_password(length, use_letters, use_numbers, use_symbols)

if result:
    print("\nGenerated Password:")
    print(result)

    with open("passwords.txt", "a") as f:
        f.write(f"{datetime.now()} --> {result}\n")

    print("\nSaved in file: passwords.txt")
else:
    print("You must select at least one option!")
