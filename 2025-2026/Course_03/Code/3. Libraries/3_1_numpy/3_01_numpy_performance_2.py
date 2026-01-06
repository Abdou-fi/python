# Memory usage
import numpy as np
import sys
a = [i for i in range(10_000_000)]
b = np.arange(10_000_000,dtype=np.int32)
c = np.arange(10_000_000,dtype=np.int16)
print("list memory :", sys.getsizeof(a))
print("numpy memory :", sys.getsizeof(b))
print("numpy memory :", sys.getsizeof(c))
