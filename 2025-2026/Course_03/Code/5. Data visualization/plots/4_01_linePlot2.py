import matplotlib.pyplot as plt
modules =['maths', 'physics', 'geo']
values_1 = [10, 15, 12]
values_2 = [8, 17, 14]
plt.plot(modules, values_1, marker='o', label='2023')
plt.plot(modules, values_2, marker='o', label='2024')
plt.title('Slopegraph')
plt.show()
