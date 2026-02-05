# Handling multiple exceptions with multiple except blocks
try:
    # This block will try to execute this code
    value = int(input("Please enter a number: "))
    result = 10 / value
except ValueError:
    # Executed if a ValueError occurs during the try block execution
    print("You must enter a valid integer.")
except ZeroDivisionError:
    # Executed if a ZeroDivisionError occurs during the try block execution
    print("Division by zero is not allowed.")
else:
    # Executed if no exceptions occur
    print("Result:", result)
finally:
    # Always executed, regardless of whether an exception occurred or not
    print("This block is always executed.")
