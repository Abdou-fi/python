# numpy Data types :
import numpy as np
# Creating arrays with different data types
int_array = np.array([1, 2, 3, 4], dtype=np.int32)
float_array = np.array([1.1, 2.2, 3.3, 4.4], dtype=np.float64)
complex_array = np.array([1+2j, 3+4j, 5+6j, 7+8j], dtype=np.complex128)

# Printing the arrays
print("Integer Array:", int_array)
print("Float Array:", float_array)
print("Complex Array:", complex_array)

# Output:
# Integer Array: [1 2 3 4]
# Float Array: [1. 2. 3. 4.]
# Complex Array: [(1.+2.j) (3.+4.j) (5.+6.j) (7.+8.j)]


# Checking the data types of the arrays
print("Data type of int_array:", int_array.dtype)
print("Data type of float_array:", float_array.dtype)
print("Data type of complex_array:", complex_array.dtype)

# Creating arrays with different data types using the astype() method
int_array = np.array([1, 2, 3, 4])
float_array = int_array.astype(np.float64)
complex_array = float_array.astype(np.complex128)

# Converted arrays
print("Converted Float Array:", float_array)
print("Converted Complex Array:", complex_array)

# Output:
# Converted Float Array: [1. 2. 3. 4.]
# Converted Complex Array: [(1.+0.j) (2.+0.j) (3.+0.j) (4.+0.j)]

# Checking the data types of the converted arrays
print("Data type of float_array after conversion:", float_array.dtype)
print("Data type of complex_array after conversion:", complex_array.dtype)

# Output:
# Data type of float_array after conversion: float64
# Data type of complex_array after conversion: complex128

# Demonstrating type casting during array operations
arr1 = np.array([1, 2, 3], dtype=np.int32)
arr2 = np.array([4, 5, 6], dtype=np.int32)

# Performing operations and observing type casting
result = arr1 + arr2
print("Result of arr1 + arr2:", result)
print("Data type of result:", result.dtype)

# Output:
# Result of arr1 + arr2: [5 7 9]
# Data type of result: int32    
# When adding an integer array to a float array
arr3 = np.array([1.5, 2.5, 3.5], dtype=np.float64)
result2 = arr1 + arr3
print("Result of arr1 + arr3:", result2)
print("Data type of result2:", result2.dtype)

# Output:   
# Result of arr1 + arr3: [2.5 4.5 6.5]
# Data type of result2: float64
# When multiplying an integer array with a complex array
arr4 = np.array([1+2j, 3+4j, 5+6j], dtype=np.complex128)
result3 = arr1 * arr4
print("Result of arr1 * arr4:", result3)
print("Data type of result3:", result3.dtype)

# Output:   
# Result of arr1 * arr4: [(1.+2.j) (6.+8.j) (15.+18.j)]
# Data type of result3: complex128  

# Demonstrating type casting during array operations with different data types
arr5 = np.array([1, 2, 3], dtype=np.int32)
arr6 = np.array([1.5, 2.5, 3.5], dtype=np.float64)
result4 = arr5 + arr6
print("Result of arr5 + arr6:", result4)
print("Data type of result4:", result4.dtype)

# Output:
# Result of arr5 + arr6: [2.5 4.5 6.5]
# Data type of result4: float64
# When multiplying an integer array with a complex array
arr7 = np.array([1+2j, 3+4j, 5+6j], dtype=np.complex128)
result5 = arr5 * arr7
print("Result of arr5 * arr7:", result5)
print("Data type of result5:", result5.dtype)

# Output:
# Result of arr5 * arr7: [(1.+2.j) (6.+8.j) (15.+18.j)]
# Data type of result5: complex128

# Demonstrating type casting during array operations with different data types
arr8 = np.array([1, 2, 3], dtype=np.int32)
arr9 = np.array([1.5, 2.5, 3.5], dtype=np.float64)
result6 = arr8 + arr9
print("Result of arr8 + arr9:", result6)
print("Data type of result6:", result6.dtype)
# Output:
# Result of arr8 + arr9: [2.5 4.5 6.5]
# Data type of result6: float64
# When multiplying an integer array with a complex array
arr10 = np.array([1+2j, 3+4j, 5+6j], dtype=np.complex128)
result7 = arr8 * arr10
print("Result of arr8 * arr10:", result7)
print("Data type of result7:", result7.dtype)

# Output:
# Result of arr8 * arr10: [(1.+2.j) (6.+8.j) (15.+18.j)]
# Data type of result7: complex128
# Demonstrating type casting during array operations with different data types
arr11 = np.array([1, 2, 3], dtype=np.int32)
arr12 = np.array([1.5, 2.5, 3.5], dtype=np.float64)
result8 = arr11 + arr12
print("Result of arr11 + arr12:", result8)
print("Data type of result8:", result8.dtype)
# Output:
# Result of arr11 + arr12: [2.5 4.5 6.5]
# Data type of result8: float64
# When multiplying an integer array with a complex array
arr13 = np.array([1+2j, 3+4j, 5+6j], dtype=np.complex128)
result9 = arr11 * arr13
print("Result of arr11 * arr13:", result9)
print("Data type of result9:", result9.dtype)


# Output:
# Result of arr11 * arr13: [(1.+2.j) (6.+8.j) (15.+18.j)]
# Data type of result9: complex128

# Demonstrating type casting during array operations with different data types
arr14 = np.array([1, 2, 3], dtype=np.int32) 
arr15 = np.array([1.5, 2.5, 3.5], dtype=np.float64)
result10 = arr14 + arr15
print("Result of arr14 + arr15:", result10)
print("Data type of result10:", result10.dtype)
# Output:
# Result of arr14 + arr15: [2.5 4.5 6.5]
# Data type of result10: float64

# When multiplying an integer array with a complex array
arr16 = np.array([1+2j, 3+4j, 5+6j], dtype=np.complex128)
result11 = arr14 * arr16
print("Result of arr14 * arr16:", result11)
print("Data type of result11:", result11.dtype)

# Output:
# Result of arr14 * arr16: [(1.+2.j) (6.+8.j) (15.+18.j)]
# Data type of result11: complex128
# Demonstrating type casting during array operations with different data types
arr17 = np.array([1, 2, 3], dtype=np.int32)
arr18 = np.array([1.5, 2.5, 3.5], dtype=np.float64)
result12 = arr17 + arr18
print("Result of arr17 + arr18:", result12)
print("Data type of result12:", result12.dtype)
# Output:
# Result of arr17 + arr18: [2.5 4.5 6.5]
# Data type of result12: float64
