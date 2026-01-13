myFile = open("test.txt", 'rt')
content =myFile.readlines()
print(content)
myFile.close()