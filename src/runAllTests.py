import unittest

class TestDiscovery(unittest.TestLoader):
	
	def findTests(self, directory="test"):
		self.discover(directory, "test_example*")

loader = TestDiscovery()
list = loader.findTests()
print list