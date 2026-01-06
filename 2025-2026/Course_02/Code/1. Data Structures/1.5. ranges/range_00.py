###########################################################################
#  A. Filali       2025-06-21                                             #
#  range                                                                  #
#                                                                         #
#  This script demonstrates the use of the range function in Python.      #
#  Range The range function is a built-in Python function that generates  #
#  a sequence of numbers, commonly used in for-loops for iteration.       #
#  It returns an immutable sequence type,                                 #
#  which is memory efficient for creating large ranges of numbers.        #
###########################################################################


# Using range with a single argument
print('\n1. -------------------------------------------------')
r=range(5)                  # creates a range from 0 to 4
print(r)                    # Output: range(0, 5) 
print(type(r))              # Output: <class 'range'>
print(list(r))              # Output: [0, 1, 2, 3, 4]   convert a range to a list

r2=range(2, 10)             # creates a range from 2 to 9
print(r2)                   # Output: range(2, 10)         # creates a range from 2 to 9
print(list(r2))             # Output: [2, 3, 4, 5, 6, 7, 8, 9]


# reverse a range
print('\n2. -------------------------------------------------')
r_reverse = range(5, 0, -1)
print(r_reverse)            # Output: range(5, 0, -1)
print(list(r_reverse))      # Output: [5, 4, 3, 2, 1]

# checking membership in a range
print('\n3. -------------------------------------------------')
r = range(5)
print(3 in r)               # Output: True
print(5 in r)               # Output: False

# using range in list comprehension
print('\n4. -------------------------------------------------')
squares = [x**2 for x in range(5)]
print(type(squares))        # Output: <class 'list'>
print(squares)              # Output: [0, 1, 4, 9, 16]

# Using range with a step
print('\n5. -------------------------------------------------')
r_step = range(0, 10, 2)
print(r_step)               # Output: range(0, 10, 2)
print(list(r_step))         # Output:  [0, 2, 4, 6, 8]

# Using range with negative step
print('\n6. -------------------------------------------------')
r_neg_step = range(10, 0, -2)
print(r_neg_step)           # Output: range(10, 0, -2)
print(list(r_neg_step))     # Output: [10, 8, 6, 4, 2]

# Using range with a negative start and end
print('\n7. -------------------------------------------------')
r_neg_start_end = range(-5, -1)
print(r_neg_start_end)       # Output: range(-5, -1)
print(list(r_neg_start_end)) # Output: [-5, -4, -3, -2]

# Using range with a negative start, end, and step
print('\n8. -------------------------------------------------')
r_neg_step_full = range(-10, -1, 2)
print(r_neg_step_full)          # Output: range(-10, -1, 2)
print(list(r_neg_step_full))    # Output: [-10, -8, -6, -4, -2]

# Using range with a single negative argument
print('\n9. -------------------------------------------------')
r_single_neg = range(-5)
print(r_single_neg)            # Output: range(0, -5)
print(list(r_single_neg))      # Output: []

# Using range with a single zero argument
print('\n10. -------------------------------------------------')
r_single_zero = range(0)        
print(r_single_zero)            # Output: range(0, 0)
print(list(r_single_zero))      # Output: []

# iterating through a range
print('\n11. -------------------------------------------------')
for i in range(5):
    print(i, end=' ')           # Output: 0 1 2 3 4
print()  # for a new line

#length of a range
print('\n12. -------------------------------------------------')
print(len(r))                  # Output: 5


# Using range in a loop with negative step
print('\n13. -------------------------------------------------')    
for i in range(5, 0, -1):
    print(i, end=' ')           # Output: 5 4 3 2 1
print()  # for a new line

# Using range with a large number
print('\n14. -------------------------------------------------')        
large_range = range(1000000)  # creates a large range
print(type(large_range))       # Output: <class 'range'>    
