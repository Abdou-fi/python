# name = "Amine"      # string
# print("name is of type", type(name), "it's value is:" , name)

# age = 30                # integer
# print("age is of type", type(age), "it's value is: ", age)

# temperature = 21.4      # float use . not ,
# print("temperature is of type", type(temperature), "it's value is: ", temperature)

# paid_membership = True          # boolean
# print("'paid_membership' is of type", type(paid_membership), "it's value is: ", paid_membership)

# point1 = complex(1, 2)  # complex number
# print("point1 is of type", type(point1), "it's value is: ", point1)

# point2 = 1+5j           # complex number
# print("point2 is of type", type(point2), "it's value is: ", point2)

# print('Hello', name, 'how are you?')

name = input("type your name : ")
print('Hello', name, 'how are you?')
print(f"hello {name} how are you?")
print("hello {} how are you?".format(name))

age = int(input("How old are you? "))
print(f"hello {name} you are {age} years old")
print("hello {} you are {} years old".format(name, age))
