# ab+c matches "abc", "abbc", "abbbc", and so on, but not "ac".

import re
text1="ab ac abc abbc abbbc"
matches=re.findall(r"ab+c", text1)
print(matches)