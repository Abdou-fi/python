# Find all email addresses

import re
text="Contact us at help@gmail.com or admin@yahoo.com" 
emails=re.findall(r"\S+@\S+", text)
print(emails)