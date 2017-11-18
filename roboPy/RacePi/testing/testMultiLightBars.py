'''
Created on 07.02.2015

@author: mario
'''

import time, sys
import pigpio

PINLIGHT = 11
PINLED = 18
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
     
def blinkLED(pin,pi):
    global toggle
    if toggle == 1:
	toggle = 0
    else:
	toggle = 1

    pi.write(pin,toggle)
    return

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    pi = pigpio.pi('racepi.local')
    pi.set_mode(PINLIGHT,pigpio.INPUT)
    pi.set_mode(PINLED,pigpio.OUTPUT)
    pi.set_mode(PINSQUAREBAR,pigpio.INPUT)
    pi.set_mode(PINMINIBAR,pigpio.INPUT)
    pi.set_mode(PINLED,pigpio.OUTPUT)
    pi.set_pull_up_down(PINSQUAREBAR,pigpio.PUD_UP)
    pi.set_pull_up_down(PINMINIBAR,pigpio.PUD_UP)

    pi.set_pull_up_down(PINLIGHT,pigpio.PUD_UP)
    event_start = pi.callback(PINLIGHT,pigpio.RISING_EDGE, lapdetect)
    #event2 = pi.callback(PINMINIBAR,pigpio.RISING_EGDE,lapdetect)
    #event3 = pi.callback(PINSQUAREBAR,pigpio.RISING_EDGE,lapdetect)
    toggle = 0
    try:
        while True:
	    level = pi.read(PINLIGHT)	
            print "Pin ",PINLIGHT,":",level
            time.sleep(0.5)
	    blinkLED(PINLED,pi)

		
    except KeyboardInterrupt:
            print "Keyboard interrupt. Shutting down..."
            pi.stop()
            print "pigpio released"
            print "Good bye"
            sys.exit()

