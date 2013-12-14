from os import listdir
from os.path import isfile, join
from os import walk
import os

class FileWalkAndFilter:
	def __init__(self, allowedExtensions):
		self.allowedExtensions = allowedExtensions

	def getFilesWithExtension(self, pathIn):
		f = []
		#print(pathIn)
		for (dirpath, dirnames, filenames) in walk(pathIn):
			for filename in filenames:
				#print(dirpath + filename)
				for expression in self.allowedExtensions:
					if(filename.find(expression, len(filename)-len(expression)) != -1):
						f.append(dirpath + filename)
						break

			for dirname in dirnames:
				#print(dirpath+dirname)
				if((dirname is str)):
					f.extend(self.getFilesWithExtension(dirpath+dirname))
		return f


		#print(f)

if __name__ == "__main__":
	inputPath = "../../../Test/Input/"
	
	#You should probably make a Test/Input folder directly above the 
	#spyglass folder

	songName = "Layla.mp3"

	#print(os.stat(inputPath + "\\" + songName))
	#print(listdir(inputPath))

	newSongFilter = FileWalkAndFilter([".mp3"])
	print(newSongFilter.getFilesWithExtension(inputPath))