# Pandas - Analyzing DataFrames
# Viewing the Data 
# One of the most used method for getting a quick overview of the DataFrame, is the head() method.
# The head() method returns the headers and a specified number of rows, starting from the top.

# Get a quick overview by printing the first 10 rows of the DataFrame:
import pandas as pd
from myfunctions import file_path
file_path = file_path('data.csv')

df = pd.read_csv(file_path)
print(df.head(10))

# Note: if the number of rows is not specified, the head() method will return the top 5 rows.
print("\n ==========================================\n")
df2 = pd.read_csv(file_path)
print(df2.head())