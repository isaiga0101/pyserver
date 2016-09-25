import sys
from os import walk

class directory(object):
	def __init__(self, path):
		self.path = path
		self.filelist = []
		self.dirlist = []
		for (dirpath, dirnames, filenames) in walk(path):
			self.filelist.extend(filenames)
			self.dirlist.extend(dirnames)
			break
	def refresh(self):
		for (dirpath, dirnames, filenames) in walk(self.path):
			self.filelist.extend(filenames)
			self.dirlist.extend(dirnames)
			break
		

#Get folder from User
dir = directory(input("Input folder path: "))
print(dir.filelist, dir.dirlist)