import math


a = float(input("enter your first number:"))
b = float(input("enter your second number: "))
c = float(input("enter your third number "))
delta = b*b- 4*a*c

print("the value of delta is:", delta)
if delta > 0:
   x1 = (-b +math.sqrt(delta)) / (2*a)
   x2 = (-b -math.sqrt(delta)) / (2*a)
   print("this equation have two solution:")
   print("x1 =", x1)
   print("x2 =", x2)

elif delta == 0:
    x = -b / (2*a)
    print("this equation have trible solutions:")
    print("x =", x)

else:
    real_part = -b / (2*a)
    imag_part =math.sqrt(-delta) / (2*a)
    print("the equation have two solution:")
    print(f"x1 = {real_part} + {imag_part}i")
    print(f"x2 = {real_part} - {imag_part}i")