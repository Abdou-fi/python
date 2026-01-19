import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ""

    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "You must select at least one character type!"

    password = "".join(random.choice(characters) for _ in range(length))
    return password


print("=== Password Generator ===")

length = int(input("Enter password length: "))

choice_letters = input("Include letters? (y/n): ").lower() == "y"
choice_numbers = input("Include numbers? (y/n): ").lower() == "y"
choice_symbols = input("Include symbols? (y/n): ").lower() == "y"

result = generate_password(length, choice_letters, choice_numbers, choice_symbols)

print("\nGenerated Password:")
print(result)
