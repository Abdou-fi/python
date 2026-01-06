import seaborn as sns # Import the Seaborn library 
import matplotlib.pyplot as plt # Import Matplotlib for additional control 
# Data 
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Sample 2D array to visualize as a heatmap # Create Heatmap 
sns.heatmap(data, annot=True, cmap='coolwarm') # Create heatmap with annotations and color map 
plt.title('Heatmap Example') # Add a title to the heatmap 
plt.show() # Display the heatmap