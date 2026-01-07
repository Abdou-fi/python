import numpy as np  

# 1D array with 5 elements
a = np.array([1,2,3,4,5])    
print (a)  

# 2D array with 2 rows and 3 columns
b=np.array( [(1,2,3),(4,5,6)] )
print (b)

# 3D array with 2 blocks, each containing 2 rows and 3 columns
c=np.array( [ [(1,2,3),(4,5,6)], [(7,8,9),(10,11,12)] ] )
print (c)