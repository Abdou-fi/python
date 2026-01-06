# Declare global variable name for use in all functions
name = str(input('Enter your name: '))


# Define function to check if name contains a vowel
def has_vowel():
    if set('aeiou').intersection(name.lower()):
        print('Your name contains a vowel.')
    else:
        print('Your name does not contain a vowel.')


# Iterate over letters in name string
def print_letters():
    for letter in name:
        print(letter)

has_vowel()
print_letters()