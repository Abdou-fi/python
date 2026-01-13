import os
os.remove("file2.txt")

if os.path.exists("file3.txt"):
  os.remove("file3.txt")
else:
  print("The file does not exist")

