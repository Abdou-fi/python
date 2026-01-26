import random

# Define range
LOWER_BOUND = 1
UPPER_BOUND = 100

secret_number = random.randint(LOWER_BOUND, UPPER_BOUND)

print(f"Guess a number between {LOWER_BOUND} and {UPPER_BOUND}.")

while True:
    guess = int(input("Enter your guess: "))
    
    if guess < secret_number:
        print("Too low! Try a higher number.")
    elif guess > secret_number:
        print("Too high! Try a lower number.")
    else:
        print("Congratulations! You guessed it right!")
        break