numbers = [1, 2, 3]
try:
    print(numbers[3]) # This will raise an IndexError as the index 3 does not exist.
except IndexError as e:
    print("Error:", e)
