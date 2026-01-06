import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
print("The shape of the arr array is:", arr.shape)    # Get the shape of the array (rows, columns)

arr.reshape((3, 2))  # Reshape the array to 3 rows and 2 columns
print(arr)
arr3=arr.reshape((3, 2))  # Reshape the array to 3 rows and 2 columns
print(arr3)