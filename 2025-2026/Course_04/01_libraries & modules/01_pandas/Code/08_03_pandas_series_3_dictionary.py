# Create a simple Pandas Series from a dictionary:
# Note: The keys of the dictionary become the labels.
import pandas as pd
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)
# To select only some of the items in the dictionary, 
# use the index argument and specify only the items you want to include in the Series.
print("\n ==========================================\n ")
myvar2 = pd.Series(calories, index = ["day1", "day2"])
print(myvar2)
print("\n ==========================================\n ")
