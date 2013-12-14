# Required
import unittest

""" 
This is an example test. Necessary functions are documented.
If you define this correctly, the tests will run from the main runner. 
"""
class TestSequenceFunctions(unittest.TestCase):

	# If necessary
    def setUp(self):
        print "I set myself up the bomb"  

    def test_veryDescriptiveName(self):
        assertTrue()

    def test_veryVERYDescriptiveName(self):
        assertTrue()
    
    # If necessary
    def tearDown(self):
    	print "I tore down that bomb I set up earlier"

""" 
You need to define a suite function. Use either of these two implentations
but name them suite() 	
"""
def suite_implOption1():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_veryDescriptiveName'))
    suite.addTest(WidgetTestCase('test_veryVERYDescriptiveName'))
    return suite

def suite_implOption2():
    tests = ['test_veryDescriptiveName', 'test_veryVERYDescriptiveName']
    return unittest.TestSuite(map(WidgetTestCase, tests))

# Required
if __name__ == '__main__':
    unittest.main()