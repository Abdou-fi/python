def make_funcs():
    funcs = [] 
    for i in range(3): 
        funcs.append(lambda: i) 
    return funcs
f1, f2, f3 = make_funcs()
print(f1(), f2(), f3())