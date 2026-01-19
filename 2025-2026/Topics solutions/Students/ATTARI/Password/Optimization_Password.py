import random
import string
from datetime import datetime

def ask_choice(text):
    while True:
        x = input(text).strip().lower()
        if x in ["y", "yes", "1", "oui"]:
            return True
        if x in ["n", "no", "0", "non"]:
            return False
        print("Please answer with y or n.")


def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
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

choice_letters = ask_choice("Include letters? (y/n): ")
choice_numbers = ask_choice("Include numbers? (y/n): ")
choice_symbols = ask_choice("Include symbols? (y/n): ")

result = generate_password(length, choice_letters, choice_numbers, choice_symbols)

if result:
    print("\nGenerated Password:")
    print(result)

    with open("passwords.txt", "a") as f:
        f.write(f"{datetime.now()} --> {result}\n")

    print("\nPassword saved in file: passwords.txt")
else:
    print("You must select at least one character type!")
