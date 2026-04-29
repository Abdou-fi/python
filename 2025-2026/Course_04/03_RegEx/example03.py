# ab*c matches "ac", "abc", "abbc", "abbbc", and so on.
import re
text="ab ac abc abbc abbbc"
matches=re.findall(r"ab*c", text)
print (matches)
