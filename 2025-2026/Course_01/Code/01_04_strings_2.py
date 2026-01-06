print("hello world")
print('hello world')
print("hello \\ world")
print("hello 'world'")
print('hello "world"')

name = "Abesselam"      # string
print("name is of type", type(name), "it's value is: ", name)

age = 30                # integer
print("age is of type", type(age), "it's value is: ", age)

temperature = 21.4      # float use . not ,
print("temperature is of type", type(temperature), "it's value is: ", temperature)

paid_membership = True          # boolean
print("'paid_membership' is of type", type(paid_membership), "it's value is: ", paid_membership)

point1 = complex(1, 2)  # complex number
print("point1 is of type", type(point1), "it's value is: ", point1)

point2 = 1+5j           # complex number
print("point2 is of type", type(point2), "it's value is: ", point2)

print(type(name), type(age), type(temperature), type(has_finished), type(point2))

print('Hello', name, 'how are you?')

name = input("type your name : ")
print(f"hello {name} how are you")
print("hello {} how are you".format(name))

print("hello \nworld")   # \n is used to create a new line
print("hello\tworld")    # \t is used to create a tab
print("hello\bworld")    # \b is used to delete the previous character
print("hello \r world")  # \r is used to replace the previous text
print("hello \a world")  # alarm
print("hello \v world")  # vertical tab
print("hello \f world")  # form feed

print("hello A")
print("hello \x42")     # \x is used to create a character with the hexadecimal value