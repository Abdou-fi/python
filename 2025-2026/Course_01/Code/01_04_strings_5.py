print("\n===========================================\n")
# Align strings with f-strings:
name = "Amine"
age = 30
print(f"|{name: <10}|{age:^5}|")

print("\n===========================================\n")

# Use f-strings with dictionary variables:
person = {"name": "Amine", "age": 30} 
print(f"My name is {person['name']} and I'm {person['age']} years old.")

print("\n===========================================\n")

# Use f-strings to format binary and hexadecimal numbers: 
num = 100
print(f"num = {num:b}")
print(f"num = {num:x}")

print("\n===========================================\n")

# Use f-strings to format dates and times: 
import datetime 
now = datetime.datetime.now() 
print(f"Today is {now:%B %d, %Y}")
print(f"Today is {now:%y%m%d}")

print("\n===========================================\n")

# Use f-strings to format currency values: 
salary = 58000 
print(f"My salary is ${salary:,}")

print("\n===========================================\n")

# Use f-strings with formatted strings: 
name = "Amine" 
age = 30 
message = f"My name is {name} and I'm {age} years old."
print(f"Message length: {len(message):<10}, Message: '{message:^20}'")

print("\n===========================================\n")

# Use f-strings to format scientific notation 
x = 1234567890.123456789 
print(f"x = {x:e}")

print("\n===========================================\n")

n:int = 1000000000
print(f'{n:_}')
print(f'{n:,}')
# th only 2 characters used for thousands separator
print(f'{n:_th}')

print("\n===========================================\n")

var: str = 'var'
print(f'{var:>20}:')
print(f'{var:_>20}:')

print(f'{var:<20}:')
print(f'{var:20}:')
print(f'{var:#<20}:')

print(f'{var:^20}:')
print(f'{var:|^20}:')

print("\n===========================================\n")

from datetime import datetime
now:datetime = datetime.now()
print(f'{now:%d.%m.%y}')
print(f'{now:%d.%m.%y (%H:%M:%S)}')
print(f'{now:%c}')   #local version of date & time
print(f'{now:%I%p}')

print("\n===========================================\n")

n: float = 1254.5678 
print(f'{n:.2f}')
print(round(n, 2))
print(f'{n:.0f}')
print(f'{n:,.3f}')
print(f'{n:_.3f}')

print("\n===========================================\n")

# debug code using fstring
a: int = 5
b: int = 10 
my_var: str = 'Bob says hi' 
print (f'a + b = {a+b}')
print (f'{a + b = }')
print(f'{bool(a) = }')
print(f'{my_var = }')

print("\n===========================================\n")