# # Python code to demonstrate naive method
# # to compute factorial
# n = 23
# fact = 1

# for i in range(1, n+1):
#     fact = fact * i

# print("The factorial of 23 is : ", end="")
# print(fact)


# Python 3 program to find factorial of given number 
def factorial(n): 
    # Checking the number is 1 or 0 then return 1 other wise return factorial
    if (n==1 or n==0):
        return 1
    else:
        return (n * factorial(n - 1)) 
# Driver Code 
num = 6; 
print("number : ", num)
print("Factorial : ", factorial(num))