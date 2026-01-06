str1="Hello WORLD"
output1 = str1.capitalize()             # capitalize : first letter to capital
print(str1, ' capitalize : ', output1)

str2 ="HELLO WORLD"
output2=str2.lower()            # lower : all letters to lower
print(str2, ' lower : ', output2)

str3="hello world"
output3=str3.upper()           # upper : all letters to capital
print(str3, ' upper : ', output3)

str4="Python"
output4=str4.center(10, '*')   # center : add stars to the left and right
print(str4, ' center : ', output4)

str5 = "HELLO WORLD"
str5 = "sdflgsfd"
output5=str5.count('l')        # count : count the number of letters
print(str5, ' count"L" : ', output5)

str6="HELLO WORLD"
output6=str6.index('O')      # index : find the index of a letter
print(str6, ' index"O" : ', output6) 

s = 'amazing' 
print(s.index('a',2,8))       # index : find the index of a letter

str7="HELLO WORLD"
output7=str7.find('OR')       # find : find the index of a letter
print(str7, ' find("OR") : ', output7)

str8="31/01/2025"
output8=str8.replace('/', '-') # replace : replace a letter
print(str8, ' replace : ', output8)

str9="31/01/2025"
output9=str9.split('/')        # split : split a string
print(str9, ' split : ', output9)

str10="abc-123"
output10=str10.isalnum()       # isalnum : check if the string is alphanumeric
print(str10, ' isalnum : ', output10)

str11="1234"
output11=str11.isnumeric()       # isnumeric : check if the string is numeric
print(str11, ' isnumeric : ', output11)

str12="hello world"
output12=str12.islower()          # islower : check if the string is lower
print(str12, ' islower : ', output12)

str13="HELLO WORLD"
output13=str13.isupper()          # isupper : check if the string is upper
print(str13, ' isupper : ', output13)
