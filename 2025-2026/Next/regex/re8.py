# Remove extra spaces

import re 
text="This has   extra   spaces"
clean=re.sub(r"\s+", " ", text)
print(clean)