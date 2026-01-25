 #*************************************************Password Generator 1****************************************************
# Algorithm Explanation()
# Step 1) Import Necessary Modules: We import the random and string modules to generate random numbers and strings.
# Step 2) Define the Function: We define a function called generate_password which takes no arguments.
# Step 3) Generate Password Length: We use random.randint(3, 25) to generate a random length for the password between 3 and 25 
#          characters.
# Step 4) Define Characters: We define the set of characters that can be used in the password, including upper and lower 
#          case letters, digits, and punctuation symbols.
# Step 5) Generate Password: We use a list comprehension and random.choice to randomly select characters from the defined 
#          set and concatenate them to form the password.
# Return Password: The function returns the generated password.
# Print Password: We call the generate_password function and print the generated password.

import random
import string
print(" ########################### Welcom to the password Generator ######################## ")

def generate_password():
    length = random.randint(3, 25)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

print(generate_password())
##############################################################################################################################@
#*************************************************Password Generator 2(My project 1)****************************************************

#  Write a program to generate a random passwords with the following conditions:
# a. The user should be able to specify the length and the number of the password desired.
# b. The password user must choose the number of letters, characters and digits.  
# c. The program should ensures that the generated passwords verifies the specified conditions.
# d. The user should be able to put all passwords in fichier.txt.

import string
from random import  choice, choices
print(" ########################### Welcom to the Password generator ######################## ")
Num=int(input("Enter the numbers of Passwords: ")) #How many passwords de you want
length_1=int(input("Enter the length of the desired Password: "))
n_letters=int(input("Enter the number of letters in the Password: "))
n_numbers=int(input("Enter the number of numbers in the Password: "))
n_ponctus=int(input("Enter the number of characters in the Password: "))
 
f=open('Password.txt','w')
if length_1 != n_letters+n_numbers+n_ponctus :
   print("invalid inputs, the sum of letters, numbers and ponctuations is different to the length of the Password ")
else:
   stop=0
   while True:
    stop+=1  
    characters_1 =(random.choices(string.ascii_letters,k=n_letters)+random.choices(string.digits,k=n_numbers)+random.choices(string.punctuation,k=n_ponctus))
    password_1 = ''.join(random.choice(characters_1) for i in range(length_1)) 
    print(password_1)
    for w in password_1+'\n':
      f.write(w)
    if stop==Num :
      break  
    
 ######################################################Guessing a random number(My project 2)*********************************************************
#*************************************************************************************************************************
#  Write a program to guess a random number with the following conditions:
# a. The user should be able to specify the interval of the random number .
# b. The user must choose a rondom number in the interval was specified above.  
# c. The program should helps the user to guess the desired number.
# d. At the end, the user should print the random number.


import random
print(" ########################### Welcom to the Guessing a random number ######################## ")

lowest_number=int(input("Enter the minimal value of the desired number :"))
highest_number=int(input("Enter the maximal value of the desired number : "))
Number=random.randrange(lowest_number,highest_number)
guess=int(input("Enter your guessing number :"))

while guess!= Number :
   if guess < Number :
      print("The guessing number is lower ")
      guess=int(input("Try to guess another number :"))
   else: 
      print("The guessing number is higher")
      guess=int(input("Try to guess another number :"))
print("############# WELL DONE, you get the right number ##############")
print("The number is", Number)


################################################## My project3###########################################################@

#*************************************************Password Generator 2(My project 1)****************************************************
#  Write a program to generate a  random passwords with the following conditions:

# a) The program should be generated a password using the standard Python library for creating graphical
#     user interfaces (GUIs) """Tkinter """ employing: Geometry managers, Event loop, Widgets,,,,,,,,
# b) The program prompts the user for the desired password length include numbers, letters and symbols. 
# c)  The progrem allows the user to write their name and password lenght.
# Note: The program assumes that the user could copy the generated password and delete all the information to repeat it again.


import secrets
import string
import tkinter as tk
from tkinter import *
from tkinter import messagebox

def generate_password():
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(int(length_entry.get())))
    G_password.delete(0, tk.END)
    G_password.insert(0, password)
    name= username_entry.get()

    if name=="":
          messagebox.showerror("Error","Name cannot be empty") 
         
    if name.isalpha()==False:
          messagebox.showerror("Error","Name must be a string")
          
      
def copy_to_clipboard(): 
    root.clipboard_clear() 
    root.clipboard_append(G_password.get())


def clear_all():
  username_entry.delete(0, 25)
  G_password.delete(0, 25)
  length_entry.delete(0, 25)


root = tk.Tk()
root.geometry("600x500")
root.title("Password generator")

empty0 = Label(text="")
empty0.grid(row=0, column=0, columnspan=2)

Button1=tk.Label(text="Password Generator", fg='darkblue', font='arial 20 bold underline')
Button1.grid(row=1, column=1,columnspan=2)

empty1 = Label(text="")
empty1.grid(row=2, column=0, columnspan=2)
        
empty2 = Label(text="")
empty2.grid(row=3, column=0, columnspan=2)    
   

username_lable =tk.Label(text="Enter user name: ", font='times 15')
username_lable.grid(row=4, column=0)

username_entry = Entry( font='times 15', bd=6 ,relief='ridge',justify='center' )
username_entry.grid(row=4, column=1)
 

empty4 = Label(text="")
empty4.grid(row= 5, column=0, columnspan=2)

length_lable= tk.Label(text="Enter password length: ", font='times 15')
length_lable.grid(row=6, column=0)

length_entry = tk.Entry( font='times 15', bd=6, relief='ridge',justify='center' )
length_entry.grid(row=6, column=1)
        
empty3 = Label(text="")
empty3.grid(row=7, column=0,columnspan=2)
 
Generated_password_lable = tk.Label(text="Generated password: ", font='times 15')
Generated_password_lable.grid(row=8, column=0)

G_password =tk.Entry( font='times 15', bd=6, relief='ridge', fg='darkgreen')
G_password.grid(row=8, column=1)

empty5 = Label(text="")
empty5.grid(row=9, column=0, columnspan=2)
  
Password =tk.Button(root, text="GENERATE PASSWORD", bd=3, relief='solid', padx=1, pady=1, font='forte 15 bold', fg='blue', bg='darkblue', command=generate_password)
Password.grid(row=11, column=1)

copy_button = tk.Button(root, text="COPY", bd=3, relief='solid', padx=1, pady=1, font='forte 15 bold', fg='blue', bg='darkblue', command=copy_to_clipboard)
copy_button.grid(row=15, column=1)

clear_button= tk.Button(root, text="CLEAR ALL", bd=3, relief='solid', padx=1, pady=1, font='forte 15 bold', fg='blue', bg='darkblue', command=clear_all)
clear_button.grid(row=20, column=1)
 

root.mainloop()







 
