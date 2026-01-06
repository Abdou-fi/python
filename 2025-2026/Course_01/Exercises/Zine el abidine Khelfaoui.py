
A = float(input("give me the number A:"))
B = float(input("give me the number B:"))
C = float(input("give me the number C:"))
delta = (B**2)-4*A*C
from math import sqrt
if delta >0:
    x1 = (-B-sqrt(delta))/2*A
    x2 = (-B+sqrt(delta))/2*A
    print(f"the first root is x1={x1} and the second root is x2={x2}")
    
elif delta == 0 :
    x = -B/2*A
    print("there is double root x=",str(x))
else :
    x1 = -B/2*A
    x2 = sqrt(-delta)/2*A
    z1 = complex(x1, x2)
    z2 = complex(x1,-x2)
    print("there is complex solution z1=", z1," z2 = ", z2 )
    





    


