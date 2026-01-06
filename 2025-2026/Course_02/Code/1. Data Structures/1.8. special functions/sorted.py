# returns a new sorted list from the items in iterable
# iterable: any iterable (list, tuple, string, etc.)
# key: a function that serves as a key for the sort comparison
# does not change the original iterable

num = [5, 2, 9, 1, 5, 6]
# Sorting in ascending order
sorted_num_asc = sorted(num)
print(sorted_num_asc)  # Output: [1, 2, 5, 5, 6, 9]

# Sorting in descending order
sorted_num_desc = sorted(num, reverse=True)
print(sorted_num_desc)  # Output: [9, 6, 5, 5, 2, 1]

# Sorting based on the length of string elements
words = ['apple', 'banana', 'kiwi', 'cherry', 'blueberry']
sorted_words = sorted(words, key=len)
print(sorted_words)  # Output: ['kiwi', 'apple', 'banana', 'cherry', 'blueberry']

# Sorting a list of tuples based on the second element
tuples = [(1, 'b'), (2, 'a'), (3, 'c')]
sorted_tuples = sorted(tuples, key=lambda x: x[1])
print(sorted_tuples)  # Output: [(2, 'a'), (1, 'b'), (3, 'c')]

# Sorting a string (returns a list of characters)
string = "hello"
sorted_string = sorted(string)
print(sorted_string)  # Output: ['e', 'h', 'l', 'l', 'o']
odd_str = list(filter(lambda x: x not in "24680", num))
print(odd_str)     # Output: [1, 3, 5, 7, 9]
predefined_string = "24680"
even_str = list(filter(lambda x: x in predefined_string, num))
print(even_str)    # Output: [2, 4, 6, 8, 10]

# Using list comprehension with a predefined string
even_comp_str = [x for x in num if x in predefined_string]
print(even_comp_str)    # Output: [2, 4, 6, 8, 10]
odd_comp_str = [x for x in num if x not in predefined_string]
print(odd_comp_str)     # Output: [1, 3, 5, 7, 9]   

# Using list comprehension with a lambda function
even_lambda_str = [x for x in num if x % 2 == 0]
print(even_lambda_str)    # Output: [2, 4, 6, 8, 10]
odd_lambda_str = [x for x in num if x % 2 != 0]
print(odd_lambda_str)     # Output: [1, 3, 5, 7, 9]

