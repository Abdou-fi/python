import random
import string
number  = int(input("Enter the total numbers of characters in the password: "))
letters = int(input("Enter the total number of letters in the password: "))
numbers = int(input("Enter the total number of numbers in the password: "))
symbols = int(input("Enter the total number of symbols in the password: "))
if letters+numbers+symbols!=number:
    print("The total number of characters in the password is not equal to the sum of the total nembers of letters, "
          "numbers and symbols.")
else :
    password = []
    lett = random.choices(string.ascii_letters,k=letters)
    num = random.choices(string.digits,k=numbers)
    sym = random.choices(string.punctuation,k=symbols)
    t = lett + num + sym
    random.shuffle(t)
    password ="".join(t)
    print(f"The password is: {password}")

