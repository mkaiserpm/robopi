'''
Created on 30.01.2015

@author: mario
'''
from RacePi_ICD import timer
from RacePi_ICD import piconnect
import pigpio
from datetime import datetime,timedelta

class Lapstat(object):
    def __init__(self,lapnum,laptime,deltatime):
        self.lapnumber = lapnum
        self.laptime = laptime
        self.laptimed = deltatime
        

class Laptimer(object):
    def __init__(self):
        self.lapcount = 0
        # laps as list of timerelems
        #self.laps = []
        self.lapstats = []
        self.state = 'STOPPED'
    
    def start(self):
        curT = datetime.now()
        lapN = 0
        lapD = timedelta(seconds=0)
        stat = Lapstat(lapN,curT,lapD)
        self.lapstats.append(stat)
        self.state = 'STARTED'
    
    def lap(self):
        if (self.state=='STARTED'):
            curLapTime = datetime.now()
            if (len(self.lapstats)==1):
                #First Lap
                lStat = self.lapstats[-1]
                lapN = 1
                lapT = curLapTime
                lapD = timedelta(seconds=0)
                
            else:
                lStat = self.lapstats[-1]
                lapN = lStat.lapnumber + 1
                lapT = curLapTime
                lapD = curLapTime - lStat.laptime
                
            self.lapstats.append(Lapstat(lapN,lapT,lapD))
    
    def trigger(self):
        if self.state == "STARTED":
            self.lap()
        if self.state == "STOPPED":
            self.start()          
            
    def stop(self):
        self.state = "STOPPED"

    def lastlap(self):
        '''
        returns timedelta element of last lap (timedelta between last two laps)
        '''
        l = len(self.lapstats)
        if (l>=2):
            dtime = self.lapstats[-1].laptimed
        else:
            dtime = timedelta(seconds=0)  
        return dtime

class Racetimer(object):
    '''
    Racetimer implements timing functions for a slotcar race 
    '''
    LTimer1 = Laptimer()
    LTimer2 = Laptimer()
    @staticmethod
    def detectlane1(pin,level,tick):
        print "Lane1 detected %d,%d,%d"%(pin,level,tick)
        #lanetimer start, lap, stop...
        Racetimer.LTimer1.trigger()
        return
    
    @staticmethod
    def detectlane2(pin,level,tick):
        print "Lane2 detected %d,%d,%d"%(pin,level,tick)
        Racetimer.LTimer2.trigger()
        return   
    
    def __init__(self, testStub = None):
        '''
        Constructor
        '''
        self.t_lane1 = timer.LANE1
        self.t_lane2 = timer.LANE2
        #self.LTimer1 = Laptimer()
        #self.LTimer2 = Laptimer()
        # Connect to Raceserver and setup lanepins
        if testStub:
            self.RPi = testStub
        else:
            self.RPi = pigpio.pi(piconnect.RACESERVER)
        self.RPi.set_mode(self.t_lane1,pigpio.INPUT)
        self.RPi.set_pull_up_down(self.t_lane1,pigpio.PUD_UP)
        self.lane1_event = self.RPi.callback(self.t_lane1,pigpio.RISING_EDGE, self.detectlane1)
        self.lane2_event = self.RPi.callback(self.t_lane2,pigpio.RISING_EDGE, self.detectlane2)

