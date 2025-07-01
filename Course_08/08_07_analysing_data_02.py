# There is also a tail() method for viewing the last rows of the DataFrame.
# The tail() method returns the headers and a specified number of rows, starting from the bottom.
import pandas as pd

df = pd.read_csv('course_08\data.csv')
print(df.tail()) 
