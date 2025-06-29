###############################################################################
#  A. Filali       2025-06-21                                                 #
#  list                                                                       #
#                                                                             #
#  Lists are a built-in data type in Python that store multiple items in a    #
#  single variable. Lists are mutable.                                        #
#  They can contain elements of different data types, including strings,      #
#  numbers, and even other lists. They can contain duplicate elements         #
#  and are defined using square brackets.                                     #
###############################################################################

# Create a list
print('\n1. -------------------------------------------------') 
my_list = [1, 2, 3, 4, 5]
# Print the list
print(my_list)  # Output: [1, 2, 3, 4, 5]

# Accessing elements
print('\n2. -------------------------------------------------') 
print(my_list[0])  # Output: 1
print(my_list[2])  # Output: 3

# Slicing a list
print('\n3. -------------------------------------------------')
sliced_list = my_list[1:4]  # Slice the list from index 1 to 3
# Print the sliced list
print(sliced_list)  # Output: [2, 3, 4]

# Slicing with step
print('\n4. -------------------------------------------------')
sliced_list = my_list[::2]  # Slice the list with a step of 2
# Print the sliced list
print(sliced_list)  # Output: [1, 3, 5]

# Negative indexing
print('\n5. -------------------------------------------------')
negative_index = my_list[-1]  # Access the last element
# Print the negative index  
print(negative_index)  # Output: 5

# Negative slicing
print('\n6. -------------------------------------------------')
negative_sliced_list = my_list[-3:-1]  # Slice the list from index -3 to -2
# Print the negative sliced list
print(negative_sliced_list)  # Output: [3, 4]

# Modifying elements
print('\n7. -------------------------------------------------')
my_list[0] = 10  # Modify the first element
# Print the modified list
print(my_list)  # Output: [10, 2, 3, 4, 5]

# Adding elements
print('\n8. -------------------------------------------------')
my_list.append(6)  # Add an element to the end of the list
# Print the list after adding an element
print(my_list)  # Output: [10, 2, 3, 4, 5, 6]

# Removing elements
print('\n9. -------------------------------------------------') 
my_list.remove(3)  # Remove the element with value 3
# Print the list after removing an element
print(my_list)  # Output: [10, 2, 4, 5, 6]  
# Inserting elements
my_list.insert(1, 4)  # Insert the value 4 at index 1
# Print the list after inserting an element
print(my_list)  # Output: [10, 4, 2, 4, 5, 6]
# Inserting an element at the end
my_list.append(2)  # Append the value 2 to the end of the list
# Print the list after appending an element
print(my_list)  # Output: [10, 4, 2, 4, 5, 6, 2]    
# popping an element
my_list.pop()  # Remove and return the last element of the list
# Print the list after popping an element
print(my_list.pop())  # Output: 2
# Print the list after popping an element   
print(my_list)  # Output: [10, 4, 2, 4, 5, 6]

# List Methods
print('\n10. -------------------------------------------------')    
# Get the length of the list
length = len(my_list)  
# Print the length of the list
print(length)  # Output: 5
# Sort the list
my_list.sort()  # Sort the list in ascending order
# Print the sorted list
print(my_list)  # Output: [2, 4, 5, 6, 10]
# Reverse the list
my_list.reverse()  # Reverse the order of the list
# Print the reversed list
print(my_list)  # Output: [10, 6, 5, 4, 2]

# Count occurrences of an element
print('\n11. -------------------------------------------------')
count_of_2 = my_list.count(2)  # Count how many times 2 appears in the list
# Print the count of 2  
print(count_of_2)  # Output: 1

# Find the index of an element
print('\n12. -------------------------------------------------')
index_of_5 = my_list.index(5)  # Find the index of the first occurrence of 5
# Print the index of 5
print(index_of_5)  # Output: 2

# List Comprehension
print('\n13. -------------------------------------------------')    
squared_list = [x**2 for x in my_list]  # Create a new list with squares of elements
# Print the squared list
print(squared_list)  # Output: [100, 36, 25, 16, 4]

# Merging Lists
print('\n14. -------------------------------------------------')    
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = list1 + list2  # Merge two lists
# Print the merged list
print(merged_list)  # Output: [1, 2, 3, 4, 5, 6]

# Checking for existence of an element
print('\n15. -------------------------------------------------')
exists = 4 in my_list  # Check if 4 is in the list
# Print the result
print(exists)  # Output: True

# iterating through a list
print('\n16. -------------------------------------------------')
for item in my_list:
    print(item, end=' ')  # Print each item in the list
print()  # for a new line

# List with Mixed Data Types
print('\n17. -------------------------------------------------')    
mixed_list = [1, "two", 3.0, True, [5, 6]]  # Create a list with mixed data types
# Print the mixed list
print(mixed_list)   # Output: [1, 'two', 3.0, True, [5, 6]]

# Nested Lists
print('\n18. -------------------------------------------------')    
nested_list = [[1, 2], [3, 4], [5, 6]]  # Create a nested list
# Print the nested list
print(nested_list)  # Output: [[1, 2], [3, 4], [5, 6]]

# Accessing elements in a nested list
print('\n19. -------------------------------------------------')
print(nested_list[0])  # Output: [1, 2]
print(nested_list[1][0])  # Output: 3
# Print the accessed nested element
print(nested_list[1][0])  # Output: 3

# List unpacking & packing
print('\n20. -------------------------------------------------')    
a, b, c, d, e = my_list  # Unpacking the list into variables
# Print the unpacked variables
print(a, b, c, d, e)  # Output: 10 4 2 4 5  
packed_list = [a, b, c, d, e]  # Packing the variables back into a list
# Print the packed list
print(packed_list)  # Output: [10, 4, 2, 4, 5]

