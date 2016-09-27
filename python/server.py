import sys
from os import walk

class directory(object):
	"Scans directory and makes lists and dictionaries based on Directory"
	def __init__(self, path):
		self.path = path
		self.filelist = []
		self.dirlist = []
		self.fullfilepaths = []
		self.fulldirpaths = []
		for (dirpath, dirnames, filenames) in walk(path):
			self.filelist.extend(filenames)
			self.dirlist.extend(dirnames)
			break
	def refresh(self):
		for (dirpath, dirnames, filenames) in walk(self.path):
			self.filelist.extend(filenames)
			self.dirlist.extend(dirnames)
			break
			
	def fullscan(self):
		nextdirs = []
		
		for dirs in self.dirlist:
			self.fulldirpaths.extend(walk(self.path+"/"+dirs))
		
#Get folder from User
dir = directory(input("Input folder path: "))
print("Initial Directory Scan")
for file in dir.filelist:
	print("Files: ", file)

for folder in dir.dirlist:
	print("Folders: ", folder)

dir.fullscan()
print("Test Full Scan: ",dir.fulldirpaths)