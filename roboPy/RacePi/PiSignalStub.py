'''
Created on 15.05.2015

@author: mario

Stub for testing pigpio signals locally
'''

class SignalStub(object):
    '''
    Signalstub replaces pigpio.pi functions including
    .set_mode
    .set_pull_up_down
    .callback
    
    Allows for external triggering of callbacks (.trigger(GPIOPIN))
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.connectedPins = {}
        self.callbacks = {}
    def trigger(self,pin):
        if pin in self.connectedPins.keys():
            self.execcallback(pin)
    def execcallback(self,pin):
        if pin in self.connectedPins.keys():
            func = self.connectedPins[pin]
            if func:
                func(pin,1,0)
    def set_mode(self,pin,mode):
        self.connectedPins[pin] = None
    
    def set_pull_up_down(self,pin,mode):
        '''
        do nothing intentionally
        this function sets the internal resistor at given GPIO PIN
        '''
        pass
    def callback(self,pin,edge,func):
        '''
        connect func to callback, forget about edge
        '''
        self.connectedPins[pin]=func
        