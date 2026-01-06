##############################################################
#  The following program is used to find out                 
#  the roots of the quadratic equation                       
#  ax² + bx + c = 0, where a, b and c are real numbers       
#  and a != 0                                                
#  using Python math and cmath libraries                        
#  
#  developped by Abdesselam Filali  
#  github: Abdou-fi
#  email : filali.a@gmail.com
##############################################################

import math
import cmath
def second_order_equation_roots( a: float, b: float, c: float) -> tuple: 
    discriminant = b**2 - 4*a*c 
    sqrtval = math.sqrt(abs(discriminant))    
    # checking condition for discriminant
    if discriminant >= 0:        # real roots
        return discriminant, (-b + sqrtval)/(2 * a),  (-b - sqrtval)/(2 * a)
    else:   # complex roots
        x1 = complex(- b / (2 * a), sqrtval/(2 * a))
        x2 = complex(- b / (2 * a),-sqrtval/(2 * a))
        return discriminant, x1, x2       
 
#############
# 2nd degree equation roots
def quadratic_equation_roots(x: float, y: float, z: float) -> tuple:
    return (y**2) - (4*x*z), (-y+cmath.sqrt((y**2) - (4*x*z)))/(2*x) , (-y-cmath.sqrt((y**2) - (4*x*z)))/(2*x)
    
# test Program 
a = 2
b = 4
c = 2
if a == 0: 
     print("Input correct quadratic equation") 
else:
    print(second_order_equation_roots(a, b, c))
    print(quadratic_equation_roots(a, b, c))
