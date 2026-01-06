#solve the equation ax^2+bx+c=0
import math
import cmath

a=float(input(' entre the value of a='))
b=float(input(' entre the value of b='))
c=float(input(' entre the value of c='))
if a == 0 :
    x = -c/b
    print (x,'is the solution of the given equation')
else :
    d = (b**2)-(4*a*c)
    print('The determinant is d=',d)
    if d == 0 :
        x=-b/2*a
        print ('The given equation has double root x=', x)
    elif d < 0 :
        x=(-b+cmath.sqrt(d))/2*a
        y=(-b-cmath.sqrt(d))/2*a
        print ("The given equation does'nt have roots in the real numbers") 
        print ("however it has two roots in the complex numbers", "x=", x, "and" , "y=", y)
    else :
        x=(-b+math.sqrt(d))/2*a
        y=(-b-math.sqrt(d))/2*a  
        print (" The given equation has two roots ", "x=", x, "and" , "y=", y)
 