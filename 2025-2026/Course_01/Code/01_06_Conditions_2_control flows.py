###############################################################################
#  A. Filali       2025-06-21                                                 #
#  Control flows                                                              #
#                                                                             #
#  Control flows in Python allow you to execute certain blocks of code        #
#  based on specific conditions. The main control flow statements are:        #
#  - if statements                                                            #
#  - for loops                                                                #
#  - while loops                                                              #
#  - try/except blocks                                                        #
#  These constructs enable you to create dynamic and responsive programs.     #
###############################################################################

# If statement
print('\n1. -------------------------------------------------') 
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")


# If-elif-else statement
print('\n2. -------------------------------------------------')
y = 15  
if y > 20:
    print("y is greater than 20")
elif y > 10:
    print("y is greater than 10")
else:
    print("y is not greater than 10")

print("\n \n")

# For loop      
print('\n3. -------------------------------------------------')
for i in range(5):
    print(i)
print("\n \n")

# While loop
print('\n4. -------------------------------------------------')
j = 0
while j < 5:
    print(j)
    j += 1
print("\n \n")

# Try/except block
print('\n5. -------------------------------------------------')
try:
    z = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

print("\n \n")

#match statement
print('\n6. -------------------------------------------------')
def get_day_of_week(day):
    match day:
        case 0:
            return "Sunday"
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case _:
            return "Invalid day"

print(get_day_of_week(9))
