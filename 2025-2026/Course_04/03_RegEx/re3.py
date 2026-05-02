# Replace all digits with X

import re
text="My number is 0608521479 and my room is 12 "
new_text=re.sub(r"\d{10}", "XXXX", text)
print(new_text)