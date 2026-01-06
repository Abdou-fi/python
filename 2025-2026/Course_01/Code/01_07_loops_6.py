# Controlling loops ; break and continue
# Example 1 : break

# for i in range(1, 6):
#   if i == 3:
#     break
#   print(i)

### Example 2 : continue
# for i in range(1, 6):
#   if i == 3:
#     continue
#   print(i)

### Example 2 : both

for num in range(1, 6): 
  if num == 3: 
    continue # Skip number 3 
  if num == 5: 
    break # Stop the loop at 5
  print(num)