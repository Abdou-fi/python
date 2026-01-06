import math

def solve_quadratic_equation():
   
    print(" ax^2 + bx + c = 0\n")

    
    try:
        a = float(input("enter the value of  a: "))
        b = float(input("enter the value of b: "))
        c = float(input("enter the value of  c: "))
    except ValueError:
        print("\n Error: inter a real numbers.")
        return


    
    if a == 0:
        print("\n 'a' should be non null .")
        return
    
    delta = b**2 - 4 * a * c
    print(f" delta= {delta}\n")

 
    if delta > 0:
        
        root1 = (-b + math.sqrt(delta)) / (2 * a)
        root2 = (-b - math.sqrt(delta)) / (2 * a)
        print("delta is positive so the equation has two real roots:")
        print(f"x1 = {root1}")
        print(f"x2 = {root2}")

    elif delta == 0:
      
        root = -b / (2 * a)
        print(" delta is null so the equation has one solution:")
        print(f"x = {root}")

    else:
        
        real_part = -b / (2 * a)
      
        imaginary_part = math.sqrt(-delta) / (2 * a)
        
        print("delta is negative so the equation has two complex roots:")
   
        print(f"x1 = {real_part:.2f} + {imaginary_part:.2f}i")
        print(f"x2 = {real_part:.2f} - {imaginary_part:.2f}i")


solve_quadratic_equation()

