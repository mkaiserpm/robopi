'''
Created on 16.11.2014

MotorController requires pyserial for accessing Pololu motor hardware controller

@author: mario
'''
import serial
motorDevice = "/dev/ttyAMA0"
mbaud = 38400
maxspeed = 255
m0move = bytearray('88898A8B'.decode('hex'))
m1move = bytearray('\x8C\x8D\x8E\x8F')
class MotorController(object):
    '''
    Implements a motor controller interface for POLOLU qik 2s9v1
    connected on serial port
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.ser = serial.Serial(motorDevice,baudrate=mbaud)
    
    def resetErr(self):
        ret = self.ser.write('\x82')
        print ret
        
    def setMotor(self,motor,forward,speedp):
        '''
        motor: int 0=Motor0(Port), 1=Motor1(Star)
        forward: boolean to indicate forward movement (True), backward (False)
        speed: speed in percent of maxspeed (0=0, 100=255)
        '''
        print 'Received command for motor: ', motor, 'Forward:', forward,' Speedp: ', speedp
        if motor == 0:
            mmove = m0move
        else:
            mmove = m1move
            #reverse motor dir due reverse installation
            forward = not forward
        print [hex(h) for h in mmove]
        offs = 0
        realSpeed = int(round(speedp/100. * maxspeed))
        if realSpeed >= 127:
            offs = 1
            realSpeed -=128
            if realSpeed == 0:
                #Avoid sudden stop of motor when 0 command is send 
                realSpeed+=1
            
        if not forward:
            offs += 2
        '''
        Put together serial string
        MotorCommand + SpeedCmd (see pololu user manual)
        '''

        assert(realSpeed <= 127)

        mvcommand = bytearray()
        mvcommand.append(mmove[offs])
        print 'CalcSpeed: ', realSpeed
        mvcommand.append(int(realSpeed))
        print 'Motorcmd: '
        print [hex(m) for m in mvcommand]
        print len(mvcommand)
        self.ser.write(mvcommand)
        
    def coastMotor(self,motor):
        '''
        sends a coast command (rolling out motor) to motor given
        motor: int = No. of Motor
        '''
        if motor == 0:
            coastcmd = '\x86'
        else:
            coastcmd = '\x87'
        print coastcmd  
        self.ser.write(coastcmd)
        
    def __del__(self):
        self.ser.close()
        
