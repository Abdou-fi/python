import seaborn as sns # Import the Seaborn library 
import matplotlib.pyplot as plt # Import Matplotlib for additional control 
# Data 
data = [10, 12, 15, 13, 17, 19, 10, 9] # Sample data for the box plot 
# Create Box Plot 
sns.boxplot(data=data, color='red') # Create a box plot to show distribution, quartiles, and outliers 
plt.title('Box Plot Example') # Add a title to the plot 
plt.show() # Display the plot