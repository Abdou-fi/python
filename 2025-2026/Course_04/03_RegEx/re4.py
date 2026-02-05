# Validate a phone number

import re
phone="9655543210"
print(bool(re.fullmatch(r"\d{10}", phone)))