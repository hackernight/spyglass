# Required
import unittest

""" 
This is an example test. Necessary functions are documented.
If you define this correctly, the tests will run from the main runner. 
"""
class ExampleTest(unittest.TestCase):

    def test_veryDescriptiveName(self):
        self.assertTrue(True)

    def test_veryVERYDescriptiveName(self):
        self.assertEqual(1,1)

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

# Required to run this individually
if __name__ == '__main__':
    unittest.main()