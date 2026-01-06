# list comprehension

my_list = [1, 2, 3, 4, 5]
squared_list01 = [x**2 for x in my_list]
squared_list02 = [x**2 for x in range(1, 6)]
squared_list03 = [x**2 for x in range(1, 6) if x % 2 == 0]
squared_list04 = [x**2 if x % 2 == 0 else x for x in range(1, 6)]
squared_list05 = [x**2 if x % 2 == 0 else x for x in my_list]
squared_list06 = [x**2 if x % 2 == 0 else x for x in my_list if x > 2]
squared_list07 = [x**2 if x % 2 == 0 else x for x in my_list if x > 2 and x < 5]
squared_list08 = [x**2 if x % 2 == 0 else x for x in my_list if x > 2 and x < 5 and x != 4]
squared_list09 = [x**2 if x % 2 == 0 else x for x in my_list if x > 2 and x < 5 and x != 4 and x != 3]
squared_list10 = [x**2 if x % 2 == 0 else x for x in my_list if x > 2 and x < 5 and x != 4 and x != 3 and x != 1]


print(squared_list01)
print(squared_list02)
print(squared_list03)
print(squared_list04)
print(squared_list05)
print(squared_list06)
print(squared_list07)
print(squared_list08)
print(squared_list09)
print(squared_list10)
