import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data)
print(df) 
print("\n ==========================================\n ")

# Pandas use the loc attribute to return one or more specified row(s)
# refer to the row index:
print(df.loc[0])   # Note: This example returns a Pandas Series.

