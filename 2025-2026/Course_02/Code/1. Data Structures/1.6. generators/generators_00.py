###########################################################################
#  A. Filali       2025-06-21                                             #
#  generators                                                             #
#                                                                         #
#  This script demonstrates the use of the generators in Python.          #
#    
###########################################################################
gen = (x for x in range (5))
print(gen)
print(type(gen))
print(list(gen))
print(list(gen))


gen2 = (x**2 for x in range (10))
for _ in gen2:
    print (_, end=" ")

print ()

for _ in gen2:
    print (_, end=" ")
        


