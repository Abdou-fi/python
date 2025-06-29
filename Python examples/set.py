###############################################################################
#  A. Filali       2025-06-21                                                 #
#  set                                                                        #
#                                                                             #
#  Sets are a built-in data type in Python that store unique elements in an   #
#  unordered collection.                                                      #
#  They are mutable, meaning that their elements can be changed.              #
###############################################################################

# Create a set
print('\n1. -------------------------------------------------')
my_set = {1, 2, 3, 4, 5}
# Print the set
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Accessing elements
print('\n2. -------------------------------------------------')
print(3 in my_set)  # Output: True
print(6 in my_set)  # Output: False

# Adding elements
print('\n3. -------------------------------------------------') 
my_set.add(6)  # Add a new element
# Print the updated set
print(my_set)  # Output: {1, 2, 3, 4, 5, 6} 

# Adding multiple elements
print('\n4. -------------------------------------------------') 
my_set.update({7, 8, 9})  # Add multiple elements
# Print the updated set 
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Removing elements
print('\n5. -------------------------------------------------')
my_set.remove(3)  # Remove an element
# Print the updated set     
print(my_set)  # Output: {1, 2, 4, 5, 6, 7, 8, 9}

# Removing an element that may not exist
print('\n6. -------------------------------------------------') 
my_set.discard(10)  # Remove an element if it exists
# Print the set (no error if element does not exist)
print(my_set)  # Output: {1, 2, 4, 5, 6, 7, 8, 9}

# Removing an element and returning it
print('\n7. -------------------------------------------------')
removed_element = my_set.pop()  # Remove and return an arbitrary element
# Print the removed element and the updated set 
print(f"Removed element: {removed_element}")  # Output: Removed element: 1 (or any other element)
print(my_set)  # Output: {2, 4, 5, 6, 7, 8, 9} (the set will be updated)

# Clearing the set
print('\n8. -------------------------------------------------')
my_set.clear()  # Remove all elements from the set
# Print the updated set
print(my_set)  # Output: set()

# Set operations
print('\n9. -------------------------------------------------')
set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union
print(set_a | set_b)  # Output: {1, 2, 3, 4, 5}

# Intersection
print(set_a & set_b)  # Output: {3}

# Difference
print(set_a - set_b)  # Output: {1, 2}  
print(set_b - set_a)  # Output: {4, 5}

# Symmetric Difference
print(set_a ^ set_b)  # Output: {1, 2, 4, 5}
# Subset
print(set_a.issubset(set_b))  # Output: False
print(set_a.issubset({1, 2, 3, 4, 5}))  # Output: True

# Superset
print(set_a.issuperset(set_b))  # Output: False     
print(set_a.issuperset({1, 2}))  # Output: True

# Copying a set
print('\n10. -------------------------------------------------')
set_copy = my_set.copy()  # Create a copy of the set
# Print the copied set
print(set_copy)  # Output: set() (empty set since my_set was cleared)

# Set Comprehension
print('\n11. -------------------------------------------------')
set_comprehension = {x * 2 for x in my_set}
# Print the set created by comprehension
print(set_comprehension)  # Output: set() (empty set since my_set was cleared)  
squared_set = {x**2 for x in range(5)}
# Print the set created by comprehension
print(squared_set)  # Output: {0, 1, 4, 9, 16} (squares of numbers from 0 to 4)

# Set with mixed data types
print('\n12. -------------------------------------------------')
mixed_set = {1, "Hello", 3.14, (2, 3)}
# Print the mixed set
print(mixed_set)  # Output: {1, 3.14, "Hello", (2, 3)}

# Nested sets
print('\n13. -------------------------------------------------')
nested_set = {1, 2, 3, frozenset({4, 5})}
# Print the nested set
print(nested_set)  # Output: {1, 2, 3, frozenset({4, 5})}   

# Accessing elements in a nested set
print('\n14. -------------------------------------------------')
for element in nested_set:
    if isinstance(element, frozenset):
        for nested_element in element:
            print(nested_element)  # Output: 4, 5 (the elements of the frozenset)

# Set operations with nested sets
print('\n15. -------------------------------------------------')
set_x = {1, 2, frozenset({3, 4})}   
set_y = {2, 3, frozenset({4, 5})}
# Union of sets with nested sets
print(set_x | set_y)  # Output: {1, 2, 3, frozenset({3, 4}), frozenset({4, 5})}
# Intersection of sets with nested sets
print(set_x & set_y)  # Output: {2, frozenset({3, 4})} (intersection of nested sets is not supported)
# Difference of sets with nested sets
print(set_x - set_y)  # Output: {1, frozenset({3, 4})} (elements in set_x not in set_y)
print(set_y - set_x)  # Output: {3, 4, frozenset({4, 5})} (elements in set_y not in set_x)
# Symmetric Difference of sets with nested sets
print(set_x ^ set_y)  # Output: {1, 3, frozenset({3, 4}), frozenset({4, 5})} (elements in either set but not both)
# Subset and Superset with nested sets
print(set_x.issubset(set_y))  # Output: False (set_x is not a subset of set_y)
print(set_y.issubset(set_x))  # Output: False (set_y is not a subset of set_x)
print(set_x.issuperset(set_y))  # Output: False (set_x is not a superset of set_y)
print(set_y.issuperset(set_x))  # Output: False (set_y is not a superset of set_x)  

# Copying a set with nested sets
print('\n16. -------------------------------------------------')
set_x_copy = set_x.copy()
# Print the copied set
print(set_x_copy)  # Output: {1, 2, frozenset({3, 4})}

# Set Comprehension with nested sets
print('\n17. -------------------------------------------------')
set_comprehension = {x * 2 for x in set_x}
# Print the set created by comprehension
print(set_comprehension)  # Output: {2, 4, frozenset({6, 8})}   (doubles the values)

# Set with mixed data types and nested sets
print('\n18. -------------------------------------------------')
mixed_nested_set = {1, "Hello", 3.14, (2, 3), frozenset({4, 5})}
# Print the mixed nested set
print(mixed_nested_set)  # Output: {1, 3.14, "Hello", (2, 3), frozenset({4, 5})}

# Accessing elements in a mixed nested set
print('\n19. -------------------------------------------------')
for element in mixed_nested_set:
    if isinstance(element, frozenset):
        for nested_element in element:
            print(nested_element)  # Output: 4, 5 (the elements of the frozenset)

# Set operations with mixed nested sets
print('\n20. -------------------------------------------------')    
set_a = {1, 2, frozenset({3, 4})}
set_b = {2, 3, frozenset({4, 5})}   
# Union of sets with mixed nested sets
print(set_a | set_b)  # Output: {1, 2, 3, frozenset({3, 4}), frozenset({4, 5})}
# Intersection of sets with mixed nested sets
print(set_a & set_b)  # Output: {2, frozenset({3, 4})} (intersection of nested sets is not supported)
# Difference of sets with mixed nested sets
print(set_a - set_b)  # Output: {1, frozenset({3, 4})} (elements in set_a not in set_b)
print(set_b - set_a)  # Output: {3, 4, frozenset({4, 5})} (elements in set_b not in set_a)
# Symmetric Difference of sets with mixed nested sets
print(set_a ^ set_b)  # Output: {1, 3, frozenset({3, 4}), frozenset({4, 5})} (elements in either set but not both)
# Subset and Superset with mixed nested sets
print(set_a.issubset(set_b))  # Output: False (set_a is not a subset of set_b)
print(set_b.issubset(set_a))  # Output: False (set_b is not a subset of set_a)
print(set_a.issuperset(set_b))  # Output: False (set_a is not a superset of set_b)
print(set_b.issuperset(set_a))  # Output: False (set_b is not a superset of set_a)  

# Copying a set with mixed nested sets
print('\n21. -------------------------------------------------')
set_a_copy = set_a.copy()
# Print the copied set
print(set_a_copy)  # Output: {1, 2, frozenset({3, 4})}

# set length
print(len(set_a_copy))  # Output: 3 

# checking for existence of an element
print('\n22. -------------------------------------------------')    
exists = 2 in set_a_copy  # Check if an element exists in the set
print(exists)  # Output: True

# checking for existence of a nested element
print('\n23. -------------------------------------------------')
nested_exists = frozenset({3, 4}) in set_a_copy  # Check if a nested element exists in the set
print(nested_exists)  # Output: True

# iterating through a set
print('\n24. -------------------------------------------------')    
for element in set_a_copy:
    print(element)  # Output: 1, 2, frozenset({3, 4}) (the elements of the set)

# using a set as a key in a dictionary
print('\n25. -------------------------------------------------')
my_dict = {frozenset({1, 2}): "Hello", frozenset({3, 4}): "World"}
# Print the dictionary
print(my_dict)  # Output: {frozenset({1, 2}): "Hello", frozenset({3, 4}): "World"}

# Accessing a value using a set key
print('\n26. -------------------------------------------------')
print(my_dict[frozenset({1, 2})])  # Output: "Hello"
print(my_dict[frozenset({3, 4})])  # Output: "World"

# Set as a return value from a function
print('\n27. -------------------------------------------------')    
def get_set():
    return {1, 2, 3}
result_set = get_set()  # Get the set from the function
# Print the returned set
print(result_set)  # Output: {1, 2, 3}

# Set as a single element in a set
print('\n28. -------------------------------------------------')
single_element_set = {frozenset({1, 2, 3})}
# Print the single element set
print(single_element_set)  # Output: {frozenset({1, 2, 3})} 

# converting list to set
print('\n29. -------------------------------------------------')
my_list = [1, 2, 3, 4, 5]
my_set_from_list = set(my_list)  # Convert list to set
# Print the set created from the list
print(my_set_from_list)  # Output: {1, 2, 3, 4, 5}  


