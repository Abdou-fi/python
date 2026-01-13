# myFile = open("test.txt", 'rt')
# print(myFile.read())
# myFile.close()


import os

# Get the directory of the current script
script_dir = os.path.dirname(__file__) 
print(script_dir)

# Join it with the filename
file_path = os.path.join(script_dir, 'test.txt')

# myFile = open(file_path, 'rt')
# print(myFile.read())
# myFile.close()

with open(file_path, 'rt') as f:
    print(f.read())

