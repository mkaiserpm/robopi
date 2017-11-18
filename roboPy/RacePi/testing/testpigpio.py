'''
Created on 07.02.2015

@author: mario
'''

import time, sys
import pigpio

PINLIGHT = 11
PINLED = 18
PINSQUAREBAR = 5
PINMINIBAR = 16
toggle = 0
def lapdetect(pin, status, tick):
    global toggle
    print "Lap detected!"
    print "pin/status/tick ", pin, "/", status, "/",tick
    if toggle == 0:
       toggle = 1
    else:
       toggle = 0
    return
     
def setLED(pin,pi):
    pi.write(pin,1)
    return

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    pi = pigpio.pi()
    pi.set_mode(PINLIGHT,pigpio.INPUT)
    pi.set_mode(PINLED,pigpio.OUTPUT)
    pi.set_pull_up_down(PINLIGHT,pigpio.PUD_OFF)
    event_start = pi.callback(PINLIGHT,pigpio.EITHER_EDGE, lapdetect)
    toggle = 0
    try:
        while True:
            level = pi.read(PINLIGHT)	
            print "Pin ",PINLIGHT,":",level
            time.sleep(0.5)
            pi.write(PINLED,toggle)

		
    except KeyboardInterrupt:
            print "Keyboard interrupt. Shutting down..."
            pi.stop()
            print "pigpio released"
            print "Good bye"
            sys.exit()

