import pandas as pd

df = pd.read_csv('course_08\data.csv')

print(df) 
print("\n ==========================================\n")
print(df.to_string())

print(pd.options.display.max_rows) 