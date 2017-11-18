#!/usr/bin/python
'''
Created on 22.09.2014

@author: kaiser
Simple QT gui to setup / start Workload Sim
'''
import sys
from PyQt4.QtGui import QMainWindow, QPushButton
from PyQt4.QtCore import QObject, pyqtSignal, SIGNAL, SLOT
from PyQt4.Qt import QApplication
from ui_worksimMain import Ui_MainWindow
sys.path.append("..")
from guiConfigBuilder import getAvailableConfigs


class qtMainWindow(QMainWindow,Ui_MainWindow):
    "Main Window of Simulation Application"
    def __init__(self,application):
        QMainWindow.__init__(self)
        self.App = application
        self.setupUi(self)
        self.pushRunButton.clicked.connect(self.runButtonClicked)
        self.pushNew.clicked.connect(self.newSettingClicked)
        self.pushSave.clicked.connect(self.saveSettingsClicked)
    
    def loadLastConfig(self):
        self.comboSettings.addItems(getAvailableConfigs())
    
    def runButtonClicked(self):
        "Run button clicked"
        print("running...")
    
    def saveSettingsClicked(self):
        "Save the selected setting"
        pass
    
    def newSettingClicked(self):
        "Save the current setting as new setting"
        pass
    
    def getDictconfig(self):
        confdict = {}
        confdict['boolAutoseed'] = str(self.checkRandom.isChecked())
        confdict['intSeed'] = self.lineSeed.text()
        confdict['boolGantt']=str(self.checkGantt.isChecked())
        confdict['boolCSV']=str(self.checkCSV.isChecked())
        confdict['boolPlot']=str(self.checkPlot.isChecked())
        confdict['intRuntime']=self.lineRuntime.text()
        confdict['listSelectedScenarios']= self.readTextFromQList(self.listScenSelected)
        
        return confdict
    def readTextFromQList(self,listwidget):
        textlist=[]
        for listitem in listwidget:
            textlist.append(listitem.text())
        return textlist
    
        
class simApplication(QApplication):
    def __init__(self,argv):
        QApplication.__init__(self,argv)
        
    def initialize(self):
        self.mainWindow = qtMainWindow(self)
        self.mainWindow.setWindowTitle("WorkloadSimulation - for internal use only - (C) Airbus Defence and Space 2014 - TAEIA")
        #self.mainWindow.setCaption()
        self.mainWindow.show()
        QObject.connect(self, SIGNAL('lastWindowClosed()'),self,SLOT('quit()'))
    
    def run(self):
        self.initialize()
        self.exec_()
        #self.exec_loop()


if __name__ == '__main__':
    mainApp = simApplication(sys.argv)
    mainApp.run()
    #sys.exit(mainApp.exec_())
    

