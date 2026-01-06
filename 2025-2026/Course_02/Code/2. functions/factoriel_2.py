# factoriel function Assumes n an int > 0 Returns n!
t=10
def fact_iter(n):
    new_t=t
    result = 1 
    for i in range(1, n+1):
        result *= i 
    return result
# test
n=1000
print(fact_iter(n))

#####################


def fact_rec(n): 
    #Assumes n an int > 0,  Returns n! 
    if n == 1: 
        return n 
    else:
        return n*fact_rec(n - 1)
y=1000
print(fact_rec(y))


