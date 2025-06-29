#################################################################################
#  A. Filali       2025-06-21                                                   #
#  dictionary                                                                   #
#                                                                               #
#  This script demonstrates the use of the dictionary in Python.                #
#  Dictionaries are a built-in data type in Python that store key-value pairs.  #
#  They are unordered, mutable, and indexed by keys,                            #
#  allowing for fast lookups and modifications.                                 #       
#  Keys must be unique and immutable (which means you can use strings,          #
#  numbers, or tuples as dictionary keys).                                      #
#  Values, on the other hand, can be of any data type and can be duplicated.    #
#  Dictionaries are defined using curly braces {}                               #
#  with key-value pairs separated by colons.                                    #
#################################################################################

# create a dictionary
print('\n1. -------------------------------------------------')
my_dict = {
    'name': 'Amine',
    'age': 26,
    'city': 'Biskra'
}
# print the dictionary
print(my_dict)             # Output: {'name': 'Amine', 'age': 26, 'city': 'Biskra'}

# Accessing Values
print('\n2. -------------------------------------------------')
nom = my_dict['name']      # 'Amine'
age = my_dict.get('age')   # 26
ville = my_dict['city']    # 'Biskra'
# print the values
print(nom)                 # Output: Amine
print(age)                 # Output: 26
print(ville)               # Output: Biskra    

# Adding or Updating Values
print('\n3. -------------------------------------------------')
my_dict['country'] = 'Algeria'  # Adding a new key-value pair
my_dict['age'] = 27             # Updating an existing key-value pair
# print the updated dictionary  
print(my_dict)                  # Output: {'name': 'Amine', 'age': 27, 'city': 'Biskra', 'country': 'Algeria'}

# Removing items
print('\n4. -------------------------------------------------')
del my_dict['city']            # Remove a key-value pair by key
print(my_dict)                 # Output: {'name': 'Amine', 'age': 27, 'country': 'Algeria'}
my_dict.pop('age')             # Remove a key-value pair and return the value
print(my_dict)                 # Output: {'name': 'Amine', 'country': 'Algeria'}

# iterating through a dictionary
print('\n5. -------------------------------------------------')
for key, value in my_dict.items():
    print(f"{key}: {value}")  # Output: name: Amine, country: Algeria

# Dictionary Methods
print('\n6. -------------------------------------------------')
keys = my_dict.keys()          # Get all keys
print(keys)                    # Output: dict_keys(['name', 'country'])
values = my_dict.values()      # Get all values
print(values)                  # Output: dict_values(['Amine', 'Algeria'])

# Dictionary Comprehension 
print('\n7. -------------------------------------------------')
squared_dict = {x: x**2 for x in range(5)}  # Create a dictionary with numbers as keys and their squares as values
print(squared_dict)                         # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Merging Dictionaries
print('\n8. -------------------------------------------------')
another_dict = {'city': 'ouargla'}
merged_dict = {**my_dict, **another_dict} # Merges two dictionaries
print(merged_dict)                        # Output: {'name': 'Amine', 'country': 'Algeria', 'city': 'ouargla'}

# checking for existence of a key
print('\n9. -------------------------------------------------')
exists = 'name' in my_dict  # Check if a key exists
print(exists)               # Output: True

# checking for existence of a value
print('\n10. ------------------------------------------------')
value_exists = 'Amine' in my_dict.values()  # Check if a value exists
print(value_exists)         # Output: True

# dictionary length
print('\n11. ------------------------------------------------')
dict_length = len(my_dict)  # Get the number of key-value pairs
print(dict_length)          # Output: 2 (after removing 'age' and 'city

# Copying a Dictionary
print('\n12. ------------------------------------------------')
copied_dict = my_dict.copy()  # Create a shallow copy of the dictionary
print(copied_dict)            # Output: {'name': 'Amine', 'country': 'Algeria'}

# Dictionary with Mixed Data Types
print('\n13. ------------------------------------------------')
mixed_dict = {
    'name': 'Amine',
    'age': 26,
    'is_student': True,
    'grades': [85, 90, 95],
    'address': {'city': 'Biskra', 'country': 'Algeria'}
}
print(mixed_dict)  # Output: {'name': 'Amine', 'age': 26, 'is_student': True, 'grades': [85, 90, 95], 'address': {'city': 'Biskra', 'country': 'Algeria'}}

# Nested Dictionaries
print('\n14. ------------------------------------------------')
nested_dict = {
    'person1': {'name': 'Amine', 'age': 26},
    'person2': {'name': 'Ahmed', 'age': 30}
}
print(nested_dict)  # Output: {'person1': {'name': 'Amine', 'age': 26}, 'person2': {'name': 'Ahmed', 'age': 30}}

#create an empty dictionary
print('\n15. ------------------------------------------------')
empty_dict = {}           # Create an empty dictionary  
print(empty_dict)         # Output: {}  

# Adding items to an empty dictionary
print('\n16. ------------------------------------------------') 
empty_dict['name'] = 'Amine'  # Add a key-value pair to the empty dictionary
empty_dict['age'] = 26        # Add another key-value pair
print(empty_dict)              # Output: {'name': 'Amine', 'age': 26}

# Clearing a dictionary
print('\n17. ------------------------------------------------') 
empty_dict.clear()  # Clear all items from the dictionary
print(empty_dict)    # Output: {}

# Dictionary with Tuples as Keys
print('\n18. ------------------------------------------------')
tuple_key_dict = {(1, 2): 'A', (3, 4): 'B'}  # Create a dictionary with tuples as keys
print(tuple_key_dict)   # Output: {(1, 2): 'A', (3, 4): 'B'}
# Accessing values using tuple keys
print(tuple_key_dict[(1, 2)])  # Output: A  

# Dictionary with Lists as Values
print('\n19. ------------------------------------------------')
list_value_dict = {'numbers': [1, 2, 3]}  # Create a dictionary with a list as a value
print(list_value_dict)  # Output: {'numbers': [1, 2, 3]}
# Accessing the list value
print(list_value_dict['numbers'])  # Output: [1, 2, 3]

# Merging two lists into a dictionary
print('\n20. ------------------------------------------------')
x = [1, 2, 3]
y = [4, 5, 6] 
print(dict(zip(x,y)))