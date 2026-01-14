# There is also a tail() method for viewing the last rows of the DataFrame.
# The tail() method returns the headers and a specified number of rows, starting from the bottom.
import pandas as pd
from myfunctions import file_path
file_path = file_path('data.csv')
df = pd.read_csv(file_path)
print(df.tail()) 
