import matplotlib.pyplot as plt

# Data for the horizontal bar chart
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

# Create the horizontal bar chart
plt.barh(categories, values, color='purple')

# Add labels and title for clarity
plt.xlabel("Values")
plt.ylabel("Categories")
plt.title("Horizontal Bar Chart Example")

# Display the plot
plt.show()
