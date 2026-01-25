#  Number Guessing Game: Create a game where the computer picks a random number, 
# and the user tries to guess it. The program provides hints if the guess is too high or too low.

import random

# Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)

# Initialize the number of attempts
attempts = 0

# Start the game
print("Welcome to the Number Guessing Game!")
print("I have picked a number between 1 and 100. Can you guess it?")

while True:
    # Get the user's guess
    guess = int(input("Enter your guess: "))
    attempts += 1

    # Check if the guess is correct
    if guess == number_to_guess:
        print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
        break
    elif guess < number_to_guess:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
        
print("Thank you for playing!") 