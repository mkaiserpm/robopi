'''
Created on 07.02.2015

@author: mario
'''

import time, sys
import pigpio

PINLAP1 = 27
PINLAP2 = 17

toggle = 0
def lap1detect(pin, status, tick):
    do_lap(1)
    return

def lap2detect(pin,status,tick): 
    do_lap(2)
    return

def do_lap(track):
    print "Lap detected on track %d"%(track)
    return

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    pi = pigpio.pi('racepi.local')
    pi.set_mode(PINLAP1,pigpio.INPUT)
    pi.set_mode(PINLAP2,pigpio.INPUT)
    pi.set_pull_up_down(PINLAP1,pigpio.PUD_UP)
    pi.set_pull_up_down(PINLAP2,pigpio.PUD_UP)
    event_start = pi.callback(PINLAP1,pigpio.RISING_EDGE, lap1detect)
    event_two = pi.callback(PINLAP2,pigpio.FALLING_EDGE, lap2detect)

    toggle = 0
    try:
        while True:
            lap1 = pi.read(PINLAP1)
            lap2 = pi.read(PINLAP2)    
            print "Lap1: %d Lap2 %d"%(lap1,lap2),
            print "\r"
            time.sleep(0.5)

    except KeyboardInterrupt:
            print "Keyboard interrupt. Shutting down..."
            pi.stop()
            print "pigpio released"
            print "Good bye"
            sys.exit()

