import matplotlib.pyplot as plt 
grades = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5] 
plt.hist(grades, bins=5, color='blue')
plt.title('Histogram Example') 
plt.xlabel('Value') 
plt.ylabel('Frequency') 
plt.show()