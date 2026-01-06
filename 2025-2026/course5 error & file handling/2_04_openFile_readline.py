myFile = open("test.txt", 'rt')
print(myFile.readline(), end='')
print(myFile.readline(), end='')
print(myFile.readline(), end='')         #, end=''
for x in myFile:
  print(x, end='')
myFile.close()