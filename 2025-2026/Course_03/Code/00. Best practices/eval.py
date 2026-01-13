expression = input("Enter an arithmetic expression : ")
# expression = "2+3*4"

result = eval(expression)
print(f"The result of the eval function applied on '{expression}' is: {result}")

# Note: Using eval can be dangerous if you're evaluating untrusted input.   
# It can execute arbitrary code and pose security risks. Use with caution.
# For safer alternatives, consider using libraries like 'asteval' or 'numexpr' for evaluating expressions.

