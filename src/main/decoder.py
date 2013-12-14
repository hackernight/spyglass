from pydub import AudioSegment

class AudioDecoder(object):
	
	""" Returns in seconds """
	def getLength(self, path):
		song = AudioSegment.from_mp3(path)
		return song.duration_seconds

	def makeWav(self, path, destination):
		song = AudioSegment.from_mp3(path)
		return song.export(destination, "wav")

if __name__ == "__main__":
	testMp3Path = "C:\Users\icbat\Music\Thatched Villagers.mp3"
	decoder = AudioDecoder()
	# convertedWav = decoder.getWav()
	print decoder.getLength(testMp3Path)