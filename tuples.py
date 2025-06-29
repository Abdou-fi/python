###############################################################################
#  A. Filali       2025-06-21                                                 #
#  tuple                                                                      #
#                                                                             #
#  Tuples are a built-in data type in Python that store ordered collections   #
#  of elements. They are immutable, meaning that once created, their elements #
#  cannot be changed.                                                         #
###############################################################################

# Create a tuple
print('\n1. -------------------------------------------------')
my_tuple = (1, 2, 3, 4, 5)
# Print the tuple
print(my_tuple)  # Output: (1, 2, 3, 4, 5)

# Accessing elements
print('\n2. -------------------------------------------------')
first_element = my_tuple[0]  # Access the first element 
second_element = my_tuple[1]  # Access the second element
# Print the accessed elements
print(first_element)  # Output: 1   
print(second_element)  # Output: 2

# Slicing a tuple
print('\n3. -------------------------------------------------')
sliced_tuple = my_tuple[1:4]  # Slice the tuple from index 1 to 3
# Print the sliced tuple
print(sliced_tuple)  # Output: (2, 3, 4)

# Slicing with step
print('\n4. -------------------------------------------------')
sliced_tuple_step = my_tuple[::2]  # Slice the tuple with a step
# Print the sliced tuple with step
print(sliced_tuple_step)  # Output: (1, 3, 5)

# Negative indexing
print('\n5. -------------------------------------------------')
negative_index = my_tuple[-1]  # Access the last element
print(negative_index)  # Output: 5  

# negative slicing
print('\n6. -------------------------------------------------')
negative_sliced_tuple = my_tuple[-3:-1]  # Slice the tuple from index -3 to -2
# Print the negative sliced tuple       
print(negative_sliced_tuple)  # Output: (3, 4)

# Negative slicing with step
print('\n7. -------------------------------------------------')
negative_sliced_tuple_step = my_tuple[-3::-1]  # Slice the tuple from index -3 to the beginning with a step
# Print the negative sliced tuple with step
print(negative_sliced_tuple_step)  # Output: (4, 3)

#negative slicing with step and negative step
print('\n8. -------------------------------------------------')
negative_sliced_tuple_step_neg = my_tuple[-1:-4:-1]  # Slice the tuple from index -1 to -3 with a negative step
# Print the negative sliced tuple with step and negative step   
print(negative_sliced_tuple_step_neg)  # Output: (5, 4, 3)

# Negative slicing with step and negative step
print('\n9. -------------------------------------------------')
negative_sliced_tuple_step_neg2 = my_tuple[-1:-4:-2]  # Slice the tuple from index -1 to -3 with a negative step of 2
# Print the negative sliced tuple with step and negative step of 2  
print(negative_sliced_tuple_step_neg2)  # Output: (5, 3)


# Tuple with mixed data types
print('\n10. -------------------------------------------------')    
mixed_tuple = (1, "Hello", 3.14, True)  # A tuple with mixed data types
# Print the mixed tuple
print(mixed_tuple)  # Output: (1, 'Hello', 3.14, True)

# Nested tuples
print('\n11. -------------------------------------------------')
nested_tuple = (1, (2, 3), (4, 5))
# Print the nested tuple
print(nested_tuple)  # Output: (1, (2, 3), (4, 5))

# Accessing elements in a nested tuple
print('\n12. -------------------------------------------------')
nested_element = nested_tuple[1][0]  # Access the first element of the second tuple
# Print the accessed nested element
print(nested_element)  # Output: 2

# Tuple unpacking & packing
print('\n13. -------------------------------------------------')
a, b, c, d, e = my_tuple  # Unpacking the tuple into variables
# Print the unpacked variables
print(a, b, c, d, e)  # Output: 1 2 3 4 5
packed_tuple = (a, b, c, d, e)  # Packing the variables back into a tuple
# Print the packed tuple    
print(packed_tuple)  # Output: (1, 2, 3, 4, 5)

# Tuple methods
print('\n14. -------------------------------------------------')    
# Count the occurrences of an element
count_of_2 = my_tuple.count(2)  # Count how many times 2 appears in the tuple
# Print the count of 2
print(count_of_2)  # Output: 1
# Find the index of an element
index_of_3 = my_tuple.index(3)  # Find the index of the first occurrence of 3
# Print the index of 3
print(index_of_3)  # Output: 2

# Length of a tuple
print('\n15. -------------------------------------------------')
length_of_tuple = len(my_tuple)  # Get the length of the tuple
# Print the length of the tuple
print(length_of_tuple)  # Output: 5

# Concatenating tuples
print('\n16. -------------------------------------------------')
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2 # Concatenate two tuples
# Print the concatenated tuple      
print(concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 6)

# Repeating tuples
print('\n17. -------------------------------------------------')
repeated_tuple = tuple1 * 3  # Repeat the tuple 3 times
# Print the repeated tuple
print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Checking membership in a tuple
print('\n18. -------------------------------------------------')
my_tuple = (1, 2, 3, 4, 5)
# Check if an element exists in the tuple
element_exists = 3 in my_tuple
# Print the result
print(element_exists)  # Output: True

# Check if an element does not exist in the tuple
print('\n19. -------------------------------------------------')
element_not_exists = 6 not in my_tuple  # Check if 6 does not exist in the tuple
# Print the result
print(element_not_exists)  # Output: True   

# Iterating through a tuple
print('\n20. -------------------------------------------------')    
for item in my_tuple:
    print(item)  # Output: 1 2 3 4 5    

# Tuple as a key in a dictionary
print('\n21. -------------------------------------------------')    
my_dict = {(1, 2): "Hello", (3, 4): "World"}
# Print the dictionary
print(my_dict)  # Output: {(1, 2): 'Hello', (3, 4): 'World'}

# Accessing a value using a tuple key
print('\n22. -------------------------------------------------')
value = my_dict[(1, 2)]  # Access the value associated with the key (1, 2)  
# Print the accessed value
print(value)  # Output: Hello

# Tuple as a return value from a function
print('\n23. -------------------------------------------------')    
def get_tuple():
    return (1, 2, 3), (4, 5, 6)  # Return a tuple
result_tuple1, result_tuple2 = get_tuple()  # Unpack the returned tuple
# Print the unpacked tuples
print(result_tuple1)  # Output: (1, 2, 3)
print(result_tuple2)  # Output: (4, 5, 6)

# Tuple as a single element in a tuple
print('\n24. -------------------------------------------------')    
single_element_tuple = (42,)  # Create a tuple with a single element
# Print the single element tuple
print(single_element_tuple)  # Output: (42,)
# Checking if a single element tuple is created correctly
print(type(single_element_tuple))  # Output: <class 'tuple'>

# tuples are immutable
print('\n25. -------------------------------------------------')
try:
    single_element_tuple[0] = 100  # Attempt to change the first element
except TypeError as e:
    print(e)  # Output: 'tuple' object does not support item assignment
# Demonstrating immutability of tuples
print(single_element_tuple)  # Output: (42,)

# Using tuples in a function
print('\n26. -------------------------------------------------')
def process_tuple(t):
    return sum(t), max(t), min(t)  # Return the sum, max, and min of the tuple
result_sum, result_max, result_min = process_tuple(my_tuple)  # Process the tuple
# Print the results
print(result_sum)  # Output: 15
print(result_max)  # Output: 5
print(result_min)  # Output: 1  

# Tuple comprehension
print('\n27. -------------------------------------------------')
tuple_comprehension = tuple(x * 2 for x in my_tuple)  # Create a new tuple with doubled values
# Print the result of the tuple comprehension
print(tuple_comprehension)  # Output: (2, 4, 6, 8, 10)  


