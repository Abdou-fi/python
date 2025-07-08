import pandas as pd
df = pd.read_csv('course_09\data1.csv')
new_df = df.dropna()
print(new_df.to_string())