import matplotlib.pyplot as plt
categories = ["category 1", "category 2", "category 3", "category 4"]
values = [80, 20, 50, 30]
fig, ax1 = plt.subplots()
ax1.bar(categories, values, color='blue')
ax1.set_ylabel('Values', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
ax2 = ax1.twinx()
cumulative_values = [sum(values[:i+1]) for i in range(len(values))]
ax2.plot(categories, cumulative_values, color='red', marker='.', linewidth=2)
ax2.set_ylabel('Cumulative Values', color='red')
ax2.tick_params(axis='y', labelcolor='red')
plt.title('Bar Chart with Cumulative Line')
plt.show()
