# hard coded vs. soft coded constants

# 1. hard coded constants
# YEAR = 2026
# birth_year = int(input("Birth Year:")) 
# age = YEAR - birth_year
# print (age)

# 2. soft coded constants
from datetime import date
birth_year = int(input("Birth Year:"))
age = date.today().year - birth_year
print(age)