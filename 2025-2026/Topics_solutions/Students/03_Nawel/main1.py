import random
n = random.randrange(1,10)
attempts = 0
guess = int(input("Enter any number: "))
while n!= guess:
    attempts += 1
    if guess < n:
        print("Too low")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("Too high!")
        guess = int(input("Enter number again: "))
    else:
      break
print("you guessed it right!!")
print(f"Number of attempts: {attempts}")



# --------------------------------------------------------------------------------------------------------------------
# 
# Program lacks comments
# does not handle invalid inputs
# 
# --------------------------------------------------------------------------------------------------------------------