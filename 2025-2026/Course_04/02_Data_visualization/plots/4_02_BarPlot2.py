import matplotlib.pyplot as plt
continents=['Asia', 'Africa', 'Europe', 'North America', 'South America', 'Oceania']
population= [4694576167, 1393676444, 745173774, 595783465, 434254119, 44491724]
plt.bar(continents, population, color='green')
plt.title('population mondiale')
plt.xlabel('Continents') 
plt.ylabel('Population in billion')
plt.show()

