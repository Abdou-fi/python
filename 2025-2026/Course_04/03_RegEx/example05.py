# {n}[23] The preceding item is matched exactly n times.

import re
text2="ab ac abc abbc abbbc"

matches=re.findall(r"ab{2}c", text2)
print(matches)
