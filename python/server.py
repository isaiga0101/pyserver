import sys
from os import walk

#Get folder from User
mypath = input("Input folder path: ")

# Scan folder
f = []
for (dirpath, dirnames, filenames) in walk(mypath):
	f.extend(filenames)
	break

print(f)