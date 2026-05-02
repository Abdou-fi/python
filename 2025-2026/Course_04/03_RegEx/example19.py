import re

txt = "helmmmlo planet heljjjlo"

#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":

x = re.findall("he.{1,9}o", txt)

print(x)
