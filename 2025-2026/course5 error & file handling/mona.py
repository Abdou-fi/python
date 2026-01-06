import matplotlib.pyplot as pl
sizes = [40,30,20,10]
lables = ['my learns','py gram','nonsense','blablablabloblonblo']

pl.pie(sizes, lables=lables, autopct='%1.2f%%')
pl.show()