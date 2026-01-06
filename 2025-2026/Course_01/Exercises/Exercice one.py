import math
import cmath

def solve_quadratic(a:float, b:float, c:float ): 
 
    Delta = b**2 - 4*a*c
    print("Delta =", Delta)
    if Delta > 0:
        x1 = (-b + math.sqrt(Delta)) / (2*a)
        x2 = (-b - math.sqrt(Delta)) / (2*a)
        print("Roots are:", x1, "and", x2)
    elif Delta == 0:
        x = -b / (2*a)
        print("Root is:", x)
    else:
        x1 = (-b + cmath.sqrt(Delta)) / (2*a)
        x2 = (-b - cmath.sqrt(Delta)) / (2*a)
        print("Complex roots are:", x1, "and", x2)


solve_quadratic(2,1,2)