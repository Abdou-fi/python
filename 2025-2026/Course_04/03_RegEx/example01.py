import re
text="i have a gray car and a grey house and a gray life" 
occurences_1=re.findall(r"gray|grey", text)   # r stands for raw string, it tells python to ignore escape characters
occurences_2=re.findall(r"gr(a|e)y", text)
print (occurences_1)
print (occurences_2)
for match in re.finditer(r"gr(a|e)y", text):
    print (match.group())
    print (match.start())
    print (match.end())
    print (match.span())