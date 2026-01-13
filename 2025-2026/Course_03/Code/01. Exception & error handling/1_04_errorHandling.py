# errors & exceptions handling
try:
    print("Try block:")
    # x = 10 / 0
    # x = 10 / "a"
    x = 10 / None
except ZeroDivisionError as e:
    print("ZeroDivisionError: ", e)
except TypeError as e:
    print("TypeError: ", e)
except Exception as e: # catch all other exceptions
    print("Exception: ", e)
