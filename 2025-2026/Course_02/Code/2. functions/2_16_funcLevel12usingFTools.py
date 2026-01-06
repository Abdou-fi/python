import time
from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n): 
    if n <= 1: 
        return n 
    else: 
        return fib(n - 1) + fib(n - 2) 
start=time.time()
result=fib(40)
print(f"Time: {time.time() - start:.10f} s") 
print(result)
