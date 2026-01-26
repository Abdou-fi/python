# Check if a given year is a leap year
year = int(input("Enter a year: "))
print(year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))