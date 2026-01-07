# in Python, constants are usually defined in all capital letters
# this is not enforced by Python, but it is a good practice
# Use constants in your code to make it more readable and maintainable
# for example, if you are using a constant in your code, you can change its value 
# in one place and it will be updated everywhere
# this is useful if you need to change the value of a constant in the future

# for example, if you are using a constant to represent the value of pi, 
# you can change its value in one place and it will be updated everywhere in your code
PI = 3.14
#PI = 3.14159

radius = float(input("Enter the radius of the circle: "))
area = PI * (radius ** 2)
print("The area of the circle is:", area)

# Constants to format monetary ammounts
CURRENCY_FORMAT = "DZD {:,.2f}"
#CURRENCY_FORMAT = "DAT {:,.3f}"

print(CURRENCY_FORMAT.format(1234567.89))
print(CURRENCY_FORMAT.format(123456789.123456789))

