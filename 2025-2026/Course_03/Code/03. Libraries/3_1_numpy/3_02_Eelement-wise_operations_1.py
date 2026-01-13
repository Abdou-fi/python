import numpy as np 
arr = np.array([1, 2, 3, 4, 5])     # Creating a NumPy array 
arr2 = np.array([10, 20, 30, 40, 50])            # Converting the array elements to float
arr4=np.array([1, 2, 3, 4])         # Creating another NumPy array  
result1 = arr * 2  # Performing mathematical operations on the array 
print(result1)     # output [2 4 6 8 10]

     # output [3 4 5 6 7]

result3 = arr + arr2 # adding arrays (must have the same shape) 
print(result3)      # output [11 22 33 44 55]

# result4 = arr + arr4 # subtracting arrays (must have the same shape)
# print(result4)       # output ValueError

result5 = arr2 - arr # subtracting arrays (must have the same shape)
print(result5)       # output [9 18 27 36 45]