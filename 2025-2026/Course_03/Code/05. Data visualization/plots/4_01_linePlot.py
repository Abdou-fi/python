import matplotlib.pyplot as pl  
x = [ '1',  2,  3,  4,  5]
z = [10.9, 12, 15, 17, 20]

pl.plot(x, z,'-b*')  # Plot x and z with green circle markers on each point
pl.title('Evolution of salary over months')
pl.xlabel('mois')
pl.ylabel('salaires')
pl.grid(which='both')
pl.show()