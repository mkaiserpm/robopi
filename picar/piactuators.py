
import donkeycar as dk
import time

class L298NBridge:
    def __init__(self,pin1,pin2,gpio_):
        self.pin1 = pin1
        self.pin2 = pin2
        self.gpio = gpio_
        #self.gpio.setmode(self.gpio.BOARD)
        self.gpio.setup(pin1,self.gpio.OUT)
        self.gpio.setup(pin2,self.gpio.OUT)
        self.gpio.output(pin1,False)
        self.gpio.output(pin2,False)
        print("Setting Motor to PINs {},{}".format(pin1,pin2))
    
    def setForward(self):
        self.gpio.output(self.pin1,False)
        self.gpio.output(self.pin2,True)
        
    def setReverse(self):
        self.gpio.output(self.pin1,True)
        self.gpio.output(self.pin2,False)
        
    def setZero(self):
        self.gpio.output(self.pin1,False)
        self.gpio.output(self.pin2,False)
    
    def setOne(self):
        self.gpio.output(self.pin1,True)
        self.gpio.output(self.pin2,True)

class PCA9685L298N:
    ''' 
    PWM motor controler using PCA9685 boards. 
    This is used for most RC Cars
    '''
    def __init__(self, channel,arda):
        # Initialise the PCA9685 using the default address (0x40).
        self.pwm = arda
        self.channel = channel
        print("My channel: {}".format(channel))

    def set_pulse(self, pulse):
        self.pwm.set_pwm(self.channel, 0, pulse) 

    def run(self, pulse):
        self.set_pulse(pulse)
        
class PWMSteeringL298N:
    """
    Wrapper over a PWM motor cotnroller to convert angles to PWM pulses.
    As well uses RaspiGPIOs to set correct L298N Motor Mode
    -1 Full Steering Left
    1 Full Steering Right
    MinPulse = 0
    MaxPulse = 4095
    """
    LEFT_ANGLE = -1 
    RIGHT_ANGLE = 1

    def __init__(self, controller=None,
                       left_pulse=-4095,
                       right_pulse=4095,
                       pin1=13,
                       pin2=15,
                       io = None):
        print("Setting Steering to PINs {},{}".format(pin1,pin2))
        self.controller = controller
        self.left_pulse = left_pulse
        self.right_pulse = right_pulse
        self.MotorH = L298NBridge(pin1,pin2,io)


    def run(self, angle):
        #map absolute angle to angle that vehicle can implement.
        #pulse = 0.
        #pulse = dk.utils.map_range(angle,
        #                        self.LEFT_ANGLE, self.RIGHT_ANGLE,
        #                        self.left_pulse, self.right_pulse)
        
        pulse = int(self.right_pulse * angle)
        
        '''
        if (pulse == 0) or (angle == 0.):
            self.MotorH.setZero()
            return
        '''
        if pulse > 0:
            self.MotorH.setForward()
        
        else:
            self.MotorH.setReverse()
            pulse*=-1
        #print("Angle: {}".format(angle))
        #print("Pulse: {}".format(pulse))
            
        if pulse > self.right_pulse:
            pulse = self.right_pulse           

        self.controller.set_pulse(pulse)

    def shutdown(self):
        self.run(0) #set steering straight



class PWMThrottleL298N:
    """
    Wrapper over a PWM motor cotnroller to convert -1 to 1 throttle
    values to PWM pulses.
    """
    MIN_THROTTLE = -1
    MAX_THROTTLE =  1

    def __init__(self, controller=None,
                       max_pulse=4095,
                       min_pulse=4095,
                       zero_pulse=0,
                       pin1 = 7,
                       pin2 = 11,
                       io = None):
        print("Setting Throttle to PINs {},{}".format(pin1,pin2))
        self.controller = controller
        self.max_pulse = max_pulse
        self.min_pulse = min_pulse
        self.zero_pulse = zero_pulse
        self.MotorH = L298NBridge(pin1,pin2,io)
        
        
        #send zero pulse to calibrate ESC
        self.controller.set_pulse(self.zero_pulse)
        time.sleep(1)


    def run(self, throttle):
        if throttle == 0:
            self.emergencystop()
            return
        pulse = int(self.max_pulse * throttle)
        '''
        if throttle > 0:
            pulse = dk.utils.map_range(throttle,
                                    0, self.MAX_THROTTLE, 
                                    self.zero_pulse, self.max_pulse)
            self.MotorH.setForward()
        else:
            pulse = dk.utils.map_range(throttle,
                                    self.MIN_THROTTLE, 0, 
                                    self.min_pulse, self.zero_pulse)
            self.MotorH.setReverse()
        '''
        if pulse > 0:
            self.MotorH.setForward()

        else:
            self.MotorH.setReverse()
            pulse *= -1
        
        if pulse > self.max_pulse:
            pulse = self.max_pulse               

        self.controller.set_pulse(pulse)
    
    def emergencystop(self):
        self.MotorH.setZero()
        self.controller.set_pulse(0)
        
        
    def shutdown(self):
        self.run(0) #stop vehicle