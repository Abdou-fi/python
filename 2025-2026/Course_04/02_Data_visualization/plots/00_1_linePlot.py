import matplotlib.pyplot as pl  
x = [1,  2,  3,  4,  5]
z = [10, 12, 15, 17, 20]
pl.plot(x, z,'ro--')              # Plot x and y with circle markers on each point
pl.title('Line Plot Example')       # Add a title to the plot
pl.xlabel('months')                 # Label for the X-axis
pl.ylabel('salary')                 # Label for the Y-axis

pl.show()