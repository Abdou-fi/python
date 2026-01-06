def AI(func, *arg):
    return func(*arg)

def triple_power(y): 
    return y**3 

def add(x, y):
    return x + y

result1 = AI(triple_power, 5)
result2 = AI(add, 5, 3)
print(result1)
print(result2)

