# pyFileHandling.py

a = open("aFile.txt", "w")
a.write("Two days till Christmas!")
a.close()

# open the file for reading
a = open("aFile.txt", "r")

# read the file contents
print(a.read())

# close the file
a.close()
