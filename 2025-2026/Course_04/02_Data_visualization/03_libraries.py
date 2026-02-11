# s="amazing"
# print(s.index('a'))

# from numpy import linspace , pi , sin , cos , exp
# import matplotlib.pyplot as plt
# x = linspace(-pi , pi , 101)
# plt.xlim(-pi , pi), plt.ylim(-2, 4)
# for y in [x - 1, x**2, sin(x), cos(x), exp(x)]:
#     plt.plot(x, y)
# plt.show ()




import matplotlib.pyplot as plt # Import the Matplotlib library
# Data 
x = [1, 2, 3, 4, 5] # X-axis data 
y = [10, 12, 15, 17, 20] # Y-axis data

# Create Line Plot
plt.plot(x, y, marker='o') # Plot x and y with 
                           #circle markers on each point 
plt.title('Line Plot Example') # Add a title to the plot
plt.xlabel('X Axis') # Label for the X-axis
plt.ylabel('Y Axis') # Label for the Y-axis
plt.show() # Display the plot




""" from numpy import linspace , pi , sin , cos , exp
import matplotlib.pyplot as plt
x = linspace(-pi , pi , 101)
plt.xlim(-pi , pi), plt.ylim(-2, 4)
for y in [x - 1, x**2, sin(x), cos(x), exp(x)]:
    plt.plot(x, y)
plt.show () """