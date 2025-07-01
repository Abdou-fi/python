# Pandas - Analyzing DataFrames

# Viewing the Data 
# One of the most used method for getting a quick overview of the DataFrame, is the head() method.
# The head() method returns the headers and a specified number of rows, starting from the top.

# Get a quick overview by printing the first 10 rows of the DataFrame:
import pandas as pd
df = pd.read_csv('course_08\data.csv')
print(df.head(10))

# Note: if the number of rows is not specified, the head() method will return the top 5 rows.

print("\n ==========================================\n")
df2 = pd.read_csv('course_08\data.csv')
print(df2.head())