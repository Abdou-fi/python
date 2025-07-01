# Create a simple Pandas Series from a list:
# With the index argument, you can name your own labels.

import pandas as pd
a = [1, 7, 2]
print("\n ==========================================\n ")
print(a)
print("\n ==========================================\n ")
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)
print("\n ==========================================\n ")
#When you have created labels, you can access an item by referring to the label.
print(myvar["y"])