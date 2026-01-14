#max_rows 
# The number of rows returned is defined in Pandas option settings.
# You can check your system's maximum rows with the pd.options.display.max_rows statement. 

import pandas as pd
from myfunctions import file_path
file_path = file_path('data.csv')

# You can change the maximum rows number with the same statement.
pd.options.display.max_rows = 9999
df = pd.read_csv(file_path)
print(df) 