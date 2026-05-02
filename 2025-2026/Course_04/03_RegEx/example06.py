#    {min,}[23] The preceding item is matched min or more times.
#    {,max} The preceding item is matched up to max times.
#   {min,max} The preceding item is matched at least min times, but not more than max times.


import re
text="ab ac abc abbc abbbc abbbbc"
matches_1=re.findall(r"ab{2,}c", text)
matches_2=re.findall(r"ab{,3}c", text)
matches_3=re.findall(r"ab{2,3}c", text)
print (matches_1)
print (matches_2)
print (matches_3)
