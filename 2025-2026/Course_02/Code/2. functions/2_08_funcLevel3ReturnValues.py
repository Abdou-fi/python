# from math import exp, cos
# def calculate(a:float,b:float)-> float :
#   return exp(a)*cos(b)

# print(calculate(10, 20))

##################################

import math
def my_func(a,b):
  return a+b, abs(a-b), math.sin(a*b), a/b
# print(my_func(10, 20))
list1=list(my_func(10, 20))
print(list1)

# what if b==0 ?