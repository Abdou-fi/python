from myfunctions import file_path
import pandas as pd

file_path = file_path('data.csv')

df = pd.read_csv(file_path)
print(df)