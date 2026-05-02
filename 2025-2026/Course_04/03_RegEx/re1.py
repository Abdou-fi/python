# Find all numbers in the text

import re
text="Order number 9 cost 456 dollars" 
nums=re.findall(r"\d+", text)
print (nums)
