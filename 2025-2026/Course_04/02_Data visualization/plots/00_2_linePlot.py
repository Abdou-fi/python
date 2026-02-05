import matplotlib.pyplot as plt

year = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025']
capitalization = [575.02, 587.97, 784.89, 778.00, 990.47, 1275.00,2079.00, 1230.00, 1756.00, 2365.00, 3800.00]


plt.plot(year, capitalization, marker='o')
plt.title('Google Capitalization for the past 11 years')
plt.xlabel('year')
plt.ylabel('Market Capitalization')
plt.show()
