file = open('test.txt', 'a')
file.write("\n")
for i in range(1, 11, 1):
    file.write(f"{i} \t: " + "Now the file has more content! \n")
file.close()
file = open('test.txt', "r")
print(file.read())