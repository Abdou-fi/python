# f = open("test.txt", "a")
# f.write("\n8. Now the file has more content!")
# f.close()

# # open and read the file after the appending:
# f = open("test.txt", "r")
# print(f.read())
# f.close()

# f = open("file2.txt", "w")
# f.write("new content!")
# f.close()

# #open and read the file after the overwriting:
# f = open("file2.txt", "r")
# print(f.read())
# f.close()

# f = open("file4.txt", "x")
# f.write("new content!")
# f.close()
#open and read the file after the overwriting:
try:
    f = open("file4.txt", "x")
    print(f.read())
    f.close()
except FileExistsError:
    print("File already exists")
    

    