'''
Created on 02.11.2014

@author: mario
'''
import sys
from PyQt4.QtGui import QMainWindow, QPushButton
from PyQt4.QtCore import QObject, pyqtSignal, SIGNAL, SLOT
from PyQt4.Qt import QApplication
from ui_roboControl import Ui_MainWindow
sys.path.append("..")

class qtMainWindow(QMainWindow,Ui_MainWindow):
    "Main Window of Simulation Application"
    def __init__(self,application):
        QMainWindow.__init__(self)
        self.App = application
        self.setupUi(self)
        
        
class robocontrolApp(QApplication):
    def __init__(self,argv):
        QApplication.__init__(self,argv)
        
    def initialize(self):
        self.mainWindow = qtMainWindow(self)
        self.mainWindow.setWindowTitle("RoboControl - MK 2014")
        #self.mainWindow.setCaption()
        self.mainWindow.show()
        QObject.connect(self, SIGNAL('lastWindowClosed()'),self,SLOT('quit()'))
    
    def run(self):
        self.initialize()
        self.exec_()
        #self.exec_loop()


if __name__ == '__main__':
    mainApp = robocontrolApp(sys.argv)
    mainApp.run()
    #sys.exit(mainApp.exec_())
