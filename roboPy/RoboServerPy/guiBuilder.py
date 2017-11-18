'''
Created on 22.09.2014

@author: kaiser
'''

from PyQt4 import uic

if __name__ == '__main__':
    print("Compiling UI files...")
    uic.compileUiDir(".")
    print("Done!")