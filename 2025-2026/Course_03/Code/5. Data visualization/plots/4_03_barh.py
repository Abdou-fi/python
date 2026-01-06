import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

plt.barh(categories, values, color='purple')

plt.xlabel("Values")
plt.ylabel("Categories")
plt.title("Horizontal Bar Chart Example")

plt.show()

