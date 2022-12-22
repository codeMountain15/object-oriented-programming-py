# pyFileHandling02.py

import os

# open the file for reading
a = open("aFile.txt", "r")

# read the file contents
print(a.read())

# close the file
a.close()

# delete the file
if os.path.exists("aFile.txt"):
  os.remove("aFile.txt")
else:
  print("The file is not here")
