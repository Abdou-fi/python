import random
secret_number = random.randint(1, 100)
attempts = 5
print("You have 5 attempts to guess the number")
for i in range(attempts):
    guess = int(input("Enter any number: "))
    if guess == secret_number:
        print("You guessed it right!!")
        break
    elif guess < secret_number:
        print("Too low")  
    else:
        print("Too high")  
else:
    print("Answer:", secret_number)