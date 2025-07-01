#max_rows 
# The number of rows returned is defined in Pandas option settings.
# You can check your system's maximum rows with the pd.options.display.max_rows statement. 

import pandas as pd
print(pd.options.display.max_rows) 
# You can change the maximum rows number with the same statement.
pd.options.display.max_rows = 9999
df = pd.read_csv('course_08\data.csv')
print(df) 