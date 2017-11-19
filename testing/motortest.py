'''
Created on 18.11.2017

@author: mario
'''

# Import required libraries
import sys
import time
import RPi.GPIO as GPIO
import time

# Use BCM GPIO references
# instead of physical pin numbers
#GPIO.setmode(GPIO.BCM)


# Define GPIO signals to use
# Physical pins 11,15,16,18
# GPIO17,GPIO22,GPIO23,GPIO24

StepPinForward=16
StepPinBackward=18
sleeptime=1


class L298NMotor():
    def __init__(self,p_en,p_in1,p_in2,gpio_):
        self.pin_enable = p_en
        self.pin_input1 = p_in1
        self.pin_input2 = p_in2
        self.gpio_ = gpio_
        #Setup Pin 
        gpio_.setup(p_en,GPIO.OUT)
        gpio_.setup(p_in1,GPIO.OUT)
        gpio_.setup(p_in2,GPIO.OUT)
        
    def off(self):
        """ Turns of all pins after use
        """
        gpio_ = self.gpio_
        gpio_.output(self.pin_enable, gpio_.LOW)
        gpio_.output(self.pin_input1, gpio_.LOW)
        gpio_.output(self.pin_input2, gpio_.LOW)
        
    def forward(self):
        self.setgpio_(True, True, False)
    
    def reverse(self):
        self.setgpio_(True,False,True)
    
    def stop(self):
        self.setgpio_(True,False,False)
    
    def rollout(self):
        self.setgpio_(False,False,False)

    def setgpio_(self,ena,in1,in2):
        self.gpio_.output(self.pin_enable,ena)
        self.gpio_.output(self.pin_input1,in1)
        self.gpio_.output(self.pin_input2,in2)

def steeringtest(m):
    for i in range(5):
        m.forward()
        time.sleep(1)
        m.reverse()

if __name__ == '__main__':
    
    GPIO.setmode(GPIO.BOARD)
    mode=GPIO.getmode()
    print(" mode ="+str(mode))
    GPIO.cleanup()
    
    
    #deinfe pin numbers
    M1EN = 29
    M1IN1 = 7
    M1IN2 = 11
    M2EN = 31
    M2IN1 = 13
    M2IN2 = 15
    
    sltime=5 #sec
    
    #Need 2 Motors
    m1 = L298NMotor(M1EN,M1IN1,M1IN2,GPIO)
    m2 = L298NMotor(M2EN,M2IN1,M2IN2,GPIO)
    
    allm = [m1,m2]
    
    print("Simple Motor Test:")
    print("Motors at full speed")
    
    print("Motos forward")
    for m in allm:
        m.forward()
        time.sleep(sltime)
        m.rollout()
    
    print("Motors backward")
    for m in allm:
        m.forward()
        time.sleep(sltime)
        m.rollout()

    print("Steering Test Motors forward")
    m1.forward()
    steeringtest(m2)
    for m in allm:
        m.stop()

    print("Done. Cleaning up")
    
    for m in allm:
        m.off()
    GPIO.cleanup()
