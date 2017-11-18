'''
Created on 07.02.2015

@author: mario
'''

import time, sys
import pigpio

PINLIGHT = 11
PINLED = 18
DEBOUNCE = 500 #debounce time of callbacks in ms
DEBOUNCETIME = 0
LASTTICK = 0
PINSQUAREBAR = 5
PINMINIBAR = 16
toggle = 0
def lapdetect(pin, status, tick):
    global toggle
    global DEBOUNCE
    global DEBOUNCETIME
    global LASTTICK
    DEBOUNCETIME = tick - LASTTICK
    LASTTICK = tick
    if DEBOUNCETIME>DEBOUNCE:
        print "Lap detected!"
        print "pin/status/tick ", pin, "/", status, "/",tick,"/Debounce: ",DEBOUNCETIME
        if toggle == 0:
            toggle = 1
        else:
            toggle = 0
    #else:
    #    print "ignoring callback due to debounce"
        
    return
     
def setLED(pin,pi):
    pi.write(pin,1)
    return

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    pi = pigpio.pi('raspi2.local')
    pi.set_mode(PINLIGHT,pigpio.INPUT)
    pi.set_mode(PINLED,pigpio.OUTPUT)
    pi.set_pull_up_down(PINLIGHT,pigpio.PUD_UP)
    event_start = pi.callback(PINLIGHT,pigpio.FALLING_EDGE, lapdetect)
    toggle = 0
    try:
        while True:
            level = pi.read(PINLIGHT)	
            print "Pin ",PINLIGHT,":",level
            time.sleep(0.5)
            #pi.write(PINLED,toggle)

		
    except KeyboardInterrupt:
            print "Keyboard interrupt. Shutting down..."
            pi.stop()
            print "pigpio released"
            print "Good bye"
            sys.exit()

