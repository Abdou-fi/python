# Extract dates from a text

import re
text= "Meeting on 12/08/2023 and 15/09/2035"
dates = re.findall(r"\d{2}/\d{2}/\d{4}", text)
print(dates)