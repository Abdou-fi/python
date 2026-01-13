list1 = [1,2,3]
list2 = list1
print(list1)
print(list2)
list1.append('hello')
print(list1)
print(list2)
print(id(list1))
print(id(list2))

tuple1=(10,20,30)
list1[0]=100
tuple1[0]=1000 #TypeError: 'tuple' object does not support item assignment
print(list1)
print(tuple1)