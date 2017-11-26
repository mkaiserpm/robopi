'''
Simple Test to check hardware connection to motor drivers
Runes full deflection any side.
'''

from piactuators import PCA9685L298N, PWMSteeringL298N, PWMThrottleL298N
import RPi.GPIO as GPIO
import Adafruit_PCA9685
import time
#Define GPIO pins (Board count)
T_IN1 = 7
T_IN2 = 11
S_IN1 = 40
S_IN2 = 38
MOTFREQ = 100
T_CHAN = 0
S_CHAN = 1
MAXPULSE = 4095

if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)
    PCA9685_pwm = Adafruit_PCA9685.PCA9685()
    PCA9685_pwm.set_pwm_freq(MOTFREQ)
    #time.sleep(1)
    throttle_controller = PCA9685L298N(T_CHAN,PCA9685_pwm)
    throttle = PWMThrottleL298N(controller=throttle_controller,
                                    max_pulse=MAXPULSE,
                                    zero_pulse=0, 
                                    min_pulse=MAXPULSE,
                                    pin1 = T_IN1,
                                    pin2 = T_IN2,
                                    io = GPIO)
    
    steering_controller = PCA9685L298N(S_CHAN,PCA9685_pwm)
    steering = PWMSteeringL298N(controller=steering_controller,
                                    left_pulse=MAXPULSE, 
                                    right_pulse=MAXPULSE,
                                    pin1 = S_IN1,
                                    pin2 = S_IN2,
                                    io = GPIO)
    
    #Test Throttle
    print("Throttle test")
    tstring = "Forward to Reverse, 2 second steps"
    tvals = [1.,0.8,0.6,0.4,0.2,0,-0.2,-0.4,-0.6,-0.8,-1.]
    print(tstring)
    for val in tvals:
        throttle.run(val)
        time.sleep(2)
    throttle.run(0)
    print("Left to Right, 2 second steps")
    for val in tvals:
        steering.run(val)
        time.sleep(2)
    steering.run(0)
    print("Test complete")
    