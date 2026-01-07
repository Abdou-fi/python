import random
print("Hi welcome to the game, This is a number guessing game.")
print("You got 5 chances to guess the number. Let's start the game")
random_number = random.randrange(15)
chances = 5
guess_counter = 0
while guess_counter < chances:
    guess_counter = guess_counter + 1
    my_guess = int(input('Please Enter your Guess : '))
    if my_guess == random_number:
        print(f'The number is {random_number} and you found it right !! in the {guess_counter} attempt')
        break
    elif guess_counter >= chances and my_guess != random_number:
        print(f'Oops sorry, The number is {random_number} better luck next time')
    elif my_guess > random_number:
        print('Your guess is higher ')
    elif my_guess < random_number:
        print('Your guess is lesser')
