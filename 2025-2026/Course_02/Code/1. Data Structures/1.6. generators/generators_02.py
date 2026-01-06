# Generators are functions that can pause and resume their execution.
# When a generator function is called, it returns a generator object, which is an iterator.
# The code inside the function is not executed yet, it is only compiled. 
# The function only executes when you iterate over the generator.

def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value) 
  
  
# The yield Keyword

# The yield keyword is what makes a function a generator.
# When yield is encountered, the function's state is saved, and the value is returned. 
# The next time the generator is called, it continues from where it left off.

#  Unlike return, which terminates the function, yield pauses it and can be called multiple times.

def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1

for num in count_up_to(5):
  print(num) 
  
  
# Generators Saves Memory
# Generators are memory-efficient because they generate values on-the-fly instead of storing everything in memory.
# For large datasets, generators save memory:

# Generator for large sequences:
def large_sequence(n):
  for i in range(n):
    yield i

# This doesn't create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen)) 



# Using next() with Generators
def simple_gen():
  yield "Emil"
  yield "Tobias"
  yield "Linus"

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen)) 