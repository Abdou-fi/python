# x // y - integer division or Euclidian division
# x % y - remainder of the division
from text_functions import glass
while True:
    try:    
        x=int(input("Enter the integer to be divided: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")
while True:
    try:    
        y=int(input("Enter the dividor: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

glass (f"{x} // {y} = {x//y} {chr(215)} {y}" if x % y == 0 else f"{x} // {y} = ({x//y} {chr(215)} {y}) + {x % y}")
