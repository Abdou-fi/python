import matplotlib.pyplot as plt
x =[3, 6 , 8, 11, 13, 14, 17, 19, 21, 24, 33, 37]
y =[7.5, 12, 13.2, 15, 17, 22, 24, 37, 34, 38.5, 42,47]

x2 =[3, 6, 8, 11, 13, 14, 17, 19, 21, 24, 33]
y2 =[50, 45, 33, 24, 21.5, 19, 14, 13, 10, 6, 3]
plt.plot(x, y, label='First Line' )
plt.plot(x2, y2, label='Second Line' )
plt.xlabel('Plot Number' )
plt.ylabel('Important var' )
plt.title('Interesting Graph\n2025 ')
plt.yticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
           ['أ','ب','ج','15B','20B','25B', '30B', '35B', '40B' ,'45B', '50B'])
plt.legend()
plt.show()