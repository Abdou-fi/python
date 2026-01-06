# Without Counter
category1 = ['Low', 'Medium', 'High', 'Low', 'Medium', 'Medium', 'Low', 'Low', 'Low'] 
frequency1 = {}
for cat in category1: 
    if cat in frequency1: 
        frequency1[cat] += 1 
    else: 
        frequency1[cat] = 1 
print(frequency1)

# With Counter
from collections import Counter
category2 = ['Low', 'Medium', 'High', 'Low', 'Medium', 'Medium', 'Low', 'Low', 'Low'] 
frequency2 = Counter(category2)
print(dict(frequency2))


