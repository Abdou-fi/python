# numerator = 10
# denominator = 0
# if denominator != 0:
#     result = numerator / denominator
# else:
#     print("Error: Cannot divide by zero")

# numerator = 10
# denominator = 0
# result = numerator / denominator if denominator != 0 else "Error: Denominator cannot be zero"
# print(result)

# numerator = 10
# denominator = 0
# try:
#     result = numerator / denominator
# except Exception:
#     print("Error: Cannot divide by zero")

numerator = 10
denominator = 0
try:
    result = numerator / denominator
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
    
    
