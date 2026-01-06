# built in Python functions
# https://docs.python.org/3/library/functions.html

# abs() - absolute value
print(abs(-5))                      # output : 5

# all() - returns True if all elements in an iterable are true
print(all([True, True, True]))      # output : True

# any() - returns True if any element in an iterable is true
print(any([False, False, True]))    # output : True

# ascii() - returns a readable representation of an object
print(ascii("hello world"))         # output : 'hello world'

# bin() - returns the binary representation of a number
print(bin(10))                      # output : 0b1010 

# bool() - returns the boolean value of the specified object
print(bool(0))                      # output : False

# chr() - returns a string representing a character
print(chr(65))                              # output : 'A'

# ord() - returns an integer representing the Unicode character
print(ord('a'))                             # output : 65

# complex() - returns a complex number
print(complex(1, 2))                        # output : (1+2j)

# enumerate() - returns an enumerate object     
print(enumerate([1, 2, 3]))                      # output : <enumerate object at 0x0000026D5D6A9D60>

# eval() - evaluates an expression
print(eval("2 + 2**4"))                           # output : 4

# float() - returns a floating point number
print(float(10))
# format() - formats a specified value
print(format(10.688, ".2f"))
