'''
Created on 16.11.2014

@author: mario
This tests runs motor test on both motors

Left Motor (Port): M0
Right Motor (Star): M1

'''
import unittest

import time

import os,sys,inspect
#parentdir = os.path.dirname(__file__)
#print "Parent ", parentdir

#sys.path.insert(0,parentdir)
#print sys.path
#from ..import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import ICD

class Test(unittest.TestCase):


    def setUp(self):
        self.mc = ICD.MotorController()


    def tearDown(self):
        pass

    def testbothMotors(self):
        for spd in range(0,101,10):
            self.mc.setMotor(0,True,spd)
            self.mc.setMotor(1,True,spd)
            time.sleep(1)
        self.mc.coastMotor(0)
        self.mc.coastMotor(1)
        
    def testMotors(self):
        #Left motor slow forward
        for i in range(2):
            for spd in range(0,101,10):
                self.mc.setMotor(i,True,spd)
                time.sleep(1)
            self.mc.coastMotor(i)
        #


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
