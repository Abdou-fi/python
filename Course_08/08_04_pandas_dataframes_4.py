# Named Indexes
# With the index argument, you can name your own indexes.
# Add a list of names to give each row a name:
import pandas as pd
data = {
  "calories": [420.9, 380.7, 390.4],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df) 

print("\n ==========================================\n ")
#refer to the named index:
print(df.loc['day3'])