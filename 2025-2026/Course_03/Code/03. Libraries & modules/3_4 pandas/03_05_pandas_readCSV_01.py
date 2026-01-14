import pandas as pd
from myfunctions import file_path
file_path = file_path('data.csv')

df = pd.read_csv(file_path)
print(df) 
print("\n ==========================================\n")
print(df)

print(pd.options.display.max_rows) 