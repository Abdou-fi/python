import numpy as np 
import matplotlib.pyplot as plt 
x = np.arange(-10, 5, 0.01)
y = np.sin(x)
plt.plot(x, y) 
plt.xlim(-5, 5)
plt.ylim(-1, 1)
plt.show()
print(np.__version__)