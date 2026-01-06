# the * and ** operators

def unpacking_function(a, b, c):
    print(a, b, c)
    
def discriminant (a, b, c):
    return b**2 - 4*a*c

# unpacking a list
my_list = [1, 2, 3]
discriminant(*my_list)
print(discriminant(*my_list))


# unpacking a tuple
my_tuple = (4, 5, 6)
discriminant(*my_tuple)

# unpacking a dictionary
my_dict = {'a': 7, 'b': 8, 'c': 9}
discriminant(**my_dict)

# unpacking a string
my_string = "hello"
print(*my_string)

# unpacking a set
my_set = {10, 11, 12}
discriminant(*my_set)

# unpacking a range
my_range = range(13, 16)
discriminant(*my_range)

# unpacking a generator
my_generator = (x for x in range(17, 20))
discriminant(*my_generator)

# unpacking a dictionary with keyword arguments
my_dict = {'a': 21, 'b': 22, 'c': 23}
discriminant(**my_dict)