import sympy as sp 
x = sp.Symbol('x') 
h = sp.log(x) 
H = sp.integrate(h, x)
print("integral of log(x) dx =", H)