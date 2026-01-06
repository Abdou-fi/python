a = [i for i in range(10_000_000)]
b = [ i for i in range(10_000_000, 20_000_000)]
c= []
import time
start = time.time()
for i in range(len(a)):
    c.append(a[i] + b[i])
print(time.time()-start)
#numpy
import numpy as np
y = np.arange(10_000_000)
z = np.arange(10_000_000, 20_000_000)
start = time.time()
x = y + z
print(time.time()-start)
