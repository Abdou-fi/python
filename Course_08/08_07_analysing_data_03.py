# Info About the Data
# The DataFrames object has a method called info(), 
# that gives you more information about the data set.

import pandas as pd
df = pd.read_csv('course_08\data.csv')
print(df.info())
