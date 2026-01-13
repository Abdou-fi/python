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

#example of using random module
print(random.random())
print(random.randrange(15))
print(random.randint(1, 10))
print(random.choice(['apple', 'banana', 'cherry']))
print(random.sample(range(100), 10))
print(random.shuffle([1, 2, 3, 4, 5]))
print(random.uniform(1, 10))    
print(random.gauss(0, 1))
print(random.betavariate(1, 1))
print(random.expovariate(1))
print(random.gammavariate(1, 1))
print(random.lognormvariate(1, 1))
print(random.normalvariate(1, 1))
print(random.vonmisesvariate(1, 1))
print(random.paretovariate(1))
print(random.weibullvariate(1, 1))
print(random.triangular(1, 10, 5))




# random vs secrets for generating random numbers
import secrets
secure_random = secrets.SystemRandom()
random_number = secure_random.randrange(15)
print(random_number)
# Note: secrets module is used for cryptographic purposes and is more secure than random module