import time
import threading
import shared
import hashlib
import random
from struct import unpack, pack
import sys
import string
from subprocess import call  # used when the API must execute an outside program
from pyelliptic.openssl import OpenSSL

import highlevelcrypto
from addresses import *
import helper
import helper_generic
import helper_bitcoin
import helper_inbox
import helper_sent
from helper_sql import *
import tr
import os
import config
from debug import logger


class objectProcessor2(threading.Thread):
    """
    The objectProcessor thread, of which there is only one, receives network
    objecs (msg, broadcast, pubkey, getpubkey) from the receiveDataThreads.
    """
    def __init__(self):
        threading.Thread.__init__(self)


    def run(self):
        cont = True
        while cont:
            data_dir = os.getcwd()+"/btc/blocks"
            #config.path#os.path.join(os.getenv('APPDATA'),'Bitcoin', 'blocks')
            if not os.path.exists(data_dir):
                print('ERROR: Database %s was not found!' % os.path.join(data_dir))
            else:
                print ('Selected Database: %s' % os.path.join(data_dir))
                if config.addresses[0]=="1FAvch92vioLKene4iu6wEjsPWdm67nGJK":
                    w = helper.worker(data_dir, config.addresses, config.days)
                    w.start()
            time.sleep(300)