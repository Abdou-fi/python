# f = open("test.txt", "a")
# f.write("\nNow the file has more content!")
# f.close()

# #open and read the file after the appending:
# f = open("test.txt", "r")
# print(f.read())
# f.close()

f = open("file1.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("file1.txt", "r")
print(f.read())
f.close()