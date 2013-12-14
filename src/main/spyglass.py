import argparse

class UserInterface(object):
	def __init__(self):
		super(UserInterface, self)

	def parseArg(self):
		parser = argparse.ArgumentParser(description='Identify your music files.')
		parser.add_argument('-s', '--source', dest='source', default= '../src/', help='This is the source dir for the music to come from')

		args = parser.parse_args()
		return(args.source)


argParser = UserInterface()
print(argParser.parseArg())
