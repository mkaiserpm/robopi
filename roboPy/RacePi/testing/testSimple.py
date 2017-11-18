'''
Created on 15.05.2015

@author: mario
'''
import unittest


class Test(unittest.TestCase):


    def testName(self):
        print "Test works!"


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()