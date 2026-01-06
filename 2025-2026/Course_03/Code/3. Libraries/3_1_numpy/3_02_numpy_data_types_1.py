import numpy as np 
arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)    # Get the data type of the array elements (int64)
arr.astype(float)   # Convert the array elements to float
print(arr.dtype)    # Get the data type of the array elements (int64)
arr2=arr.astype(float)   # Convert the array elements to float
print(arr2.dtype)   # Get the data type of the array elements (float64)