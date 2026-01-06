import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 500)

x = 16 * np.sin(t) ** 3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

plt.figure(figsize=(5, 5))
plt.plot(x, y, color='red', linewidth=8)
plt.title('Heart shape pattern plot', fontsize=16)
plt.axis("equal")
plt.axis("off")
plt.show()