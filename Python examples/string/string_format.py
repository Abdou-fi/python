# python string format() method

name_input = input('enter your name:')
age_input = int(input('enter your age:'))
                 
message1 = "Hello, I am {} and I am {} years old.".format(name_input, age_input)
print(message1)

message2 = "Hello, I am {name} and I am {age} years old.".format(age = age_input, name = name_input)
print(message2)


