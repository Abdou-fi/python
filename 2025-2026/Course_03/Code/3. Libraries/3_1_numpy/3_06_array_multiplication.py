import numpy as np

# array multiplication using * operator
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print(np.dot(a, b))  # output [[19 22] [43 50]]

# flatten an array

arr = np.array([[1,2],[3,4]])
print(arr.flatten())  # output [1 2 3 4]
