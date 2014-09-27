try:
    import locale
except:
    pass

withMessagingMenu = False
try:
    from gi.repository import MessagingMenu
    from gi.repository import Notify
    withMessagingMenu = True
except ImportError:
    MessagingMenu = None
import bitcoin
from addresses import *
import shared
from electrumfirst import *
import sys
from time import strftime, localtime, gmtime
import time
import os
import hashlib
from pyelliptic.openssl import OpenSSL
import pickle
import platform
import debug
from debug import logger
import subprocess
import datetime
import random
import shelve
import threading
import multiprocessing
class electrumfirst(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.parent = parent
        QtCore.QObject.connect(self.ui.startelectrum, QtCore.SIGNAL("clicked()"), self.click_elec);
        QtCore.QObject.connect(self.ui.startbxb, QtCore.SIGNAL("clicked()"), self.click_bxb);
        QtCore.QObject.connect(self.ui.bitcoinqt, QtCore.SIGNAL("clicked()"), self.click_bitcoinqt);
    def click_elec(self):
        subprocess.Popen([os.getcwd()+'/electrum/bin/electrum.exe'], shell=True)
        settings = shelve.open("settings.slv")
        settings["electrumon"] = True
        settings.close()
        os._exit(0)
    def click_bxb(self):
        settings = shelve.open("settings.slv")
        settings["electrumon"] = True
        settings.close()
        restart_program()
    def click_bitcoinqt(self):
        settings = shelve.open("settings.slv")
        settings["electrumon"] = False
        settings.close()
        restart_program()
def run():
    app = QtGui.QApplication(sys.argv)
    myapp = electrumfirst()
    myapp.show()
    sys.exit(app.exec_())

def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)