# Split Text using regex

import re
text="apple, banana; orange | mango"
parts = re.split(r"[,;|]", text)
print (parts)