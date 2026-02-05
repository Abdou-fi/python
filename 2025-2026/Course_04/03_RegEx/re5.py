# Extract hashtags

import re
text="Learning #python and #ai is fun" 
tag=re.findall(r"#\w+", text)
print(tag)