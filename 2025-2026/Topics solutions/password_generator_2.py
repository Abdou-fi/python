# Password Generator: 
# A utility that generates a strong, random password based on user-specified criteria 
# like length and the inclusion of numbers, symbols, or letters.

# The program prompts the user for the desired password length and whether to include numbers and symbols. 
# It then generates a random password based on these criteria and displays it to the user. 
# The password is generated using the `random.choice()` function to select characters from the specified character set.

# Note: The program assumes that the user will input valid responses (yes/no) when prompted.


import random

def generate_password(length, include_numbers, include_symbols):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if include_numbers:
        characters += "0123456789"
    if include_symbols:
        characters += "!@#$%^&*()_+-=[]{}|;:,.<>?/"
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password

password_length = int(input("Enter the desired password length: "))

include_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
include_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

password = generate_password(password_length, include_numbers, include_symbols)
print("Generated password:", password)
