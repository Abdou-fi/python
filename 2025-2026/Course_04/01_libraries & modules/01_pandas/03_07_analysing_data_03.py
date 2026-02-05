# Info About the Data
# The DataFrames object has a method called info(), 
# that gives you more information about the data set.

import pandas as pd
from myfunctions import file_path
file_path = file_path('data.csv')
df = pd.read_csv(file_path)
print(df.info())
