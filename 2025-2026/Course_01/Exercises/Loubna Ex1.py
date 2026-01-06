import math

def seconnd_degree(a, b, c)

    if a == 0:
        x = -c/b
        print("La solution de l'équation est:", x)
    else :
        diter=b**2 - 4*a*c
        print("Le diterminant = ", diter)
        if diter == 0 :
            x = -b/(2*a)
            print("La solution de l'équation est:", x)
        elif diter < 0 :
          
            x1 = (-b + math.sqrt(abs(diter))*1j) / (2 * a)
            x2 = (-b - math.sqrt(abs(diter))*1j) / (2 * a)
            print("Les solutions de l'équation sont : x1 =", x1, ", x2 =", x2)
        else :
            x1=(-b + math.sqrt(diter)) / (2 * a)
            x2=(-b - math.sqrt(diter)) / (2 * a)
            print("Les solutions de l'équation sont : x1 =", x1, ", x2 =", x2)

        