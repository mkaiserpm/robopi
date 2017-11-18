'''
Created on 07.02.2015

@author: mario
'''

import time, sys
import pigpio

def lapdetect(pin, status, tick):
    print "Lap detected!"
    print "pin/status/tick ", pin, "/", status, "/",tick
     


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    pi = pigpio.pi()
    pi.set_mode(23,pigpio.INPUT)
    pi.set_pull_up_down(23,pigpio.PUD_OFF)
    event_start = pi.callback(23,pigpio.FALLING_EDGE, lapdetect)
    try:
        while True:
	    level = pi.read(23)	
            print "Pin 23:",level
            time.sleep(0.5)
    except KeyboardInterrupt:
            print "Keyboard interrupt. Shutting down..."
            pi.stop()
            print "pigpio released"
            print "Good bye"
            sys.exit()

