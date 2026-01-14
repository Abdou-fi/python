import pandas as pd
from myfunctions import file_path
file_path = file_path('data.json')

df = pd.read_json(file_path)
print(df) 