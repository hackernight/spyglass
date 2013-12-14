from os import listdir
from os.path import isfile, join
import os
from mutagen.mp4 import MP4
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
import mutagen


class SongHandler:
	def __init__(self, path):
		self.audio = EasyID3(path)

	def getVal(self, fieldIn):
		try:
			return audio[fieldIn]
		except:
			return ''

	def setVal(self, fieldIn, valIn):
		audio[fieldIn] = valIn
		audio.save()

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

	newSongClass = SongHandler(inputPath + "\\" + songName3)
	print(newSongClass.getVal('date'))
