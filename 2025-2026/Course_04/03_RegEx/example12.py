import re
txt = "That will be 59 dollars"
#Find all digit characters:
x = re.findall("\W", txt)
print(x)