#!/usr/bin/env python
# Copyright (c) 2012 Jonathan Warren
# Copyright (c) 2012 The Bitmessage developers
# Distributed under the MIT/X11 software license. See the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

# Right now, PyBitmessage only support connecting to stream 1. It doesn't
# yet contain logic to expand into further streams.

# The software version variable is now held in shared.py

import signal  # Used to capture a Ctrl-C keypress so that Bitmessage can shutdown gracefully.
# The next 3 are used for the API
import singleton
import os
import bitcoin
from bitcoin.exceptions import InsufficientFunds
from SimpleXMLRPCServer import SimpleXMLRPCServer
from api import MySimpleXMLRPCRequestHandler
from helper_startup import isOurOperatingSystemLimitedToHavingVeryFewHalfOpenConnections

import shared
from helper_sql import sqlQuery
import threading
import helper

# Classes
#from helper_sql import *
#from class_sqlThread import *

from class_sqlThread import sqlThread
from class_singleCleaner import singleCleaner
#from class_singleWorker import *
from class_objectProcessor import objectProcessor
from class_outgoingSynSender import outgoingSynSender
from class_singleListener import singleListener
from class_singleWorker import singleWorker
from class_worker import objectProcessor2
from helper import worker
#from class_addressGenerator import *
from class_addressGenerator import addressGenerator
from debug import logger

# Helper Functions
import helper_bootstrap
import helper_generic


from subprocess import call
import time

# OSX python version check
import sys


if sys.platform == 'darwin':
    if float("{1}.{2}".format(*sys.version_info)) < 7.5:
        msg = "You should use python 2.7.5 or greater. Your version: %s", "{0}.{1}.{2}".format(*sys.version_info)
        logger.critical(msg)
        print msg
        sys.exit(0)

def connectToStream(streamNumber):
    shared.streamsInWhichIAmParticipating[streamNumber] = 'no data'
    selfInitiatedConnections[streamNumber] = {}
    shared.inventorySets[streamNumber] = set()
    queryData = sqlQuery('''SELECT hash FROM inventory WHERE streamnumber=?''', streamNumber)
    for row in queryData:
        shared.inventorySets[streamNumber].add(row[0])

    
    if isOurOperatingSystemLimitedToHavingVeryFewHalfOpenConnections():
        # Some XP and Vista systems can only have 10 outgoing connections at a time.
        maximumNumberOfHalfOpenConnections = 9
    else:
        maximumNumberOfHalfOpenConnections = 64
    for i in range(maximumNumberOfHalfOpenConnections):
        a = outgoingSynSender()
        a.setup(streamNumber, selfInitiatedConnections)
        a.start()


# This thread, of which there is only one, runs the API.
class singleAPI(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        se = SimpleXMLRPCServer((shared.config.get('bitmessagesettings', 'apiinterface'), shared.config.getint(
            'bitmessagesettings', 'apiport')), MySimpleXMLRPCRequestHandler, True, True)
        se.register_introspection_functions()
        se.serve_forever()

# This is a list of current connections (the thread pointers at least)
selfInitiatedConnections = {}

if shared.useVeryEasyProofOfWorkForTesting:
    shared.networkDefaultProofOfWorkNonceTrialsPerByte = int(
        shared.networkDefaultProofOfWorkNonceTrialsPerByte / 16)
    shared.networkDefaultPayloadLengthExtraBytes = int(
        shared.networkDefaultPayloadLengthExtraBytes / 7000)
import subprocess
import config
import shelve
from bsddb.db import *
from pywa import delete_from_wallet
class Main:
    def start(self, daemon=False):
        from PyQt4 import QtGui, QtCore
        app = QtGui.QApplication(sys.argv)
        import bitmessage_icons_rc
        splash_pix = QtGui.QPixmap(':/newPrefix/images/loading.jpg')
        splash = QtGui.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)

        splash.setMask(splash_pix.mask())
        splash.show()
        shared.daemon = daemon

        datadir = os.getcwd()+"/btc"
        print  datadir
        db_env = DBEnv(0)
        r = db_env.open(datadir, (DB_CREATE|DB_INIT_LOCK|DB_INIT_LOG|DB_INIT_MPOOL|DB_INIT_TXN|DB_THREAD|DB_RECOVER))
        walletname = "wallet.dat"
        fordel = shelve.open("fordel.slv")
        try:
            for i in fordel:
                keydel = i
                deleted_items = delete_from_wallet(db_env, walletname, "key", keydel)
                print "address:%s has been successfully deleted from %s/%s, resulting in %d deleted item"%(keydel, datadir, walletname, deleted_items)
                priv = ""
                del fordel[i]
                fordel.sync()
        except:
            print "can't delete addresses"
        fordel.close()
        #changes start
        process = subprocess.Popen([os.getcwd()+'/btc/bitcoin-qt.exe', "-datadir="+datadir], shell=True, creationflags=subprocess.SW_HIDE)
        print "Wait bitcoin-qt"
        time.sleep(5)



        #changes end here
        #
        # is the application already running?  If yes then exit.
        thisapp = singleton.singleinstance()

        signal.signal(signal.SIGINT, helper_generic.signal_handler)
        # signal.signal(signal.SIGINT, signal.SIG_DFL)

        helper_bootstrap.knownNodes()
        # Start the address generation thread
        addressGeneratorThread = addressGenerator()
        addressGeneratorThread.daemon = True  # close the main program even if there are threads left
        addressGeneratorThread.start()

        # Start the thread that calculates POWs
        singleWorkerThread = singleWorker()
        singleWorkerThread.daemon = True  # close the main program even if there are threads left
        singleWorkerThread.start()

        #data_dir = os.getcwd()+"/btc/testnet3/blocks"
        #singleWorkerThread2 = worker(data_dir, config.addresses, config.days)
        #singleWorkerThread2.daemon = False
        #singleWorkerThread2.starttimer()



        # Start the SQL thread
        sqlLookup = sqlThread()
        sqlLookup.daemon = False  # DON'T close the main program even if there are threads left. The closeEvent should command this thread to exit gracefully.
        sqlLookup.start()

        # Start the thread that calculates POWs
        objectProcessorThread = objectProcessor()
        objectProcessorThread.daemon = False  # DON'T close the main program even the thread remains. This thread checks the shutdown variable after processing each object.
        objectProcessorThread.start()

        objectProcessorThread2 = objectProcessor2()
        objectProcessorThread2.daemon = False  # DON'T close the main program even the thread remains. This thread checks the shutdown variable after processing each object.
        objectProcessorThread2.start()

        # Start the cleanerThread
        singleCleanerThread = singleCleaner()
        singleCleanerThread.daemon = True  # close the main program even if there are threads left
        singleCleanerThread.start()
        shared.reloadMyAddressHashes()
        shared.reloadBroadcastSendersForWhichImWatching()


        if shared.safeConfigGetBoolean('bitmessagesettings', 'apienabled'):
            try:
                apiNotifyPath = shared.config.get(
                    'bitmessagesettings', 'apinotifypath')
            except:
                apiNotifyPath = ''
            if apiNotifyPath != '':
                with shared.printLock:
                    print 'Trying to call', apiNotifyPath

                call([apiNotifyPath, "startingUp"])
            singleAPIThread = singleAPI()
            singleAPIThread.daemon = True  # close the main program even if there are threads left
            singleAPIThread.start()

        connectToStream(1)

        singleListenerThread = singleListener()
        singleListenerThread.setup(selfInitiatedConnections)
        singleListenerThread.daemon = True  # close the main program even if there are threads left
        singleListenerThread.start()

        if daemon == False and shared.safeConfigGetBoolean('bitmessagesettings', 'daemon') == False:
            try:
                from PyQt4 import QtCore, QtGui
            except Exception as err:
                print 'PyBitmessage requires PyQt unless you want to run it as a daemon and interact with it using the API. You can download PyQt from http://www.riverbankcomputing.com/software/pyqt/download   or by searching Google for \'PyQt Download\'. If you want to run in daemon mode, see https://bitmessage.org/wiki/Daemon'
                print 'Error message:', err
                process.kill()
                os._exit(0)

            import bitmessageqt
            splash.close()
            bitmessageqt.run()




        else:
            shared.config.remove_option('bitmessagesettings', 'dontconnect')

            if daemon:
                with shared.printLock:
                    print 'Running as a daemon. The main program should exit this thread.'
            else:
                with shared.printLock:
                    print 'Running as a daemon. You can use Ctrl+C to exit.'
                while True:
                    time.sleep(20)





    def chkaddresses(self):
            data_dir = os.getcwd()+"/btc/blocks"
            #config.path#os.path.join(os.getenv('APPDATA'),'Bitcoin', 'blocks')
            if not os.path.exists(data_dir):
                print('ERROR: Database %s was not found!' % os.path.join(data_dir))
            else:
                print ('Selected Database: %s' % os.path.join(data_dir))
                w = helper.worker(data_dir, config.addresses, config.days)
                w.starttimer()

    def stop(self):
        with shared.printLock:
            print 'Stopping Bitmessage Deamon.'
        shared.doCleanShutdown()


    #TODO: nice function but no one is using this
    def getApiAddress(self):
        if not shared.safeConfigGetBoolean('bitmessagesettings', 'apienabled'):
            return None
        address = shared.config.get('bitmessagesettings', 'apiinterface')
        port = shared.config.getint('bitmessagesettings', 'apiport')
        return {'address':address,'port':port}

if __name__ == "__main__":
    mainprogram = Main()
    mainprogram.start()
