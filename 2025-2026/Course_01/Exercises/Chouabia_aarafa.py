import math
# Demander à l'utilisateur d'entrer les valeurs
a = float(input("Entrez la valeur de a : "))
b = float(input("Entrez la valeur de b : "))
c = float(input("Entrez la valeur de c : "))

# Calcul du discriminant
delta = b**2 - 4*a*c
print("La valeur du discriminant ? est :", delta)

# Détermination du type de solutions
if delta > 0:
    print("L'équation admet deux solutions réelles et distinctes.")
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("La premiï¿½re solution x1 =", x1)
    print("La deuxiï¿½me solution x2 =", x2)

elif delta == 0:
    print("L'équation admet une solution réelle double.")
    x = -b / (2*a)
    print("La solution est x =", x)

else:
    print("L'équation admet deux solutions complexes.")
    partie_reelle = -b / (2*a)
    partie_imaginaire = math.sqrt(-delta) / (2*a)
    x1=complex( partie_reelle, partie_imaginaire)
    x2=complex( partie_reelle, -partie_imaginaire)
    print("x1 =", x1)
    print("x2 =", x2)
    print(type(x1))