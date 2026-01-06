
# List comprehension

# Basic way (long) 

numbers = [1, 2, 3, 4, 5] 
squared_basic = []
for n in numbers:
    squared_basic.append(n ** 2)
print("Basic:", squared_basic)

# Clean way (list comprehension) 
numbers = [1, 2, 3, 4, 5] 
squared_clean = [n**2 for n in numbers]
print("Clean:", squared_clean)