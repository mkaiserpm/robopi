'''
Created on 18.11.2017

@author: mario
'''

# Import required libraries
import sys
import time
import RPi.GPIO as GPIO
import time
#import numpy as np
import Adafruit_PCA9685


# Die Variable duty_cycle gibt die maximale Einschaltdauer der 
# Motoren pro 100 Herts vor. Dier liegt zwischen 0 bis 4095.
# FÃ¼r die Geschwindigkeit der Motoren beginnt die Einschaltdauer
# immer bei 0 und endet bei einem Wert ]0, 4095[.
duty_cycle = 4095

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
    def __init__(self,pwm,pwmchan,p_in1,p_in2,gpio_):
        self.pwm = pwm
        self.pwmchan = pwmchan
        self.pin_input1 = p_in1
        self.pin_input2 = p_in2
        self.gpio_ = gpio_
        #Setup Pin 
        #gpio_.setup(p_en,GPIO.OUT)
        gpio_.setup(p_in1,GPIO.OUT)
        gpio_.setup(p_in2,GPIO.OUT)
        
    def off(self):
        """ Turns of all pins after use
        """
        gpio_ = self.gpio_
        #gpio_.output(self.pin_enable, gpio_.LOW)
        gpio_.output(self.pin_input1, gpio_.LOW)
        gpio_.output(self.pin_input2, gpio_.LOW)
        self.pwm.set_pwm(self.pwmchan,0,0)
        
    def forward(self):
        self.setgpio_(True, False)
    
    def reverse(self):
        self.setgpio_(False,True)
    
    def setpwm(self,pwmval):
        print("PWMval {}".format(pwmval))
        power = pwmval
        if power < 0:
           # Rueckwaertsmodus Motor
           print("Reverse")
           self.reverse()
           pwm = -int(duty_cycle * power)
           if pwm > duty_cycle:
              pwm = duty_cycle
        elif power > 0:
           # Vorwaertsmodus Motor
           print("Forward")
           self.forward()
           pwm = int(duty_cycle * power)
           if pwm > duty_cycle:
              pwm = duty_cycle
        else:
           # Stoppmodus fuer den linken Motor
           self.off()
           pwm = 0
        print("Setting pwm to {}".format(pwm))   
        self.pwm.set_pwm(self.pwmchan,0,pwm)
    
    def stop(self):
        self.pwm.set_pwm(self.pwmchan,0,0)
        self.setgpio_(False,False)
    
    def rollout(self):
        self.setgpio_(False,False)

    def setgpio_(self,in1,in2):
        #self.gpio_.output(self.pin_enable,ena)
        self.gpio_.output(self.pin_input1,in1)
        self.gpio_.output(self.pin_input2,in2)

def steeringtest(m):
    rvals = [-1 + i*(2/40.) for i in range(40)]
    for rval in rvals:
        m.setpwm(rval)
        time.sleep(0.5)
        

if __name__ == '__main__':
    
    GPIO.setmode(GPIO.BOARD)
    mode=GPIO.getmode()
    print(" mode ="+str(mode))
    GPIO.cleanup()
    
    
    #deinfe pin numbers
    #M1EN = 29
    M1IN1 = 7
    M1IN2 = 11
    #M2EN = 31
    M2IN1 = 38
    M2IN2 = 40
    
    sltime=5 #sec
    
    PCA9685_pwm = Adafruit_PCA9685.PCA9685()
    PCA9685_pwm.set_pwm_freq(60)
    
    #Need 2 Motors
    m1 = L298NMotor(PCA9685_pwm,0,M1IN1,M1IN2,GPIO)
    m2 = L298NMotor(PCA9685_pwm,1,M2IN1,M2IN2,GPIO)
    
    allm = [m1,m2]
    
    print("PWM Motor Test:")
    print("Motors at full speed")
    
    print("Motos from reverse to forward, 10 steps")
    
    for m in allm:
        for cycle in range(10):
            pwmpercent = -1 + (cycle*2/10.) 
            m.setpwm(pwmpercent)
            time.sleep(1)
            m.rollout()

    print("Full Speed to stop")
    m1.setpwm(0.99)
    time.sleep(5)
    m1.stop()

    print("Steering Test")
    steeringtest(m2)
    print("Done. Cleaning up")
    
    for m in allm:
        m.off()
    GPIO.cleanup()
