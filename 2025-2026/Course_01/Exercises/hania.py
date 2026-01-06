import math

# Ask the user to enter three numbers: a, D, and C 
a = float(input("Enter the value of a: ")) 
b = float(input("Enter the value of b: ")) 
c = float(input("Enter the value of c: ")) 

# Compute the discriminant: 
Delta = b**2 - 4*a*c

if Delta > 0: 
    # Positive discriminant 
    x1 = (-b + math. sqrt(Delta)) / (2*a) 
    x2 = (-b - math. sqrt(Delta)) / (2*a) 
    print("The discriminant is positive.") 
    print("Two real solutions :") 
    print("x1 =", x1)
    print("x2 =", x2) 
elif Delta == 0: 
    # Zero discriminant 
    x = -b / (2*a)
    print("The discriminant is zero.") 
    print("One real repeated solution:") 
    print("x = :", x)
else: 
    # Negative discriminant
    print("The discriminant is negative.")
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-Delta) / (2*a)
    print("The descriminant is negative")
    print("Two complex solutions :")
    print("x1 = {} + {}i".format(real_part, imaginary_part))
    print("x1 = {} - {}i".format(real_part, imaginary_part))
