from os.path import isfile, join
import os
from mutagen.mp4 import MP4
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
import mutagen

#The songhandler will, in the future, be able to use more than just MP3

class SongHandler:
	def __init__(self, path, eValsIn):
		self.audio = EasyID3(path)
		self.listOfExpectedValues = eValsIn

	def getVal(self, fieldIn):
		try:
			return audio[fieldIn]
		except:
			return ''

	def setVal(self, values):
		for currentField in values:
			audio[currentField] = values[currentField]
		audio.save()

	def returnExpectedFields(self):
		returnDict = {};
		for strVal in self.listOfExpectedValues:
			returnDict[strVal] = self.getVal(strVal)
		return returnDict

if __name__ == "__main__":
	inputPath = "../../../Test/Input/"
	
	#You should probably make a Test/Input folder directly above the 
	#spyglass folder

	songName = "01 Artist - Track 1.m4a"
	songName2 = "01 Track 1.mp3"
	songName3 = "Layla.mp3"

	#print(os.stat(inputPath + "\\" + songName))
	#print(os.st_flags(inputPath + "\\" + songName))

	audio = EasyID3(inputPath + "\\" + songName3)
	print(audio['date'])
	print(audio)

	try:
		print(audio['stuff'])
	except:
		print('')

	newSongClass = SongHandler(inputPath + "\\" + songName3,['artist','title','album']) 
	print(newSongClass.getVal('date'))

	print(newSongClass.returnExpectedFields())
