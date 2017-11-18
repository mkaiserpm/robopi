#!/usr/bin/python
'''
Created on 10.11.2014

@author: mario

Tests the Cable connections and GPIO output / serial connection to motor driver
(MD: MotorDriver)

PIN    GPIO   Connected Function
1        -    MD3,3 V 
4        -    MD5V VMot
8        14   MD Serial RX
9        GND  MD Ground
10       15   MD Serial TX
11       17   LED Green
12       18   LEDCam 
13       21   LED Red Blinking
14       GND
17       3V3  ULN2803a 3,3 V
20       GND  MD VMot Gnd
25       GND  ULN2803a GND
'''
import testing
import RPi.GPIO as GPIO
import time


class Test(testing.TestCase):


    def setUp(self):
        self.LEDBLINK = 13
        self.LEDCAM = 12
        self.LEDGREEN = 11
        GPIO.setmode(GPIO.BOARD) # use PIN No. not PPIO No.
        

    def tearDown(self):
        GPIO.cleanup()


    def testLEDCam(self):
        #LED Cam is on Pin 12 / GPIO18
        GPIO.setup(self.LEDCAM, GPIO.OUT)
        GPIO.output(self.LEDCAM, GPIO.HIGH)
        #Power down after 5 sec
        time.sleep(5)
        GPIO.output(self.LEDCAM,GPIO.LOW)
        
    def testLEDGreen(self):
        GPIO.setup(self.LEDGREEN, GPIO.OUT)
        GPIO.output(self.LEDGREEN, GPIO.HIGH)
        #Power down after 5 sec
        time.sleep(2)
        GPIO.output(self.LEDGREEN,GPIO.LOW)
        time.sleep(1)
        GPIO.setup(self.LEDGREEN, GPIO.OUT)
        GPIO.output(self.LEDGREEN, GPIO.HIGH)
        #Power down after 5 sec
        time.sleep(2)
        GPIO.output(self.LEDGREEN,GPIO.LOW)
        
    def testLEDRed(self):
        #LED red should be self blinking
        GPIO.setup(self.LEDBLINK, GPIO.OUT)
        GPIO.output(self.LEDBLINK, GPIO.HIGH)
        #Power down after 5 sec
        time.sleep(10)
        GPIO.output(self.LEDBLINK,GPIO.LOW)
    
    def testAllOn(self):
        GPIO.setup(self.LEDBLINK, GPIO.OUT)
        GPIO.setup(self.LEDCAM, GPIO.OUT)
        GPIO.setup(self.LEDGREEN, GPIO.OUT)
        
        GPIO.output(self.LEDBLINK, GPIO.HIGH)
        GPIO.output(self.LEDCAM, GPIO.HIGH)
        GPIO.output(self.LEDGREEN, GPIO.HIGH)
        
        time.sleep(5)
        GPIO.output(self.LEDBLINK,GPIO.LOW)
        GPIO.output(self.LEDGREEN,GPIO.LOW)
        GPIO.output(self.LEDCAM,GPIO.LOW)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    testing.main()