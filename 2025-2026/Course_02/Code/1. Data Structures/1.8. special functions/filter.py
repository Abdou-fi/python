# filter elements from an iterable based on a condition
# filter(function, iterable)
# function: a function that takes an element of the iterable as input and returns True or False

# Using filter with a lambda function
num=[1,2,3,4,5,6,7,8,9,10]
even = list(filter(lambda x: x%2==0, num))
print(even)         # Output: [2, 4, 6, 8, 10]
odd = list(filter(lambda x: x%2!=0, num))
print(odd)          # Output: [1, 3, 5, 7, 9]   

# Using list comprehension
even_comp = [x for x in num if x%2==0]
print(even_comp)    # Output: [2, 4, 6, 8, 10]
odd_comp = [x for x in num if x%2!=0]
print(odd_comp)     # Output: [1, 3, 5, 7, 9]

# Using a defined function
def is_even(x):
    return x % 2 == 0
even_func = list(filter(is_even, num))
print(even_func)    # Output: [2, 4, 6, 8, 10]  

def is_odd(x):
    return x % 2 != 0
odd_func = list(filter(is_odd, num))
print(odd_func)     # Output: [1, 3, 5, 7, 9]

# Using list comprehension with defined functions
even_comp_func = [x for x in num if is_even(x)]
print(even_comp_func)    # Output: [2, 4, 6, 8, 10]
odd_comp_func = [x for x in num if is_odd(x)]
print(odd_comp_func)     # Output: [1, 3, 5, 7, 9]

# Using filter with a predefined set
predefined_set = {2, 4, 6, 8, 10}
even_set = list(filter(lambda x: x in predefined_set, num))
print(even_set)    # Output: [2, 4, 6, 8, 10]
odd_set = list(filter(lambda x: x not in predefined_set, num))
print(odd_set)     # Output: [1, 3, 5, 7, 9]

# Using list comprehension with a predefined set
even_comp_set = [x for x in num if x in predefined_set]
print(even_comp_set)    # Output: [2, 4, 6, 8, 10]
odd_comp_set = [x for x in num if x not in predefined_set]
print(odd_comp_set)     # Output: [1, 3, 5, 7, 9]

# Using filter with a predefined list
predefined_list = [2, 4, 6, 8, 10]
even_list = list(filter(lambda x: x in predefined_list, num))
print(even_list)    # Output: [2, 4, 6, 8, 10]
odd_list = list(filter(lambda x: x not in predefined_list, num))
print(odd_list)     # Output: [1, 3, 5, 7, 9]

# Using list comprehension with a predefined list
even_comp_list = [x for x in num if x in predefined_list]
print(even_comp_list)    # Output: [2, 4, 6, 8, 10]
odd_comp_list = [x for x in num if x not in predefined_list]
print(odd_comp_list)     # Output: [1, 3, 5, 7, 9]

# Using filter with a predefined tuple
predefined_tuple = (2, 4, 6, 8, 10)
even_tuple = list(filter(lambda x: x in predefined_tuple, num))
print(even_tuple)    # Output: [2, 4, 6, 8, 10]
odd_tuple = list(filter(lambda x: x not in predefined_tuple, num))
print(odd_tuple)     # Output: [1, 3, 5, 7, 9]

# Using list comprehension with a predefined tuple
even_comp_tuple = [x for x in num if x in predefined_tuple]
print(even_comp_tuple)    # Output: [2, 4, 6, 8, 10]
odd_comp_tuple = [x for x in num if x not in predefined_tuple]
print(odd_comp_tuple)     # Output: [1, 3, 5, 7, 9]

# Using filter with a predefined dictionary

predefined_dict = {2: 'even', 4: 'even', 6: 'even', 8: 'even', 10: 'even'}
even_dict = list(filter(lambda x: x in predefined_dict, num))
print(even_dict)    # Output: [2, 4, 6, 8, 10]      
odd_dict = list(filter(lambda x: x not in predefined_dict, num))
print(odd_dict)     # Output: [1, 3, 5, 7, 9]

# Using list comprehension with a predefined dictionary
even_comp_dict = [x for x in num if x in predefined_dict]
print(even_comp_dict)    # Output: [2, 4, 6, 8, 10]

odd_comp_dict = [x for x in num if x not in predefined_dict]
print(odd_comp_dict)     # Output: [1, 3, 5, 7, 9]

# Using filter with a predefined string
predefined_string = '246810'
even_string = list(filter(lambda x: x in predefined_string, num))
print(even_string)    # Output: [2, 4, 6, 8, 10]
odd_string = list(filter(lambda x: x not in predefined_string, num))
print(odd_string)     # Output: [1, 3, 5, 7, 9]

# Using list comprehension with a predefined string
even_comp_string = [x for x in num if x in predefined_string]
print(even_comp_string)    # Output: [2, 4, 6, 8, 10]
odd_comp_string = [x for x in num if x not in predefined_string]
print(odd_comp_string)     # Output: [1, 3, 5, 7, 9]

# Using filter with a predefined range
predefined_range = range(2, 11, 2)
even_range = list(filter(lambda x: x in predefined_range, num))
print(even_range)    # Output: [2, 4, 6, 8, 10]
odd_range = list(filter(lambda x: x not in predefined_range, num))
print(odd_range)     # Output: [1, 3, 5, 7, 9]

# Using list comprehension with a predefined range
even_comp_range = [x for x in num if x in predefined_range]
print(even_comp_range)    # Output: [2, 4, 6, 8, 10]
odd_comp_range = [x for x in num if x not in predefined_range]
print(odd_comp_range)     # Output: [1, 3, 5, 7, 9]

# Using filter with a predefined generator
predefined_generator = (x for x in range(2, 11, 2))
even_generator = list(filter(lambda x: x in predefined_generator, num))
print(even_generator)    # Output: [2, 4, 6, 8, 10]
odd_generator = list(filter(lambda x: x not in predefined_generator, num))
print(odd_generator)     # Output: [1, 3, 5, 7, 9]

# Using list comprehension with a predefined generator
even_comp_generator = [x for x in num if x in predefined_generator]
print(even_comp_generator)    # Output: [2, 4, 6, 8, 10]
odd_comp_generator = [x for x in num if x not in predefined_generator]
print(odd_comp_generator)     # Output: [1, 3, 5, 7, 9]

# Using filter with a predefined frozenset
predefined_frozenset = frozenset([2, 4, 6, 8, 10])
even_frozenset = list(filter(lambda x: x in predefined_frozenset, num))
print(even_frozenset)    # Output: [2, 4, 6, 8, 10]
odd_frozenset = list(filter(lambda x: x not in predefined_frozenset, num))
print(odd_frozenset)     # Output: [1, 3, 5, 7, 9]

# Using list comprehension with a predefined frozenset
even_comp_frozenset = [x for x in num if x in predefined_frozenset]
print(even_comp_frozenset)    # Output: [2, 4, 6, 8, 10]
odd_comp_frozenset = [x for x in num if x not in predefined_frozenset]
print(odd_comp_frozenset)     # Output: [1, 3, 5, 7, 9]





    



