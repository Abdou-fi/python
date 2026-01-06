
# Python Coding Challenge-Question With Answer
a = [1, 2, 3]
b = [10, 20, 30]
for i, j in zip(a, b): 
    i = i + 100
    print(i, j)
#Answer --> clcoding.com (ID - 291125)
# A. 110 120 130 
# B. 10 20 30 
# C. Error
# D. 101 102 103

"""
https://github.com/Abdou-fi/python/tree/main/2025-2026/Course_02
"""



countries = ['France',
                  'Germany',
                  'Greece']
capitals = ['Paris',
                'Berlin',
                'Athens']
for country, capital in zip(countries, capitals):
        print(f"the Capital city of {country} is {capital}")
