# Replace all digits with X

import re
text="My number is 8521479"
new_text=re.sub(r"\d", "X", text)
print(new_text)