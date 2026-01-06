import pyfiglet
import random 
import time
import os

def clear_screen():
    # Function to clear the screen in cmd
    os.system('cls' if os.name == 'nt' else 'clear')

def happy_birthday():
    colors = ['red', 'green', 'blue', 'yellow', 'magenta','rose', 'cyan', 'white']
    ascii_art = pyfiglet.figlet_format("Happy Birthday, Mehdi", font="slant")
    while True:
        for color in colors:
            # Print the text in different colors to create blinking effect
            clear_screen()
            print(pyfiglet.figlet_format("Happy Birthday, Mehdi", font="slant", justify="center"))
            print("\033[{}m".format(random.randint(31, 37)), end='')
            time.sleep(0.5)
            clear_screen()
            time.sleep(0.5)

happy_birthday()