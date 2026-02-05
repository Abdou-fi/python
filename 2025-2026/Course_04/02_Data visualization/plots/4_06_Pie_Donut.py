import matplotlib.pyplot as plt 
sizes = [40, 30, 20, 10] 
labels = ['A', 'B', 'C', 'D'] 
plt.pie(sizes, labels=labels, autopct='%1.1f%%', wedgeprops={'width':0.2})
plt.show()
