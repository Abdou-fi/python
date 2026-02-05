# Find all numbers in the text

import re
text="Order 123 cost 456 dollars" 
nums=re.findall(r"\d+", text)
print (nums)
