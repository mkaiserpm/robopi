'''
Created on 15.05.2015

@author: mario


Test the PIGPIO Signal stub
'''
import unittest
import parentFolders
from PiSignalStub import SignalStub
from Racetimer import Racetimer, Laptimer
from RacePi_ICD import timer
import time
from datetime import datetime,timedelta

class TestSignal(unittest.TestCase):


    def setUp(self):
        self.SigStub = SignalStub()

    def tearDown(self):
        pass

    def testTrigger(self):
        lTimer = Laptimer()
        lTimer.trigger()
        time.sleep(0.5)
        lTimer.trigger()
        time.sleep(0.4)
        lTimer.trigger()

    def testConnection(self):
        testTimer = Racetimer(self.SigStub)
        self.SigStub.trigger(timer.LANE1)
        self.SigStub.trigger(timer.LANE2)

    def testLane1timer(self):
        testTimer = Racetimer(self.SigStub)
        self.SigStub.trigger(timer.LANE1)
        time.sleep(0.5)
        self.SigStub.trigger(timer.LANE1)
        lastlap = testTimer.LTimer1.lastlap()
        print lastlap.microseconds
        self.assertAlmostEqual(lastlap.microseconds,500000,delta=10000)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()