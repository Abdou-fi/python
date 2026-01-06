# hard coded vs. soft coded constants

# 1. hard coded constants
birth_year = int(input("Birth Year:")) 
age = 2025 - birth_year
print (age)

# 2. soft coded constants
from datetime import date
birth_year = int(input("Birth Year:"))
date.today().year - birth_year
print(age)