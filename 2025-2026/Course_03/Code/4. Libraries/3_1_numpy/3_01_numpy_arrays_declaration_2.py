import numpy as np  

arr1 = np.zeros((5, 2))
print(arr1)
arr1[(1, 1)]=7
print(arr1)

arr2 = np.ones((2,2))
print(arr2)

arr3 = np.full((2,2), 7.)
print(arr3)
print(arr3.dtype)

arr4 = np.eye(3)
print(arr4)

arr5 = np.random.random((2,2))
print(arr5)

arr6 = np.arange(0, 30, 5)
print(arr6)

arr7 = np.linspace(0, 5, 21)
print(arr7)
