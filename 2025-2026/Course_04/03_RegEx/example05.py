# {n}[23] The preceding item is matched exactly n times.

import re

text="ab ac abc abbc abbbc"

matches=re.findall(r"ab{2,3}c", text)
print(matches)
