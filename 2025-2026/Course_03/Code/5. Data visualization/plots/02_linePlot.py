import matplotlib.pyplot as plt

year = ['2015', 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
capitalization = [38.76, 39.48, 52.48, 52.06, 66.73, 87.31, 144.33, 87.91, 118.36]

plt.plot(year, capitalization, marker='o')
plt.title('Google Capitalization for the past 9 years')
plt.xlabel('year')
plt.ylabel('Market Capitalization')
plt.show()