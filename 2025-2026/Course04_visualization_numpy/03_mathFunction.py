import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.01)
y = np.sqrt(x)
z = np.cos(x)
h = np.sin(x)
plt.plot(x, y)
plt.plot(x, z)
plt.plot(x, h)
plt.show()