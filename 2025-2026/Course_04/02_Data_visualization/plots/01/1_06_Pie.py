import matplotlib.pyplot as plt 
sizes = [40, 37, 22, 9]
labels = ['A', 'B', 'C', 'D'] 
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.show()

