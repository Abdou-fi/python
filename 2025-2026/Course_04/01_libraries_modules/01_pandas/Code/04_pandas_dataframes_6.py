import pandas as pd

from myfunctions import file_path
file_path = file_path('../data/data.csv')

df = pd.read_csv(file_path)
print(df) 