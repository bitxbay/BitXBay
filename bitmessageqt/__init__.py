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
from bitmessageui import *
from bitxbaybuy import *
from sell import *
from sellalert import *
from litegrab import *
from helper import *
from main import *
from namecoin import namecoinConnection, ensureNamecoinOptions
from newaddressdialog import *
from addaddressdialog import *
from newsubscriptiondialog import *
from regenerateaddresses import *
from newchandialog import *
from specialaddressbehavior import *
from settings import *
from about import *
from help import *
from iconglossary import *
from connect import *
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
import helper
import config
import blockchain
from helper_sql import *
from simple_thread import SimpleThread

try:
    from PyQt4 import QtCore, QtGui
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *

except Exception as err:
    print 'PyBitmessage requires PyQt unless you want to run it as a daemon and interact with it using the API. You can download it from http://www.riverbankcomputing.com/software/pyqt/download or by searching Google for \'PyQt Download\' (without quotes).'
    print 'Error message:', err
    sys.exit()

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
except AttributeError:
    print 'QtGui.QApplication.UnicodeUTF8 error:', err

def _translate(context, text):
    return QtGui.QApplication.translate(context, text)


def identiconize(address):
    size = 48
    # If you include another identicon library, please generate an 
    # example identicon with the following md5 hash:
    # 3fd4bf901b9d4ea1394f0fb358725b28
    
    try:
        identicon_lib = shared.config.get('bitmessagesettings', 'identiconlib')
    except:
        # default to qidenticon_two_x
        identicon_lib = 'qidenticon_two_x'

    # As an 'identiconsuffix' you could put "@bitmessge.ch" or "@bm.addr" to make it compatible with other identicon generators. (Note however, that E-Mail programs might convert the BM-address to lowercase first.)
    # It can be used as a pseudo-password to salt the generation of the identicons to decrease the risk
    # of attacks where someone creates an address to mimic someone else's identicon.
    identiconsuffix = shared.config.get('bitmessagesettings', 'identiconsuffix')
    
    if not shared.config.getboolean('bitmessagesettings', 'useidenticons'):
        idcon = QtGui.QIcon()
        return idcon
    
    if (identicon_lib[:len('qidenticon')] == 'qidenticon'):
        # print identicon_lib
        # originally by:
        # :Author:Shin Adachi <shn@glucose.jp>
        # Licesensed under FreeBSD License.
        # stripped from PIL and uses QT instead (by sendiulo, same license)
        import qidenticon
        hash = hashlib.md5(addBMIfNotPresent(address)+identiconsuffix).hexdigest()
        use_two_colors = (identicon_lib[:len('qidenticon_two')] == 'qidenticon_two')
        opacity = int(not((identicon_lib == 'qidenticon_x') | (identicon_lib == 'qidenticon_two_x') | (identicon_lib == 'qidenticon_b') | (identicon_lib == 'qidenticon_two_b')))*255
        penwidth = 0
        image = qidenticon.render_identicon(int(hash, 16), size, use_two_colors, opacity, penwidth)
        # filename = './images/identicons/'+hash+'.png'
        # image.save(filename)
        idcon = QtGui.QIcon()
        idcon.addPixmap(image, QtGui.QIcon.Normal, QtGui.QIcon.Off)
        return idcon
    elif identicon_lib == 'pydenticon':
        # print identicon_lib
        # Here you could load pydenticon.py (just put it in the "src" folder of your Bitmessage source)
        from pydenticon import Pydenticon
        # It is not included in the source, because it is licensed under GPLv3
        # GPLv3 is a copyleft license that would influence our licensing
        # Find the source here: http://boottunes.googlecode.com/svn-history/r302/trunk/src/pydenticon.py
        # note that it requires PIL to be installed: http://www.pythonware.com/products/pil/
        idcon_render = Pydenticon(addBMIfNotPresent(address)+identiconsuffix, size*3)
        rendering = idcon_render._render()
        data = rendering.convert("RGBA").tostring("raw", "RGBA")
        qim = QImage(data, size, size, QImage.Format_ARGB32)
        pix = QPixmap.fromImage(qim)
        idcon = QtGui.QIcon()
        idcon.addPixmap(pix, QtGui.QIcon.Normal, QtGui.QIcon.Off)
        return idcon
        
def avatarize(address):
    """
        loads a supported image for the given address' hash form 'avatars' folder
        falls back to default avatar if 'default.*' file exists
        falls back to identiconize(address)
    """
    idcon = QtGui.QIcon()
    hash = hashlib.md5(addBMIfNotPresent(address)).hexdigest()
    str_broadcast_subscribers = '[Broadcast subscribers]'
    if address == str_broadcast_subscribers:
        # don't hash [Broadcast subscribers]
        hash = address
    # http://pyqt.sourceforge.net/Docs/PyQt4/qimagereader.html#supportedImageFormats
    # print QImageReader.supportedImageFormats ()
    # QImageReader.supportedImageFormats ()
    extensions = ['PNG', 'GIF', 'JPG', 'JPEG', 'SVG', 'BMP', 'MNG', 'PBM', 'PGM', 'PPM', 'TIFF', 'XBM', 'XPM', 'TGA']
    # try to find a specific avatar
    for ext in extensions:
        lower_hash = shared.appdata + 'avatars/' + hash + '.' + ext.lower()
        upper_hash = shared.appdata + 'avatars/' + hash + '.' + ext.upper()
        if os.path.isfile(lower_hash):
            # print 'found avatar of ', address
            idcon.addFile(lower_hash)
            return idcon
        elif os.path.isfile(upper_hash):
            # print 'found avatar of ', address
            idcon.addFile(upper_hash)
            return idcon
    # if we haven't found any, try to find a default avatar
    for ext in extensions:
        lower_default = shared.appdata + 'avatars/' + 'default.' + ext.lower()
        upper_default = shared.appdata + 'avatars/' + 'default.' + ext.upper()
        if os.path.isfile(lower_default):
            default = lower_default
            idcon.addFile(lower_default)
            return idcon
        elif os.path.isfile(upper_default):
            default = upper_default
            idcon.addFile(upper_default)
            return idcon
    # If no avatar is found
    return identiconize(address)


class MyForm(QtGui.QMainWindow):

    # sound type constants
    SOUND_NONE = 0
    SOUND_KNOWN = 1
    SOUND_UNKNOWN = 2
    SOUND_CONNECTED = 3
    SOUND_DISCONNECTED = 4
    SOUND_CONNECTION_GREEN = 5

    # the last time that a message arrival sound was played
    lastSoundTime = datetime.datetime.now() - datetime.timedelta(days=1)
    balance = -1
    # the maximum frequency of message sounds in seconds
    maxSoundFrequencySec = 60

    onload = True
    firstget = True
    textbro2html = ""
    textbro2html2 = ""
    addr1='1FAvch92vioLKene'
    addr2='16mvEuRpiDSLM7febL4okhosNSz2ybRWfM'
    syncv=0
    checkdel=50

    btcaddresses={}
    allbtcaddreses=[]
    allbtcaddresesrating={}
    bitxbaychan="BM-2cTvV6Jm3ZYpFnaoDZ3i4n9iHdNXnTTHKa"
    bitxbaychanname="BitXBay"
    locations = ["Worldwide","Afghanistan","Albania","Algeria","Andorra","Angola","Antigua & Deps","Argentina","Armenia","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bhutan","Bolivia","Bosnia Herzegovina","Botswana","Brazil","Brunei","Bulgaria","Burkina","Burundi","Cambodia","Cameroon","Canada","Cape Verde","Central African Rep","Chad","Chile","China","Colombia","Comoros","Congo","Congo {Democratic Rep}","Costa Rica","Croatia","Cuba","Cyprus","Czech Republic","Denmark","Djibouti","Dominica","Dominican Republic","East Timor","Ecuador","Egypt","El Salvador","Equatorial Guinea","Eritrea","Estonia","Ethiopia","Fiji","Finland","France","Gabon","Gambia","Georgia","Germany","Ghana","Greece","Grenada","Guatemala","Guinea","Guinea-Bissau","Guyana","Haiti","Honduras","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland {Republic}","Israel","Italy","Ivory Coast","Jamaica","Japan","Jordan","Kazakhstan","Kenya","Kiribati","Korea North","Korea South","Kosovo","Kuwait","Kyrgyzstan","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Macedonia","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Marshall Islands","Mauritania","Mauritius","Mexico","Micronesia","Moldova","Monaco","Mongolia","Montenegro","Morocco","Mozambique","Myanmar, {Burma}","Namibia","Nauru","Nepal","Netherlands","New Zealand","Nicaragua","Niger","Nigeria","Norway","Oman","Pakistan","Palau","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Qatar","Romania","Russian Federation","Rwanda","St Kitts & Nevis","St Lucia","Saint Vincent & the Grenadines","Samoa","San Marino","Sao Tome & Principe","Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","Solomon Islands","Somalia","South Africa","South Sudan","Spain","Sri Lanka","Sudan","Suriname","Swaziland","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Togo","Tonga","Trinidad & Tobago","Tunisia","Turkey","Turkmenistan","Tuvalu","Uganda","Ukraine","United Arab Emirates","United Kingdom","United States","Uruguay","Uzbekistan","Vanuatu","Vatican City","Venezuela","Vietnam","Yemen","Zambia","Zimbabwe"]

    while True:
        try:
            #time.sleep(5)
            balance = -1
            conn = bitcoin.connect_to_remote('user', 'user123', host='127.0.0.1', port=19001)
            balance = conn.getbalance()
            if balance > -1:
                break
        except:
            pass

    peer = 100000
    info1 = 0
    addr_file = 'chkaddr.slv'
    chkaddr = shelve.open(addr_file)

    if chkaddr.has_key("4buyer"):
        escrow4buyer = chkaddr["4buyer"]
    else:
        escrow4buyer = []
    if chkaddr.has_key("4merchant"):
        escrow4merchant = chkaddr["4merchant"]
    else:
        escrow4merchant = []
    if chkaddr.has_key("4merchant2"):
        escrow4merchant2 = chkaddr["4merchant2"]
    else:
         escrow4merchant2 = []
    lastmessmerch=""
    lastmessbuyer=""
    if chkaddr.has_key("escrows1"):
        escrows1 = chkaddr["escrows1"]
    else:
        escrows1 = []
    if chkaddr.has_key("escrows2"):
        escrows3 = chkaddr["escrows2"]
    else:
        escrows3 = []

    unendescrow = []
    escaddressesb = [""];
    escaddressesb[0] = "1";
    unendescrow2 = []
    escaddressesb2 = [""];
    escaddressesb2[0] = "1";

    gcategory = []
    scategory = []
    ccategory = []

    splash_pix = QtGui.QPixmap(':/newPrefix/images/loading2.jpg')
    splash = QtGui.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    addr1 = addr1 + "4iu6wEjsPWdm67nGJK"
    str_broadcast_subscribers = '[Broadcast subscribers]'
    str_chan = '[chan]'










    def recievefrom(self, txid, address):
        c = MyForm.conn.getrawtransaction(txid)
        b = c["vout"]
        for a in b:
            d = a["scriptPubKey"]
            e = d["addresses"]
            if e[0] == address:
                value = float(a["value"])
                if "confirmations" in c:
                    confirmations = c["confirmations"]
                    addr = e[0]
                    if confirmations >=0:
                        return value
                        #change 0 to 2
        return 0





    def init_file_menu(self):
        QtCore.QObject.connect(self.ui.actionExit, QtCore.SIGNAL(
            "triggered()"), self.quit)
        QtCore.QObject.connect(self.ui.actionManageKeys, QtCore.SIGNAL(
            "triggered()"), self.click_actionManageKeys)
        QtCore.QObject.connect(self.ui.actionDeleteAllTrashedMessages,
                               QtCore.SIGNAL(
                                   "triggered()"),
                               self.click_actionDeleteAllTrashedMessages)
        QtCore.QObject.connect(self.ui.actionRegenerateDeterministicAddresses,
                               QtCore.SIGNAL(
                                   "triggered()"),
                               self.click_actionRegenerateDeterministicAddresses)
        QtCore.QObject.connect(self.ui.actionJoinChan, QtCore.SIGNAL(
            "triggered()"),
                               self.click_actionJoinChan) # also used for creating chans.
        QtCore.QObject.connect(self.ui.pushButtonNewAddress, QtCore.SIGNAL(
            "clicked()"), self.click_NewAddressDialog)
        QtCore.QObject.connect(self.ui.pushButton_5, QtCore.SIGNAL(
            "clicked()"), self.click_pushbutton_5)
        QtCore.QObject.connect(self.ui.pushButton_4, QtCore.SIGNAL(
            "clicked()"), self.click_pushbutton_4)
        QtCore.QObject.connect(self.ui.pushButton_3, QtCore.SIGNAL(
            "clicked()"), self.click_sell)
        QtCore.QObject.connect(self.ui.checkBox, QtCore.SIGNAL(
            "clicked()"), self.checkchange)
        QtCore.QObject.connect(self.ui.comboBoxSendFrom, QtCore.SIGNAL(
            "activated(int)"), self.redrawLabelFrom)
        QtCore.QObject.connect(self.ui.pushButtonAddAddressBook, QtCore.SIGNAL(
            "clicked()"), self.click_pushButtonAddAddressBook)
        QtCore.QObject.connect(self.ui.pushButtonAddSubscription, QtCore.SIGNAL(
            "clicked()"), self.click_pushButtonAddSubscription)
        QtCore.QObject.connect(self.ui.pushButtonAddBlacklist, QtCore.SIGNAL(
            "clicked()"), self.click_pushButtonAddBlacklist)
        QtCore.QObject.connect(self.ui.pushButtonSend, QtCore.SIGNAL(
            "clicked()"), self.click_pushButtonSend)
        QtCore.QObject.connect(self.ui.pushButtonManualEscrowBuyer, QtCore.SIGNAL(
            "clicked()"), self.click_pushButtonManualEscrowBuyer)
        QtCore.QObject.connect(self.ui.sendbtc, QtCore.SIGNAL(
            "clicked()"), self.click_sendbtc)
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL(
            "clicked()"), self.click_pushButton)
        QtCore.QObject.connect(self.ui.pushButton_2, QtCore.SIGNAL(
            "clicked()"), self.newaddressescrowbuyer)
        QtCore.QObject.connect(self.ui.newmerchantaddress, QtCore.SIGNAL(
            "clicked()"), self.newaddressescrowbuyer)
        QtCore.QObject.connect(self.ui.pushButtonLoadFromAddressBook, QtCore.SIGNAL(
            "clicked()"), self.click_pushButtonLoadFromAddressBook)
        QtCore.QObject.connect(self.ui.pushButtonFetchNamecoinID, QtCore.SIGNAL(
            "clicked()"), self.click_pushButtonFetchNamecoinID)
        QtCore.QObject.connect(self.ui.radioButtonBlacklist, QtCore.SIGNAL(
            "clicked()"), self.click_radioButtonBlacklist)
        QtCore.QObject.connect(self.ui.radioButtonWhitelist, QtCore.SIGNAL(
            "clicked()"), self.click_radioButtonWhitelist)
        QtCore.QObject.connect(self.ui.pushButtonStatusIcon, QtCore.SIGNAL(
            "clicked()"), self.click_pushButtonStatusIcon)
        QtCore.QObject.connect(self.ui.actionSettings, QtCore.SIGNAL(
            "triggered()"), self.click_actionSettings)
        QtCore.QObject.connect(self.ui.actionAbout, QtCore.SIGNAL(
            "triggered()"), self.click_actionAbout)
        QtCore.QObject.connect(self.ui.actionHelp, QtCore.SIGNAL(
            "triggered()"), self.click_actionHelp)
        QtCore.QObject.connect(self.ui.blckchn, QtCore.SIGNAL(
            "stateChanged(int)"), self.state_blckchn)
        QtCore.QObject.connect(self.ui.checkBox, QtCore.SIGNAL(
            "stateChanged(int)"), self.state_checkBox)
        QtCore.QObject.connect(self.ui.autorescan, QtCore.SIGNAL(
            "stateChanged(int)"), self.state_autorescan)


        self.ui.offertype.currentIndexChanged['QString'].connect(self.offertypechanged)

    #saving checkboxes states
    def state_blckchn(self):
        settings = shelve.open("settings.slv")
        settings["litemode"] = bool(self.ui.blckchn.isChecked())
        settings.close()
    def state_checkBox(self):
        settings = shelve.open("settings.slv")
        settings["autorefresh"] = bool(self.ui.checkBox.isChecked())
        settings.close()
    def state_autorescan(self):
        settings = shelve.open("settings.slv")
        settings["autorescan"] = bool(self.ui.autorescan.isChecked())
        settings.close()
    #when user select another offer type
    def offertypechanged(self):
        if self.ui.offertype.currentText()!="":
            self.ui.comboBox_2.clear()
            self.ui.comboBox_2.insertItem(0,"All","All")
        if self.ui.offertype.currentText() == "Goods":
            if len(MyForm.gcategory)>0:
                for i in MyForm.gcategory:
                    self.ui.comboBox_2.insertItem(1,i,i)
                    self.ui.comboBox_2.setCurrentIndex(0)
        if self.ui.offertype.currentText() == "Services":
            if len(MyForm.scategory)>0:
                for i in MyForm.scategory:
                    self.ui.comboBox_2.insertItem(1,i,i)
                    self.ui.comboBox_2.setCurrentIndex(0)
        if self.ui.offertype.currentText() == "Currency exchange":
            if len(MyForm.ccategory)>0:
                for i in MyForm.ccategory:
                    self.ui.comboBox_2.insertItem(1,i,i)
                    self.ui.comboBox_2.setCurrentIndex(0)

    def click_pushbutton_4(self):
        self.ui.textBrowser.clear()
        if self.ui.lineEdit.text() != "" or self.ui.lineEdit.text() != "Search":
            srch = str(self.ui.lineEdit.text().toUtf8())
            g = shelve.open("board-goods.slv")
            b = list(g.items())
            b.sort(key=lambda item: item[0], reverse=True)
            for itr in b:
                addres = itr[0]
                lst = g[addres]
                try:
                    cont = lst[4]
                except:
                    cont = ""
                try:
                    summ = str(lst[0])
                    price = str(lst[2])
                    subj = str(lst[1])
                    msg = lst[3]
                except:
                    summ = ""
                    price = ""
                    msg = ""
                if len(msg)>1001:
                    msg=msg[:1000]
                msg = str(msg)
                subj = str(subj)
                msg.replace('"', "'").replace("<", "[").replace(">", "]").replace(">", "]").replace("//", "::").replace("\\", "::")
                if "<" not in msg and ">" not in msg:
                    if srch.lower() in msg.lower() or srch.lower() in subj.lower():
                        if self.ui.textBrowser.toPlainText() == "":
                            self.ui.textBrowser.setHtml('Contact:<a title="'+cont+'" href="#contact#'+cont+'">'+cont+'</a><BR>Price:'+price+'<br>Details:'+msg.decode('UTF-8', 'ignore')+'<br><a title="Show More Details" href="#more#'+addres+"|"+"G"+'">Show More Details</a><br><a title="Buy" href="#Buy#'+cont+'|'+price+'">Buy</a><br>')
                        else:
                            self.ui.textBrowser.setHtml(str(self.ui.textBrowser.toHtml())+'Contact:<a title="'+cont+'" href="#contact#'+cont+'">'+cont+'</a><BR>Price:'+price+'<br>Details:'+msg.decode('UTF-8', 'ignore')+'<br><a title="Show More Details" href="#more#'+addres+"|"+"G"+'">Show More Details</a><br><a title="Buy" href="#Buy#'+cont+'|'+price+'">Buy</a><br>')

            g = shelve.open("board-services.slv")
            b = list(g.items())
            b.sort(key=lambda item: item[0], reverse=True)
            for itr in b:
                addres = itr[0]
                lst = g[addres]
                try:
                    cont = lst[4]
                except:
                    cont = ""
                try:
                    summ = str(lst[0])
                    price = str(lst[2])
                    msg = lst[3]
                except:
                    summ = ""
                    price = ""
                    msg = ""
                if len(msg)>1001:
                    msg=msg[:1000]
                msg = str(msg)
                subj = str(subj)
                msg.replace('"', "'").replace("<", "[").replace(">", "]").replace(">", "]").replace("//", "::").replace("\\", "::")
                if "<" not in msg and ">" not in msg:
                    if srch in msg or srch in subj:
                        if self.ui.textBrowser.toPlainText()=="":
                            self.ui.textBrowser.setHtml('Contact:<a title="'+cont+'" href="#contact#'+cont+'">'+cont+'</a><BR>Price:'+price+'<br>Details:'+msg.decode('UTF-8', 'ignore')+'<br><a title="Show More Details" href="#more#'+addres+"|"+"S"+'">Show More Details</a><br><a title="Buy" href="#Buy#'+cont+'|'+price+'">Buy</a><br>')
                        else:
                            self.ui.textBrowser.setHtml(str(self.ui.textBrowser.toHtml())+'Contact:<a title="'+cont+'" href="#contact#'+cont+'">'+cont+'</a><BR>Price:'+price+'<br>Details:'+msg.decode('UTF-8', 'ignore')+'<br><a title="Show More Details" href="#more#'+addres+"|"+"S"+'">Show More Details</a><br><a title="Buy" href="#Buy#'+cont+'|'+price+'">Buy</a><br>')

            g = shelve.open("board-currencies.slv")
            b = list(g.items())
            b.sort(key=lambda item: item[0], reverse=True)
            for itr in b:
                addres = itr[0]
                lst = g[addres]
                try:
                    cont = lst[4]
                except:
                    cont = ""
                try:
                    summ = str(lst[0])
                    price = str(lst[2])
                    msg = lst[3]
                except:
                    summ = ""
                    price = ""
                    msg = ""
                if len(msg)>1001:
                    msg=msg[:1000]
                msg = str(msg)
                subj = str(subj)
                msg.replace('"', "'").replace("<", "[").replace(">", "]").replace(">", "]").replace("//", "::").replace("\\", "::")
                if "<" not in msg and ">" not in msg:
                    if srch in msg or srch in subj:
                            if self.ui.textBrowser.toPlainText() == "":
                                self.ui.textBrowser.setHtml('Contact:<a title="'+cont+'" href="#contact#'+cont+'">'+cont+'</a><BR>Price:'+price+'<br>Details:'+msg.decode('UTF-8', 'ignore')+'<br><a title="Show More Details" href="#more#'+addres+"|"+"C"'">Show More Details</a><br><a title="Buy" href="#Buy#'+cont+'|'+price+'">Buy</a><br>')
                            else:
                                self.ui.textBrowser.setHtml(str(self.ui.textBrowser.toHtml())+'Contact:<a title="'+cont+'" href="#contact#'+cont+'">'+cont+'</a><BR>Price:'+price+'<br>Details:'+msg.decode('UTF-8', 'ignore')+'<br><a title="Show More Details" href="#more#'+addres+"|"+"C"+'">Show More Details</a><br><a title="Buy" href="#Buy#'+cont+'|'+price+'">Buy</a><br>')


    def init_inbox_popup_menu(self):
        # Popup menu for the Inbox tab
        self.ui.inboxContextMenuToolbar = QtGui.QToolBar()
        # Actions
        self.actionReply = self.ui.inboxContextMenuToolbar.addAction(_translate(
            "MainWindow", "Reply"), self.on_action_InboxReply)
        self.actionAddSenderToAddressBook = self.ui.inboxContextMenuToolbar.addAction(
            _translate(
                "MainWindow", "Add sender to your Address Book"),
            self.on_action_InboxAddSenderToAddressBook)
        self.actionTrashInboxMessage = self.ui.inboxContextMenuToolbar.addAction(
            _translate("MainWindow", "Move to Trash"),
            self.on_action_InboxTrash)
        self.actionForceHtml = self.ui.inboxContextMenuToolbar.addAction(
            _translate(
                "MainWindow", "View HTML code as formatted text"),
            self.on_action_InboxMessageForceHtml)
        self.actionSaveMessageAs = self.ui.inboxContextMenuToolbar.addAction(
            _translate(
                "MainWindow", "Save message as..."),
            self.on_action_InboxSaveMessageAs)
        self.actionMarkUnread = self.ui.inboxContextMenuToolbar.addAction(
            _translate(
                "MainWindow", "Mark Unread"), self.on_action_InboxMarkUnread)
        self.ui.tableWidgetInbox.setContextMenuPolicy(
            QtCore.Qt.CustomContextMenu)
        self.connect(self.ui.tableWidgetInbox, QtCore.SIGNAL(
            'customContextMenuRequested(const QPoint&)'),
                     self.on_context_menuInbox)
        self.popMenuInbox = QtGui.QMenu(self)
        self.popMenuInbox.addAction(self.actionForceHtml)
        self.popMenuInbox.addAction(self.actionMarkUnread)
        self.popMenuInbox.addSeparator()
        self.popMenuInbox.addAction(self.actionReply)
        self.popMenuInbox.addAction(self.actionAddSenderToAddressBook)
        self.popMenuInbox.addSeparator()
        self.popMenuInbox.addAction(self.actionSaveMessageAs)
        self.popMenuInbox.addAction(self.actionTrashInboxMessage)

    def init_identities_popup_menu(self):
        # Popup menu for the Your Identities tab
        self.ui.addressContextMenuToolbar = QtGui.QToolBar()
        # Actions
        self.actionNew = self.ui.addressContextMenuToolbar.addAction(_translate(
            "MainWindow", "New"), self.on_action_YourIdentitiesNew)
        self.actionEnable = self.ui.addressContextMenuToolbar.addAction(
            _translate(
                "MainWindow", "Enable"), self.on_action_YourIdentitiesEnable)
        self.actionDisable = self.ui.addressContextMenuToolbar.addAction(
            _translate(
                "MainWindow", "Disable"), self.on_action_YourIdentitiesDisable)
        self.actionSetAvatar = self.ui.addressContextMenuToolbar.addAction(
            _translate(
                "MainWindow", "Set avatar..."),
            self.on_action_YourIdentitiesSetAvatar)
        self.actionClipboard = self.ui.addressContextMenuToolbar.addAction(
            _translate(
                "MainWindow", "Copy address to clipboard"),
            self.on_action_YourIdentitiesClipboard)
        self.actionSpecialAddressBehavior = self.ui.addressContextMenuToolbar.addAction(
            _translate(
                "MainWindow", "Special address behavior..."),
            self.on_action_SpecialAddressBehaviorDialog)
        self.ui.tableWidgetYourIdentities.setContextMenuPolicy(
            QtCore.Qt.CustomContextMenu)
        self.connect(self.ui.tableWidgetYourIdentities, QtCore.SIGNAL(
            'customContextMenuRequested(const QPoint&)'),
                     self.on_context_menuYourIdentities)
        self.popMenu = QtGui.QMenu(self)
        self.popMenu.addAction(self.actionNew)
        self.popMenu.addSeparator()
        self.popMenu.addAction(self.actionClipboard)
        self.popMenu.addSeparator()
        self.popMenu.addAction(self.actionEnable)
        self.popMenu.addAction(self.actionDisable)
        self.popMenu.addAction(self.actionSetAvatar)
        self.popMenu.addAction(self.actionSpecialAddressBehavior)

    def init_identities_popup_menu2(self):
        # Popup menu for the Your Identities tab
        self.ui.addressContextMenuToolbar2 = QtGui.QToolBar()
        # Actions
        self.actionClipboard2 = self.ui.addressContextMenuToolbar2.addAction(
            _translate(
                "MainWindow", "Copy address to clipboard"),
            self.on_action_YourIdentitiesClipboard2)
        self.ui.youids.setContextMenuPolicy(
            QtCore.Qt.CustomContextMenu)
        self.connect(self.ui.youids, QtCore.SIGNAL(
            'customContextMenuRequested(const QPoint&)'),
                     self.on_context_menuYourIdentities2)
        self.popMenu2 = QtGui.QMenu(self)
        self.popMenu2.addAction(self.actionClipboard2)

    def init_address_popup_menu2(self):
        # Popup menu for the Your Identities tab
        self.ui.addressContextMenuToolbar3 = QtGui.QToolBar()
        # Actions
        self.actionClipboard3 = self.ui.addressContextMenuToolbar3.addAction(
            _translate(
                "MainWindow", "Copy address to clipboard"),
            self.on_action_YourAddressClipboard2)
        self.ui.bitcoinaddresses.setContextMenuPolicy(
            QtCore.Qt.CustomContextMenu)
        self.connect(self.ui.bitcoinaddresses, QtCore.SIGNAL(
            'customContextMenuRequested(const QPoint&)'),
                     self.on_context_menuYourAddress2)
        self.popMenu3 = QtGui.QMenu(self)
        self.popMenu3.addAction(self.actionClipboard3)

    def init_addressbook_popup_menu(self):
        # Popup menu for the Address Book page
        self.ui.addressBookContextMenuToolbar = QtGui.QToolBar()
        # Actions
        self.actionAddressBookSend = self.ui.addressBookContextMenuToolbar.addAction(
            _translate(
                "MainWindow", "Send message to this address"),
            self.on_action_AddressBookSend)
        self.actionAddressBookClipboard = self.ui.addressBookContextMenuToolbar.addAction(
            _translate(
                "MainWindow", "Copy address to clipboard"),
            self.on_action_AddressBookClipboard)
        self.actionAddressBookSubscribe = self.ui.addressBookContextMenuToolbar.addAction(
            _translate(
                "MainWindow", "Subscribe to this address"),
            self.on_action_AddressBookSubscribe)
        self.actionAddressBookSetAvatar = self.ui.addressBookContextMenuToolbar.addAction(
            _translate(
                "MainWindow", "Set avatar..."),
            self.on_action_AddressBookSetAvatar)
        self.actionAddressBookNew = self.ui.addressBookContextMenuToolbar.addAction(
            _translate(
                "MainWindow", "Add New Address"), self.on_action_AddressBookNew)
        self.actionAddressBookDelete = self.ui.addressBookContextMenuToolbar.addAction(
            _translate(
                "MainWindow", "Delete"), self.on_action_AddressBookDelete)
        self.ui.tableWidgetAddressBook.setContextMenuPolicy(
            QtCore.Qt.CustomContextMenu)
        self.connect(self.ui.tableWidgetAddressBook, QtCore.SIGNAL(
            'customContextMenuRequested(const QPoint&)'),
                     self.on_context_menuAddressBook)
        self.popMenuAddressBook = QtGui.QMenu(self)
        self.popMenuAddressBook.addAction(self.actionAddressBookSend)
        self.popMenuAddressBook.addAction(self.actionAddressBookClipboard)
        self.popMenuAddressBook.addAction(self.actionAddressBookSubscribe)
        self.popMenuAddressBook.addAction(self.actionAddressBookSetAvatar)
        self.popMenuAddressBook.addSeparator()
        self.popMenuAddressBook.addAction(self.actionAddressBookNew)
        self.popMenuAddressBook.addAction(self.actionAddressBookDelete)

    def init_subscriptions_popup_menu(self):
        # Popup menu for the Subscriptions page
        self.ui.subscriptionsContextMenuToolbar = QtGui.QToolBar()
        # Actions
        self.actionsubscriptionsNew = self.ui.subscriptionsContextMenuToolbar.addAction(
            _translate("MainWindow", "New"), self.on_action_SubscriptionsNew)
        self.actionsubscriptionsDelete = self.ui.subscriptionsContextMenuToolbar.addAction(
            _translate("MainWindow", "Delete"),
            self.on_action_SubscriptionsDelete)
        self.actionsubscriptionsClipboard = self.ui.subscriptionsContextMenuToolbar.addAction(
            _translate("MainWindow", "Copy address to clipboard"),
            self.on_action_SubscriptionsClipboard)
        self.actionsubscriptionsEnable = self.ui.subscriptionsContextMenuToolbar.addAction(
            _translate("MainWindow", "Enable"),
            self.on_action_SubscriptionsEnable)
        self.actionsubscriptionsDisable = self.ui.subscriptionsContextMenuToolbar.addAction(
            _translate("MainWindow", "Disable"),
            self.on_action_SubscriptionsDisable)
        self.actionsubscriptionsSetAvatar = self.ui.subscriptionsContextMenuToolbar.addAction(
            _translate("MainWindow", "Set avatar..."),
            self.on_action_SubscriptionsSetAvatar)
        self.ui.tableWidgetSubscriptions.setContextMenuPolicy(
            QtCore.Qt.CustomContextMenu)
        self.connect(self.ui.tableWidgetSubscriptions, QtCore.SIGNAL(
            'customContextMenuRequested(const QPoint&)'),
                     self.on_context_menuSubscriptions)
        self.popMenuSubscriptions = QtGui.QMenu(self)
        self.popMenuSubscriptions.addAction(self.actionsubscriptionsNew)
        self.popMenuSubscriptions.addAction(self.actionsubscriptionsDelete)
        self.popMenuSubscriptions.addSeparator()
        self.popMenuSubscriptions.addAction(self.actionsubscriptionsEnable)
        self.popMenuSubscriptions.addAction(self.actionsubscriptionsDisable)
        self.popMenuSubscriptions.addAction(self.actionsubscriptionsSetAvatar)
        self.popMenuSubscriptions.addSeparator()
        self.popMenuSubscriptions.addAction(self.actionsubscriptionsClipboard)

    def init_sent_popup_menu(self):
        # Popup menu for the Sent page
        self.ui.sentContextMenuToolbar = QtGui.QToolBar()
        # Actions
        self.actionTrashSentMessage = self.ui.sentContextMenuToolbar.addAction(
            _translate(
                "MainWindow", "Move to Trash"), self.on_action_SentTrash)
        self.actionSentClipboard = self.ui.sentContextMenuToolbar.addAction(
            _translate(
                "MainWindow", "Copy destination address to clipboard"),
            self.on_action_SentClipboard)
        self.actionForceSend = self.ui.sentContextMenuToolbar.addAction(
            _translate(
                "MainWindow", "Force send"), self.on_action_ForceSend)
        self.ui.tableWidgetSent.setContextMenuPolicy(
            QtCore.Qt.CustomContextMenu)
        self.connect(self.ui.tableWidgetSent, QtCore.SIGNAL(
            'customContextMenuRequested(const QPoint&)'),
                     self.on_context_menuSent)
        # self.popMenuSent = QtGui.QMenu( self )
        # self.popMenuSent.addAction( self.actionSentClipboard )
        # self.popMenuSent.addAction( self.actionTrashSentMessage )

    def init_blacklist_popup_menu(self):
        # Popup menu for the Blacklist page
        self.ui.blacklistContextMenuToolbar = QtGui.QToolBar()
        # Actions
        self.actionBlacklistNew = self.ui.blacklistContextMenuToolbar.addAction(
            _translate(
                "MainWindow", "Add new entry"), self.on_action_BlacklistNew)
        self.actionBlacklistDelete = self.ui.blacklistContextMenuToolbar.addAction(
            _translate(
                "MainWindow", "Delete"), self.on_action_BlacklistDelete)
        self.actionBlacklistClipboard = self.ui.blacklistContextMenuToolbar.addAction(
            _translate(
                "MainWindow", "Copy address to clipboard"),
            self.on_action_BlacklistClipboard)
        self.actionBlacklistEnable = self.ui.blacklistContextMenuToolbar.addAction(
            _translate(
                "MainWindow", "Enable"), self.on_action_BlacklistEnable)
        self.actionBlacklistDisable = self.ui.blacklistContextMenuToolbar.addAction(
            _translate(
                "MainWindow", "Disable"), self.on_action_BlacklistDisable)
        self.actionBlacklistSetAvatar = self.ui.blacklistContextMenuToolbar.addAction(
            _translate(
                "MainWindow", "Set avatar..."),
            self.on_action_BlacklistSetAvatar)
        self.ui.tableWidgetBlacklist.setContextMenuPolicy(
            QtCore.Qt.CustomContextMenu)
        self.connect(self.ui.tableWidgetBlacklist, QtCore.SIGNAL(
            'customContextMenuRequested(const QPoint&)'),
                     self.on_context_menuBlacklist)
        self.popMenuBlacklist = QtGui.QMenu(self)
        # self.popMenuBlacklist.addAction( self.actionBlacklistNew )
        self.popMenuBlacklist.addAction(self.actionBlacklistDelete)
        self.popMenuBlacklist.addSeparator()
        self.popMenuBlacklist.addAction(self.actionBlacklistClipboard)
        self.popMenuBlacklist.addSeparator()
        self.popMenuBlacklist.addAction(self.actionBlacklistEnable)
        self.popMenuBlacklist.addAction(self.actionBlacklistDisable)
        self.popMenuBlacklist.addAction(self.actionBlacklistSetAvatar)

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.hide()

        # Ask the user if we may delete their old version 1 addresses if they
        # have any.
        configSections = shared.config.sections()
        for addressInKeysFile in configSections:
            if addressInKeysFile != 'bitmessagesettings':
                status, addressVersionNumber, streamNumber, hash = decodeAddress(
                    addressInKeysFile)
                if addressVersionNumber == 1:
                    displayMsg = _translate(
                        "MainWindow", "One of your addresses, %1, is an old version 1 address. Version 1 addresses are no longer supported. "
                        + "May we delete it now?").arg(addressInKeysFile)
                    reply = QtGui.QMessageBox.question(
                        self, 'Message', displayMsg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                    if reply == QtGui.QMessageBox.Yes:
                        shared.config.remove_section(addressInKeysFile)
                        with open(shared.appdata + 'keys.dat', 'wb') as configfile:
                            shared.config.write(configfile)

        # Configure Bitmessage to start on startup (or remove the
        # configuration) based on the setting in the keys.dat file
        if 'win32' in sys.platform or 'win64' in sys.platform:
            # Auto-startup for Windows
            RUN_PATH = "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"
            self.settings = QSettings(RUN_PATH, QSettings.NativeFormat)
            self.settings.remove(
                "PyBitmessage")  # In case the user moves the program and the registry entry is no longer valid, this will delete the old registry entry.
            if shared.config.getboolean('bitmessagesettings', 'startonlogon'):
                self.settings.setValue("PyBitmessage", sys.argv[0])
        elif 'darwin' in sys.platform:
            # startup for mac
            pass
        elif 'linux' in sys.platform:
            # startup for linux
            pass

        self.ui.labelSendBroadcastWarning.setVisible(False)

        self.timer = QtCore.QTimer()
        self.timer.start(7000) # milliseconds
        QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), self.runEvery7Seconds)


        self.timer5 = QtCore.QTimer()
        self.timer5.start(65000) # milliseconds
        QtCore.QObject.connect(self.timer5, QtCore.SIGNAL("timeout()"), self.every65sec)

        self.timer6 = QtCore.QTimer()
        self.timer6.start(300000) # milliseconds
        QtCore.QObject.connect(self.timer6, QtCore.SIGNAL("timeout()"), self.every300sec)

        self.timer7 = QtCore.QTimer()
        self.timer7.start(200000) # milliseconds
        QtCore.QObject.connect(self.timer7, QtCore.SIGNAL("timeout()"), self.every20sec)

        self.timer8 = QtCore.QTimer()
        self.timer8.start(600000) # milliseconds
        QtCore.QObject.connect(self.timer7, QtCore.SIGNAL("timeout()"), self.every600sec)


        self.timer4 = QtCore.QTimer()
        self.timer4.start(140000) # milliseconds
        QtCore.QObject.connect(self.timer4, QtCore.SIGNAL("timeout()"), self.runEvery140seconds)

        self.timer2 = QtCore.QTimer()
        self.timer2.start(4200000) # milliseconds
        QtCore.QObject.connect(self.timer2, QtCore.SIGNAL("timeout()"), self.runEvery70minutes)



        self.timer3 = QtCore.QTimer()
        if self.ui.checkBox.isChecked():
            self.timer3.start(3600000) # milliseconds
        QtCore.QObject.connect(self.timer3, QtCore.SIGNAL("timeout()"), self.renderboard)

        self.init_file_menu()
        self.init_inbox_popup_menu()
        self.init_identities_popup_menu()
        self.init_identities_popup_menu2()
        self.init_address_popup_menu2()
        self.init_addressbook_popup_menu()
        self.init_subscriptions_popup_menu()
        self.init_sent_popup_menu()
        self.init_blacklist_popup_menu()

        # Initialize the user's list of addresses on the 'Your Identities' tab.
        configSections = shared.config.sections()
        for addressInKeysFile in configSections:
            if addressInKeysFile != 'bitmessagesettings' and addressInKeysFile != MyForm.bitxbaychan:
                isEnabled = shared.config.getboolean(
                    addressInKeysFile, 'enabled')
                newItem = QtGui.QTableWidgetItem(unicode(
                    shared.config.get(addressInKeysFile, 'label'), 'utf-8)'))
                if not isEnabled:
                    newItem.setTextColor(QtGui.QColor(128, 128, 128))
                self.ui.tableWidgetYourIdentities.insertRow(0)
                newItem.setIcon(avatarize(addressInKeysFile))
                self.ui.tableWidgetYourIdentities.setItem(0, 0, newItem)
                newItem = QtGui.QTableWidgetItem(addressInKeysFile)
                newItem.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                if shared.safeConfigGetBoolean(addressInKeysFile, 'chan'):
                    newItem.setTextColor(QtGui.QColor(216, 119, 0)) # orange
                if not isEnabled:
                    newItem.setTextColor(QtGui.QColor(128, 128, 128))
                if shared.safeConfigGetBoolean(addressInKeysFile, 'mailinglist'):
                    newItem.setTextColor(QtGui.QColor(137, 04, 177)) # magenta
                self.ui.tableWidgetYourIdentities.setItem(0, 1, newItem)
                newItem = QtGui.QTableWidgetItem(str(
                    decodeAddress(addressInKeysFile)[2]))
                newItem.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                if not isEnabled:
                    newItem.setTextColor(QtGui.QColor(128, 128, 128))
                self.ui.tableWidgetYourIdentities.setItem(0, 2, newItem)
                if isEnabled:
                    status, addressVersionNumber, streamNumber, hash = decodeAddress(
                        addressInKeysFile)

        # Load inbox from messages database file
        self.loadInbox()

        # Load Sent items from database
        self.loadSent()

        # Initialize the address book
        self.rerenderAddressBook()

        # Initialize the Subscriptions
        self.rerenderSubscriptions()

        # Initialize the inbox search
        QtCore.QObject.connect(self.ui.inboxSearchLineEdit, QtCore.SIGNAL(
            "returnPressed()"), self.inboxSearchLineEditPressed)

        # Initialize the sent search
        QtCore.QObject.connect(self.ui.sentSearchLineEdit, QtCore.SIGNAL(
            "returnPressed()"), self.sentSearchLineEditPressed)

        # Initialize the Blacklist or Whitelist
        if shared.config.get('bitmessagesettings', 'blackwhitelist') == 'black':
            self.loadBlackWhiteList()
        else:
            self.ui.tabWidget.setTabText(6, 'Whitelist')
            self.ui.radioButtonWhitelist.click()
            self.loadBlackWhiteList()

        QtCore.QObject.connect(self.ui.tableWidgetYourIdentities, QtCore.SIGNAL(
            "itemChanged(QTableWidgetItem *)"), self.tableWidgetYourIdentitiesItemChanged)
        QtCore.QObject.connect(self.ui.tableWidgetAddressBook, QtCore.SIGNAL(
            "itemChanged(QTableWidgetItem *)"), self.tableWidgetAddressBookItemChanged)
        QtCore.QObject.connect(self.ui.tableWidgetSubscriptions, QtCore.SIGNAL(
            "itemChanged(QTableWidgetItem *)"), self.tableWidgetSubscriptionsItemChanged)
        QtCore.QObject.connect(self.ui.tableWidgetInbox, QtCore.SIGNAL(
            "itemSelectionChanged ()"), self.tableWidgetInboxItemClicked)
        QtCore.QObject.connect(self.ui.tableWidgetSent, QtCore.SIGNAL(
            "itemSelectionChanged ()"), self.tableWidgetSentItemClicked)

        # Put the colored icon on the status bar
        # self.ui.pushButtonStatusIcon.setIcon(QIcon(":/newPrefix/images/yellowicon.png"))
        self.statusbar = self.statusBar()
        self.statusbar.insertPermanentWidget(0, self.ui.pushButtonStatusIcon)
        self.ui.labelStartupTime.setText(_translate("MainWindow", "Since startup on %1").arg(
            unicode(strftime(shared.config.get('bitmessagesettings', 'timeformat'), localtime(int(time.time()))),'utf-8')))
        self.numberOfMessagesProcessed = 0
        self.numberOfBroadcastsProcessed = 0
        self.numberOfPubkeysProcessed = 0

        # Set the icon sizes for the identicons
        identicon_size = 3*7
        self.ui.tableWidgetInbox.setIconSize(QtCore.QSize(identicon_size, identicon_size))
        self.ui.tableWidgetSent.setIconSize(QtCore.QSize(identicon_size, identicon_size))
        self.ui.tableWidgetYourIdentities.setIconSize(QtCore.QSize(identicon_size, identicon_size))
        self.ui.tableWidgetSubscriptions.setIconSize(QtCore.QSize(identicon_size, identicon_size))
        self.ui.tableWidgetAddressBook.setIconSize(QtCore.QSize(identicon_size, identicon_size))
        self.ui.tableWidgetBlacklist.setIconSize(QtCore.QSize(identicon_size, identicon_size))
        
        self.UISignalThread = UISignaler()
        QtCore.QObject.connect(self.UISignalThread, QtCore.SIGNAL(
            "writeNewAddressToTable(PyQt_PyObject,PyQt_PyObject,PyQt_PyObject)"), self.writeNewAddressToTable)
        QtCore.QObject.connect(self.UISignalThread, QtCore.SIGNAL(
            "updateStatusBar(PyQt_PyObject)"), self.updateStatusBar)
        QtCore.QObject.connect(self.UISignalThread, QtCore.SIGNAL(
            "updateSentItemStatusByHash(PyQt_PyObject,PyQt_PyObject)"), self.updateSentItemStatusByHash)
        QtCore.QObject.connect(self.UISignalThread, QtCore.SIGNAL(
            "updateSentItemStatusByAckdata(PyQt_PyObject,PyQt_PyObject)"), self.updateSentItemStatusByAckdata)
        QtCore.QObject.connect(self.UISignalThread, QtCore.SIGNAL(
            "displayNewInboxMessage(PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject)"), self.displayNewInboxMessage)
        QtCore.QObject.connect(self.UISignalThread, QtCore.SIGNAL(
            "displayNewSentMessage(PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject)"), self.displayNewSentMessage)
        QtCore.QObject.connect(self.UISignalThread, QtCore.SIGNAL(
            "updateNetworkStatusTab()"), self.updateNetworkStatusTab)
        QtCore.QObject.connect(self.UISignalThread, QtCore.SIGNAL(
            "updateNumberOfMessagesProcessed()"), self.updateNumberOfMessagesProcessed)
        QtCore.QObject.connect(self.UISignalThread, QtCore.SIGNAL(
            "updateNumberOfPubkeysProcessed()"), self.updateNumberOfPubkeysProcessed)
        QtCore.QObject.connect(self.UISignalThread, QtCore.SIGNAL(
            "updateNumberOfBroadcastsProcessed()"), self.updateNumberOfBroadcastsProcessed)
        QtCore.QObject.connect(self.UISignalThread, QtCore.SIGNAL(
            "setStatusIcon(PyQt_PyObject)"), self.setStatusIcon)
        QtCore.QObject.connect(self.UISignalThread, QtCore.SIGNAL(
            "changedInboxUnread(PyQt_PyObject)"), self.changedInboxUnread)
        QtCore.QObject.connect(self.UISignalThread, QtCore.SIGNAL(
            "rerenderInboxFromLabels()"), self.rerenderInboxFromLabels)
        QtCore.QObject.connect(self.UISignalThread, QtCore.SIGNAL(
            "rerenderSentToLabels()"), self.rerenderSentToLabels)
        QtCore.QObject.connect(self.UISignalThread, QtCore.SIGNAL(
            "rerenderAddressBook()"), self.rerenderAddressBook)
        QtCore.QObject.connect(self.UISignalThread, QtCore.SIGNAL(
            "rerenderSubscriptions()"), self.rerenderSubscriptions)
        QtCore.QObject.connect(self.UISignalThread, QtCore.SIGNAL(
            "removeInboxRowByMsgid(PyQt_PyObject)"), self.removeInboxRowByMsgid)
        QtCore.QObject.connect(self.UISignalThread, QtCore.SIGNAL(
            "displayAlert(PyQt_PyObject,PyQt_PyObject,PyQt_PyObject)"), self.displayAlert)
        self.UISignalThread.start()

        # Below this point, it would be good if all of the necessary global data
        # structures were initialized.

        self.rerenderComboBoxSendFrom()
        self.rerenderFromBoxEscrow()
        self.rerenderYourIdentities_2()
        # Check to see whether we can connect to namecoin. Hide the 'Fetch Namecoin ID' button if we can't.
        try:
            options = {}
            options["type"] = shared.config.get('bitmessagesettings', 'namecoinrpctype')
            options["host"] = shared.config.get('bitmessagesettings', 'namecoinrpchost')
            options["port"] = shared.config.get('bitmessagesettings', 'namecoinrpcport')
            options["user"] = shared.config.get('bitmessagesettings', 'namecoinrpcuser')
            options["password"] = shared.config.get('bitmessagesettings', 'namecoinrpcpassword')
            nc = namecoinConnection(options)
            if nc.test()[0] == 'failed':
                self.ui.pushButtonFetchNamecoinID.hide()
        except:
            print 'There was a problem testing for a Namecoin daemon. Hiding the Fetch Namecoin ID button'
            self.ui.pushButtonFetchNamecoinID.hide()


    def checkchange(self):
        if self.ui.checkBox.isChecked():
            self.timer3.start(3600000) # milliseconds
        else:
            self.timer3.stop()

    def click_pushbutton_5(self):
        self.renderboard()


    #render decentralized trade browser text, check if message signed with right address ect.
    def renderboard(self):
        self.ui.textBrowser.clear()
        if self.ui.offertype.currentText() == "Goods":
            g = shelve.open("board-goods.slv")
            b = list(g.items())
            b.sort(key=lambda item: item[0], reverse=True)
            for itr in b:
                addres = itr[0]
                lst = g[addres]
                try:
                    cont = lst[4]
                except:
                    cont = ""
                try:
                    loc = lst[6]
                except:
                    loc = ""
                try:
                    summ = str(lst[0])
                    price = str(lst[2])
                    subj = str(lst[1])
                    msg = lst[3]
                except:
                    summ = ""
                    price = ""
                    msg = ""
                if len(msg)>1001:
                    msg=msg[:1000]
                msg = msg.decode('UTF-8', 'ignore')
                subj = subj.decode('UTF-8', 'ignore')
                msg.replace('"', "'").replace("<", "[").replace(">", "]").replace(">", "]").replace("//", "::").replace("\\", "::")
                if "<" not in msg and ">" not in msg:
                    if self.ui.comboBox_2.currentText() == "All" or self.ui.comboBox_2.currentText() == subj or self.ui.comboBox_2.currentText() == "":
                        if self.ui.location.currentText() == "Worldwide" or self.ui.location.currentText() == loc:
                            if self.ui.textBrowser.toPlainText() == "":
                                self.ui.textBrowser.setHtml('Contact:<a title="'+cont+'" href="#contact#'+cont+'">'+cont+'</a><BR>Price:'+price+'<br>Details:'+msg+'<br><a title="Show More Details" href="#more#'+addres+"|"+"G"+'">Show More Details</a><br><a title="Buy" href="#Buy#'+cont+'|'+price+'">Buy</a><br>')
                            else:
                                self.ui.textBrowser.setHtml(str(self.ui.textBrowser.toHtml())+'Contact:<a title="'+cont+'" href="#contact#'+cont+'">'+cont+'</a><BR>Price:'+price+'<br>Details:'+msg+'<br><a title="Show More Details" href="#more#'+addres+"|"+"G"+'">Show More Details</a><br><a title="Buy" href="#Buy#'+cont+'|'+price+'">Buy</a><br>')

        elif self.ui.offertype.currentText()== "Services":
            g = shelve.open("board-services.slv")
            b = list(g.items())
            b.sort(key=lambda item: item[0], reverse=True)
            for itr in b:
                addres = itr[0]
                lst = g[addres]
                try:
                    cont = lst[4]
                except:
                    cont = ""
                try:
                    loc = lst[6]
                except:
                    loc = ""
                try:
                    summ = str(lst[0])
                    price = str(lst[2])
                    msg = lst[3]
                except:
                    summ = ""
                    price = ""
                    msg = ""
                if len(msg)>1001:
                    msg=msg[:1000]
                msg = msg.decode('UTF-8', 'ignore')
                subj = subj.decode('UTF-8', 'ignore')
                msg.replace('"', "'").replace("<", "[").replace(">", "]").replace(">", "]").replace("//", "::").replace("\\", "::")
                if "<" not in msg and ">" not in msg:
                    if self.ui.comboBox_2.currentText() == "All" or self.ui.comboBox_2.currentText() == subj or self.ui.comboBox_2.currentText() == "":
                        if self.ui.location.currentText() == "Worldwide" or self.ui.location.currentText() == loc:
                            if self.ui.textBrowser.toPlainText()=="":
                                self.ui.textBrowser.setHtml('Contact:<a title="'+cont+'" href="#contact#'+cont+'">'+cont+'</a><BR>Price:'+price+'<br>Details:'+msg+'<br><a title="Show More Details" href="#more#'+addres+"|"+"S"+'">Show More Details</a><br><a title="Buy" href="#Buy#'+cont+'|'+price+'">Buy</a><br>')
                            else:
                                self.ui.textBrowser.setHtml(str(self.ui.textBrowser.toHtml())+'Contact:<a title="'+cont+'" href="#contact#'+cont+'">'+cont+'</a><BR>Price:'+price+'<br>Details:'+msg+'<br><a title="Show More Details" href="#more#'+addres+"|"+"S"+'">Show More Details</a><br><a title="Buy" href="#Buy#'+cont+'|'+price+'">Buy</a><br>')

        elif self.ui.offertype.currentText() == "Currency exchange":
            g = shelve.open("board-currencies.slv")
            b = list(g.items())
            b.sort(key=lambda item: item[0], reverse=True)
            for itr in b:
                addres = itr[0]
                lst = g[addres]
                try:
                    cont = lst[4]
                except:
                    cont = ""
                try:
                    loc = lst[6]
                except:
                    loc = ""
                try:
                    summ = str(lst[0])
                    price = str(lst[2])
                    msg = lst[3]
                except:
                    summ = ""
                    price = ""
                    msg = ""
                if len(msg)>1001:
                    msg=msg[:1000]
                msg = msg.decode('UTF-8', 'ignore')
                subj = subj.decode('UTF-8', 'ignore')
                msg.replace('"', "'").replace("<", "[").replace(">", "]").replace(">", "]").replace("//", "::").replace("\\", "::")
                if "<" not in msg and ">" not in msg:
                    if self.ui.location.currentText() == "Worldwide" or self.ui.location.currentText() == loc:
                        if self.ui.comboBox_2.currentText() == "All" or self.ui.comboBox_2.currentText() == subj or self.ui.comboBox_2.currentText() == "":
                            if self.ui.textBrowser.toPlainText() == "":
                                self.ui.textBrowser.setHtml('Contact:<a title="'+cont+'" href="#contact#'+cont+'">'+cont+'</a><BR>Price:'+price+'<br>Details:'+msg+'<br><a title="Show More Details" href="#more#'+addres+"|"+"C"'">Show More Details</a><br><a title="Buy" href="#Buy#'+cont+'|'+price+'">Buy</a><br>')
                            else:
                                self.ui.textBrowser.setHtml(str(self.ui.textBrowser.toHtml())+'Contact:<a title="'+cont+'" href="#contact#'+cont+'">'+cont+'</a><BR>Price:'+price+'<br>Details:'+msg+'<br><a title="Show More Details" href="#more#'+addres+"|"+"C"+'">Show More Details</a><br><a title="Buy" href="#Buy#'+cont+'|'+price+'">Buy</a><br>')


    # Show or hide the application window after clicking an item within the
    # tray icon or, on Windows, the try icon itself.
    def appIndicatorShowOrHideWindow(self):
        if not self.actionShow.isChecked():
            self.hide()
        else:
            if sys.platform[0:3] == 'win':
                self.setWindowFlags(Qt.Window)
            # else:
                # self.showMaximized()
            self.show()
            self.setWindowState(
                self.windowState() & ~QtCore.Qt.WindowMinimized | QtCore.Qt.WindowActive)
            self.activateWindow()

    # pointer to the application
    # app = None
    # The most recent message
    newMessageItem = None

    # The most recent broadcast
    newBroadcastItem = None

    # show the application window
    def appIndicatorShow(self):
        if self.actionShow is None:
            return
        if not self.actionShow.isChecked():
            self.actionShow.setChecked(True)
            self.appIndicatorShowOrHideWindow()

    # unchecks the show item on the application indicator
    def appIndicatorHide(self):
        if self.actionShow is None:
            return
        if self.actionShow.isChecked():
            self.actionShow.setChecked(False)
            self.appIndicatorShowOrHideWindow()

    # application indicator show or hide
    """# application indicator show or hide
    def appIndicatorShowBitmessage(self):
        #if self.actionShow == None:
        #    return
        print self.actionShow.isChecked()
        if not self.actionShow.isChecked():
            self.hide()
            #self.setWindowState(self.windowState() & QtCore.Qt.WindowMinimized)
        else:
            self.appIndicatorShowOrHideWindow()"""

    # Show the program window and select inbox tab
    def appIndicatorInbox(self, mm_app, source_id):
        self.appIndicatorShow()
        # select inbox
        self.ui.tabWidget.setCurrentIndex(0)
        selectedItem = None
        if source_id == 'Subscriptions':
            # select unread broadcast
            if self.newBroadcastItem is not None:
                selectedItem = self.newBroadcastItem
                self.newBroadcastItem = None
        else:
            # select unread message
            if self.newMessageItem is not None:
                selectedItem = self.newMessageItem
                self.newMessageItem = None
        # make it the current item
        if selectedItem is not None:
            try:
                self.ui.tableWidgetInbox.setCurrentItem(selectedItem)
            except Exception:
                self.ui.tableWidgetInbox.setCurrentCell(0, 0)
            self.tableWidgetInboxItemClicked()
        else:
            # just select the first item
            self.ui.tableWidgetInbox.setCurrentCell(0, 0)
            self.tableWidgetInboxItemClicked()

    # Show the program window and select send tab
    def appIndicatorSend(self):
        self.appIndicatorShow()
        self.ui.tabWidget.setCurrentIndex(1)

    # Show the program window and select subscriptions tab
    def appIndicatorSubscribe(self):
        self.appIndicatorShow()
        self.ui.tabWidget.setCurrentIndex(4)

    # Show the program window and select the address book tab
    def appIndicatorAddressBook(self):
        self.appIndicatorShow()
        self.ui.tabWidget.setCurrentIndex(5)

    # Load Sent items from database
    def loadSent(self, where="", what=""):
        what = "%" + what + "%"
        if where == "To":
            where = "toaddress"
        elif where == "From":
            where = "fromaddress"
        elif where == "Subject":
            where = "subject"
        elif where == "Message":
            where = "message"
        else:
            where = "toaddress || fromaddress || subject || message"

        sqlStatement = '''
            SELECT toaddress, fromaddress, subject, status, ackdata, lastactiontime 
            FROM sent WHERE folder="sent" AND %s LIKE ? 
            ORDER BY lastactiontime
            ''' % (where,)

        while self.ui.tableWidgetSent.rowCount() > 0:
            self.ui.tableWidgetSent.removeRow(0)

        queryreturn = sqlQuery(sqlStatement, what)
        for row in queryreturn:
            toAddress, fromAddress, subject, status, ackdata, lastactiontime = row
            subject = shared.fixPotentiallyInvalidUTF8Data(subject)

            if shared.config.has_section(fromAddress):
                fromLabel = shared.config.get(fromAddress, 'label')
            if fromLabel == '':
                fromLabel = fromAddress

            toLabel = ''
            queryreturn = sqlQuery(
                '''select label from addressbook where address=?''', toAddress)
            if queryreturn != []:
                for row in queryreturn:
                    toLabel, = row
            if toLabel == '':
                # It might be a broadcast message. We should check for that
                # label.
                queryreturn = sqlQuery(
                    '''select label from subscriptions where address=?''', toAddress)

                if queryreturn != []:
                    for row in queryreturn:
                        toLabel, = row
            
            if toLabel == '':
                if shared.config.has_section(toAddress):
                    toLabel = shared.config.get(toAddress, 'label')
            if toLabel == '':
                toLabel = toAddress

            self.ui.tableWidgetSent.insertRow(0)
            toAddressItem = QtGui.QTableWidgetItem(unicode(toLabel, 'utf-8'))
            toAddressItem.setToolTip(unicode(toLabel, 'utf-8'))
            toAddressItem.setIcon(avatarize(toAddress))
            toAddressItem.setData(Qt.UserRole, str(toAddress))
            toAddressItem.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ui.tableWidgetSent.setItem(0, 0, toAddressItem)

            if fromLabel == '':
                fromLabel = fromAddress
            fromAddressItem = QtGui.QTableWidgetItem(unicode(fromLabel, 'utf-8'))
            fromAddressItem.setToolTip(unicode(fromLabel, 'utf-8'))
            fromAddressItem.setIcon(avatarize(fromAddress))
            fromAddressItem.setData(Qt.UserRole, str(fromAddress))
            fromAddressItem.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ui.tableWidgetSent.setItem(0, 1, fromAddressItem)

            subjectItem = QtGui.QTableWidgetItem(unicode(subject, 'utf-8'))
            subjectItem.setToolTip(unicode(subject, 'utf-8'))
            subjectItem.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ui.tableWidgetSent.setItem(0, 2, subjectItem)

            if status == 'awaitingpubkey':
                statusText = _translate(
                    "MainWindow", "Waiting for their encryption key. Will request it again soon.")
            elif status == 'doingpowforpubkey':
                statusText = _translate(
                    "MainWindow", "Encryption key request queued.")
            elif status == 'msgqueued':
                statusText = _translate(
                    "MainWindow", "Queued.")
            elif status == 'msgsent':
                statusText = _translate("MainWindow", "Message sent. Waiting for acknowledgement. Sent at %1").arg(
                    unicode(strftime(shared.config.get('bitmessagesettings', 'timeformat'), localtime(lastactiontime)),'utf-8'))
            elif status == 'msgsentnoackexpected':
                statusText = _translate("MainWindow", "Message sent. Sent at %1").arg(
                    unicode(strftime(shared.config.get('bitmessagesettings', 'timeformat'), localtime(lastactiontime)),'utf-8'))
            elif status == 'doingmsgpow':
                statusText = _translate(
                    "MainWindow", "Need to do work to send message. Work is queued.")
            elif status == 'ackreceived':
                statusText = _translate("MainWindow", "Acknowledgement of the message received %1").arg(
                    unicode(strftime(shared.config.get('bitmessagesettings', 'timeformat'), localtime(lastactiontime)),'utf-8'))
            elif status == 'broadcastqueued':
                statusText = _translate(
                    "MainWindow", "Broadcast queued.")
            elif status == 'broadcastsent':
                statusText = _translate("MainWindow", "Broadcast on %1").arg(unicode(strftime(
                    shared.config.get('bitmessagesettings', 'timeformat'), localtime(lastactiontime)),'utf-8'))
            elif status == 'toodifficult':
                statusText = _translate("MainWindow", "Problem: The work demanded by the recipient is more difficult than you are willing to do. %1").arg(
                    unicode(strftime(shared.config.get('bitmessagesettings', 'timeformat'), localtime(lastactiontime)),'utf-8'))
            elif status == 'badkey':
                statusText = _translate("MainWindow", "Problem: The recipient\'s encryption key is no good. Could not encrypt message. %1").arg(
                    unicode(strftime(shared.config.get('bitmessagesettings', 'timeformat'), localtime(lastactiontime)),'utf-8'))
            elif status == 'forcepow':
                statusText = _translate(
                    "MainWindow", "Forced difficulty override. Send should start soon.")
            else:
                statusText = _translate("MainWindow", "Unknown status: %1 %2").arg(status).arg(unicode(
                    strftime(shared.config.get('bitmessagesettings', 'timeformat'), localtime(lastactiontime)),'utf-8'))
            newItem = myTableWidgetItem(statusText)
            newItem.setToolTip(statusText)
            newItem.setData(Qt.UserRole, QByteArray(ackdata))
            newItem.setData(33, int(lastactiontime))
            newItem.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ui.tableWidgetSent.setItem(0, 3, newItem)
        self.ui.tableWidgetSent.sortItems(3, Qt.DescendingOrder)
        self.ui.tableWidgetSent.keyPressEvent = self.tableWidgetSentKeyPressEvent

    # Load inbox from messages database file
    def loadInbox(self, where="", what=""):
        what = "%" + what + "%"
        if where == "To":
            where = "toaddress"
        elif where == "From":
            where = "fromaddress"
        elif where == "Subject":
            where = "subject"
        elif where == "Message":
            where = "message"
        else:
            where = "toaddress || fromaddress || subject || message"

        sqlStatement = '''
            SELECT msgid, toaddress, fromaddress, subject, received, read
            FROM inbox WHERE folder="inbox" AND %s LIKE ?
            ORDER BY received
            ''' % (where,)

        while self.ui.tableWidgetInbox.rowCount() > 0:
            self.ui.tableWidgetInbox.removeRow(0)

        font = QFont()
        font.setBold(True)
        queryreturn = sqlQuery(sqlStatement, what)
        for row in queryreturn:
            msgid, toAddress, fromAddress, subject, received, read = row
            subject = shared.fixPotentiallyInvalidUTF8Data(subject)
            if str(fromAddress) == MyForm.bitxbaychan or str(toAddress) == MyForm.bitxbaychan:
                    error=""
            else:
                try:
                    if toAddress == self.str_broadcast_subscribers:
                        toLabel = self.str_broadcast_subscribers
                    else:
                        toLabel = shared.config.get(toAddress, 'label')
                except:
                    toLabel = ''
                if toLabel == '':
                    toLabel = toAddress
    
                fromLabel = ''
                if shared.config.has_section(fromAddress):
                    fromLabel = shared.config.get(fromAddress, 'label')
                
                if fromLabel == '':  # If the fromAddress isn't one of our addresses and isn't a chan
                    queryreturn = sqlQuery(
                        '''select label from addressbook where address=?''', fromAddress)
                    if queryreturn != []:
                        for row in queryreturn:
                            fromLabel, = row
    
                if fromLabel == '':  # If this address wasn't in our address book...
                    queryreturn = sqlQuery(
                        '''select label from subscriptions where address=?''', fromAddress)
                    if queryreturn != []:
                        for row in queryreturn:
                            fromLabel, = row
                if fromLabel == '':
                    fromLabel = fromAddress
                
                # message row
                self.ui.tableWidgetInbox.insertRow(0)
                # to
                to_item = QtGui.QTableWidgetItem(unicode(toLabel, 'utf-8'))
                to_item.setToolTip(unicode(toLabel, 'utf-8'))
                to_item.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                if not read:
                    to_item.setFont(font)
                to_item.setData(Qt.UserRole, str(toAddress))
                if shared.safeConfigGetBoolean(toAddress, 'mailinglist'):
                    to_item.setTextColor(QtGui.QColor(137, 04, 177)) # magenta
                if shared.safeConfigGetBoolean(str(toAddress), 'chan'):
                    to_item.setTextColor(QtGui.QColor(216, 119, 0)) # orange
                to_item.setIcon(avatarize(toAddress))
                self.ui.tableWidgetInbox.setItem(0, 0, to_item)
                # from
                from_item = QtGui.QTableWidgetItem(unicode(fromLabel, 'utf-8'))
                from_item.setToolTip(unicode(fromLabel, 'utf-8'))
                from_item.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                if not read:
                    from_item.setFont(font)
                from_item.setData(Qt.UserRole, str(fromAddress))
                if shared.safeConfigGetBoolean(str(fromAddress), 'chan'):
                    from_item.setTextColor(QtGui.QColor(216, 119, 0)) # orange
                from_item.setIcon(avatarize(fromAddress))
    
    
    
                # bitxbay changes
                queryreturn = sqlQuery(
                    '''select message from inbox where msgid=?''', msgid)
                if queryreturn != []:
                    for row in queryreturn:
                        messageText, = row
                messageText = shared.fixPotentiallyInvalidUTF8Data(messageText)
                messageText = unicode(messageText, 'utf-8')
    

                self.ui.textBrowser_2.setOpenLinks(False)
                self.ui.textBrowser.setOpenLinks(False)
                self.ui.textBrowser_3.setOpenLinks(False)
    
    
                font = QFont()
                font.setBold(False)
                self.ui.textEditInboxMessage.setCurrentFont(font)
    
    
                #changes end here
    
                font = QFont()
                font.setBold(False)
                self.ui.textEditInboxMessage.setCurrentFont(font)
    
                self.ui.tableWidgetInbox.setItem(0, 1, from_item)
                # subject
                subject_item = QtGui.QTableWidgetItem(unicode(subject, 'utf-8'))
                subject_item.setToolTip(unicode(subject, 'utf-8'))
                subject_item.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                if not read:
                    subject_item.setFont(font)
                self.ui.tableWidgetInbox.setItem(0, 2, subject_item)
                # time received
                time_item = myTableWidgetItem(unicode(strftime(shared.config.get(
                    'bitmessagesettings', 'timeformat'), localtime(int(received))), 'utf-8'))
                time_item.setToolTip(unicode(strftime(shared.config.get(
                    'bitmessagesettings', 'timeformat'), localtime(int(received))), 'utf-8'))
                time_item.setData(Qt.UserRole, QByteArray(msgid))
                time_item.setData(33, int(received))
                time_item.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                if not read:
                    time_item.setFont(font)
                self.ui.tableWidgetInbox.setItem(0, 3, time_item)
    
            self.ui.tableWidgetInbox.sortItems(3, Qt.DescendingOrder)
            self.ui.tableWidgetInbox.keyPressEvent = self.tableWidgetInboxKeyPressEvent


    def rendertextbrowser2(self):
        data_file = 'escrow.slv'
        sh = shelve.open(data_file)
        self.ui.textBrowser_2.setHtml("")
        for mess in sh.keys():
            messageText2 = sh[mess]
            try:
                start = messageText2.index('{cont{') + len('{cont{')
                end = messageText2.index('}cont}', start)
                loadedescrow=messageText2[start:end]
            except ValueError:
                error=''
            addrmerch = loadedescrow
            try:
                start = messageText2.index('{lbl{') + len('{lbl{')
                end = messageText2.index('}lbl}', start)
                lbl = messageText2[start:end]
            except ValueError:
                lbl = loadedescrow
            if lbl=="":
                lbl = loadedescrow
            loadedescrow = lbl
            try:
                start = messageText2.index('{escrowaddr3{') + len('{escrowaddr3{')
                end = messageText2.index('}escrowaddr3}', start)
                escrow2addr=messageText2[start:end]
            except ValueError:
                error=''
                escrow2addr=""
            try:
                start = messageText2.index('{escrowaddr1{') + len('{escrowaddr1{')
                end = messageText2.index('}escrowaddr1}', start)
                escrow1addr=messageText2[start:end]
            except ValueError:
                error=''
                escrow1addr=""
            try:
                start = messageText2.index('{amount{') + len('{amount{')
                end = messageText2.index('}amount}', start)
                amount11=messageText2[start:end]
            except ValueError:
                error=''
                amount11=""
            try:
                start = messageText2.index('{id{') + len('{id{')
                end = messageText2.index('}id}', start)
                idescrow=messageText2[start:end]
            except ValueError:
                error=''
                idescrow=""
            if "lfa01{status{started-buyer-1" in messageText2 and amount11!="":
                if self.onlygoodsymbols(loadedescrow):
                    escrowmessagetext = "<p>"+'<a href="#contact#'+addrmerch+'">'+loadedescrow+'</a>'+" | "+"Waiting for the merchant reply. Deal amount:"+amount11+'</p>'+'  <a href="#cancel#'+idescrow+'">Cancel</a>   '+"<br>"
                    escrowmessagetext = escrowmessagetext.decode("utf-8")
                    MyForm.lastmessbuyer = escrowmessagetext + self.ui.textBrowser_2.toHtml()
                    self.ui.textBrowser_2.setHtml(MyForm.lastmessbuyer)
                    MyForm.textbro2html2 = self.ui.textBrowser_2.toHtml()
            elif "lfa01{status{started-buyer-3" in messageText2 and amount11!="" and escrow2addr!="" and "lfa01{status{started-buyer-4" not in messageText2:
                if self.onlygoodsymbols(loadedescrow):
                    escrowmessagetext = "<p>"+'<a href="#contact#'+addrmerch+'">'+loadedescrow+'</a>'+" | "+"Something go wrong.You should try to repeat. But be careful. Send "+str(float(amount11)*0.05)+" To address:"+escrow1addr+'</p> '+'  <a href="#resend#'+idescrow+'">Resend</a>   '+'  <a href="#cancel#'+idescrow+'">Cancel</a>   '+"<br>"
                    escrowmessagetext = escrowmessagetext.decode("utf-8")
                    self.ui.textBrowser_2.setHtml(escrowmessagetext + self.ui.textBrowser_2.toHtml())
                    MyForm.textbro2html2 = self.ui.textBrowser_2.toHtml()
            elif "lfa01{status{started-buyer-4" in messageText2 and amount11!="" and escrow2addr!="" and "lfa01{status{started-buyer-5" not in messageText2:
                if self.onlygoodsymbols(loadedescrow):
                    escrowmessagetext = "<p>"+'<a href="#contact#'+addrmerch+'">'+loadedescrow+'</a>'+" | "+"Waiting for the merchant insurance payment. Deal amount:"+amount11+'</p> ' + '  <a href="#cancel#'+idescrow+'">Cancel</a>   '+"<br>"
                    escrowmessagetext = escrowmessagetext.decode("utf-8")
                    self.ui.textBrowser_2.setHtml(escrowmessagetext + self.ui.textBrowser_2.toHtml())
                    MyForm.textbro2html2 = self.ui.textBrowser_2.toHtml()
            elif "lfa01{status{started-buyer04" in messageText2 and amount11!="" and escrow2addr!="" and "lfa01{status{started-buyer-4" not in messageText2:
                if self.onlygoodsymbols(loadedescrow):
                    escrowmessagetext = "<p>"+'<a href="#contact#'+addrmerch+'">'+loadedescrow+'</a>'+" | "+"Something go wrong.You should try to repeat. But be careful. Send "+str(float(amount11)*0.05)+" To address:"+escrow1addr+'</p> '+'  <a href="#resend#'+idescrow+'">Resend</a>   '+'  <a href="#cancel#'+idescrow+'">Cancel</a>   '+"<br>"
                    escrowmessagetext = escrowmessagetext.decode("utf-8")
                    self.ui.textBrowser_2.setHtml(escrowmessagetext + self.ui.textBrowser_2.toHtml())
                    MyForm.textbro2html2 = self.ui.textBrowser_2.toHtml()
            elif "lfa01{status{started-buyer-5" in messageText2 and amount11!="" and escrow2addr!="" and "lfa01{status{started-buyer-4" not in messageText2:
                if self.onlygoodsymbols(loadedescrow):
                    escrowmessagetext = "<p>"+'<a href="#contact#'+addrmerch+'">'+loadedescrow+'</a>'+" | "+"Waiting for the merchant insurance payment confirmation. Deal amount:"+amount11+'</p> ' + "<br>"
                    escrowmessagetext = escrowmessagetext.decode("utf-8")
                    self.ui.textBrowser_2.setHtml(escrowmessagetext + self.ui.textBrowser_2.toHtml())
                    MyForm.textbro2html2 = self.ui.textBrowser_2.toHtml()
            elif "lfa01{status{started-buyer-6" in messageText2 and amount11!="" and "lfa01{status{started-buyer-4" not in messageText2:
                if self.onlygoodsymbols(loadedescrow):
                    escrowmessagetext = "<p>"+'<a href="#contact#'+addrmerch+'">'+loadedescrow+'</a>'+" | "+"You paid the whole amount of deal. Wait for the merchant`s work. And SIGN ONLY WHEN YOU SURE SATISFIED! After you do it the merchant get all money and you get back 5% insurance. Deal amount:"+amount11+'</p> '+'  <a href="#sign'+'{'+idescrow+'}' + '">Sign</a>     ' +"<br>"
                    escrowmessagetext = escrowmessagetext.decode("utf-8")
                    self.ui.textBrowser_2.setHtml(escrowmessagetext + self.ui.textBrowser_2.toHtml())
                    MyForm.textbro2html = self.ui.textBrowser_2.toHtml()
            elif "lfa01{status{started-buyer06" in messageText2 and amount11!="" and "lfa01{status{started-buyer-6" not in messageText2:
                if self.onlygoodsymbols(loadedescrow):
                    escrowmessagetext = "<p>"+'<a href="#contact#'+addrmerch+'">'+loadedescrow+'</a>'+" | "+"Something go wrong.You should try to repeat. But be careful. Send "+str(float(amount11)*0.05)+" To address:"+escrow2addr+'</p> '+'  <a href="#3resend#'+idescrow+'">Resend</a>   '+'  <a href="#cancel#'+idescrow+'">Cancel</a>   '+"<br>"
                    escrowmessagetext = escrowmessagetext.decode("utf-8")
                    self.ui.textBrowser_2.setHtml(escrowmessagetext + self.ui.textBrowser_2.toHtml())
                    MyForm.textbro2html2 = self.ui.textBrowser_2.toHtml()
            elif "lfa01{status{started-buyer-7" in messageText2 and amount11!="" and "lfa01{status{started-buyer-4" not in messageText2:
                if self.onlygoodsymbols(loadedescrow):
                    self.ui.textBrowser_2.setHtml("<p>"+'<a href="#contact#'+addrmerch+'">'+loadedescrow+'</a>'+" | "+"You signed this deal. Wait all messages and insurance money. Deal amount:"+amount11+'</p> '+"<br>"+self.ui.textBrowser_2.toHtml())
                    MyForm.textbro2html = self.ui.textBrowser_2.toHtml()
            elif "lfa01{status{started-buyer-8" in messageText2 and amount11!="" and "lfa01{status{started-buyer-4" not in messageText2:
                if self.onlygoodsymbols(loadedescrow):
                    self.ui.textBrowser_2.setHtml("<p>"+'<a href="#contact#'+addrmerch+'">'+loadedescrow+'</a>'+" | "+"Wait all messages and insurance money. Deal amount:"+amount11+'</p> '+"<br>"+self.ui.textBrowser_2.toHtml())
                    MyForm.textbro2html = self.ui.textBrowser_2.toHtml()
        sh.close()

    def rendertextbrowser3(self):
        sh2 = shelve.open('escrowm.slv')
        self.ui.textBrowser_3.setHtml("")
        for mess in sh2.keys():
            messageText2 = sh2[mess]
            try:
                start = messageText2.index('{cont{') + len('{cont{')
                end = messageText2.index('}cont}', start)
                loadedescrow=messageText2[start:end]
            except ValueError:
                error=''
            try:
                start = messageText2.index('{lbl{') + len('{lbl{')
                end = messageText2.index('}lbl}', start)
                lbl = messageText2[start:end]
            except ValueError:
                lbl = loadedescrow
            if lbl=="":
                lbl = loadedescrow
            if len(lbl)>50:
                lbl=lbl[:50]
            addrmerchant = loadedescrow
            loadedescrow = lbl
            try:
                start = messageText2.index('{escrowaddr2{') + len('{escrowaddr2{')
                end = messageText2.index('}escrowaddr2}', start)
                esc2=messageText2[start:end]
            except ValueError:
                error=''
                escrow2addr=""
            try:
                start = messageText2.index('{escrowaddr3{') + len('{escrowaddr3{')
                end = messageText2.index('}escrowaddr3}', start)
                escrow2addr=messageText2[start:end]
            except ValueError:
                error=''
                escrow2addr=""
            try:
                start = messageText2.index('{amount{') + len('{amount{')
                end = messageText2.index('}amount}', start)
                amount11=messageText2[start:end]
            except ValueError:
                error=''
                amount11=""
            try:
                start = messageText2.index('{id{') + len('{id{')
                end = messageText2.index('}id}', start)
                idescrow=messageText2[start:end]
            except ValueError:
                error=''
                idescrow=""

            try:
                start = messageText2.index('{comment{') + len('{comment{')
                end = messageText2.index('}comment}', start)
                comment=messageText2[start:end]
            except ValueError:
                comment=""
            if len(comment)>550:
                comment=comment[:550]

            try:
                start = messageText2.index('{cont2{') + len('{cont2{')
                end = messageText2.index('}cont2}', start)
                addrbuyer=messageText2[start:end]
            except ValueError:
                error=""

            if messageText2[0:29] == "alfa01{status{started-buyer-1":
                try:
                    start = messageText2.index('{pub1{') + len('{pub1{')
                    end = messageText2.index('}pub1}', start)
                    buy1=messageText2[start:end]
                except ValueError:
                    error="bitcoin address error"
                try:
                    start = messageText2.index('{pub2{') + len('{pub2{')
                    end = messageText2.index('}pub2}', start)
                    buy2=messageText2[start:end]
                except ValueError:
                    error="bitcoin address error"
                try:
                    start = messageText2.index('{pub3{') + len('{pub3{')
                    end = messageText2.index('}pub3}', start)
                    buy3=messageText2[start:end]
                except ValueError:
                    error="bitcoin address error"

                if self.onlygoodsymbols(loadedescrow):
                    escrowmessagetext = "<p>"+'<a href="#contact#'+addrbuyer+'">'+loadedescrow+'</a>'+" | "+"New deal. Deal amount:"+amount11+'</p>'+'  <a href="#accept#addrbuyer='+addrbuyer+'#addrmerchant='+addrmerchant+'#buy1='+buy1+'#buy2='+buy2+'#buy3='+buy3+'#idescrow='+idescrow+'#amount='+amount11+'#lbl='+lbl+'">Accept</a>   '+'  <a href="#cancel#'+idescrow+'">Cancel</a>   '+"<br>"+comment+"<br>"
                    escrowmessagetext = escrowmessagetext.decode("utf-8")
                    MyForm.lastmessbuyer = escrowmessagetext + self.ui.textBrowser_3.toHtml()
                    self.ui.textBrowser_3.setHtml(MyForm.lastmessbuyer)



            if "lfa01{status{started-buyer-2" in messageText2 and amount11!="":
                if self.onlygoodsymbols(loadedescrow):
                    escrowmessagetext = "<p>"+'<a href="#contact#'+addrbuyer+'">'+loadedescrow+'</a>'+" | "+"Wait for the buyer insurance payment. Deal amount:"+amount11+'</p>'+'  <a href="#cancel#'+idescrow+'">Cancel</a>   '+"<br>"+comment+"<br>"
                    escrowmessagetext = escrowmessagetext.decode("utf-8")
                    MyForm.lastmessbuyer = escrowmessagetext + self.ui.textBrowser_3.toHtml()
                    self.ui.textBrowser_3.setHtml(MyForm.lastmessbuyer)
            elif "lfa01{status{started-buyer-3" in messageText2 and amount11!="" and escrow2addr!="" and "lfa01{status{started-buyer-5" not in messageText2:
                if self.onlygoodsymbols(loadedescrow):
                    escrowmessagetext = "<p>"+'<a href="#contact#'+addrbuyer+'">'+loadedescrow+'</a>'+" | "+"Something go wrong."+ '<a href="#paymanualy#address=' + esc2 + '#amount=' + amount11 + '">Pay Manually</a>+</p> '+'  <a href="#cancel#'+idescrow+'">Cancel</a>   '+"<br>"+comment+"<br>"
                    escrowmessagetext = escrowmessagetext.decode("utf-8")
                    self.ui.textBrowser_3.setHtml(escrowmessagetext + self.ui.textBrowser_3.toHtml())
            elif "lfa01{status{started-buyer-4" in messageText2 and amount11!="" and escrow2addr!="" and "lfa01{status{started-buyer-5" not in messageText2:
                if self.onlygoodsymbols(loadedescrow):
                    escrowmessagetext = "<p>"+'<a href="#contact#'+addrbuyer+'">'+loadedescrow+'</a>'+" | "+"Wait for the buyer insurance payment confirmations. Deal amount:"+amount11+'</p>' +'  <a href="#cancel#'+idescrow+'">Cancel</a>   '+"<br>"+comment+"<br>"
                    escrowmessagetext = escrowmessagetext.decode("utf-8")
                    self.ui.textBrowser_3.setHtml(escrowmessagetext + self.ui.textBrowser_3.toHtml())
            elif "lfa01{status{started-buyer05" in messageText2 and amount11!="" and "lfa01{status{started-buyer-5" not in messageText2:
                if self.onlygoodsymbols(loadedescrow):
                    escrowmessagetext = "<p>"+'<a href="#contact#'+addrbuyer+'">'+loadedescrow+'</a>'+" | "+"Something go wrong.You should try to repeat. But be careful. Send "+str(float(amount11)*0.05)+" To address:"+esc2+'</p> '+'  <a href="#2resend#'+idescrow+'">Resend</a>   '+'  <a href="#cancel#'+idescrow+'">Cancel</a>   '+"<br>"
                    escrowmessagetext = escrowmessagetext.decode("utf-8")
                    self.ui.textBrowser_3.setHtml(escrowmessagetext + self.ui.textBrowser_3.toHtml())
            elif "lfa01{status{started-buyer-5" in messageText2 and amount11!="" and escrow2addr!="" and "lfa01{status{started-buyer-4" not in messageText2:
                if self.onlygoodsymbols(loadedescrow):
                    escrowmessagetext = "<p>"+'<a href="#contact#'+addrbuyer+'">'+loadedescrow+'</a>'+" | "+"Waiting for the buyer main payment." + '</p> ' +'  <a href="#cancel#'+idescrow+'">Cancel</a>   '+"<br>"+comment+"<br>"
                    escrowmessagetext = escrowmessagetext.decode("utf-8")
                    self.ui.textBrowser_3.setHtml(escrowmessagetext + self.ui.textBrowser_3.toHtml())
            elif "lfa01{status{started-buyer-6" in messageText2 and amount11!="" and "lfa01{status{started-buyer-4" not in messageText2:
                if self.onlygoodsymbols(loadedescrow):
                    escrowmessagetext = "<p>"+'<a href="#contact#'+addrbuyer+'">'+loadedescrow+'</a>'+" | "+"All the money was received. Follow your part of the deal, then ask to sign deal. The buyer must sign only when satisfied. Deal amount:"+amount11+'</p> ' +'  <a href="#cancel#'+idescrow+'">Cancel</a>   '+"<br>"+comment+"<br>"
                    escrowmessagetext = escrowmessagetext.decode("utf-8")
                    self.ui.textBrowser_3.setHtml(escrowmessagetext+self.ui.textBrowser_3.toHtml())
            elif "lfa01{status{started-buyer-7" in messageText2 and amount11!="" and "lfa01{status{started-buyer-4" not in messageText2:
                if self.onlygoodsymbols(loadedescrow):
                    escrowmessagetext = "<p>"+'<a href="#contact#'+addrbuyer+'">'+loadedescrow+'</a>'+" | "+"The buyer signed this deal. Wait all messages and insurence money. Deal amount:"+amount11+'</p> '+"<br>"
                    escrowmessagetext = escrowmessagetext.decode("utf-8")
                    self.ui.textBrowser_3.setHtml(escrowmessagetext + self.ui.textBrowser_3.toHtml())
            elif "lfa01{status{started-buyer-8" in messageText2 and amount11!="" and "lfa01{status{started-buyer-4" not in messageText2:
                if self.onlygoodsymbols(loadedescrow):
                    escrowmessagetext = "<p>"+'<a href="#contact#'+addrbuyer+'">'+loadedescrow+'</a>'+" | "+"Deal ended. Deal amount:"+amount11+'</p> '+"<br>"
                    escrowmessagetext = escrowmessagetext.decode("utf-8")
                    self.ui.textBrowser_3.setHtml(escrowmessagetext + self.ui.textBrowser_3.toHtml())
            elif "lfa01{status{started-buyer61" in messageText2 and amount11!="" and "lfa01{status{started-buyer62" not in messageText2:
                if self.onlygoodsymbols(loadedescrow):
                    escrowmessagetext = "<p>"+'<a href="#contact#'+addrbuyer+'">'+loadedescrow+'</a>'+" | "+"The buyer request cancel deal. Deal amount:"+amount11+'</p> '+ '  <a href="#agree#id='+idescrow+'">Agree</a>' +'  <a href="#continue#id='+idescrow+'">Disagree and try request to continue deal</a>'  +"<br>"
                    escrowmessagetext = escrowmessagetext.decode("utf-8")
                    self.ui.textBrowser_3.setHtml(escrowmessagetext + self.ui.textBrowser_3.toHtml())
        sh2.close()

    def signbuyer(self, escrowid):
        data_file = 'escrow.slv'
        sh = shelve.open(data_file)
        messageText3 = sh[escrowid]
        try:
            start = messageText3.index('{cont2{') + len('{cont2{')
            end = messageText3.index('}cont2}', start)
            fromadd = messageText3[start:end]
        except ValueError:
            error = ''
            fromadd = ""

        fromAddress = fromadd

        try:
            start = messageText3.index('{cont{') + len('{cont{')
            end = messageText3.index('}cont}', start)
            toadd = messageText3[start:end]
        except ValueError:
            error = ''
            toadd = ""

        try:
            start = messageText3.index('{badd1{') + len('{badd1{')
            end = messageText3.index('}badd1}', start)
            badd1 = messageText3[start:end]

        except ValueError:
            error = ''
            badd1 = ""


        try:
            start = messageText3.index('{badd3{') + len('{badd3{')
            end = messageText3.index('}badd3}', start)
            badd3 = messageText3[start:end]
        except ValueError:
            error = ''
            badd3 = ""

        try:
            priv1 = MyForm.conn.dumpprivkey(badd1)
        except:
            priv1 = ""
        try:
            priv3 = MyForm.conn.dumpprivkey(badd3)
        except:
            priv3 = ""

        if priv1!="" and priv3!="":
            toAddress = toadd

            subject = "buer sign escrow deal"
            if toAddress != '':
                status, addressVersionNumber, streamNumber, ripe = decodeAddress(
                    toAddress)
                if status != 'success':
                    with shared.printLock:
                        print 'Error: Could not decode', toAddress, ':', status

                    if status == 'missingbm':
                        self.statusBar().showMessage(_translate(
                            "MainWindow", "Error: Bitmessage addresses start with BM-   Please check %1").arg(toAddress))
                    elif status == 'checksumfailed':
                        self.statusBar().showMessage(_translate(
                            "MainWindow", "Error: The address %1 is not typed or copied correctly. Please check it.").arg(toAddress))
                    elif status == 'invalidcharacters':
                        self.statusBar().showMessage(_translate(
                            "MainWindow", "Error: The address %1 contains invalid characters. Please check it.").arg(toAddress))
                    elif status == 'versiontoohigh':
                        self.statusBar().showMessage(_translate(
                            "MainWindow", "Error: The address version in %1 is too high. Either you need to upgrade your Bitmessage software or your acquaintance is being clever.").arg(toAddress))
                    elif status == 'ripetooshort':
                        self.statusBar().showMessage(_translate(
                            "MainWindow", "Error: Some data encoded in the address %1 is too short. There might be something wrong with the software of your acquaintance.").arg(toAddress))
                    elif status == 'ripetoolong':
                        self.statusBar().showMessage(_translate(
                            "MainWindow", "Error: Some data encoded in the address %1 is too long. There might be something wrong with the software of your acquaintance.").arg(toAddress))
                    else:
                        self.statusBar().showMessage(_translate(
                            "MainWindow", "Error: Something is wrong with the address %1.").arg(toAddress))
                elif fromAddress == '':
                    self.statusBar().showMessage(_translate(
                        "MainWindow", "Error: You must specify a From address. If you don\'t have one, go to the \'Your Identities\' tab."))
                else:
                    toAddress = addBMIfNotPresent(toAddress)
                    if addressVersionNumber > 4 or addressVersionNumber <= 1:
                        QMessageBox.about(self, _translate("MainWindow", "Address version number"), _translate(
                            "MainWindow", "Concerning the address %1, Bitmessage cannot understand address version numbers of %2. Perhaps upgrade Bitmessage to the latest version.").arg(toAddress).arg(str(addressVersionNumber)))
                    if streamNumber > 1 or streamNumber == 0:
                        QMessageBox.about(self, _translate("MainWindow", "Stream number"), _translate("MainWindow", "Concerning the address %1, Bitmessage cannot handle stream numbers of %2. Perhaps upgrade Bitmessage to the latest version.").arg(toAddress).arg(str(streamNumber)))
                    self.statusBar().showMessage('')
                    if shared.statusIconColor == 'red':
                        self.statusBar().showMessage(_translate(
                            "MainWindow", "Warning: You are currently not connected. Bitmessage will do the work necessary to send the message but it won\'t send until you connect."))
                    message0 = sh[escrowid]
                    message = "alfa01"+"{status{"+"started-buyer-7"+"}status}"+ str(message0[37:]) + "{private1{" + str(priv1) +"}private1}"+"{private3{"+ str(priv3) + "}private3}"

                    sh[escrowid] = message
                    sh.sync()
                    ackdata = OpenSSL.rand(32)
                    t = ()
                    sqlExecute(
                        '''INSERT INTO sent VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                        '',
                        toAddress,
                        ripe,
                        fromAddress,
                        subject,
                        message,
                        ackdata,
                        int(time.time()),
                        'msgqueued',
                        1,
                        1,
                        'sent',
                        2)

                    toLabel = ''
                    queryreturn = sqlQuery('''select label from addressbook where address=?''',
                                            toAddress)
                    if queryreturn != []:
                        for row in queryreturn:
                            toLabel, = row

                    self.displayNewSentMessage(
                        toAddress, toLabel, fromAddress, subject, message, ackdata)
                    shared.workerQueue.put(('sendmessage', toAddress))
        sh.close()



    def sndmessage(self,message,subject, fromAddress, toAddress):
        if toAddress != '':
                    status, addressVersionNumber, streamNumber, ripe = decodeAddress(
                        toAddress)
                    if status != 'success':
                        with shared.printLock:
                            print 'Error: Could not decode', toAddress, ':', status

                        if status == 'missingbm':
                            self.statusBar().showMessage(_translate(
                                "MainWindow", "Error: Bitmessage addresses start with BM-   Please check %1").arg(toAddress))
                        elif status == 'checksumfailed':
                            self.statusBar().showMessage(_translate(
                                "MainWindow", "Error: The address %1 is not typed or copied correctly. Please check it.").arg(toAddress))
                        elif status == 'invalidcharacters':
                            self.statusBar().showMessage(_translate(
                                "MainWindow", "Error: The address %1 contains invalid characters. Please check it.").arg(toAddress))
                        elif status == 'versiontoohigh':
                            self.statusBar().showMessage(_translate(
                                "MainWindow", "Error: The address version in %1 is too high. Either you need to upgrade your Bitmessage software or your acquaintance is being clever.").arg(toAddress))
                        elif status == 'ripetooshort':
                            self.statusBar().showMessage(_translate(
                                "MainWindow", "Error: Some data encoded in the address %1 is too short. There might be something wrong with the software of your acquaintance.").arg(toAddress))
                        elif status == 'ripetoolong':
                            self.statusBar().showMessage(_translate(
                                "MainWindow", "Error: Some data encoded in the address %1 is too long. There might be something wrong with the software of your acquaintance.").arg(toAddress))
                        else:
                            self.statusBar().showMessage(_translate(
                                "MainWindow", "Error: Something is wrong with the address %1.").arg(toAddress))
                    elif fromAddress == '':
                        self.statusBar().showMessage(_translate(
                            "MainWindow", "Error: You must specify a From address. If you don\'t have one, go to the \'Your Identities\' tab."))
                    else:
                        toAddress = addBMIfNotPresent(toAddress)
                        if addressVersionNumber > 4 or addressVersionNumber <= 1:
                            QMessageBox.about(self, _translate("MainWindow", "Address version number"), _translate(
                                "MainWindow", "Concerning the address %1, Bitmessage cannot understand address version numbers of %2. Perhaps upgrade Bitmessage to the latest version.").arg(toAddress).arg(str(addressVersionNumber)))
                        if streamNumber > 1 or streamNumber == 0:
                            QMessageBox.about(self, _translate("MainWindow", "Stream number"), _translate("MainWindow", "Concerning the address %1, Bitmessage cannot handle stream numbers of %2. Perhaps upgrade Bitmessage to the latest version.").arg(toAddress).arg(str(streamNumber)))
                        self.statusBar().showMessage('')
                        if shared.statusIconColor == 'red':
                            self.statusBar().showMessage(_translate(
                                "MainWindow", "Warning: You are currently not connected. Bitmessage will do the work necessary to send the message but it won\'t send until you connect."))

                        ackdata = OpenSSL.rand(32)
                        t = ()
                        sqlExecute(
                            '''INSERT INTO sent VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                            '',
                            toAddress,
                            ripe,
                            fromAddress,
                            subject,
                            message,
                            ackdata,
                            int(time.time()),
                            'msgqueued',
                            1,
                            1,
                            'sent',
                            2)

                        toLabel = ''
                        queryreturn = sqlQuery('''select label from addressbook where address=?''',
                                               toAddress)
                        if queryreturn != []:
                            for row in queryreturn:
                                toLabel, = row

                        self.displayNewSentMessage(
                            toAddress, toLabel, fromAddress, subject, message, ackdata)
                        shared.workerQueue.put(('sendmessage', toAddress))

                        self.ui.comboBoxSendFrom.setCurrentIndex(0)
                        self.ui.labelFrom.setText('')
                        self.ui.lineEditTo.setText('')
                        self.ui.lineEditSubject.setText('')
                        self.ui.textEditMessage.setText('')
                        self.ui.tabWidget.setCurrentIndex(2)
                        self.ui.tableWidgetSent.setCurrentCell(0, 0)



    #when buyer canceled deal
    def buyercancel(self, idesc):
        sh = shelve.open("escrow.slv")
        gooo = True
        if sh.has_key(idesc):
            gooo = True
        else:
            gooo = False
        if idesc in sh.keys():
            if sh[idesc][:29] == "alfa01{status{started-buyer-1":
                #sand cancel request to merchant
                message = "alfa01"+"{status{"+"started-buyer10"+"}status}"+ str(sh[idesc][37:])
                text = sh[idesc]

                subject = "Buyer request to cancel deal"
                try:
                    start = text.index('{cont2{') + len('{cont2{')
                    end = text.index('}cont2}', start)
                    fromAddress = text[start:end]
                except ValueError:
                    error=''
                    fromAddress = ""
                try:
                    start = text.index('{cont{') + len('{cont{')
                    end = text.index('}cont}', start)
                    toAddress = text[start:end]
                except ValueError:
                    error=''
                    toAddress = ""
                self.sndmessage(message,subject,fromAddress,toAddress)
                del sh[idesc]
                sh.sync()
                gooo = False
            if gooo:
                if sh[idesc][:29] == "alfa01{status{started-buyer-2":
                    #sand cancel request to merchant
                    message = "alfa01"+"{status{"+"started-buyer20"+"}status}"+ str(sh[idesc][37:])
                    text = sh[idesc]

                    subject = "Buyer request to cancel deal"
                    try:
                        start = text.index('{cont2{') + len('{cont2{')
                        end = text.index('}cont2}', start)
                        fromAddress = text[start:end]
                    except ValueError:
                        error=''
                        fromAddress = ""
                    try:
                        start = text.index('{cont{') + len('{cont{')
                        end = text.index('}cont}', start)
                        toAddress = text[start:end]
                    except ValueError:
                        error=''
                        toAddress = ""
                    self.sndmessage(message,subject,fromAddress,toAddress)
                    del sh[idesc]
                    sh.sync()
                    gooo = False
            if gooo:
                if sh[idesc][:29] == "alfa01{status{started-buyer-3":
                    #sand cancel request to merchant
                    message = "alfa01"+"{status{"+"started-buyer30"+"}status}"+ str(sh[idesc][37:])
                    text = sh[idesc]

                    subject = "Buyer request to cancel deal"
                    try:
                        start = text.index('{cont2{') + len('{cont2{')
                        end = text.index('}cont2}', start)
                        fromAddress = text[start:end]
                    except ValueError:
                        error=''
                        fromAddress = ""
                    try:
                        start = text.index('{cont{') + len('{cont{')
                        end = text.index('}cont}', start)
                        toAddress = text[start:end]
                    except ValueError:
                        error=''
                        toAddress = ""
                    self.sndmessage(message,subject,fromAddress,toAddress)
                    del sh[idesc]
                    sh.sync()
                    chk1 = shelve.open("chk1pay.slv")
                    chk2 = shelve.open("chk2pay.slv")
                    chk3 = shelve.open("chk3pay.slv")
                    try:
                        del chk1[idesc]
                    except:
                        error=""
                    try:
                        del chk2[idesc]
                    except:
                        error=""
                    try:
                        del chk3[idesc]
                    except:
                        error=""
                    chk1.sync()
                    chk2.sync()
                    chk3.sync()
                    chk1.close()
                    chk2.close()
                    chk3.close()
                    gooo = False
            if gooo:
                if sh[idesc][:29] == "alfa01{status{started-buyer-4":
                    #sand cancel request to merchant
                    text = sh[idesc]
                    try:
                        start = text.index('{badd2{') + len('{badd2{')
                        end = text.index('}badd2}', start)
                        baddr2 = text[start:end]
                    except ValueError:
                        error=''
                        baddr2 = ""
                    try:
                        private2 = MyForm.conn.dumpprivkey(baddr2)
                    except:
                        private2 = ""
                    if private2!="":
                        message = "alfa01"+"{status{"+"started-buyer40"+"}status}"+ str(sh[idesc][37:]) +"{private2{"+ str(private2)+"}private2}"

                        subject = "Buyer request to cancel deal"
                        try:
                            start = text.index('{cont2{') + len('{cont2{')
                            end = text.index('}cont2}', start)
                            fromAddress = text[start:end]
                        except ValueError:
                            error=''
                            fromAddress = ""
                        try:
                            start = text.index('{cont{') + len('{cont{')
                            end = text.index('}cont}', start)
                            toAddress = text[start:end]
                        except ValueError:
                            error=''
                            toAddress = ""
                        self.sndmessage(message,subject,fromAddress,toAddress)
                        del sh[idesc]
                        sh.sync()
                        chk1 = shelve.open("chk1pay.slv")
                        chk2 = shelve.open("chk2pay.slv")
                        chk3 = shelve.open("chk3pay.slv")
                        try:
                            del chk1[idesc]
                        except:
                            error=""
                        try:
                            del chk2[idesc]
                        except:
                            error=""
                        try:
                            del chk3[idesc]
                        except:
                            error=""
                        chk1.sync()
                        chk2.sync()
                        chk3.sync()
                        chk1.close()
                        chk2.close()
                        chk3.close()
                        gooo = False
            if gooo:
                if sh[idesc][:29] == "alfa01{status{started-buyer-5":
                    #sand cancel request to merchant
                    text = sh[idesc]
                    try:
                        start = text.index('{badd2{') + len('{badd2{')
                        end = text.index('}badd2}', start)
                        baddr2 = text[start:end]
                    except ValueError:
                        error=''
                        baddr2 = ""
                    try:
                        private2 = MyForm.conn.dumpprivkey(baddr2)
                    except:
                        private2 = ""
                    if private2!="":
                        message = "alfa01"+"{status{"+"started-buyer50"+"}status}"+ str(sh[idesc][37:])+"{private2{"+ str(private2) +"}private2}"

                        subject = "Buyer request to cancel deal"
                        try:
                            start = text.index('{cont2{') + len('{cont2{')
                            end = text.index('}cont2}', start)
                            fromAddress = text[start:end]
                        except ValueError:
                            error=''
                            fromAddress = ""
                        try:
                            start = text.index('{cont{') + len('{cont{')
                            end = text.index('}cont}', start)
                            toAddress = text[start:end]
                        except ValueError:
                            error=''
                            toAddress = ""
                        self.sndmessage(message,subject,fromAddress,toAddress)
                        sh[idesc] = message
                        sh.sync()
                        chk1 = shelve.open("chk1pay.slv")
                        chk2 = shelve.open("chk2pay.slv")
                        chk3 = shelve.open("chk3pay.slv")
                        try:
                            del chk1[idesc]
                        except:
                            error=""
                        try:
                            del chk2[idesc]
                        except:
                            error=""
                        try:
                            del chk3[idesc]
                        except:
                            error=""
                        chk1.sync()
                        chk2.sync()
                        chk3.sync()
                        chk1.close()
                        chk2.close()
                        chk3.close()
            if gooo:
                if sh[idesc][:29] == "alfa01{status{started-buyer-6":
                    #sand cancel request to merchant
                    text = sh[idesc]
                    try:
                        start = text.index('{badd2{') + len('{badd2{')
                        end = text.index('}badd2}', start)
                        baddr = text[start:end]
                    except ValueError:
                        error=''
                        baddr2 = ""
                    try:
                        private2 = MyForm.conn.dumpprivkey(baddr2)
                    except:
                        private2 = ""
                    message = "alfa01"+"{status{"+"started-buyer60"+"}status}"+ str(sh[idesc][37:])

                    subject = "Buyer request to cancel deal"
                    try:
                        start = text.index('{cont2{') + len('{cont2{')
                        end = text.index('}cont2}', start)
                        fromAddress = text[start:end]
                    except ValueError:
                        error=''
                        fromAddress = ""
                    try:
                        start = text.index('{cont{') + len('{cont{')
                        end = text.index('}cont}', start)
                        toAddress = text[start:end]
                    except ValueError:
                        error=''
                        toAddress = ""
                    self.sndmessage(message,subject,fromAddress,toAddress)
                    sh[idesc] = message
                    sh.sync()
                    chk1 = shelve.open("chk1pay.slv")
                    chk2 = shelve.open("chk2pay.slv")
                    chk3 = shelve.open("chk3pay.slv")
                    try:
                        del chk1[idesc]
                    except:
                        error=""
                    try:
                        del chk2[idesc]
                    except:
                        error=""
                    try:
                        del chk3[idesc]
                    except:
                        error=""
                    chk1.sync()
                    chk2.sync()
                    chk3.sync()
                    chk1.close()
                    chk2.close()
                    chk3.close()
        sh.close()
        gooo = True

    #when merchant cancel the deal
    def merchantcencel(self, idesc):
        sh2 = shelve.open("escrowm.slv")
        gooo = True
        if idesc in sh2.keys():
            text = sh2[idesc]
            if sh2[idesc][:29] == "alfa01{status{started-buyer-1":
                #sand cancel request to buyer
                message = "alfa01"+"{status{"+"started-buyer14"+"}status}"+ str(sh2[idesc][37:])
                subject = "Buyer request to cancel deal"
                try:
                    start = text.index('{cont{') + len('{cont{')
                    end = text.index('}cont}', start)
                    fromAddress = text[start:end]
                except ValueError:
                    error=''
                    fromAddress = ""
                try:
                    start = text.index('{cont2{') + len('{cont2{')
                    end = text.index('}cont2}', start)
                    toAddress = text[start:end]
                except ValueError:
                    error=''
                    toAddress = ""
                self.sndmessage(message,subject,fromAddress,toAddress)
                del sh2[idesc]
                chk1 = shelve.open("chk1pay.slv")
                chk2 = shelve.open("chk2pay.slv")
                chk3 = shelve.open("chk3pay.slv")
                try:
                    del chk1[idesc]
                except:
                    error=""
                try:
                    del chk2[idesc]
                except:
                    error=""
                try:
                    del chk3[idesc]
                except:
                    error=""
                chk1.sync()
                chk2.sync()
                chk3.sync()
                chk1.close()
                chk2.close()
                chk3.close()
                sh2.sync()
                gooo = False
            if gooo:
                if sh2[idesc][:29] == "alfa01{status{started-buyer-2":
                    #sand cancel request to merchant
                    try:
                        start = text.index('{maddr1{') + len('{maddr1{')
                        end = text.index('}maddr1}', start)
                        maddr1 = text[start:end]
                    except ValueError:
                        error=''
                        maddr1 = ""
                    try:
                        private1 = MyForm.conn.dumpprivkey(maddr1)
                    except:
                        private1=""
                    try:
                        start = text.index('{maddr3{') + len('{maddr3{')
                        end = text.index('}maddr3}', start)
                        maddr3 = text[start:end]
                    except ValueError:
                        error=''
                        maddr3 = ""
                    try:
                        private3 = MyForm.conn.dumpprivkey(maddr3)
                    except:
                        private3 = ""
                    if private3!="" and private1!="":
                        message = "alfa01" + "{status{" + "started-buyer24" + "}status}" + str(sh2[idesc][37:]) + "{private3{" + str(private3) + "}private3}" + "{private1{" + str(private1) + "}private1}"
                        text = sh2[idesc]

                        subject = "Buyer request to cancel deal"
                        try:
                            start = text.index('{cont{') + len('{cont{')
                            end = text.index('}cont}', start)
                            fromAddress = text[start:end]
                        except ValueError:
                            error=''
                            fromAddress = ""
                        try:
                            start = text.index('{cont2{') + len('{cont2{')
                            end = text.index('}cont2}', start)
                            toAddress = text[start:end]
                        except ValueError:
                            error=''
                            toAddress = ""
                        self.sndmessage(message,subject,fromAddress,toAddress)
                        del sh2[idesc]
                        chk1 = shelve.open("chk1pay.slv")
                        chk2 = shelve.open("chk2pay.slv")
                        chk3 = shelve.open("chk3pay.slv")
                        try:
                            del chk1[idesc]
                        except:
                            error=""
                        try:
                            del chk2[idesc]
                        except:
                            error=""
                        try:
                            del chk3[idesc]
                        except:
                            error=""
                        chk1.sync()
                        chk2.sync()
                        chk3.sync()
                        chk1.close()
                        chk2.close()
                        chk3.close()
                        sh2.sync()
                        gooo = False
            if gooo:
                if sh2[idesc][:29] == "alfa01{status{started-buyer-3":
                    #sand cancel request to merchant
                    try:
                        start = text.index('{maddr1{') + len('{maddr1{')
                        end = text.index('}maddr1}', start)
                        maddr1 = text[start:end]
                    except ValueError:
                        error=''
                        maddr1 = ""
                    try:
                        private1 = MyForm.conn.dumpprivkey(maddr1)
                    except:
                        private1 = ""
                    try:
                        start = text.index('{maddr3{') + len('{maddr3{')
                        end = text.index('}maddr3}', start)
                        maddr3 = text[start:end]
                    except ValueError:
                        error=''
                        maddr3 = ""
                    try:
                        private3 = MyForm.conn.dumpprivkey(maddr3)
                    except:
                        private3 = ""
                    if private1!="" and private3!="":
                        message = "alfa01"+"{status{"+"started-buyer34"+"}status}" + str(sh2[idesc][37:]) + "{private3{"+ str(private3)+ "}private3}" + "{private1{" + str(private1) + "}private1}"
                        text = sh2[idesc]

                        subject = "Buyer request to cancel deal"
                        try:
                            start = text.index('{cont2{') + len('{cont2{')
                            end = text.index('}cont2}', start)
                            fromAddress = text[start:end]
                        except ValueError:
                            error=''
                            fromAddress = ""
                        try:
                            start = text.index('{cont{') + len('{cont{')
                            end = text.index('}cont}', start)
                            toAddress = text[start:end]
                        except ValueError:
                            error=''
                            toAddress = ""
                        self.sndmessage(message,subject,fromAddress,toAddress)
                        del sh2[idesc]
                        chk1 = shelve.open("chk1pay.slv")
                        chk2 = shelve.open("chk2pay.slv")
                        chk3 = shelve.open("chk3pay.slv")
                        try:
                            del chk1[idesc]
                        except:
                            error=""
                        try:
                            del chk2[idesc]
                        except:
                            error=""
                        try:
                            del chk3[idesc]
                        except:
                            error=""
                        chk1.sync()
                        chk2.sync()
                        chk3.sync()
                        chk1.close()
                        chk2.close()
                        chk3.close()
                        sh2.sync()
                        gooo = False
            if gooo:
                if sh2[idesc][:29] == "alfa01{status{started-buyer-4":
                    #sand cancel request to merchant
                    text = sh2[idesc]
                    try:
                        start = text.index('{maddr1{') + len('{maddr1{')
                        end = text.index('}maddr1}', start)
                        maddr1 = text[start:end]
                    except ValueError:
                        error=''
                        maddr1 = ""
                    try:
                        private1 = MyForm.conn.dumpprivkey(maddr1)
                    except:
                        private1 = ""
                    try:
                        start = text.index('{maddr3{') + len('{maddr3{')
                        end = text.index('}maddr3}', start)
                        maddr3 = text[start:end]
                    except ValueError:
                        error=''
                        maddr3 = ""
                    try:
                        private3 = MyForm.conn.dumpprivkey(maddr3)
                    except:
                        private3 = ""
                    if private1!="" and private3!="":
                        message = "alfa01"+"{status{"+"started-buyer44"+"}status}"+ str(sh2[idesc][37:])+"{private3{" + str(private3) + "}private3}" + "{private1{" + str(private1) + "}private1}"

                        subject = "Buyer request to cancel deal"
                        try:
                            start = text.index('{cont{') + len('{cont{')
                            end = text.index('}cont}', start)
                            fromAddress = text[start:end]
                        except ValueError:
                            error=''
                            fromAddress = ""
                        try:
                            start = text.index('{cont2{') + len('{cont2{')
                            end = text.index('}cont2}', start)
                            toAddress = text[start:end]
                        except ValueError:
                            error=''
                            toAddress = ""
                        self.sndmessage(message,subject,fromAddress,toAddress)
                        sh2[idesc]=message
                        chk1 = shelve.open("chk1pay.slv")
                        chk2 = shelve.open("chk2pay.slv")
                        chk3 = shelve.open("chk3pay.slv")
                        try:
                            del chk1[idesc]
                        except:
                            error=""
                        try:
                            del chk2[idesc]
                        except:
                            error=""
                        try:
                            del chk3[idesc]
                        except:
                            error=""
                        chk1.sync()
                        chk2.sync()
                        chk3.sync()
                        chk1.close()
                        chk2.close()
                        chk3.close()
                        sh2.sync()
            if gooo:
                if sh2[idesc][:29] == "alfa01{status{started-buyer-5":
                    #sand cancel request to merchant
                    text = sh2[idesc]
                    try:
                        start = text.index('{maddr1{') + len('{maddr1{')
                        end = text.index('}maddr1}', start)
                        maddr1 = text[start:end]
                    except ValueError:
                        error=''
                        maddr1 = ""
                    try:
                        private1 = MyForm.conn.dumpprivkey(maddr1)
                    except:
                        private1 = ""
                    try:
                        start = text.index('{maddr3{') + len('{maddr3{')
                        end = text.index('}maddr3}', start)
                        maddr3 = text[start:end]
                    except ValueError:
                        error=''
                        maddr3 = ""
                    try:
                        private3 = MyForm.conn.dumpprivkey(maddr3)
                    except:
                        private3 = ""
                    if private1!="" and private3!="":
                        message = "alfa01"+"{status{"+"started-buyer54"+"}status}"+ str(sh2[idesc][37:])+"{private3{" + str(private3) + "}private3}"+"{private1{" + str(private1) + "}private1}"

                        subject = "Buyer request to cancel deal"
                        try:
                            start = text.index('{cont2{') + len('{cont2{')
                            end = text.index('}cont2}', start)
                            fromAddress = text[start:end]
                        except ValueError:
                            error=''
                            fromAddress = ""
                        try:
                            start = text.index('{cont{') + len('{cont{')
                            end = text.index('}cont}', start)
                            toAddress = text[start:end]
                        except ValueError:
                            error=''
                            toAddress = ""
                        self.sndmessage(message,subject,fromAddress,toAddress)
                        sh2[idesc] = message
                        chk1 = shelve.open("chk1pay.slv")
                        chk2 = shelve.open("chk2pay.slv")
                        chk3 = shelve.open("chk3pay.slv")
                        try:
                            del chk1[idesc]
                        except:
                            error=""
                        try:
                            del chk2[idesc]
                        except:
                            error=""
                        try:
                            del chk3[idesc]
                        except:
                            error=""
                        chk1.sync()
                        chk2.sync()
                        chk3.sync()
                        chk1.close()
                        chk2.close()
                        chk3.close()
                        sh2.sync()
                if sh2[idesc][:29] == "alfa01{status{started-buyer-6":
                    #sand cancel request to merchant
                    text = sh2[idesc]
                    try:
                        start = text.index('{maddr1{') + len('{maddr1{')
                        end = text.index('}maddr1}', start)
                        maddr1 = text[start:end]
                    except ValueError:
                        error=''
                        maddr1 = ""
                    try:
                        private1 = MyForm.conn.dumpprivkey(maddr1)
                    except:
                        private1 = ""
                    try:
                        start = text.index('{maddr3{') + len('{maddr3{')
                        end = text.index('}maddr3}', start)
                        maddr3 = text[start:end]
                    except ValueError:
                        error=''
                        maddr3 = ""
                    try:
                        private3 = MyForm.conn.dumpprivkey(maddr3)
                    except:
                        private3 = ""

                    if private1!="" and private3!="":
                        message = "alfa01"+"{status{"+"started-buyer64"+"}status}"+ str(sh2[idesc][37:])+"{private3{" + str(private3) + "}private3}"+"{private1{" + str(private1) + "}private1}"

                        subject = "Buyer request to cancel deal"
                        try:
                            start = text.index('{cont2{') + len('{cont2{')
                            end = text.index('}cont2}', start)
                            fromAddress = text[start:end]
                        except ValueError:
                            error=''
                            fromAddress = ""
                        try:
                            start = text.index('{cont{') + len('{cont{')
                            end = text.index('}cont}', start)
                            toAddress = text[start:end]
                        except ValueError:
                            error=''
                            toAddress = ""
                        self.sndmessage(message,subject,fromAddress,toAddress)
                        sh2[idesc] = message
                        sh2.sync()
                        chk1 = shelve.open("chk1pay.slv")
                        chk2 = shelve.open("chk2pay.slv")
                        chk3 = shelve.open("chk3pay.slv")
                        try:
                            del chk1[idesc]
                        except:
                            error=""
                        try:
                            del chk2[idesc]
                        except:
                            error=""
                        try:
                            del chk3[idesc]
                        except:
                            error=""
                        chk1.sync()
                        chk2.sync()
                        chk3.sync()
                        chk1.close()
                        chk2.close()
                        chk3.close()
        sh2.close()
        self.rendertextbrowser3()


    #resend for buyer if something go wrong

    def resendbuyer(self, idesc):
        sh = shelve.open("escrow.slv")
        if sh.has_key(idesc):
            if sh[idesc][:29] == "alfa01{status{started-buyer-3" or "alfa01{status{started-buyer04":
                blc=0
                txid=""
                try:
                    blc=MyForm.conn.getbalance()
                except:
                    blc=0
                sendResult1=False
                try:
                    start = sh[idesc].index('{escrowaddr1{') + len('{escrowaddr1{')
                    end = sh[idesc].index('}escrowaddr1}', start)
                    esc1 = sh[idesc][start:end]
                except ValueError:
                    error = ''
                    esc1=""
                try:
                    start = sh[idesc].index('{cont2{') + len('{cont2{')
                    end = sh[idesc].index('}cont2}', start)
                    fromAddress = sh[idesc][start:end]
                except ValueError:
                    error = ''
                    fromAddress=""
                try:
                    start = sh[idesc].index('{cont{') + len('{cont{')
                    end = sh[idesc].index('}cont}', start)
                    toAddress = sh[idesc][start:end]
                except ValueError:
                    error = ''
                    toAddress=""
                try:
                    start = sh[idesc].index('{amount{') + len('{amount{')
                    end = sh[idesc].index('}amount}', start)
                    amount11 = sh[idesc][start:end]
                except ValueError:
                    error = ''
                    amount11=""
                try:
                    txid=MyForm.conn.sendtoaddress(esc1,float(amount11)*0.05)
                    sendResult1=True
                except:
                    sendResult1=False

                if sendResult1 and txid != "":
                    messageesc = "alfa01"+"{status{"+"started-buyer-4"+"}status}"+ str(sh[idesc][37:])+"{txid1{"+ str(txid)+"}txid1}"
                    sh[idesc] = messageesc
                    sh.sync()
                    self.buyerpay1(messageesc, toAddress, fromAddress)

                elif blc < float(amount11)*0.05:
                    self.statusBar().showMessage(_translate(
                        "MainWindow", "Insufficient funds! You can try pay manualy."))
                    messageesc = "alfa01"+"{status{"+"started-buyer04"+"}status}" + str(sh[idesc][37:])
                    sh[idesc] = messageesc
                    sh.sync()

                else:
                    messageesc = "alfa01"+"{status{"+"started-buyer04"+"}status}"+str(sh[idesc][37:])
                    sh[idesc] = messageesc
                    sh.sync()
                    self.statusBar().showMessage(_translate(
                        "MainWindow", "Warning: Bitcoin error. Try to restart bitcoin client."))
                sh.sync()
                self.rendertextbrowser2()
        sh.close()

    def resendmerchant(self, idesc):
        sh2 = shelve.open("escrowm.slv")
        chk1payment = shelve.open("chk1payment.slv")
        if sh2.has_key(idesc):
            if sh2[idesc][:29] == "alfa01{status{started-buyer05":
                txid=""
                try:
                    start = messageText2.index('{amount{') + len('{amount{')
                    end = messageText2.index('}amount}', start)
                    amount15 = messageText2[start:end]
                except ValueError:
                    error = ''
                    amount15=""
                try:
                    start = messageText2.index('{cont2{') + len('{cont2{')
                    end = messageText2.index('}cont2}', start)
                    toadd = messageText2[start:end]
                except ValueError:
                    error = ''
                try:
                    start = messageText2.index('{cont{') + len('{cont{')
                    end = messageText2.index('}cont}', start)
                    fromadd = messageText2[start:end]
                except ValueError:
                    error = ''
                try:
                    start = messageText2.index('{escrowaddr2{') + len('{escrowaddr2{')
                    end = messageText2.index('}escrowaddr2}', start)
                    esc2 = messageText2[start:end]
                except ValueError:
                    error = ''
                    esc2=""
                try:
                    start = messageText2.index('{escrowaddr3{') + len('{escrowaddr3{')
                    end = messageText2.index('}escrowaddr3}', start)
                    esc3 = messageText2[start:end]
                except ValueError:
                    error = ''
                    esc3=""
                try:
                    txid2 = MyForm.conn.sendtoaddress(esc2, float(amount15)*0.05)
                except:
                    error = ""
                    txid2 = ""

                if txid2 != "":
                    message = "alfa01"+"{status{"+"started-buyer-5"+"}status}"+ str(messageText2[37:]) + "{txid2{"+str(txid2)+"}txid2}"
                    sh2[key] = message
                    self.buyerpay1(message, toadd, fromadd)
                    del chk1payment[key]
                    chk1payment.sync()
                else:
                    message = "alfa01"+"{status{"+"started-buyer05"+"}status}"+str(messageText2[37:])
                    sh2[key] = message
                sh2.sync()
                self.rendertextbrowser3()
        sh2.close()
        chk1payment.close()

    def resendbuyer2(self, idesc):
        sh = shelve.open("escrow.slv")
        chk2payment = shelve.open("chk2payment.slv")
        if sh.has_key(idesc):
            if sh[idesc][:29] == "alfa01{status{started-buyer06":
                try:
                    start = messageText2.index('{amount{') + len('{amount{')
                    end = messageText2.index('}amount}', start)
                    amount15 = messageText2[start:end]
                except ValueError:
                    error = ''
                    amount15=""
                try:
                    start = messageText2.index('{id{') + len('{id{')
                    end = messageText2.index('}id}', start)
                    accnt = messageText2[start:end]
                except ValueError:
                    error = ''
                    accnt=""
                try:
                    start = messageText2.index('{cont2{') + len('{cont2{')
                    end = messageText2.index('}cont2}', start)
                    toadd = messageText2[start:end]
                except ValueError:
                    error = ''
                try:
                    start = messageText2.index('{cont{') + len('{cont{')
                    end = messageText2.index('}cont}', start)
                    fromadd = messageText2[start:end]
                except ValueError:
                    error = ''
                try:
                    start = messageText2.index('{escrowaddr2{') + len('{escrowaddr2{')
                    end = messageText2.index('}escrowaddr2}', start)
                    esc2 = messageText2[start:end]
                except ValueError:
                    error = ''
                    esc2=""
                try:
                    start = messageText2.index('{escrowaddr3{') + len('{escrowaddr3{')
                    end = messageText2.index('}escrowaddr3}', start)
                    esc3 = messageText2[start:end]
                except ValueError:
                    error = ''
                    esc3=""
                try:
                    txid3 = MyForm.conn.sendtoaddress(esc3, float(amount15))
                except:
                    error = ""
                    txid3 = ""

                if txid3 != "":
                    message = "alfa01"+"{status{"+"started-buyer-6"+"}status}"+ str(messageText2[37:])+"{txid3{"+str(txid3)+"}txid3}"
                    sh[key] = message
                    sh.sync()
                    self.buyerpay1(message, fromadd, toadd)
                    del chk2payment[key]
                    chk2payment.sync()

                else:
                    message = "alfa01" + "{status{" + "started-buyer06" + "}status}" + str(messageText2[37:])
                    sh[key] = message
                    sh.sync()

                self.rendertextbrowser2()
        sh.close()
        chk2payment.close()



    #links in trade board
    def on_anchor_clicked3(self,url):
        text = str(url.toString().toUtf8())
        if text.startswith('#contact#'):
            try:
                start = text.index('#contact#') + len('#contact#')
                contct = text[start:]
            except ValueError:
                contct = ""
            if contct!="":
                self.ui.tabWidget_2.setCurrentIndex(3)
                self.ui.tabWidget.setCurrentIndex(1)
                self.ui.lineEditTo.setText(contct)
        if text.startswith('#Buy#'):
            try:
                start = text.index('#Buy#') + len('#Buy#')
                end = text.index("|", start)
                price = text[end+1:]
                buy = text[start:end]
            except ValueError:
                buy = ""
                price = ""
            if buy!="":
                self.ui.tabWidget_2.setCurrentIndex(1)
                self.ui.tabWidget_3.setCurrentIndex(0)
                self.ui.lineEdit_2.setText(buy)
                pri = float(price)
                self.ui.spinBox_2.setValue(pri)
        if text.startswith('#more#'):
            try:
                start = text.index('#more#') + len('#more#')
                end = text.index("|", start)
                category = text[end+1:]
                more = text[start:end]
            except ValueError:
                more = ""
                category = ""
            if more!="" and len(more)<250001:
                if category=="G":
                    g = shelve.open("board-goods.slv")
                    g.close()
                elif category=="S":
                    s = shelve.open("board-services.slv")
                    s.close()
                elif category=="C":
                    c = shelve.open("board-currencies.slv")
                    c.close()

    #links in escrow browser actions
    def on_anchor_clicked(self,url):
        self.ui.textBrowser_2.setHtml("Wait please...")
        text = str(url.toString().toUtf8())
        if text.startswith('#contact#'):
            try:
                start = text.index('#contact#') + len('#contact#')
                contct = text[start:]
            except ValueError:
                contct = ""
            if contct!="":
                self.ui.tabWidget_2.setCurrentIndex(3)
                self.ui.tabWidget.setCurrentIndex(1)
                self.ui.lineEditTo.setText(contct)
        if text.startswith('#sign'):
            try:
                start = text.index('{') + len('}')
                end = text.index('}', start)
                escrowid = text[start:end]
            except ValueError:
                error=''
                escrowid = ""
            if escrowid != "":
                self.signbuyer(escrowid)
                self.ui.textBrowser_2.setHtml('Deal just signed. That mean deal successfully ended. Few minutes need for make necessary actions. Wait for deposit. <a href="#back">Back to deal browser</a>')
        if text.startswith('#cancel'):
            try:
                start = text.index('#cancel#') + len('#cancel#')
                idesc = text[start:]
            except ValueError:
                error=""
                idesc=""
            if idesc!="":
                self.buyercancel(idesc)
                self.ui.textBrowser_2.setHtml('Deal just canceled. Wait for merchant`s answer and your deposit. <a href="#back">Back to deal browser</a>')
        if text.startswith('#resend'):
            try:
                start = text.index('#resend#') + len('#resend#')
                idesc = text[start:]
            except ValueError:
                error=""
                idesc=""
            if idesc!="":
                self.resendbuyer(idesc)

        if text.startswith('#3resend'):
            try:
                start = text.index('#3resend#') + len('#3resend#')
                idesc = text[start:]
            except ValueError:
                error=""
                idesc=""
            if idesc!="":
                self.resendbuyer2(idesc)
        if text.startswith('#back'):
            self.ui.textBrowser_2.setHtml(MyForm.textbro2html)
        self.rendertextbrowser2()
        self.rendertextbrowser3()

    def on_anchor_clicked2(self,url):
        self.ui.textBrowser_3.setHtml("Wait please...")
        text = str(url.toString().toUtf8())
        if text.startswith('#contact#'):
            try:
                start = text.index('#contact#') + len('#contact#')
                contct = text[start:]
            except ValueError:
                contct = ""
            if contct!="":
                self.ui.tabWidget_2.setCurrentIndex(3)
                self.ui.tabWidget.setCurrentIndex(1)
                self.ui.lineEditTo.setText(contct)
        if text.startswith('#2resend'):
            try:
                start = text.index('#2resend#') + len('#2resend#')
                idesc = text[start:]
            except ValueError:
                error=""
                idesc=""
            if idesc!="":
                self.resendmerchant(idesc)
        if text.startswith('#accept'):
            try:
                start = text.index('#addrbuyer=') + len('#addrbuyer=')
                end = text.index('#addrmerchant=', start)
                addrbuyer = text[start:end]
            except ValueError:
                error=''
            try:
                start = text.index('#addrmerchant=') + len('#addrmerchant=')
                end = text.index('#buy1=', start)
                addrmerchant = text[start:end]
            except ValueError:
                error=''
            try:
                start = text.index('#buy1=') + len('#buy1=')
                end = text.index('#buy2=', start)
                buy1 = text[start:end]
            except ValueError:
                error=''
            try:
                start = text.index('#buy2=') + len('#buy2=')
                end = text.index('#buy3=', start)
                buy2 = text[start:end]
            except ValueError:
                error=''
            try:
                start = text.index('#buy3=') + len('#buy3=')
                end = text.index('#idescrow=', start)
                buy3 = text[start:end]
            except ValueError:
                error=''
            try:
                start = text.index('#idescrow=') + len('#idescrow=')
                end = text.index('#amount=', start)
                idescrow = text[start:end]
            except ValueError:
                error=''
            try:
                start = text.index('#amount=') + len('#amount=')
                end = text.index('#lbl=', start)
                amount = text[start:end]
            except ValueError:
                error=''
            try:
                start = text.index('#lbl=') + len('#lbl=')
                lbl = text[start:]
            except ValueError:
                error=''
                lbl=""
            if lbl=="":
                lbl = addrbuyer
            if len(lbl)>50:
                lbl=lbl[:50]

            if MyForm.balance>=float(amount)*0.05+0.0002:
                self.merchantreply(addrbuyer, addrmerchant, buy1, buy2, buy3, idescrow, amount, lbl)
            else:
                self.statusBar().showMessage(_translate("MainWindow", "Error: Insufficient founds. For complete deal you need "+str(amount*1.05+0.0002)))

        if text.startswith('#sign'):
            self.ui.textBrowser_3.setHtml('Deal just signed. That mean deal successfully ended. Wait for deposit. <a href="#back">Back to deal browser</a>')
        if text.startswith('#cancel'):
            try:
                start = text.index('#cancel#') + len('#cancel#')
                idesc = text[start:]
            except ValueError:
                error=""
                idesc=""
            if idesc!="":
                self.merchantcencel(idesc)
                self.ui.textBrowser_3.setHtml('Deal just canceled. Wait for merchant`s answer and your deposit. <a href="#back">Back to deal browser</a>')
        if text.startswith('#confirm'):
            self.ui.textBrowser_3.setHtml('Deal just confirmed <a href="#back">Back to deal browser</a>')
        if text.startswith('#back'):
            self.ui.textBrowser_3.setHtml(MyForm.textbro2html2)
        if text.startswith('#agree'):
            try:
                start = text.index('#id=') + len('#id=')
                ides = text[start:]
            except ValueError:
                error=''
            sh2 = shelve.open("escrowm.slv")
            text = sh2[ides]
            sh2.close()
            try:
                start = text.index('{cont{') + len('{cont{')
                end = text.index('}cont}', start)
                cont = text[start:end]
            except ValueError:
                error=''
                cont=""
            try:
                start = text.index('{cont2{') + len('{cont2{')
                end = text.index('}cont2}', start)
                cont2 = text[start:end]
            except ValueError:
                error=''
                cont2=""
            self.sndmessage(str(sh2[ides]),"merchant agree".encode("utf-8"),cont.encode("utf-8"),cont2.encode("utf-8"))
        self.rendertextbrowser2()
        self.rendertextbrowser3()


    #check if bad chars in escrow/trade message
    def onlygoodsymbols(self, symbol):
        if any(c in symbol for c in ( '#' ,  '\\'  , '[' , ']' , '{' , '}'  , '|' , '>' , '<' , 'href'  , '=')):
            return False
        else:
            return True

    # create application indicator
    def appIndicatorInit(self, app):
        self.initTrayIcon("can-icon-24px-red.png", app)
        if sys.platform[0:3] == 'win':
            traySignal = "activated(QSystemTrayIcon::ActivationReason)"
            QtCore.QObject.connect(self.tray, QtCore.SIGNAL(
                traySignal), self.__icon_activated)

        m = QMenu()

        self.actionStatus = QtGui.QAction(_translate(
            "MainWindow", "Not Connected"), m, checkable=False)
        m.addAction(self.actionStatus)

        # separator
        actionSeparator = QtGui.QAction('', m, checkable=False)
        actionSeparator.setSeparator(True)
        m.addAction(actionSeparator)

        # show bitmessage
        self.actionShow = QtGui.QAction(_translate(
            "MainWindow", "Show Bitmessage"), m, checkable=True)
        self.actionShow.setChecked(not shared.config.getboolean(
            'bitmessagesettings', 'startintray'))
        self.actionShow.triggered.connect(self.appIndicatorShowOrHideWindow)
        if not sys.platform[0:3] == 'win':
            m.addAction(self.actionShow)

        # Send
        actionSend = QtGui.QAction(_translate(
            "MainWindow", "Send"), m, checkable=False)
        actionSend.triggered.connect(self.appIndicatorSend)
        m.addAction(actionSend)

        # Subscribe
        actionSubscribe = QtGui.QAction(_translate(
            "MainWindow", "Subscribe"), m, checkable=False)
        actionSubscribe.triggered.connect(self.appIndicatorSubscribe)
        m.addAction(actionSubscribe)

        # Address book
        actionAddressBook = QtGui.QAction(_translate(
            "MainWindow", "Address Book"), m, checkable=False)
        actionAddressBook.triggered.connect(self.appIndicatorAddressBook)
        m.addAction(actionAddressBook)

        # separator
        actionSeparator = QtGui.QAction('', m, checkable=False)
        actionSeparator.setSeparator(True)
        m.addAction(actionSeparator)

        # Quit
        m.addAction(_translate(
            "MainWindow", "Quit"), self.quit)

        self.tray.setContextMenu(m)
        self.tray.show()

    # Ubuntu Messaging menu object
    mmapp = None

    # is the operating system Ubuntu?
    def isUbuntu(self):
        for entry in platform.uname():
            if "Ubuntu" in entry:
                return True
        return False

    # When an unread inbox row is selected on then clear the messaging menu
    def ubuntuMessagingMenuClear(self, inventoryHash):
        global withMessagingMenu

        # if this isn't ubuntu then don't do anything
        if not self.isUbuntu():
            return

        # has messageing menu been installed
        if not withMessagingMenu:
            return

        # if there are no items on the messaging menu then
        # the subsequent query can be avoided
        if not (self.mmapp.has_source("Subscriptions") or self.mmapp.has_source("Messages")):
            return

        queryreturn = sqlQuery(
            '''SELECT toaddress, read FROM inbox WHERE msgid=?''', inventoryHash)
        for row in queryreturn:
            toAddress, read = row
            if not read:
                if toAddress == self.str_broadcast_subscribers:
                    if self.mmapp.has_source("Subscriptions"):
                        self.mmapp.remove_source("Subscriptions")
                else:
                    if self.mmapp.has_source("Messages"):
                        self.mmapp.remove_source("Messages")

    # returns the number of unread messages and subscriptions
    def getUnread(self):
        unreadMessages = 0
        unreadSubscriptions = 0

        queryreturn = sqlQuery(
            '''SELECT msgid, toaddress, read FROM inbox where folder='inbox' ''')
        for row in queryreturn:
            msgid, toAddress, read = row

            try:
                if toAddress == self.str_broadcast_subscribers:
                    toLabel = self.str_broadcast_subscribers
                else:
                    toLabel = shared.config.get(toAddress, 'label')
            except:
                toLabel = ''
            if toLabel == '':
                toLabel = toAddress

            if not read:
                if toLabel == self.str_broadcast_subscribers:
                    # increment the unread subscriptions
                    unreadSubscriptions = unreadSubscriptions + 1
                else:
                    # increment the unread messages
                    unreadMessages = unreadMessages + 1
        return unreadMessages, unreadSubscriptions

    # show the number of unread messages and subscriptions on the messaging
    # menu
    def ubuntuMessagingMenuUnread(self, drawAttention):
        unreadMessages, unreadSubscriptions = self.getUnread()
        # unread messages
        if unreadMessages > 0:
            self.mmapp.append_source(
                "Messages", None, "Messages (" + str(unreadMessages) + ")")
            if drawAttention:
                self.mmapp.draw_attention("Messages")

        # unread subscriptions
        if unreadSubscriptions > 0:
            self.mmapp.append_source("Subscriptions", None, "Subscriptions (" + str(
                unreadSubscriptions) + ")")
            if drawAttention:
                self.mmapp.draw_attention("Subscriptions")

    # initialise the Ubuntu messaging menu
    def ubuntuMessagingMenuInit(self):
        global withMessagingMenu

        # if this isn't ubuntu then don't do anything
        if not self.isUbuntu():
            return

        # has messageing menu been installed
        if not withMessagingMenu:
            print 'WARNING: MessagingMenu is not available.  Is libmessaging-menu-dev installed?'
            return

        # create the menu server
        if withMessagingMenu:
            try:
                self.mmapp = MessagingMenu.App(
                    desktop_id='pybitmessage.desktop')
                self.mmapp.register()
                self.mmapp.connect('activate-source', self.appIndicatorInbox)
                self.ubuntuMessagingMenuUnread(True)
            except Exception:
                withMessagingMenu = False
                print 'WARNING: messaging menu disabled'

    # update the Ubuntu messaging menu
    def ubuntuMessagingMenuUpdate(self, drawAttention, newItem, toLabel):
        global withMessagingMenu

        # if this isn't ubuntu then don't do anything
        if not self.isUbuntu():
            return

        # has messageing menu been installed
        if not withMessagingMenu:
            print 'WARNING: messaging menu disabled or libmessaging-menu-dev not installed'
            return

        # remember this item to that the messaging menu can find it
        if toLabel == self.str_broadcast_subscribers:
            self.newBroadcastItem = newItem
        else:
            self.newMessageItem = newItem

        # Remove previous messages and subscriptions entries, then recreate them
        # There might be a better way to do it than this
        if self.mmapp.has_source("Messages"):
            self.mmapp.remove_source("Messages")

        if self.mmapp.has_source("Subscriptions"):
            self.mmapp.remove_source("Subscriptions")

        # update the menu entries
        self.ubuntuMessagingMenuUnread(drawAttention)

    # returns true if the given sound category is a connection sound
    # rather than a received message sound
    def isConnectionSound(self, category):
        if (category is self.SOUND_CONNECTED or
            category is self.SOUND_DISCONNECTED or
            category is self.SOUND_CONNECTION_GREEN):
            return True
        return False

    # play a sound
    def playSound(self, category, label):
        # filename of the sound to be played
        soundFilename = None

        # whether to play a sound or not
        play = True

        # if the address had a known label in the address book
        if label is not None:
            # Does a sound file exist for this particular contact?
            if (os.path.isfile(shared.appdata + 'sounds/' + label + '.wav') or
                os.path.isfile(shared.appdata + 'sounds/' + label + '.mp3')):
                soundFilename = shared.appdata + 'sounds/' + label

        # Avoid making sounds more frequently than the threshold.
        # This suppresses playing sounds repeatedly when there
        # are many new messages
        if (soundFilename is None and
            not self.isConnectionSound(category)):
            # elapsed time since the last sound was played
            dt = datetime.datetime.now() - self.lastSoundTime
            # suppress sounds which are more frequent than the threshold
            if dt.total_seconds() < self.maxSoundFrequencySec:
                play = False

        if soundFilename is None:
            # the sound is for an address which exists in the address book
            if category is self.SOUND_KNOWN:
                soundFilename = shared.appdata + 'sounds/known'
            # the sound is for an unknown address
            elif category is self.SOUND_UNKNOWN:
                soundFilename = shared.appdata + 'sounds/unknown'
            # initial connection sound
            elif category is self.SOUND_CONNECTED:
                soundFilename = shared.appdata + 'sounds/connected'
            # disconnected sound
            elif category is self.SOUND_DISCONNECTED:
                soundFilename = shared.appdata + 'sounds/disconnected'
            # sound when the connection status becomes green
            elif category is self.SOUND_CONNECTION_GREEN:
                soundFilename = shared.appdata + 'sounds/green'            

        if soundFilename is not None and play is True:
            if not self.isConnectionSound(category):
                # record the last time that a received message sound was played
                self.lastSoundTime = datetime.datetime.now()

            # if not wav then try mp3 format
            if not os.path.isfile(soundFilename + '.wav'):
                soundFilename = soundFilename + '.mp3'
            else:
                soundFilename = soundFilename + '.wav'

            if os.path.isfile(soundFilename):
                if 'linux' in sys.platform:
                    # Note: QSound was a nice idea but it didn't work
                    if '.mp3' in soundFilename:
                        gst_available=False
                        try:
                            subprocess.call(["gst123", soundFilename],
                                            stdin=subprocess.PIPE, 
                                            stdout=subprocess.PIPE)
                            gst_available=True
                        except:
                            print "WARNING: gst123 must be installed in order to play mp3 sounds"
                        if not gst_available:
                            try:
                                subprocess.call(["mpg123", soundFilename],
                                                stdin=subprocess.PIPE, 
                                                stdout=subprocess.PIPE)
                                gst_available=True
                            except:
                                print "WARNING: mpg123 must be installed in order to play mp3 sounds"
                    else:
                        try:
                            subprocess.call(["aplay", soundFilename],
                                            stdin=subprocess.PIPE, 
                                            stdout=subprocess.PIPE)
                        except:
                            print "WARNING: aplay must be installed in order to play WAV sounds"
                elif sys.platform[0:3] == 'win':
                    # use winsound on Windows
                    import winsound
                    winsound.PlaySound(soundFilename, winsound.SND_FILENAME)

    # initialise the message notifier
    def notifierInit(self):
        global withMessagingMenu
        if withMessagingMenu:
            Notify.init('pybitmessage')

    # shows a notification
    def notifierShow(self, title, subtitle, fromCategory, label):
        global withMessagingMenu

        self.playSound(fromCategory, label);

        if withMessagingMenu:
            n = Notify.Notification.new(
                title, subtitle, 'notification-message-email')
            try:
                n.show()
            except:
                # n.show() has been known to throw this exception:
                # gi._glib.GError: GDBus.Error:org.freedesktop.Notifications.
                # MaxNotificationsExceeded: Exceeded maximum number of
                # notifications
                pass
            return
        else:
            self.tray.showMessage(title, subtitle, 1, 2000)

    def tableWidgetInboxKeyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Delete:
            self.on_action_InboxTrash()
        return QtGui.QTableWidget.keyPressEvent(self.ui.tableWidgetInbox, event)

    def tableWidgetSentKeyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Delete:
            self.on_action_SentTrash()
        return QtGui.QTableWidget.keyPressEvent(self.ui.tableWidgetSent, event)

    def click_actionManageKeys(self):
        if 'darwin' in sys.platform or 'linux' in sys.platform:
            if shared.appdata == '':
                # reply = QtGui.QMessageBox.information(self, 'keys.dat?','You
                # may manage your keys by editing the keys.dat file stored in
                # the same directory as this program. It is important that you
                # back up this file.', QMessageBox.Ok)
                reply = QtGui.QMessageBox.information(self, 'keys.dat?', _translate(
                    "MainWindow", "You may manage your keys by editing the keys.dat file stored in the same directory as this program. It is important that you back up this file."), QMessageBox.Ok)

            else:
                QtGui.QMessageBox.information(self, 'keys.dat?', _translate(
                    "MainWindow", "You may manage your keys by editing the keys.dat file stored in\n %1 \nIt is important that you back up this file.").arg(shared.appdata), QMessageBox.Ok)
        elif sys.platform == 'win32' or sys.platform == 'win64':
            if shared.appdata == '':
                reply = QtGui.QMessageBox.question(self, _translate("MainWindow", "Open keys.dat?"), _translate(
                    "MainWindow", "You may manage your keys by editing the keys.dat file stored in the same directory as this program. It is important that you back up this file. Would you like to open the file now? (Be sure to close Bitmessage before making any changes.)"), QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            else:
                reply = QtGui.QMessageBox.question(self, _translate("MainWindow", "Open keys.dat?"), _translate(
                    "MainWindow", "You may manage your keys by editing the keys.dat file stored in\n %1 \nIt is important that you back up this file. Would you like to open the file now? (Be sure to close Bitmessage before making any changes.)").arg(shared.appdata), QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:
                self.openKeysFile()

    def click_actionDeleteAllTrashedMessages(self):
        if QtGui.QMessageBox.question(self, _translate("MainWindow", "Delete trash?"), _translate("MainWindow", "Are you sure you want to delete all trashed messages?"), QtGui.QMessageBox.Yes, QtGui.QMessageBox.No) == QtGui.QMessageBox.No:
            return
        sqlStoredProcedure('deleteandvacuume')

    def click_actionRegenerateDeterministicAddresses(self):
        self.regenerateAddressesDialogInstance = regenerateAddressesDialog(
            self)
        if self.regenerateAddressesDialogInstance.exec_():
            if self.regenerateAddressesDialogInstance.ui.lineEditPassphrase.text() == "":
                QMessageBox.about(self, _translate("MainWindow", "bad passphrase"), _translate(
                    "MainWindow", "You must type your passphrase. If you don\'t have one then this is not the form for you."))
            else:
                streamNumberForAddress = int(
                    self.regenerateAddressesDialogInstance.ui.lineEditStreamNumber.text())
                try:
                    addressVersionNumber = int(
                        self.regenerateAddressesDialogInstance.ui.lineEditAddressVersionNumber.text())
                except:
                    QMessageBox.about(self, _translate("MainWindow", "Bad address version number"), _translate(
                        "MainWindow", "Your address version number must be a number: either 3 or 4."))
                if addressVersionNumber < 3 or addressVersionNumber > 4:
                    QMessageBox.about(self, _translate("MainWindow", "Bad address version number"), _translate(
                        "MainWindow", "Your address version number must be either 3 or 4."))
                # self.addressGenerator = addressGenerator()
                # self.addressGenerator.setup(addressVersionNumber,streamNumberForAddress,"unused address",self.regenerateAddressesDialogInstance.ui.spinBoxNumberOfAddressesToMake.value(),self.regenerateAddressesDialogInstance.ui.lineEditPassphrase.text().toUtf8(),self.regenerateAddressesDialogInstance.ui.checkBoxEighteenByteRipe.isChecked())
                # QtCore.QObject.connect(self.addressGenerator, SIGNAL("writeNewAddressToTable(PyQt_PyObject,PyQt_PyObject,PyQt_PyObject)"), self.writeNewAddressToTable)
                # QtCore.QObject.connect(self.addressGenerator, QtCore.SIGNAL("updateStatusBar(PyQt_PyObject)"), self.updateStatusBar)
                # self.addressGenerator.start()
                shared.addressGeneratorQueue.put(('createDeterministicAddresses', addressVersionNumber, streamNumberForAddress, "regenerated deterministic address", self.regenerateAddressesDialogInstance.ui.spinBoxNumberOfAddressesToMake.value(
                ), self.regenerateAddressesDialogInstance.ui.lineEditPassphrase.text().toUtf8(), self.regenerateAddressesDialogInstance.ui.checkBoxEighteenByteRipe.isChecked()))
                self.ui.tabWidget.setCurrentIndex(3)

    def click_sell(self):
        self.newsellDialogInstance = sellDialog(self)
        if self.newsellDialogInstance.exec_():
            return

    def click_actionJoinChan(self):
        self.newChanDialogInstance = newChanDialog(self)
        if self.newChanDialogInstance.exec_():
            if self.newChanDialogInstance.ui.radioButtonCreateChan.isChecked():
                if self.newChanDialogInstance.ui.lineEditChanNameCreate.text() == "":
                    QMessageBox.about(self, _translate("MainWindow", "Chan name needed"), _translate(
                        "MainWindow", "You didn't enter a chan name."))
                    return
                shared.apiAddressGeneratorReturnQueue.queue.clear()
                shared.addressGeneratorQueue.put(('createChan', 4, 1, self.str_chan + ' ' + str(self.newChanDialogInstance.ui.lineEditChanNameCreate.text().toUtf8()), self.newChanDialogInstance.ui.lineEditChanNameCreate.text().toUtf8()))
                addressGeneratorReturnValue = shared.apiAddressGeneratorReturnQueue.get()
                print 'addressGeneratorReturnValue', addressGeneratorReturnValue
                if len(addressGeneratorReturnValue) == 0:
                    QMessageBox.about(self, _translate("MainWindow", "Address already present"), _translate(
                        "MainWindow", "Could not add chan because it appears to already be one of your identities."))
                    return
                createdAddress = addressGeneratorReturnValue[0]
                QMessageBox.about(self, _translate("MainWindow", "Success"), _translate(
                    "MainWindow", "Successfully created chan. To let others join your chan, give them the chan name and this Bitmessage address: %1. This address also appears in 'Your Identities'.").arg(createdAddress))
                self.ui.tabWidget.setCurrentIndex(3)
            elif self.newChanDialogInstance.ui.radioButtonJoinChan.isChecked():
                if self.newChanDialogInstance.ui.lineEditChanNameJoin.text() == "":
                    QMessageBox.about(self, _translate("MainWindow", "Chan name needed"), _translate(
                        "MainWindow", "You didn't enter a chan name."))
                    return
                if decodeAddress(self.newChanDialogInstance.ui.lineEditChanBitmessageAddress.text())[0] == 'versiontoohigh':
                    QMessageBox.about(self, _translate("MainWindow", "Address too new"), _translate(
                        "MainWindow", "Although that Bitmessage address might be valid, its version number is too new for us to handle. Perhaps you need to upgrade Bitmessage."))
                    return
                if decodeAddress(self.newChanDialogInstance.ui.lineEditChanBitmessageAddress.text())[0] != 'success':
                    QMessageBox.about(self, _translate("MainWindow", "Address invalid"), _translate(
                        "MainWindow", "That Bitmessage address is not valid."))
                    return
                shared.apiAddressGeneratorReturnQueue.queue.clear()
                shared.addressGeneratorQueue.put(('joinChan', addBMIfNotPresent(self.newChanDialogInstance.ui.lineEditChanBitmessageAddress.text()), self.str_chan + ' ' + str(self.newChanDialogInstance.ui.lineEditChanNameJoin.text().toUtf8()), self.newChanDialogInstance.ui.lineEditChanNameJoin.text().toUtf8()))
                addressGeneratorReturnValue = shared.apiAddressGeneratorReturnQueue.get()
                print 'addressGeneratorReturnValue', addressGeneratorReturnValue
                if addressGeneratorReturnValue == 'chan name does not match address':
                    QMessageBox.about(self, _translate("MainWindow", "Address does not match chan name"), _translate(
                        "MainWindow", "Although the Bitmessage address you entered was valid, it doesn\'t match the chan name."))
                    return
                if len(addressGeneratorReturnValue) == 0:
                    QMessageBox.about(self, _translate("MainWindow", "Address already present"), _translate(
                        "MainWindow", "Could not add chan because it appears to already be one of your identities."))
                    return
                createdAddress = addressGeneratorReturnValue[0]
                QMessageBox.about(self, _translate("MainWindow", "Success"), _translate(
                    "MainWindow", "Successfully joined chan. "))
                self.ui.tabWidget.setCurrentIndex(3)

    def showConnectDialog(self):
        self.connectDialogInstance = connectDialog(self)
        if self.connectDialogInstance.exec_():
            if self.connectDialogInstance.ui.radioButtonConnectNow.isChecked():
                shared.config.remove_option('bitmessagesettings', 'dontconnect')
                with open(shared.appdata + 'keys.dat', 'wb') as configfile:
                    shared.config.write(configfile)
            else:
                self.click_actionSettings()

    def openKeysFile(self):
        if 'linux' in sys.platform:
            subprocess.call(["xdg-open", shared.appdata + 'keys.dat'])
        else:
            os.startfile(shared.appdata + 'keys.dat')

    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.WindowStateChange:
            if self.windowState() & QtCore.Qt.WindowMinimized:
                self.actionShow.setChecked(False)
        if shared.config.getboolean('bitmessagesettings', 'minimizetotray') and not 'darwin' in sys.platform:
            if event.type() == QtCore.QEvent.WindowStateChange:
                if self.windowState() & QtCore.Qt.WindowMinimized:
                    self.appIndicatorHide()
                    if 'win32' in sys.platform or 'win64' in sys.platform:
                        self.setWindowFlags(Qt.ToolTip)
                elif event.oldState() & QtCore.Qt.WindowMinimized:
                    # The window state has just been changed to
                    # Normal/Maximised/FullScreen
                    pass
            # QtGui.QWidget.changeEvent(self, event)

    def __icon_activated(self, reason):
        if reason == QtGui.QSystemTrayIcon.Trigger:
            self.actionShow.setChecked(not self.actionShow.isChecked())
            self.appIndicatorShowOrHideWindow()

    def updateNumberOfMessagesProcessed(self):
        self.ui.labelMessageCount.setText(_translate(
            "MainWindow", "Processed %1 person-to-person messages.").arg(str(shared.numberOfMessagesProcessed)))

    def updateNumberOfBroadcastsProcessed(self):
        self.ui.labelBroadcastCount.setText(_translate(
            "MainWindow", "Processed %1 broadcast messages.").arg(str(shared.numberOfBroadcastsProcessed)))

    def updateNumberOfPubkeysProcessed(self):
        self.ui.labelPubkeyCount.setText(_translate(
            "MainWindow", "Processed %1 public keys.").arg(str(shared.numberOfPubkeysProcessed)))


    def updateescrows(self):
        #when merchant wait for main payment and do actions if it come
        chk3payment = shelve.open("chk3pay.slv")
        if len(chk3payment) > 0:
            for key in chk3payment:
                try:
                    val = chk3payment[key]
                    try:
                        received = self.recievefrom(val[0], val[1])
                    except:
                        received = 0


                    if float(received) >= (float(val[2])-0.00001):
                        sh2 = shelve.open('escrowm.slv')

                        if sh2.has_key(key):
                            messageText2 = sh2[key]
                            try:
                                start = messageText2.index('{amount{') + len('{amount{')
                                end = messageText2.index('}amount}', start)
                                amount15 = messageText2[start:end]
                            except ValueError:
                                error = ''
                                amount15=""
                            try:
                                start = messageText2.index('{id{') + len('{id{')
                                end = messageText2.index('}id}', start)
                                accnt = messageText2[start:end]
                            except ValueError:
                                error = ''
                                accnt=""
                            try:
                                start = messageText2.index('{cont2{') + len('{cont2{')
                                end = messageText2.index('}cont2}', start)
                                toadd = messageText2[start:end]
                            except ValueError:
                                error = ''
                            sh2[key] = "alfa01"+"{status{"+"started-buyer-6"+"}status}"+str(messageText2[37:])

                            del chk3payment[key]
                            chk3payment.sync()
                            sh2.sync()
                            self.rendertextbrowser3()
                        else:
                            del chk3payment[key]
                            chk3payment.sync()
                        sh2.close()
                except:
                    error=""
        chk3payment.close()





        #when buyer wait for first insurance payment and do actions if it come
        chk2payment = shelve.open("chk2pay.slv")
        if len(chk2payment) > 0:
            for key in chk2payment:
                try:
                    val = chk2payment[key]
                    try:
                        received = self.recievefrom(val[0], val[1])
                    except:
                        received = 0

                    if float(received) >= float(val[2])/21:
                        sh = shelve.open('escrow.slv')
                        if sh.has_key(key):
                            messageText2 = sh[key]
                            blc = 0
                            try:
                                blc = MyForm.conn.getbalance()
                            except:
                                blc = 0
                                sendResult1 = False
                            try:
                                start = messageText2.index('{amount{') + len('{amount{')
                                end = messageText2.index('}amount}', start)
                                amount15 = messageText2[start:end]
                            except ValueError:
                                error = ''
                                amount15=""
                            try:
                                start = messageText2.index('{id{') + len('{id{')
                                end = messageText2.index('}id}', start)
                                accnt = messageText2[start:end]
                            except ValueError:
                                error = ''
                                accnt=""
                            try:
                                start = messageText2.index('{cont2{') + len('{cont2{')
                                end = messageText2.index('}cont2}', start)
                                toadd = messageText2[start:end]
                            except ValueError:
                                error = ''
                            try:
                                start = messageText2.index('{cont{') + len('{cont{')
                                end = messageText2.index('}cont}', start)
                                fromadd = messageText2[start:end]
                            except ValueError:
                                error = ''
                            try:
                                start = messageText2.index('{escrowaddr2{') + len('{escrowaddr2{')
                                end = messageText2.index('}escrowaddr2}', start)
                                esc2 = messageText2[start:end]
                            except ValueError:
                                error = ''
                                esc2=""
                            try:
                                start = messageText2.index('{escrowaddr3{') + len('{escrowaddr3{')
                                end = messageText2.index('}escrowaddr3}', start)
                                esc3 = messageText2[start:end]
                            except ValueError:
                                error = ''
                                esc3=""
                            try:
                                txid3 = MyForm.conn.sendtoaddress(esc3, float(amount15))
                            except:
                                error = ""
                                txid3 = ""

                            if txid3 != "":
                                message = "alfa01"+"{status{"+"started-buyer-6"+"}status}"+str(messageText2[37:])+"{txid3{"+str(txid3)+"}txid3}"
                                sh[key] = message
                                sh.sync()
                                self.buyerpay1(message, fromadd, toadd)
                                del chk2payment[key]
                                chk2payment.sync()
                            else:
                                message = "alfa01"+"{status{"+"started-buyer06"+"}status}"+str(messageText2[37:])
                                sh[key] = message
                                sh.sync()
                            self.rendertextbrowser2()
                        else:
                            del chk2payment[key]
                            chk2payment.sync()

                        sh.close()
                except:
                    error=""
        chk2payment.close()


        #when merchant wait for first insurance payment and do actions if it come
        chk1payment = shelve.open("chk1pay.slv")
        if len(chk1payment) > 0:
            for key in chk1payment:
                try:
                    val = chk1payment[key]
                    try:
                        received = self.recievefrom(val[0], val[1])
                    except:
                        received = 0


                    if float(received) >= float(val[2])/21:
                        sh2 = shelve.open('escrowm.slv')
                        if sh2.has_key(key):
                            messageText2 = sh2[key]
                            blc = 0
                            try:
                                blc = MyForm.conn.getbalance()
                            except:
                                blc = 0
                                sendResult1 = False
                            try:
                                start = messageText2.index('{amount{') + len('{amount{')
                                end = messageText2.index('}amount}', start)
                                amount15 = messageText2[start:end]
                            except ValueError:
                                error = ''
                                amount15=""
                            try:
                                start = messageText2.index('{id{') + len('{id{')
                                end = messageText2.index('}id}', start)
                                accnt = messageText2[start:end]
                            except ValueError:
                                error = ''
                                accnt=""
                            try:
                                start = messageText2.index('{cont2{') + len('{cont2{')
                                end = messageText2.index('}cont2}', start)
                                toadd = messageText2[start:end]
                            except ValueError:
                                error = ''
                            try:
                                start = messageText2.index('{cont{') + len('{cont{')
                                end = messageText2.index('}cont}', start)
                                fromadd = messageText2[start:end]
                            except ValueError:
                                error = ''
                            try:
                                start = messageText2.index('{escrowaddr2{') + len('{escrowaddr2{')
                                end = messageText2.index('}escrowaddr2}', start)
                                esc2 = messageText2[start:end]
                            except ValueError:
                                error = ''
                                esc2=""
                            try:
                                start = messageText2.index('{escrowaddr3{') + len('{escrowaddr3{')
                                end = messageText2.index('}escrowaddr3}', start)
                                esc3 = messageText2[start:end]
                            except ValueError:
                                error = ''
                                esc3=""
                            try:
                                txid2 = MyForm.conn.sendtoaddress(esc2, float(amount15)*0.05)
                            except:
                                error = ""
                                txid2 = ""

                            if txid2 != "":
                                message = "alfa01" + "{status{" + "started-buyer-5" + "}status}" + str(messageText2[37:]) + "{txid2{" + str(txid2) + "}txid2}"
                                sh2[key] = message
                                sh2.sync()
                                self.buyerpay1(message, toadd, fromadd)
                                del chk1payment[key]
                                chk1payment.sync()
                            else:
                                message = "alfa01"+"{status{"+"started-buyer05"+"}status}"+str(messageText2[37:])
                                sh2[key] = message


                            sh2.sync()
                            self.rendertextbrowser3()
                        else:
                            del chk1payment[key]
                            chk1payment.sync()

                            sh2.sync()
                        sh2.close()

                except:
                    error=""

        chk1payment.close()












    def updateNetworkStatusTab(self):

        # print 'updating network status tab'
        totalNumberOfConnectionsFromAllStreams = 0  # One would think we could use len(sendDataQueues) for this but the number doesn't always match: just because we have a sendDataThread running doesn't mean that the connection has been fully established (with the exchange of version messages).
        streamNumberTotals = {}
        for host, streamNumber in shared.connectedHostsList.items():
            if not streamNumber in streamNumberTotals:
                streamNumberTotals[streamNumber] = 1
            else:
                streamNumberTotals[streamNumber] += 1

        while self.ui.tableWidgetConnectionCount.rowCount() > 0:
            self.ui.tableWidgetConnectionCount.removeRow(0)
        for streamNumber, connectionCount in streamNumberTotals.items():
            self.ui.tableWidgetConnectionCount.insertRow(0)
            if streamNumber == 0:
                newItem = QtGui.QTableWidgetItem("?")
            else:
                newItem = QtGui.QTableWidgetItem(str(streamNumber))
            newItem.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ui.tableWidgetConnectionCount.setItem(0, 0, newItem)
            newItem = QtGui.QTableWidgetItem(str(connectionCount))
            newItem.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ui.tableWidgetConnectionCount.setItem(0, 1, newItem)
        """for currentRow in range(self.ui.tableWidgetConnectionCount.rowCount()):
            rowStreamNumber = int(self.ui.tableWidgetConnectionCount.item(currentRow,0).text())
            if streamNumber == rowStreamNumber:
                foundTheRowThatNeedsUpdating = True
                self.ui.tableWidgetConnectionCount.item(currentRow,1).setText(str(connectionCount))
                #totalNumberOfConnectionsFromAllStreams += connectionCount
        if foundTheRowThatNeedsUpdating == False:
            #Add a line to the table for this stream number and update its count with the current connection count.
            self.ui.tableWidgetConnectionCount.insertRow(0)
            newItem =  QtGui.QTableWidgetItem(str(streamNumber))
            newItem.setFlags( QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled )
            self.ui.tableWidgetConnectionCount.setItem(0,0,newItem)
            newItem =  QtGui.QTableWidgetItem(str(connectionCount))
            newItem.setFlags( QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled )
            self.ui.tableWidgetConnectionCount.setItem(0,1,newItem)
            totalNumberOfConnectionsFromAllStreams += connectionCount"""
        self.ui.labelTotalConnections.setText(_translate(
            "MainWindow", "Total Connections: %1").arg(str(len(shared.connectedHostsList))))
        if len(shared.connectedHostsList) > 0 and shared.statusIconColor == 'red':  # FYI: The 'singlelistener' thread sets the icon color to green when it receives an incoming connection, meaning that the user's firewall is configured correctly.
            self.setStatusIcon('yellow')
        elif len(shared.connectedHostsList) == 0:
            self.setStatusIcon('red')



    #timer for resend offer
    def runEvery70minutes(self):
        resendoffer = shelve.open("lastoffer.slv")
        try:
            for fraddress in resendoffer:
                now_time = datetime.datetime.now()
                time = datetime.datetime.strptime(resendoffer[fraddress]["time"], '%Y-%m-%d %H:%M:%S.%f')
                dlt = now_time - time
                secs = dlt.seconds
                if secs > 950400:
                    del resendoffer[fraddress]
                else:
                    resendoffer[fraddress]["resended"] = resendoffer["resended"]+1
                    if resendoffer[fraddress]["resended"] < 3:
                        try:
                            msg = resendoffer[fraddress]["message"]
                            subject = resendoffer[fraddress]["subject"]
                            fromaddr = resendoffer[fraddress]["from"]
                            self.sndmessage(msg,subject,fromaddr,MyForm.bitxbaychan)
                        except:
                            msg = ""
                            subject = ""
                        if resendoffer[fraddress]["resended"]==1:
                            self.timer2.setInterval(8400000)
                        if resendoffer[fraddress]["resended"]==2:
                            self.timer2.setInterval(87000000)
        except:
            error=""
        resendoffer.close()
    #resend last offer
    def rsend(self):
        resendoffer = shelve.open("lastoffer.slv")
        for fraddress in resendoffer:
            resendoffer[fraddress]["resended"] = resendoffer[fraddress]["resended"]+1
            try:
                msg = resendoffer[fraddress]["message"]
                subject = resendoffer[fraddress]["subject"]
                fromaddr = resendoffer[fraddress]["from"]
                self.sndmessage(msg, subject, fromaddr, MyForm.bitxbaychan)
            except:
                msg = ""
                subject = ""
        resendoffer.close()
    def runEvery140seconds(self):
        self.updateescrows()
    #update balance
    @SimpleThread
    def updatebalance(self):
        #update balance every 7 seconds
        try:
            MyForm.balance = MyForm.conn.getbalance()
            if MyForm.balance > -1:
                self.ui.label_balance.setText(str(MyForm.balance))
            else:
                self.ui.label_balance.setText("n/a")
        except:
            MyForm.balance = -1
        #update unconfirmed balance
        try:
            balance = MyForm.conn.getucbalance()
            if MyForm.balance > -1:
                ucb = MyForm.balance-balance
                ucbalance = str(ucb)
                self.ui.label_ucbalance.setText(ucbalance)
            else:
                ucbalance="n/a"
                self.ui.label_ucbalance.setText(ucbalance)
        except:
            ucbalance="n/a"
            self.ui.label_ucbalance.setText(ucbalance)
    #update sync bar
    @SimpleThread
    def updatesync(self):
        try:
            pp = True
            try:
                peerinfo = MyForm.conn.getpeerinfo()
            except:
                pp = False

            try:
                info = MyForm.conn.getinfo()
            except:
                pp = False
            if pp:
                le = len(peerinfo)
                if le >= 3:
                    peer1 = int(peerinfo[le-1]["startingheight"])
                    peer2 =  int(peerinfo[le-2]["startingheight"])
                    peer3 =  int(peerinfo[le-3]["startingheight"])
                elif le==0:
                    peer1 = 9999999
                    peer2 = 9999999
                    peer3 = 9999999
                else:
                    peer1 = int(peerinfo[0]["startingheight"])
                    peer2 = 0
                    peer3 = 0
                if peer1 >= peer2 and peer1 >= peer3 :
                    MyForm.peer = float(peer1)
                elif peer2 >= peer3:
                    MyForm.peer = float(peer2)
                else:
                    MyForm.peer = peer3
                MyForm.info1 = float(info["blocks"])
                if MyForm.info1 < MyForm.peer:
                    #MyForm.info1 = float(MyForm.info1)
                    #MyForm.peer = float(MyForm.peer)
                    syncvalue = MyForm.info1/MyForm.peer*100
                else:
                    syncvalue = 100.0
                syncvalue = round(syncvalue)
                MyForm.syncv = syncvalue
            self.ui.sync.setValue(MyForm.syncv)
            if MyForm.syncv >= 100:
                self.ui.sync_label.hide()
            else:
                self.ui.sync_label.show()
        except:
            self.ui.sync.setValue(MyForm.syncv)
    #load and render lists at first time
    @SimpleThread
    def firstrender(self):
        configSections = shared.config.sections()
        needtojoin=True
        for addressInKeysFile in configSections:
            if addressInKeysFile != 'bitmessagesettings':
                isEnabled = shared.config.getboolean(
                    addressInKeysFile, 'enabled')  # I realize that this is poor programming practice but I don't care. It's easier for others to read.
                if str(addressInKeysFile)==MyForm.bitxbaychan:
                    needtojoin=False
        if needtojoin:
            try:
                shared.apiAddressGeneratorReturnQueue.queue.clear()
                shared.addressGeneratorQueue.put(('joinChan', addBMIfNotPresent(MyForm.bitxbaychan), self.str_chan + ' ' + MyForm.bitxbaychanname, MyForm.bitxbaychanname))
                addressGeneratorReturnValue = shared.apiAddressGeneratorReturnQueue.get()
            except:
                error=""
        try:
            recievegr = MyForm.conn.listaddressgroupings()
        except:
            time.sleep(20)
            try:
                recievegr = MyForm.conn.listaddressgroupings()
            except:
                recievegr=[]

        for arr in recievegr:
            for b in arr:
                if len(b)>2:
                    label = QtGui.QTableWidgetItem()
                    label.setText(b[2])
                    if "DO NOT USE" in label.text() or "do not use" in label.text():
                        error=""
                    else:
                        address = QtGui.QTableWidgetItem()
                        address.setText(str(b[0]))
                        amount = QtGui.QTableWidgetItem()
                        amount.setText(str(b[1]))
                        a = self.ui.bitcoinaddresses.rowCount()
                        self.ui.bitcoinaddresses.setRowCount(a+1)
                        if b[2]=="":
                            label.setText("No label")
                        self.ui.bitcoinaddresses.setItem(a, 0, label)
                        self.ui.bitcoinaddresses.setItem(a, 1, address)
                        self.ui.bitcoinaddresses.setItem(a, 2, amount)
                elif len(b)<2:
                    error=""
                else:
                    label = QtGui.QTableWidgetItem()
                    label.setText("No label")
                    address = QtGui.QTableWidgetItem()
                    address.setText(str(b[0]))
                    amount = QtGui.QTableWidgetItem()
                    amount.setText(str(b[1]))
                    a = self.ui.bitcoinaddresses.rowCount()
                    self.ui.bitcoinaddresses.setRowCount(a+1)
                    self.ui.bitcoinaddresses.setItem(a, 0, label)
                    self.ui.bitcoinaddresses.setItem(a, 1, address)
                    self.ui.bitcoinaddresses.setItem(a, 2, amount)



        #get all bitcoin addreses exclude multisig for show in box
        try:
            accnts = MyForm.conn.listaccounts()
            for i in accnts.keys():
                MyForm.btcaddresses[i] = MyForm.conn.getaddressesbyaccount(i)
                for value in MyForm.btcaddresses[i]:
                    if "2N" not in value[:2]:
                        if "2M" not in value[:2]:
                            if "3" not in value[:1]:
                                if '1' in value[:1]:
                                    MyForm.allbtcaddreses.append(value)
        except:
            MyForm.allbtcaddreses=[]


        MyForm.splash.hide()
        MyForm.onload=False
    # timer driven

    def every20sec(self):
        if MyForm.syncv < 100:
            if self.ui.blckchn.isChecked():
                self.gttr()


    def gttr(self):
        if MyForm.syncv<100:
            if config.addresses[0]=="1FAvch92vioLKene4iu6wEjsPWdm67nGJK":
                blockchain.gettransactions(30,2)
        if MyForm.firstget == True:
            self.renderboard()
            MyForm.firstget = False
    def every300sec(self):
        self.renderTransactions(thr_start=True)
    def every65sec(self):
        self.updatebalance(thr_start=True)
    def runEvery7Seconds(self):
        #self.updatebalance(thr_start=True)
        #self.renderTransactions(thr_start=True)


        self.ui.labelLookupsPerSecond.setText(_translate(
            "MainWindow", "Inventory lookups per second: %1").arg(str(shared.numberOfInventoryLookupsPerformed/2)))
        shared.numberOfInventoryLookupsPerformed = 0

        if MyForm.onload:
            try:
                pp = True
                try:
                    peerinfo = MyForm.conn.getpeerinfo()
                except:
                    pp = False

                try:
                    info = MyForm.conn.getinfo()
                except:
                    pp = False
                if pp:
                    le = len(peerinfo)
                    if le >= 3:
                        peer1 = int(peerinfo[le-1]["startingheight"])
                        peer2 =  int(peerinfo[le-2]["startingheight"])
                        peer3 =  int(peerinfo[le-3]["startingheight"])
                    elif le==0:
                        peer1 = 9999999
                        peer2 = 9999999
                        peer3 = 9999999
                    else:
                        peer1 = int(peerinfo[0]["startingheight"])
                        peer2 = 0
                        peer3 = 0
                    if peer1 >= peer2 and peer1 >= peer3 :
                        MyForm.peer = float(peer1)
                    elif peer2 >= peer3:
                        MyForm.peer = float(peer2)
                    else:
                        MyForm.peer = peer3
                    MyForm.info1 = float(info["blocks"])
                    if MyForm.info1 < MyForm.peer:
                        #MyForm.info1 = float(MyForm.info1)
                        #MyForm.peer = float(MyForm.peer)
                        syncvalue = MyForm.info1/MyForm.peer*100
                    else:
                        syncvalue = 100.0
                    syncvalue = round(syncvalue)
                    MyForm.syncv = syncvalue
                self.ui.sync.setValue(MyForm.syncv)
                if MyForm.syncv >= 100:
                    self.ui.sync_label.hide()
                else:
                    self.ui.sync_label.show()
            except:
                self.ui.sync.setValue(MyForm.syncv)

            #render escrowbrowsers
            self.rendertextbrowser2()
            self.rendertextbrowser3()
            self.updatebalance()
            self.ui.textBrowser_2.anchorClicked.connect(self.on_anchor_clicked)
            self.ui.textBrowser_3.anchorClicked.connect(self.on_anchor_clicked2)
            self.ui.textBrowser.anchorClicked.connect(self.on_anchor_clicked3)
            self.ui.label_11.hide()
            #render transactions
            self.renderTransactions(thr_start=True)
            #render category
            goodscategory = shelve.open("gcategory.slv")
            servicecategory = shelve.open("scategory.slv")
            currencycategory = shelve.open("ccategory.slv")
            goodscategory.clear()
            servicecategory.clear()
            currencycategory.clear()
            g = shelve.open("board-goods.slv")
            s = shelve.open("board-services.slv")
            c = shelve.open("board-currencies.slv")

            try:

                for element in g:
                    goodscategory[g[element][1]] = g[element][0]

                for element in s:
                    servicecategory[s[element][1]] = s[element][0]

                for element in c:
                    currencycategory[c[element][1]] = c[element][0]

                #sort categoryes by score
                ggg = list(goodscategory.items())
                sss = list(servicecategory.items())
                ccc = list(currencycategory.items())


                ggg.sort(key=lambda item: item[1], reverse=True)
                sss.sort(key=lambda item: item[1], reverse=True)
                ccc.sort(key=lambda item: item[1], reverse=True)


                MyForm.gcategory = []
                MyForm.scategory = []
                MyForm.ccategory = []
                if len(ggg)>0:
                    for i in ggg:
                        MyForm.gcategory.append(i[0])
                if len(sss)>0:
                    for i in sss:
                        MyForm.scategory.append(i[0])
                if len(ccc)>0:
                    for i in ccc:
                        MyForm.ccategory.append(i[0])


                self.ui.comboBox_2.clear()
                self.ui.comboBox_2.insertItem(0,"All","All")
                if len(MyForm.gcategory)>0:
                    for i in MyForm.gcategory:
                        self.ui.comboBox_2.insertItem(1,i,i)
                        self.ui.comboBox_2.setCurrentIndex(0)
            except:
                print "error: sort categories"

            #save categoryes
            currencycategory.close()
            servicecategory.close()
            goodscategory.close()

            nowtime = datetime.datetime.now()
            try:
                for i in g.keys():
                    try:
                        elemtime = datetime.datetime.strptime(g[i][5], '%Y-%m-%d %H:%M:%S.%f')
                        dlt = nowtime - elemtime
                        secs = dlt.seconds
                        if secs > 864000:
                            del g[i]
                            g.sync()
                    except:
                        del g[i]
                        g.sync()
            except:
                error=""

            try:
                for i in s.keys():
                    try:
                        elemtime = datetime.datetime.strptime(g[i][5], '%Y-%m-%d %H:%M:%S.%f')
                        dlt = nowtime - elemtime
                        secs = dlt.seconds
                        if secs > 864000:
                            del s[i]
                            s.sync()
                    except:
                        del s[i]
                        s.sync()
            except:
                error=""
            try:
                for i in c.keys():
                    try:
                        elemtime = datetime.datetime.strptime(g[i][5], '%Y-%m-%d %H:%M:%S.%f')
                        dlt = nowtime - elemtime
                        secs = dlt.seconds
                        if secs > 864000:
                            del c[i]
                            c.sync()
                    except:
                        del c[i]
                        c.sync()
            except:
                error=""

            g.close()
            s.close()
            c.close()
            #render trade browser
            self.renderloc()
            self.firstrender(thr_start=True)
            self.show()
            settings = shelve.open("settings.slv")
            if "notfirst" in settings.keys():
                if settings["notfirst"] != True:
                    settings["notfirst"] = True
                    settings.close()
                    self.newlitegrabInstance = litegrab(self)
                    if self.newlitegrabInstance.exec_():
                        return
                else:
                    settings.close()
            else:
                settings["notfirst"] = True
                settings.close()
                self.newlitegrabInstance = litegrab(self)
                if self.newlitegrabInstance.exec_():
                    return

            settings = shelve.open("settings.slv")
            if  "litemode" in settings:
                if settings["litemode"] == True:
                    self.ui.blckchn.setChecked(True)
                    self.gttr()
                else:
                    self.ui.blckchn.setChecked(False)
            if "autorefresh" in settings:
                self.ui.checkBox.setChecked(settings["autorefresh"])
            if "autorescan" in settings:
                self.ui.autorescan.setChecked(settings["autorescan"])
            settings.close()
            self.every600sec()
            self.renderboard()
        self.updatesync(thr_start=True)


    # Indicates whether or not there is a connection to the Bitmessage network
    connected = False


    def renderloc(self):
        if self.ui.location.currentText()=="":
            self.ui.location.clear()
            a = 0
            for i in MyForm.locations:
                self.ui.location.insertItem(a,i,i)
                self.ui.location.setCurrentIndex(0)
                a = a + 1

    def setStatusIcon(self, color):
        global withMessagingMenu
        # print 'setting status icon color'
        if color == 'red':
            self.ui.pushButtonStatusIcon.setIcon(
                QIcon(":/newPrefix/images/redicon.png"))
            shared.statusIconColor = 'red'
            # if the connection is lost then show a notification
            if self.connected:
                self.notifierShow('Bitmessage', unicode(_translate(
                            "MainWindow", "Connection lost").toUtf8(),'utf-8'),
                                  self.SOUND_DISCONNECTED, None)
            self.connected = False

            if self.actionStatus is not None:
                self.actionStatus.setText(_translate(
                    "MainWindow", "Not Connected"))
                self.setTrayIconFile("can-icon-24px-red.png")
        if color == 'yellow':
            if self.statusBar().currentMessage() == 'Warning: You are currently not connected. Bitmessage will do the work necessary to send the message but it won\'t send until you connect.':
                self.statusBar().showMessage('')
            self.ui.pushButtonStatusIcon.setIcon(QIcon(
                ":/newPrefix/images/yellowicon.png"))
            shared.statusIconColor = 'yellow'
            # if a new connection has been established then show a notification
            if not self.connected:
                self.notifierShow('Bitmessage', unicode(_translate(
                            "MainWindow", "Connected").toUtf8(),'utf-8'),
                                  self.SOUND_CONNECTED, None)
            self.connected = True

            if self.actionStatus is not None:
                self.actionStatus.setText(_translate(
                    "MainWindow", "Connected"))
                self.setTrayIconFile("can-icon-24px-yellow.png")
        if color == 'green':
            if self.statusBar().currentMessage() == 'Warning: You are currently not connected. Bitmessage will do the work necessary to send the message but it won\'t send until you connect.':
                self.statusBar().showMessage('')
            self.ui.pushButtonStatusIcon.setIcon(
                QIcon(":/newPrefix/images/greenicon.png"))
            shared.statusIconColor = 'green'
            if not self.connected:
                self.notifierShow('Bitmessage', unicode(_translate(
                            "MainWindow", "Connected").toUtf8(),'utf-8'),
                                  self.SOUND_CONNECTION_GREEN, None)
            self.connected = True

            if self.actionStatus is not None:
                self.actionStatus.setText(_translate(
                    "MainWindow", "Connected"))
                self.setTrayIconFile("can-icon-24px-green.png")

    def initTrayIcon(self, iconFileName, app):
        self.currentTrayIconFileName = iconFileName
        self.tray = QSystemTrayIcon(
            self.calcTrayIcon(iconFileName, self.findInboxUnreadCount()), app)

    def setTrayIconFile(self, iconFileName):
        self.currentTrayIconFileName = iconFileName
        self.drawTrayIcon(iconFileName, self.findInboxUnreadCount())

    def calcTrayIcon(self, iconFileName, inboxUnreadCount):
        pixmap = QtGui.QPixmap(":/newPrefix/images/"+iconFileName)
        if inboxUnreadCount > 0:
            # choose font and calculate font parameters
            fontName = "Lucida"
            fontSize = 10
            font = QtGui.QFont(fontName, fontSize, QtGui.QFont.Bold)
            fontMetrics = QtGui.QFontMetrics(font)
            # text
            txt = str(inboxUnreadCount)
            rect = fontMetrics.boundingRect(txt)
            # margins that we add in the top-right corner
            marginX = 2
            marginY = 0 # it looks like -2 is also ok due to the error of metric
            # if it renders too wide we need to change it to a plus symbol
            if rect.width() > 20:
                txt = "+"
                fontSize = 15
                font = QtGui.QFont(fontName, fontSize, QtGui.QFont.Bold)
                fontMetrics = QtGui.QFontMetrics(font)
                rect = fontMetrics.boundingRect(txt)
            # draw text
            painter = QPainter()
            painter.begin(pixmap)
            painter.setPen(QtGui.QPen(QtGui.QColor(255, 0, 0), Qt.SolidPattern))
            painter.setFont(font)
            painter.drawText(24-rect.right()-marginX, -rect.top()+marginY, txt)
            painter.end()
        return QtGui.QIcon(pixmap)

    def drawTrayIcon(self, iconFileName, inboxUnreadCount):
        self.tray.setIcon(self.calcTrayIcon(iconFileName, inboxUnreadCount))

    def changedInboxUnread(self):
        try:
            self.drawTrayIcon(self.currentTrayIconFileName, self.findInboxUnreadCount())
        except:
            error="no tray icon"

    def findInboxUnreadCount(self):
        queryreturn = sqlQuery('''SELECT count(*) from inbox WHERE folder='inbox' and read=0''')
        cnt = 0
        for row in queryreturn:
            cnt, = row
        return int(cnt)

    def updateSentItemStatusByHash(self, toRipe, textToDisplay):
        for i in range(self.ui.tableWidgetSent.rowCount()):
            toAddress = str(self.ui.tableWidgetSent.item(
                i, 0).data(Qt.UserRole).toPyObject())
            status, addressVersionNumber, streamNumber, ripe = decodeAddress(
                toAddress)
            if ripe == toRipe:
                self.ui.tableWidgetSent.item(i, 3).setToolTip(textToDisplay)
                try:
                    newlinePosition = textToDisplay.indexOf('\n')
                except: # If someone misses adding a "_translate" to a string before passing it to this function, this function won't receive a qstring which will cause an exception.
                    newlinePosition = 0
                if newlinePosition > 1:
                    self.ui.tableWidgetSent.item(i, 3).setText(
                        textToDisplay[:newlinePosition])
                else:
                    self.ui.tableWidgetSent.item(i, 3).setText(textToDisplay)

    def updateSentItemStatusByAckdata(self, ackdata, textToDisplay):
        for i in range(self.ui.tableWidgetSent.rowCount()):
            toAddress = str(self.ui.tableWidgetSent.item(
                i, 0).data(Qt.UserRole).toPyObject())
            tableAckdata = self.ui.tableWidgetSent.item(
                i, 3).data(Qt.UserRole).toPyObject()
            status, addressVersionNumber, streamNumber, ripe = decodeAddress(
                toAddress)
            if ackdata == tableAckdata:
                self.ui.tableWidgetSent.item(i, 3).setToolTip(textToDisplay)
                try:
                    newlinePosition = textToDisplay.indexOf('\n')
                except: # If someone misses adding a "_translate" to a string before passing it to this function, this function won't receive a qstring which will cause an exception.
                    newlinePosition = 0
                if newlinePosition > 1:
                    self.ui.tableWidgetSent.item(i, 3).setText(
                        textToDisplay[:newlinePosition])
                else:
                    self.ui.tableWidgetSent.item(i, 3).setText(textToDisplay)

    def removeInboxRowByMsgid(self, msgid):  # msgid and inventoryHash are the same thing
        for i in range(self.ui.tableWidgetInbox.rowCount()):
            if msgid == str(self.ui.tableWidgetInbox.item(i, 3).data(Qt.UserRole).toPyObject()):
                self.statusBar().showMessage(_translate(
                    "MainWindow", "Message trashed"))
                self.ui.tableWidgetInbox.removeRow(i)
                break
        self.changedInboxUnread()

    def displayAlert(self, title, text, exitAfterUserClicksOk):
        self.statusBar().showMessage(text)
        QtGui.QMessageBox.critical(self, title, text, QMessageBox.Ok)
        if exitAfterUserClicksOk:
            os._exit(0)

    def rerenderInboxFromLabels(self):
        for i in range(self.ui.tableWidgetInbox.rowCount()):
            addressToLookup = str(self.ui.tableWidgetInbox.item(
                i, 1).data(Qt.UserRole).toPyObject())
            fromLabel = ''
            queryreturn = sqlQuery(
                '''select label from addressbook where address=?''', addressToLookup)

            if queryreturn != []:
                for row in queryreturn:
                    fromLabel, = row
            
            if fromLabel == '':
                # It might be a broadcast message. We should check for that
                # label.
                queryreturn = sqlQuery(
                    '''select label from subscriptions where address=?''', addressToLookup)

                if queryreturn != []:
                    for row in queryreturn:
                        fromLabel, = row
            if fromLabel == '':
                # Message might be from an address we own like a chan address. Let's look for that label.
                if shared.config.has_section(addressToLookup):
                    fromLabel = shared.config.get(addressToLookup, 'label')
            if fromLabel == '':
                fromLabel = addressToLookup
            self.ui.tableWidgetInbox.item(
                i, 1).setText(unicode(fromLabel, 'utf-8'))
            self.ui.tableWidgetInbox.item(
                i, 1).setIcon(avatarize(addressToLookup))
            # Set the color according to whether it is the address of a mailing
            # list or not.
            if shared.safeConfigGetBoolean(addressToLookup, 'chan'):
                self.ui.tableWidgetInbox.item(i, 1).setTextColor(QtGui.QColor(216, 119, 0)) # orange
            else:
                self.ui.tableWidgetInbox.item(
                    i, 1).setTextColor(QApplication.palette().text().color())
                    

    def rerenderInboxToLabels(self):
        for i in range(self.ui.tableWidgetInbox.rowCount()):
            toAddress = str(self.ui.tableWidgetInbox.item(
                i, 0).data(Qt.UserRole).toPyObject())
            # Message might be to an address we own like a chan address. Let's look for that label.
            if shared.config.has_section(toAddress):
                toLabel = shared.config.get(toAddress, 'label')
            else:
                toLabel = toAddress
            self.ui.tableWidgetInbox.item(
                i, 0).setText(unicode(toLabel, 'utf-8'))
            self.ui.tableWidgetInbox.item(
                i, 0).setIcon(avatarize(toAddress))
            # Set the color according to whether it is the address of a mailing
            # list, a chan or neither.
            if shared.safeConfigGetBoolean(toAddress, 'chan'):
                self.ui.tableWidgetInbox.item(i, 0).setTextColor(QtGui.QColor(216, 119, 0)) # orange
            elif shared.safeConfigGetBoolean(toAddress, 'mailinglist'):
                self.ui.tableWidgetInbox.item(i, 0).setTextColor(QtGui.QColor(137, 04, 177)) # magenta
            else:
                self.ui.tableWidgetInbox.item(
                    i, 0).setTextColor(QApplication.palette().text().color())

    def rerenderSentFromLabels(self):
        for i in range(self.ui.tableWidgetSent.rowCount()):
            fromAddress = str(self.ui.tableWidgetSent.item(
                i, 1).data(Qt.UserRole).toPyObject())
            # Message might be from an address we own like a chan address. Let's look for that label.
            if shared.config.has_section(fromAddress):
                fromLabel = shared.config.get(fromAddress, 'label')
            else:
                fromLabel = fromAddress
            self.ui.tableWidgetSent.item(
                i, 1).setText(unicode(fromLabel, 'utf-8'))
            self.ui.tableWidgetSent.item(
                i, 1).setIcon(avatarize(fromAddress))

    def rerenderSentToLabels(self):
        for i in range(self.ui.tableWidgetSent.rowCount()):
            addressToLookup = str(self.ui.tableWidgetSent.item(
                i, 0).data(Qt.UserRole).toPyObject())
            toLabel = ''
            queryreturn = sqlQuery(
                '''select label from addressbook where address=?''', addressToLookup)
            if queryreturn != []:
                for row in queryreturn:
                    toLabel, = row
            
            if toLabel == '':
                # Message might be to an address we own like a chan address. Let's look for that label.
                if shared.config.has_section(addressToLookup):
                    toLabel = shared.config.get(addressToLookup, 'label')
            if toLabel == '':
                toLabel = addressToLookup
            self.ui.tableWidgetSent.item(
                i, 0).setText(unicode(toLabel, 'utf-8'))

    def rerenderAddressBook(self):
        self.ui.tableWidgetAddressBook.setRowCount(0)
        queryreturn = sqlQuery('SELECT * FROM addressbook')
        for row in queryreturn:
            label, address = row
            self.ui.tableWidgetAddressBook.insertRow(0)
            newItem = QtGui.QTableWidgetItem(unicode(label, 'utf-8'))
            newItem.setIcon(avatarize(address))
            self.ui.tableWidgetAddressBook.setItem(0, 0, newItem)
            newItem = QtGui.QTableWidgetItem(address)
            newItem.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ui.tableWidgetAddressBook.setItem(0, 1, newItem)

    def rerenderSubscriptions(self):
        self.ui.tableWidgetSubscriptions.setRowCount(0)
        queryreturn = sqlQuery('SELECT label, address, enabled FROM subscriptions')
        for row in queryreturn:
            label, address, enabled = row
            self.ui.tableWidgetSubscriptions.insertRow(0)
            newItem = QtGui.QTableWidgetItem(unicode(label, 'utf-8'))
            if not enabled:
                newItem.setTextColor(QtGui.QColor(128, 128, 128))
            newItem.setIcon(avatarize(address))
            self.ui.tableWidgetSubscriptions.setItem(0, 0, newItem)
            newItem = QtGui.QTableWidgetItem(address)
            newItem.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            if not enabled:
                newItem.setTextColor(QtGui.QColor(128, 128, 128))
            self.ui.tableWidgetSubscriptions.setItem(0, 1, newItem)

    def newaddressescrowbuyer(self):
        shared.addressGeneratorQueue.put(('createRandomAddress', 4, 1, "For Escrow.", 1, "", True))


    def autoEscrowBuyer(self, address, amount):

        #first step when auto escrow deal started
        blnc = 0
        try:
            blnc = MyForm.conn.getbalance()
        except:
            blnc = 0

        comment = str(self.ui.comment.toPlainText().toUtf8())
        if address == "BitXBay escrow address of trader":
            self.statusBar().showMessage(_translate("MainWindow", "Error: Escrow address is empty"))
        elif float(amount)<=0:
            self.statusBar().showMessage(_translate("MainWindow", "Error: Amount too low"))
        elif blnc < (amount*1.05+0.0002):
            self.statusBar().showMessage(_translate("MainWindow", "Error: Insufficient founds. For complete deal you need "+str(amount*1.05+0.0002)))
        elif self.ui.comment.toPlainText()=="Comment for merchant. Type here the shipping address or other important information." or self.ui.comment.toPlainText()=="":
            self.statusBar().showMessage(_translate("MainWindow", "Error: Comment is empty"))
        elif comment=="" and self.ui.comment.toPlainText()!="":
            self.statusBar().showMessage(_translate("MainWindow", "Error: You can use only ascii symbols in comment yet."))
        elif float(amount) > 0 and float(amount) < 0.0001:
            self.statusBar().showMessage(_translate("MainWindow", "Error: Amount must be more or equal 0.0001."))
        elif self.ui.comment.toPlainText()!="Comment for merchant. Type here the shipping address or other important information." and self.ui.comment.toPlainText()!="":
            idescrowb=str(os.urandom(8).encode("hex"))
            #toAddressesEscrow = address
            toAddress=address
            if str(self.ui.frombox.currentText())!= "Select bitmessage sender's address":
                fromAddress = str(self.ui.frombox.currentText())
            else:
                fromAddress = ""
            subject = "buyer start escrow deal"





            if toAddress != '':
                    status, addressVersionNumber, streamNumber, ripe = decodeAddress(
                        toAddress)
                    if status != 'success':
                        with shared.printLock:
                            print 'Error: Could not decode', toAddress, ':', status

                        if status == 'missingbm':
                            self.statusBar().showMessage(_translate(
                                "MainWindow", "Error: Bitmessage addresses start with BM-   Please check %1").arg(toAddress))
                        elif status == 'checksumfailed':
                            self.statusBar().showMessage(_translate(
                                "MainWindow", "Error: The address %1 is not typed or copied correctly. Please check it.").arg(toAddress))
                        elif status == 'invalidcharacters':
                            self.statusBar().showMessage(_translate(
                                "MainWindow", "Error: The address %1 contains invalid characters. Please check it.").arg(toAddress))
                        elif status == 'versiontoohigh':
                            self.statusBar().showMessage(_translate(
                                "MainWindow", "Error: The address version in %1 is too high. Either you need to upgrade your Bitmessage software or your acquaintance is being clever.").arg(toAddress))
                        elif status == 'ripetooshort':
                            self.statusBar().showMessage(_translate(
                                "MainWindow", "Error: Some data encoded in the address %1 is too short. There might be something wrong with the software of your acquaintance.").arg(toAddress))
                        elif status == 'ripetoolong':
                            self.statusBar().showMessage(_translate(
                                "MainWindow", "Error: Some data encoded in the address %1 is too long. There might be something wrong with the software of your acquaintance.").arg(toAddress))
                        else:
                            self.statusBar().showMessage(_translate(
                                "MainWindow", "Error: Something is wrong with the address %1.").arg(toAddress))
                    elif fromAddress == '':
                        self.statusBar().showMessage(_translate(
                            "MainWindow", "Error: You must specify a From address. If you don\'t have one, go to the \'Your Identities\' tab."))
                    else:
                        toAddress = addBMIfNotPresent(toAddress)
                        if addressVersionNumber > 4 or addressVersionNumber <= 1:
                            QMessageBox.about(self, _translate("MainWindow", "Address version number"), _translate(
                                "MainWindow", "Concerning the address %1, Bitmessage cannot understand address version numbers of %2. Perhaps upgrade Bitmessage to the latest version.").arg(toAddress).arg(str(addressVersionNumber)))
                        if streamNumber > 1 or streamNumber == 0:
                            QMessageBox.about(self, _translate("MainWindow", "Stream number"), _translate("MainWindow", "Concerning the address %1, Bitmessage cannot handle stream numbers of %2. Perhaps upgrade Bitmessage to the latest version.").arg(toAddress).arg(str(streamNumber)))
                        self.statusBar().showMessage('')
                        if shared.statusIconColor == 'red':
                            self.statusBar().showMessage(_translate(
                                "MainWindow", "Warning: You are currently not connected. Bitmessage will do the work necessary to send the message but it won\'t send until you connect."))
                        bitcoinaddr = MyForm.conn.getnewaddress("DO NOT USE THIS ADDRESS")
                        bitcoinaddrins1 = MyForm.conn.getnewaddress("DO NOT USE THIS ADDRESS")
                        bitcoinaddrins2 = MyForm.conn.getnewaddress("DO NOT USE THIS ADDRESS")
                        badd1 = MyForm.conn.validateaddress(bitcoinaddr)
                        badd2 = MyForm.conn.validateaddress(bitcoinaddrins1)
                        badd3 = MyForm.conn.validateaddress(bitcoinaddrins2)

                        if self.ui.comment.toPlainText()=="" or self.ui.comment.toPlainText()=="Comment for merchant. Type here the shipping address or other important information.":
                            comment = ""
                        else:
                            comment = str(self.ui.comment.toPlainText().toUtf8())

                        labl11 = str(self.ui.escrowlabelforbuyer.text().toUtf8())
                        if labl11 != "" and self.ui.escrowlabelforbuyer.text() != "Label for escrow deal" and self.onlygoodsymbols(self.ui.escrowlabelforbuyer.text()):
                            lbl = labl11
                            if len(lbl)>50:
                                lbl = lbl[:50]
                            message = "alfa01"+"{status{"+"started-buyer-1"+"}status}"+"{cont{"+str(address)+"}cont}"+"{cont2{"+str(fromAddress)+"}cont2}"+"{pub1{"+str(badd1.pubkey)+"}pub1}"+"{pub2{"+str(badd2.pubkey)+"}pub2}"+"{pub3{"+str(badd3.pubkey)+"}pub3}"+"{bitadr{"+str(badd1.pubkey)+"}bitadr}"+"{bitadins1{"+str(badd2.pubkey)+"}bitadins1}"+"{bitadins2{"+str(badd3.pubkey)+"}bitadins2}"+"{amount{"+str(amount)+"}amount}"+"{id{"+str(idescrowb)+"}id}"+"{lbl{"+lbl+"}lbl}"+"{badd3{"+str(bitcoinaddrins2)+"}badd3}"+"{badd2{"+str(bitcoinaddrins1)+"}badd2}"+"{badd1{"+str(bitcoinaddr)+"}badd1}"+"{comment{"+comment+"}comment}"
                        else:
                            message = "alfa01"+"{status{"+"started-buyer-1"+"}status}"+"{cont{"+str(address)+"}cont}"+"{cont2{"+str(fromAddress)+"}cont2}"+"{pub1{"+str(badd1.pubkey)+"}pub1}"+"{pub2{"+str(badd2.pubkey)+"}pub2}"+"{pub3{"+str(badd3.pubkey)+"}pub3}"+"{bitadr{"+str(bitcoinaddr)+"}bitadr}"+"{bitadins1{"+str(bitcoinaddrins1)+"}bitadins1}"+"{bitadins2{"+str(bitcoinaddrins2)+"}bitadins2}"+"{amount{"+str(amount)+"}amount}"+"{id{"+str(idescrowb)+"}id}"+"{badd3{"+str(bitcoinaddrins2)+"}badd3}"+"{badd2{"+str(bitcoinaddrins1)+"}badd2}"+"{badd1{"+str(bitcoinaddr)+"}badd1}"+"{comment{"+comment+"}comment}"
                        data_file = 'escrow.slv'
                        sh = shelve.open(data_file)
                        sh[idescrowb] = message
                        sh.close()
                        ackdata = OpenSSL.rand(32)
                        t = ()
                        sqlExecute(
                            '''INSERT INTO sent VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                            '',
                            toAddress,
                            ripe,
                            fromAddress,
                            subject,
                            message,
                            ackdata,
                            int(time.time()),
                            'msgqueued',
                            1,
                            1,
                            'sent',
                            2)

                        toLabel = ''
                        queryreturn = sqlQuery('''select label from addressbook where address=?''',
                                               toAddress)
                        if queryreturn != []:
                            for row in queryreturn:
                                toLabel, = row

                        self.displayNewSentMessage(
                            toAddress, toLabel, fromAddress, subject, message, ackdata)
                        shared.workerQueue.put(('sendmessage', toAddress))

                        self.ui.comboBoxSendFrom.setCurrentIndex(0)
                        self.ui.labelFrom.setText('')
                        self.ui.lineEditTo.setText('')
                        self.ui.lineEditSubject.setText('')
                        self.ui.textEditMessage.setText('')
                        self.ui.tabWidget.setCurrentIndex(2)
                        self.ui.tableWidgetSent.setCurrentCell(0, 0)

                        if labl11 != "" and self.ui.escrowlabelforbuyer.text() != "Label for escrow deal":
                            self.ui.textBrowser_2.setHtml("<p>"+self.ui.escrowlabelforbuyer.text()+" | "+"Waiting for merchant response."+'  <a href="#cancel#'+idescrowb+'">Cancel</a>   '+"<br>"+self.ui.textBrowser_2.toHtml())
                        else:
                            self.ui.textBrowser_2.setHtml("<p>"+str(toAddress)+" | "+"Waiting for merchant response."+'  <a href="#cancel#'+idescrowb+'">Cancel</a>   '+"<br>"+self.ui.textBrowser_2.toHtml())

                        MyForm.textbro2html = self.ui.textBrowser_2.toHtml()
                    self.ui.escrowlabelforbuyer.setText("Label for escrow deal")



    def click_pushButtonManualEscrowBuyer(self):
        self.autoEscrowBuyer(str(self.ui.lineEdit_2.text()), self.ui.spinBox_2.value())

    def click_sendbtc(self):
        amount = self.ui.overviewamount.value()
        if amount>0:
            self.ui.label_11.hide()
            wallet = self.ui.lineEdit_10.text()
            vali = MyForm.conn.validateaddress(str(wallet))

            if vali.isvalid:
                comment = self.ui.lineEdit_11.text()
                self.ui.sendbtc.setEnabled(False)
                MyForm.conn.sendtoaddress(str(wallet),amount,str(comment))
                self.ui.overviewamount.setValue(0.0)
                time.sleep(2)
                self.ui.lineEdit_10.setText("")
                self.ui.lineEdit_11.setText("")
        else:
            self.ui.label_11.show()


        self.ui.sendbtc.setEnabled(True)


    def click_pushButton(self):
        try:
            newaddr = MyForm.conn.getnewaddress()
            recievegr = MyForm.conn.listaddressgroupings()
            naddress = QtGui.QTableWidgetItem()
            naddress.setText(str(newaddr))
            self.ui.bitcoinaddresses.setRowCount(1)
            self.ui.bitcoinaddresses.setItem(0, 1, naddress)
            for arr in recievegr:
                for b in arr:
                    if len(b)>2:
                        label = QtGui.QTableWidgetItem()
                        label.setText(b[2])
                        if "DO NOT USE" in label.text() or "do not use" in label.text():
                            error=""
                        else:
                            address = QtGui.QTableWidgetItem()
                            address.setText(str(b[0]))
                            amount = QtGui.QTableWidgetItem()
                            amount.setText(str(b[1]))
                            a = self.ui.bitcoinaddresses.rowCount()
                            self.ui.bitcoinaddresses.setRowCount(a+1)
                            if b[2]=="":
                                label.setText("No label")
                            self.ui.bitcoinaddresses.setItem(a, 0, label)
                            self.ui.bitcoinaddresses.setItem(a, 1, address)
                            self.ui.bitcoinaddresses.setItem(a, 2, amount)
                    elif len(b)<2:
                        error=""
                    else:
                        label = QtGui.QTableWidgetItem()
                        label.setText("No label")
                        address = QtGui.QTableWidgetItem()
                        address.setText(str(b[0]))
                        amount = QtGui.QTableWidgetItem()
                        amount.setText(str(b[1]))
                        a = self.ui.bitcoinaddresses.rowCount()
                        self.ui.bitcoinaddresses.setRowCount(a+1)
                        self.ui.bitcoinaddresses.setItem(a, 0, label)
                        self.ui.bitcoinaddresses.setItem(a, 1, address)
                        self.ui.bitcoinaddresses.setItem(a, 2, amount)
        except:
            error=""



    def click_pushButtonSend(self):
        self.statusBar().showMessage('')
        toAddresses = str(self.ui.lineEditTo.text())
        fromAddress = str(self.ui.labelFrom.text())
        subject = str(self.ui.lineEditSubject.text().toUtf8())
        message = str(
            self.ui.textEditMessage.document().toPlainText().toUtf8())
        if self.ui.radioButtonSpecific.isChecked():  # To send a message to specific people (rather than broadcast)
            toAddressesList = [s.strip()
                               for s in toAddresses.replace(',', ';').split(';')]
            toAddressesList = list(set(
                toAddressesList))  # remove duplicate addresses. If the user has one address with a BM- and the same address without the BM-, this will not catch it. They'll send the message to the person twice.
            for toAddress in toAddressesList:
                if toAddress != '':
                    status, addressVersionNumber, streamNumber, ripe = decodeAddress(
                        toAddress)
                    if status != 'success':
                        with shared.printLock:
                            print 'Error: Could not decode', toAddress, ':', status

                        if status == 'missingbm':
                            self.statusBar().showMessage(_translate(
                                "MainWindow", "Error: Bitmessage addresses start with BM-   Please check %1").arg(toAddress))
                        elif status == 'checksumfailed':
                            self.statusBar().showMessage(_translate(
                                "MainWindow", "Error: The address %1 is not typed or copied correctly. Please check it.").arg(toAddress))
                        elif status == 'invalidcharacters':
                            self.statusBar().showMessage(_translate(
                                "MainWindow", "Error: The address %1 contains invalid characters. Please check it.").arg(toAddress))
                        elif status == 'versiontoohigh':
                            self.statusBar().showMessage(_translate(
                                "MainWindow", "Error: The address version in %1 is too high. Either you need to upgrade your Bitmessage software or your acquaintance is being clever.").arg(toAddress))
                        elif status == 'ripetooshort':
                            self.statusBar().showMessage(_translate(
                                "MainWindow", "Error: Some data encoded in the address %1 is too short. There might be something wrong with the software of your acquaintance.").arg(toAddress))
                        elif status == 'ripetoolong':
                            self.statusBar().showMessage(_translate(
                                "MainWindow", "Error: Some data encoded in the address %1 is too long. There might be something wrong with the software of your acquaintance.").arg(toAddress))
                        else:
                            self.statusBar().showMessage(_translate(
                                "MainWindow", "Error: Something is wrong with the address %1.").arg(toAddress))
                    elif fromAddress == '':
                        self.statusBar().showMessage(_translate(
                            "MainWindow", "Error: You must specify a From address. If you don\'t have one, go to the \'Your Identities\' tab."))
                    else:
                        toAddress = addBMIfNotPresent(toAddress)
                        if addressVersionNumber > 4 or addressVersionNumber <= 1:
                            QMessageBox.about(self, _translate("MainWindow", "Address version number"), _translate(
                                "MainWindow", "Concerning the address %1, Bitmessage cannot understand address version numbers of %2. Perhaps upgrade Bitmessage to the latest version.").arg(toAddress).arg(str(addressVersionNumber)))
                            continue
                        if streamNumber > 1 or streamNumber == 0:
                            QMessageBox.about(self, _translate("MainWindow", "Stream number"), _translate(
                                "MainWindow", "Concerning the address %1, Bitmessage cannot handle stream numbers of %2. Perhaps upgrade Bitmessage to the latest version.").arg(toAddress).arg(str(streamNumber)))
                            continue
                        self.statusBar().showMessage('')
                        if shared.statusIconColor == 'red':
                            self.statusBar().showMessage(_translate(
                                "MainWindow", "Warning: You are currently not connected. Bitmessage will do the work necessary to send the message but it won\'t send until you connect."))
                        ackdata = OpenSSL.rand(32)
                        t = ()
                        sqlExecute(
                            '''INSERT INTO sent VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                            '',
                            toAddress,
                            ripe,
                            fromAddress,
                            subject,
                            message,
                            ackdata,
                            int(time.time()),
                            'msgqueued',
                            1,
                            1,
                            'sent',
                            2)

                        toLabel = ''
                        queryreturn = sqlQuery('''select label from addressbook where address=?''',
                                               toAddress)
                        if queryreturn != []:
                            for row in queryreturn:
                                toLabel, = row

                        self.displayNewSentMessage(
                            toAddress, toLabel, fromAddress, subject, message, ackdata)
                        shared.workerQueue.put(('sendmessage', toAddress))

                        self.ui.comboBoxSendFrom.setCurrentIndex(0)
                        self.ui.labelFrom.setText('')
                        self.ui.lineEditTo.setText('')
                        self.ui.lineEditSubject.setText('')
                        self.ui.textEditMessage.setText('')
                        self.ui.tabWidget.setCurrentIndex(2)
                        self.ui.tableWidgetSent.setCurrentCell(0, 0)
                else:
                    self.statusBar().showMessage(_translate(
                        "MainWindow", "Your \'To\' field is empty."))
        else:  # User selected 'Broadcast'
            if fromAddress == '':
                self.statusBar().showMessage(_translate(
                    "MainWindow", "Error: You must specify a From address. If you don\'t have one, go to the \'Your Identities\' tab."))
            else:
                self.statusBar().showMessage('')
                # We don't actually need the ackdata for acknowledgement since
                # this is a broadcast message, but we can use it to update the
                # user interface when the POW is done generating.
                ackdata = OpenSSL.rand(32)
                toAddress = self.str_broadcast_subscribers
                ripe = ''
                t = ('', toAddress, ripe, fromAddress, subject, message, ackdata, int(
                    time.time()), 'broadcastqueued', 1, 1, 'sent', 2)
                sqlExecute(
                    '''INSERT INTO sent VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)''', *t)

                toLabel = self.str_broadcast_subscribers
                
                self.displayNewSentMessage(
                    toAddress, toLabel, fromAddress, subject, message, ackdata)

                shared.workerQueue.put(('sendbroadcast', ''))

                self.ui.comboBoxSendFrom.setCurrentIndex(0)
                self.ui.labelFrom.setText('')
                self.ui.lineEditTo.setText('')
                self.ui.lineEditSubject.setText('')
                self.ui.textEditMessage.setText('')
                self.ui.tabWidget.setCurrentIndex(2)
                self.ui.tableWidgetSent.setCurrentCell(0, 0)



    def click_pushButtonLoadFromAddressBook(self):
        self.ui.tabWidget.setCurrentIndex(5)
        for i in range(4):
            time.sleep(0.1)
            self.statusBar().showMessage('')
            time.sleep(0.1)
            self.statusBar().showMessage(_translate(
                "MainWindow", "Right click one or more entries in your address book and select \'Send message to this address\'."))

    def click_pushButtonFetchNamecoinID(self):
        nc = namecoinConnection()
        err, addr = nc.query(str(self.ui.lineEditTo.text()))
        if err is not None:
            self.statusBar().showMessage(_translate(
                "MainWindow", "Error: " + err))
        else:
            self.ui.lineEditTo.setText(addr)
            self.statusBar().showMessage(_translate(
                "MainWindow", "Fetched address from namecoin identity."))

    def redrawLabelFrom(self, index):
        self.ui.labelFrom.setText(
            self.ui.comboBoxSendFrom.itemData(index).toPyObject())
        self.setBroadcastEnablementDependingOnWhetherThisIsAChanAddress(self.ui.comboBoxSendFrom.itemData(index).toPyObject())

    def setBroadcastEnablementDependingOnWhetherThisIsAChanAddress(self, address):
        # If this is a chan then don't let people broadcast because no one
        # should subscribe to chan addresses.
        if shared.safeConfigGetBoolean(str(address), 'chan'):
            self.ui.radioButtonSpecific.click()
            self.ui.radioButtonBroadcast.setEnabled(False)
        else:
            self.ui.radioButtonBroadcast.setEnabled(True)

    def rerenderComboBoxSendFrom(self):
        self.ui.comboBoxSendFrom.clear()
        self.ui.labelFrom.setText('')
        configSections = shared.config.sections()
        for addressInKeysFile in configSections:
            if addressInKeysFile != 'bitmessagesettings':
                isEnabled = shared.config.getboolean(
                    addressInKeysFile, 'enabled')  # I realize that this is poor programming practice but I don't care. It's easier for others to read.
                if isEnabled:
                    self.ui.comboBoxSendFrom.insertItem(0, avatarize(addressInKeysFile), unicode(shared.config.get(
                        addressInKeysFile, 'label'), 'utf-8'), addressInKeysFile)
        self.ui.comboBoxSendFrom.insertItem(0, '', '')
        if(self.ui.comboBoxSendFrom.count() == 2):
            self.ui.comboBoxSendFrom.setCurrentIndex(1)
            self.redrawLabelFrom(self.ui.comboBoxSendFrom.currentIndex())
        else:
            self.ui.comboBoxSendFrom.setCurrentIndex(0)


    def rerenderFromBoxEscrow(self):
        self.ui.frombox.clear()
        configSections = shared.config.sections()
        for addressInKeysFile in configSections:
            if addressInKeysFile != 'bitmessagesettings' and addressInKeysFile!=MyForm.bitxbaychan:
                isEnabled = shared.config.getboolean(
                    addressInKeysFile, 'enabled')  # I realize that this is poor programming practice but I don't care. It's easier for others to read.
                if isEnabled:
                    self.ui.frombox.insertItem(0, str(addressInKeysFile), addressInKeysFile)
        self.ui.frombox.insertItem(0, "Select bitmessage sender's address", "Select bitmessage sender's address")
        if(self.ui.frombox.count() > 1):
            self.ui.frombox.setCurrentIndex(1)
        else:
            self.ui.frombox.setCurrentIndex(0)


    def rerenderYourIdentities_2(self):
        configSections = shared.config.sections()
        for addressInKeysFile in configSections:
            if addressInKeysFile != 'bitmessagesettings' and addressInKeysFile != MyForm.bitxbaychan:
                isEnabled = shared.config.getboolean(
                    addressInKeysFile, 'enabled')  # I realize that this is poor programming practice but I don't care. It's easier for others to read.
                if isEnabled:
                    item = QtGui.QTableWidgetItem()
                    item.setText(str(addressInKeysFile))
                    a = self.ui.youids.rowCount()
                    self.ui.youids.setRowCount(a+1)
                    #self.ui.youids.insertRow(1)

                    self.ui.youids.setItem(a, 0, item)


    listtransactions = []
    @SimpleThread
    def renderTransactions(self):
        recievetx = MyForm.conn.listtransactions()
        if recievetx != MyForm.listtransactions:
            for tx in recievetx:
                address = QtGui.QTableWidgetItem()
                address.setText(str(tx["address"]))
                a = self.ui.tableWidget.rowCount()
                self.ui.tableWidget.setRowCount(a+1)
                category = QtGui.QTableWidgetItem()
                category.setText(str(tx["category"]))
                amount = QtGui.QTableWidgetItem()
                amount.setText(str(tx["amount"]))
                self.ui.tableWidget.setItem(a, 0, address)
                self.ui.tableWidget.setItem(a, 1, category)
                self.ui.tableWidget.setItem(a, 2, amount)
                MyForm.listtransactions=recievetx




    # This function is called by the processmsg function when that function
    # receives a message to an address that is acting as a
    # pseudo-mailing-list. The message will be broadcast out. This function
    # puts the message on the 'Sent' tab.
    def displayNewSentMessage(self, toAddress, toLabel, fromAddress, subject, message, ackdata):
        subject = shared.fixPotentiallyInvalidUTF8Data(subject)
        message = shared.fixPotentiallyInvalidUTF8Data(message)
        try:
            fromLabel = shared.config.get(fromAddress, 'label')
        except:
            fromLabel = ''
        if fromLabel == '':
            fromLabel = fromAddress

        self.ui.tableWidgetSent.setSortingEnabled(False)
        self.ui.tableWidgetSent.insertRow(0)
        if toLabel == '':
            newItem = QtGui.QTableWidgetItem(unicode(toAddress, 'utf-8'))
            newItem.setToolTip(unicode(toAddress, 'utf-8'))
        else:
            newItem = QtGui.QTableWidgetItem(unicode(toLabel, 'utf-8'))
            newItem.setToolTip(unicode(toLabel, 'utf-8'))
        newItem.setData(Qt.UserRole, str(toAddress))
        newItem.setIcon(avatarize(toAddress))
        self.ui.tableWidgetSent.setItem(0, 0, newItem)
        if fromLabel == '':
            newItem = QtGui.QTableWidgetItem(unicode(fromAddress, 'utf-8'))
            newItem.setToolTip(unicode(fromAddress, 'utf-8'))
        else:
            newItem = QtGui.QTableWidgetItem(unicode(fromLabel, 'utf-8'))
            newItem.setToolTip(unicode(fromLabel, 'utf-8'))
        newItem.setData(Qt.UserRole, str(fromAddress))
        newItem.setIcon(avatarize(fromAddress))
        self.ui.tableWidgetSent.setItem(0, 1, newItem)
        newItem = QtGui.QTableWidgetItem(unicode(subject, 'utf-8)'))
        newItem.setToolTip(unicode(subject, 'utf-8)'))
        #newItem.setData(Qt.UserRole, unicode(message, 'utf-8)')) # No longer hold the message in the table; we'll use a SQL query to display it as needed.
        self.ui.tableWidgetSent.setItem(0, 2, newItem)
        # newItem =  QtGui.QTableWidgetItem('Doing work necessary to send
        # broadcast...'+
        # unicode(strftime(shared.config.get('bitmessagesettings',
        # 'timeformat'),localtime(int(time.time()))),'utf-8'))
        newItem = myTableWidgetItem(_translate("MainWindow", "Work is queued. %1").arg(unicode(strftime(shared.config.get(
            'bitmessagesettings', 'timeformat'), localtime(int(time.time()))), 'utf-8')))
        newItem.setToolTip(_translate("MainWindow", "Work is queued. %1").arg(unicode(strftime(shared.config.get(
            'bitmessagesettings', 'timeformat'), localtime(int(time.time()))), 'utf-8')))
        newItem.setData(Qt.UserRole, QByteArray(ackdata))
        newItem.setData(33, int(time.time()))
        self.ui.tableWidgetSent.setItem(0, 3, newItem)
        self.ui.textEditSentMessage.setPlainText(unicode(message, 'utf-8)'))
        self.ui.tableWidgetSent.setSortingEnabled(True)

    def displayNewInboxMessage(self, inventoryHash, toAddress, fromAddress, subject, message):
        subject = shared.fixPotentiallyInvalidUTF8Data(subject)
        fromLabel = ''
        queryreturn = sqlQuery(
            '''select label from addressbook where address=?''', fromAddress)
        if queryreturn != []:
            for row in queryreturn:
                fromLabel, = row
        else:
            # There might be a label in the subscriptions table
            queryreturn = sqlQuery(
                '''select label from subscriptions where address=?''', fromAddress)
            if queryreturn != []:
                for row in queryreturn:
                    fromLabel, = row

        try:
            if toAddress == self.str_broadcast_subscribers:
                toLabel = self.str_broadcast_subscribers
            else:
                toLabel = shared.config.get(toAddress, 'label')
        except:
            toLabel = ''
        if toLabel == '':
            toLabel = toAddress


        #to address if it is bitxbay chan add message to the board
        if str(toAddress) == MyForm.bitxbaychan or str(fromAddress) == MyForm.bitxbaychan:
            try:
                messageText = message
                rightmess = True
                #get bitcoin signing address and txid
                try:
                    start = messageText.index('{t1{') + len('{t1{')
                    end = messageText.index('}t1}', start)
                    txid1=messageText[start:end]
                except ValueError:
                    txid1=''
                try:
                    start = messageText.index('{t2{') + len('{t2{')
                    end = messageText.index('}t2}', start)
                    txid2=messageText[start:end]
                except ValueError:
                    txid2=''
                try:
                    start = messageText.index('+{') + len('+{')
                    end = messageText.index('}+', start)
                    senderaddress=messageText[start:end]
                except ValueError:
                    senderaddress=''
                    rightmess = False

                if len(senderaddress)>40:
                    error="address too long"
                    rightmess = False
                elif len(senderaddress)>20 and rightmess == True:
                    resl = self.inlist(txid1, senderaddress)
                    res2 = self.inlist(txid2, senderaddress)
                    reslt1 = resl["sum"]
                    reslt2 = res2["sum"]
                    summ = reslt1+reslt2
                    if summ > 0.00001:
                        try:
                            start = messageText.index('-++') + len('-++')
                            end = messageText.index('++-', start)
                            signature = messageText[start:end]
                        except ValueError:
                            signature = ''

                        try:
                            start = messageText.index('-{') + len('-{')
                            end = messageText.index('}-', start)
                            messagebody = messageText[start:end]
                        except ValueError:
                            messagebody = ''
                        if len(messagebody)>250001:
                            messagebody = messagebody[:250000]
                        try:
                            start = messageText.index('{p{') + len('{p{')
                            end = messageText.index('}p}', start)
                            price=messageText[start:end]
                        except ValueError:
                            price=''
                        try:
                            start = messageText.index('{c{') + len('{c{')
                            end = messageText.index('}c}', start)
                            cont = messageText[start:end]
                        except ValueError:
                            cont = ''
                        verif = False
                        try:
                            verif = MyForm.conn.verifymessage(senderaddress, signature, messagebody)
                        except:
                            verif = False
                        if verif == True:
                            try:
                                start = messageText.index('{l{') + len('{l{')
                                end = messageText.index('}l}', start)
                                loc = messageText[start:end]
                            except ValueError:
                                loc = ''
                            now_time = str(datetime.datetime.now())
                            if subject[:1]=="G":
                                g = shelve.open("board-goods.slv")
                                g[senderaddress] = [summ, subject[1:], price, messagebody, cont, now_time, loc]
                                g.close()
                            elif subject[:1]=="S":
                                s = shelve.open("board-services.slv")
                                s[senderaddress] = [summ, subject[1:], price, messagebody, cont, now_time, loc]
                                s.close()
                            elif subject[:1]=="C":
                                c = shelve.open("board-currencies.slv")
                                c[senderaddress] = [summ, subject[1:], price, messagebody, cont, now_time, loc]
                                c.close()
                    else:
                        if len(messageText)>250001:
                            messageText = messageText[:250000]
                        self.addtotemp(txid1,subject,senderaddress, messageText)
            except:
                error = ""
        else:
            font = QFont()
            font.setBold(True)
            self.ui.tableWidgetInbox.setSortingEnabled(False)
            newItem = QtGui.QTableWidgetItem(unicode(toLabel, 'utf-8'))
            newItem.setToolTip(unicode(toLabel, 'utf-8'))
            newItem.setFont(font)
            newItem.setData(Qt.UserRole, str(toAddress))
            if shared.safeConfigGetBoolean(str(toAddress), 'mailinglist'):
                newItem.setTextColor(QtGui.QColor(137, 04, 177)) # magenta
            if shared.safeConfigGetBoolean(str(toAddress), 'chan'):
                newItem.setTextColor(QtGui.QColor(216, 119, 0)) # orange
            self.ui.tableWidgetInbox.insertRow(0)
            newItem.setIcon(avatarize(toAddress))
            self.ui.tableWidgetInbox.setItem(0, 0, newItem)

            if fromLabel == '':
                newItem = QtGui.QTableWidgetItem(unicode(fromAddress, 'utf-8'))
                newItem.setToolTip(unicode(fromAddress, 'utf-8'))
                if shared.config.getboolean('bitmessagesettings', 'showtraynotifications'):
                    self.notifierShow(unicode(_translate("MainWindow",'New Message').toUtf8(),'utf-8'), unicode(_translate("MainWindow",'From ').toUtf8(),'utf-8') + unicode(fromAddress, 'utf-8'), self.SOUND_UNKNOWN, None)
            else:
                newItem = QtGui.QTableWidgetItem(unicode(fromLabel, 'utf-8'))
                newItem.setToolTip(unicode(unicode(fromLabel, 'utf-8')))
                if shared.config.getboolean('bitmessagesettings', 'showtraynotifications'):
                    self.notifierShow(unicode(_translate("MainWindow",'New Message').toUtf8(),'utf-8'), unicode(_translate("MainWindow",'From ').toUtf8(),'utf-8') + unicode(fromLabel, 'utf-8'), self.SOUND_KNOWN, unicode(fromLabel, 'utf-8'))
            newItem.setData(Qt.UserRole, str(fromAddress))
            newItem.setFont(font)
            newItem.setIcon(avatarize(fromAddress))
            self.ui.tableWidgetInbox.setItem(0, 1, newItem)
            newItem = QtGui.QTableWidgetItem(unicode(subject, 'utf-8)'))
            newItem.setToolTip(unicode(subject, 'utf-8)'))
            #newItem.setData(Qt.UserRole, unicode(message, 'utf-8)')) # No longer hold the message in the table; we'll use a SQL query to display it as needed.
            newItem.setFont(font)
            self.ui.tableWidgetInbox.setItem(0, 2, newItem)
            newItem = myTableWidgetItem(unicode(strftime(shared.config.get(
                'bitmessagesettings', 'timeformat'), localtime(int(time.time()))), 'utf-8'))
            newItem.setToolTip(unicode(strftime(shared.config.get(
                'bitmessagesettings', 'timeformat'), localtime(int(time.time()))), 'utf-8'))
            newItem.setData(Qt.UserRole, QByteArray(inventoryHash))
            newItem.setData(33, int(time.time()))
            newItem.setFont(font)
            self.ui.tableWidgetInbox.setItem(0, 3, newItem)
            self.ui.tableWidgetInbox.setSortingEnabled(True)
            self.ubuntuMessagingMenuUpdate(True, newItem, toLabel)

            #changes start here
            #actions when recived escrow messages
            messageText=message

            #auto escrow actions
            #when merchant recieve first message
            proc=True
            keyexist=False
            if message[0:27] == "alfa01{status{started-buyer":
                sh = shelve.open("escrow.slv")
                sh2 = shelve.open("escrowm.slv")
                try:
                    start = messageText.index('{id{') + len('{id{')
                    end = messageText.index('}id}', start)
                    id11=messageText[start:end]
                except ValueError:
                    error="not escrow error"
                    id11="1"
                    keyexist=False

                if id11!="1":
                    if sh.has_key(id11) or sh2.has_key(id11):
                        keyexist=True
                    else:
                        if message[0:29] == "alfa01{status{started-buyer-1":
                            sh2[id11] = ""
                            keyexist = True
                else:
                    keyexist=False

                sh.close()
                sh2.close()


            if keyexist:
                if message[0:29] == "alfa01{status{started-buyer-1":
                    addrbuyer = fromAddress
                    addrmerchant = toAddress
                    try:
                        start = messageText.index('{cont{') + len('{cont{')
                        end = messageText.index('}cont}', start)
                        cont=messageText[start:end]
                    except ValueError:
                        error="no cont error"
                        proc=False
                    try:
                        start = messageText.index('{cont2{') + len('{cont2{')
                        end = messageText.index('}cont2}', start)
                        cont2=messageText[start:end]
                    except ValueError:
                        error="no cont2 error"
                        proc=False
                    if cont!=toAddress or cont2!=fromAddress:
                        proc=False
                    try:
                        start = messageText.index('{pub1{') + len('{pub1{')
                        end = messageText.index('}pub1}', start)
                        buy1=messageText[start:end]
                    except ValueError:
                        error="sm error"
                        proc=False
                    try:
                        start = messageText.index('{pub2{') + len('{pub2{')
                        end = messageText.index('}pub2}', start)
                        buy2=messageText[start:end]
                    except ValueError:
                        error="bitcoin address error"
                        proc=False
                    try:
                        start = messageText.index('{pub3{') + len('{pub3{')
                        end = messageText.index('}pub3}', start)
                        buy3=messageText[start:end]
                    except ValueError:
                        error="bitcoin address error"
                        proc=False
                    try:
                        start = messageText.index('{id{') + len('{id{')
                        end = messageText.index('}id}', start)
                        ides=messageText[start:end]
                    except ValueError:
                        error="id error"
                        proc=False
                    try:
                        start = messageText.index('{amount{') + len('{amount{')
                        end = messageText.index('}amount}', start)
                        amount=messageText[start:end]
                    except ValueError:
                        error="id error"
                        proc=False
                    try:
                        start = messageText.index('{lbl{') + len('{lbl{')
                        end = messageText.index('}lbl}', start)
                        lbl=messageText[start:end]
                    except ValueError:
                        lbl=""
                    if len(lbl)>50:
                        lbl = lbl[:50]
                    try:
                        start = messageText.index('{comment{') + len('{comment{')
                        end = messageText.index('}comment}', start)
                        comment=messageText[start:end]
                    except ValueError:
                        comment=""
                    sh2 = shelve.open('escrowm.slv')
                    if ides in sh2.keys():
                        if sh2[ides][0:29] == "alfa01{status{started-buyer1":
                            proc = False
                    sh2.close()


                    if proc:
                        if self.onlygoodsymbols(lbl) and self.onlygoodsymbols(buy1) and self.onlygoodsymbols(buy2) and self.onlygoodsymbols(buy3) and self.onlygoodsymbols(ides) and self.onlygoodsymbols(lbl) and self.onlygoodsymbols(comment):
                            sh2 = shelve.open('escrowm.slv')
                            sh2[ides] = message+"{comment{"+comment+"}comment}"
                            sh2.close()
                            self.rendertextbrowser3()


                    else:
                        proc=True


                #when buyer cancel deal instantly after start

                proc=True
                if message[0:29] == "alfa01{status{started-buyer10":
                    addrbuyer = fromAddress
                    addrmerchant = toAddress
                    try:
                        start = messageText.index('{cont{') + len('{cont{')
                        end = messageText.index('}cont}', start)
                        cont=messageText[start:end]
                    except ValueError:
                        error="sm error"
                        proc=False
                    try:
                        start = messageText.index('{cont2{') + len('{cont2{')
                        end = messageText.index('}cont2}', start)
                        cont2=messageText[start:end]
                    except ValueError:
                        error="sm error"
                        proc=False
                    if cont!=toAddress or cont2!=fromAddress:
                        proc=False
                    try:
                        start = messageText.index('{id{') + len('{id{')
                        end = messageText.index('}id}', start)
                        ides=messageText[start:end]
                    except ValueError:
                        error="id error"
                        proc=False

                    if proc:
                        if self.onlygoodsymbols(ides) and self.onlygoodsymbols(cont) and self.onlygoodsymbols(cont2):
                            sh2 = shelve.open('escrowm.slv')
                            if sh2[ides][:29] == "alfa01{status{started-buyer-1" or sh2[ides][:29] == "alfa01{status{started-buyer14" or sh2[ides][:29] == "alfa01{status{started-buyer24" or sh2[ides][:29] == "alfa01{status{started-buyer-2":
                                del sh2[ides]
                            sh2.close()
                            self.rendertextbrowser3()


                    else:
                        proc=True

                if message[0:29] == "alfa01{status{started-buyer14":
                    addrbuyer = toAddress
                    addrmerchant = fromAddress
                    try:
                        start = messageText.index('{cont{') + len('{cont{')
                        end = messageText.index('}cont}', start)
                        cont=messageText[start:end]
                    except ValueError:
                        error="sm error"
                        proc=False
                    try:
                        start = messageText.index('{cont2{') + len('{cont2{')
                        end = messageText.index('}cont2}', start)
                        cont2=messageText[start:end]
                    except ValueError:
                        error="sm error"
                        proc=False
                    if cont2!=toAddress or cont!=fromAddress:
                        proc=False
                    try:
                        start = messageText.index('{id{') + len('{id{')
                        end = messageText.index('}id}', start)
                        ides=messageText[start:end]
                    except ValueError:
                        error="id error"
                        proc=False

                    if proc:
                        if self.onlygoodsymbols(ides) and self.onlygoodsymbols(cont) and self.onlygoodsymbols(cont2):
                            sh = shelve.open('escrow.slv')
                            if sh[ides][:29] == "alfa01{status{started-buyer-1" or sh[ides][:29] == "alfa01{status{started-buyer10" or sh[ides][:29] == "alfa01{status{started-buyer14" or sh[ides][:29] == "alfa01{status{started-buyer-2" or sh[ides][:29] == "alfa01{status{started-buyer20" or sh[ides][:29] == "alfa01{status{started-buyer-3" or sh[ides][:29] == "alfa01{status{started-buyer30":
                                del sh[ides]
                            sh.close()
                            self.rendertextbrowser3()


                    else:
                        proc=True

                #when buyer cancel deal on step 2
                if message[0:29] == "alfa01{status{started-buyer20":
                    addrbuyer = fromAddress
                    addrmerchant = toAddress
                    try:
                        start = messageText.index('{cont{') + len('{cont{')
                        end = messageText.index('}cont}', start)
                        cont=messageText[start:end]
                    except ValueError:
                        error="sm error"
                        proc=False
                    try:
                        start = messageText.index('{cont2{') + len('{cont2{')
                        end = messageText.index('}cont2}', start)
                        cont2=messageText[start:end]
                    except ValueError:
                        error="sm error"
                        proc=False
                    if cont!=toAddress or cont2!=fromAddress:
                        proc=False
                    try:
                        start = messageText.index('{id{') + len('{id{')
                        end = messageText.index('}id}', start)
                        ides=messageText[start:end]
                    except ValueError:
                        error="id error"
                        proc=False

                    if proc:
                        if self.onlygoodsymbols(ides) and self.onlygoodsymbols(cont) and self.onlygoodsymbols(cont2):
                            sh2 = shelve.open('escrowm.slv')
                            if sh2[ides][:29] == "alfa01{status{started-buyer-2" or "alfa01{status{started-buyer-1" or "alfa01{status{started-buyer14" or "alfa01{status{started-buyer24" or "alfa01{status{started-buyer34" or "alfa01{status{started-buyer-3" or "alfa01{status{started-buyer-1":
                                del sh2[ides]
                            sh2.close()
                            self.rendertextbrowser2()


                    else:
                        proc=True

                if message[0:29] == "alfa01{status{started-buyer24":
                    addrbuyer = toAddress
                    addrmerchant = fromAddress
                    try:
                        start = messageText.index('{cont{') + len('{cont{')
                        end = messageText.index('}cont}', start)
                        cont=messageText[start:end]
                    except ValueError:
                        error="sm error"
                        proc=False
                    try:
                        start = messageText.index('{cont2{') + len('{cont2{')
                        end = messageText.index('}cont2}', start)
                        cont2=messageText[start:end]
                    except ValueError:
                        error="sm error"
                        proc=False
                    if cont2!=toAddress or cont!=fromAddress:
                        proc=False
                    try:
                        start = messageText.index('{id{') + len('{id{')
                        end = messageText.index('}id}', start)
                        ides=messageText[start:end]
                    except ValueError:
                        error="id error"
                        proc=False

                    if proc:
                        if self.onlygoodsymbols(ides) and self.onlygoodsymbols(cont) and self.onlygoodsymbols(cont2):
                            sh = shelve.open('escrow.slv')
                            if sh[ides][:29] == "alfa01{status{started-buyer-2" or sh[ides][:29] == "alfa01{status{started-buyer-1" or sh[ides][:29] == "alfa01{status{started-buyer-3" or sh[ides][:29] == "alfa01{status{started-buyer-4":
                                try:
                                    start = messageText.index('{private2{') + len('{private2{')
                                    end = messageText.index('}private2}', start)
                                    private2 = messageText[start:end]
                                except ValueError:
                                    error = ""
                                    private2 = ""
                                try:
                                    start = sh[ides].index('{escrowaddr2{') + len('{escrowaddr2{')
                                    end = sh[ides].index('}escrowaddr2}', start)
                                    esc2 = sh[ides][start:end]
                                except ValueError:
                                    error = ""
                                    esc2 = ""
                                if self.ui.autorescan.isChecked():
                                    try:
                                        MyForm.conn.importprivkey(private2, "DO NOT USE THIS ADDRESS", True)
                                    except:
                                        error= ""
                                else:
                                    try:
                                        MyForm.conn.importprivkey(private2, "DO NOT USE THIS ADDRESS", False)
                                    except:
                                        error= ""

                                a2 = MyForm.conn.validateaddress(esc2)

                                scam2 = False
                                for addre2 in a2.addresses:
                                    b2 = MyForm.conn.validateaddress(addre2)
                                    if b2.ismine == False:
                                        scam2 = True
                                        continue

                                if scam2:
                                    scam2=False
                                else:
                                    del sh[ides]
                                    sh.sync()



                            sh.close()
                            self.rendertextbrowser2()


                    else:
                        proc=True

                #when buyer cancel deal on step 3
                if message[0:29] == "alfa01{status{started-buyer30":
                    addrbuyer = toAddress
                    addrmerchant = fromAddress
                    try:
                        start = messageText.index('{cont{') + len('{cont{')
                        end = messageText.index('}cont}', start)
                        cont=messageText[start:end]
                    except ValueError:
                        error="sm error"
                        proc=False
                    try:
                        start = messageText.index('{cont2{') + len('{cont2{')
                        end = messageText.index('}cont2}', start)
                        cont2=messageText[start:end]
                    except ValueError:
                        error="sm error"
                        proc=False
                    if cont!=toAddress or cont2!=fromAddress:
                        proc=False
                    try:
                        start = messageText.index('{id{') + len('{id{')
                        end = messageText.index('}id}', start)
                        ides=messageText[start:end]
                    except ValueError:
                        error="id error"
                        proc=False

                    if proc:
                        if self.onlygoodsymbols(ides) and self.onlygoodsymbols(cont) and self.onlygoodsymbols(cont2):
                            sh2 = shelve.open('escrowm.slv')
                            if sh2[ides][:29] == "alfa01{status{started-buyer-3" or "alfa01{status{started-buyer34":
                                del sh2[ides]
                            sh2.close()
                            self.rendertextbrowser3()


                    else:
                        proc=True

                if message[0:29] == "alfa01{status{started-buyer34":
                    addrbuyer = fromAddress
                    addrmerchant = toAddress
                    try:
                        start = messageText.index('{cont{') + len('{cont{')
                        end = messageText.index('}cont}', start)
                        cont=messageText[start:end]
                    except ValueError:
                        error="sm error"
                        proc=False
                    try:
                        start = messageText.index('{cont2{') + len('{cont2{')
                        end = messageText.index('}cont2}', start)
                        cont2=messageText[start:end]
                    except ValueError:
                        error="sm error"
                        proc=False
                    if cont2!=toAddress or cont!=fromAddress:
                        proc=False
                    try:
                        start = messageText.index('{id{') + len('{id{')
                        end = messageText.index('}id}', start)
                        ides=messageText[start:end]
                    except ValueError:
                        error="id error"
                        proc=False

                    if proc:
                        if self.onlygoodsymbols(ides) and self.onlygoodsymbols(cont) and self.onlygoodsymbols(cont2):
                            sh = shelve.open('escrow.slv')
                            if sh[ides][:29] == "alfa01{status{started-buyer-3" or  "alfa01{status{started-buyer30":
                                del sh[ides]
                            sh.close()
                            self.rendertextbrowser3()


                    else:
                        proc=True

                if message[0:29] == "alfa01{status{started-buyer44":
                    addrbuyer = fromAddress
                    addrmerchant = toAddress
                    try:
                        start = messageText.index('{cont{') + len('{cont{')
                        end = messageText.index('}cont}', start)
                        cont=messageText[start:end]
                    except ValueError:
                        error="sm error"
                        proc=False
                    try:
                        start = messageText.index('{cont2{') + len('{cont2{')
                        end = messageText.index('}cont2}', start)
                        cont2=messageText[start:end]
                    except ValueError:
                        error="sm error"
                        proc=False
                    if cont2!=toAddress or cont!=fromAddress:
                        proc=False
                    try:
                        start = messageText.index('{id{') + len('{id{')
                        end = messageText.index('}id}', start)
                        ides=messageText[start:end]
                    except ValueError:
                        error="id error"
                        proc=False

                    try:
                        start = messageText.index('{private1{') + len('{private1{')
                        end = messageText.index('}private1}', start)
                        private1=messageText[start:end]
                    except ValueError:
                        error="id error"
                        proc=False


                    if proc:
                        if self.onlygoodsymbols(ides) and self.onlygoodsymbols(cont) and self.onlygoodsymbols(private1):
                            sh = shelve.open('escrow.slv')
                            if sh[ides][:29] == "alfa01{status{started-buyer-3" or sh[ides][:29] == "alfa01{status{started-buyer-4" or sh[ides][:29] == "alfa01{status{started-buyer40":
                                if self.ui.autorescan.isChecked():
                                    try:
                                        MyForm.conn.importprivkey(private1, "DO NOT USE THIS ADDRESS", True)
                                    except:
                                        error=""
                                else:
                                    try:
                                        MyForm.conn.importprivkey(private1, "DO NOT USE THIS ADDRESS", False)
                                    except:
                                        error=""

                                try:
                                    start = sh[ides].index('{escrowaddr1{') + len('{escrowaddr1{')
                                    end = sh[ides].index('}escrowaddr1}', start)
                                    esc1 = sh[ides][start:end]
                                except ValueError:
                                    error = ""
                                    esc1 = ""

                                a2 = MyForm.conn.validateaddress(esc1)

                                scam2 = False
                                for addre2 in a2.addresses:
                                    b2 = MyForm.conn.validateaddress(addre2)
                                    if b2.ismine == False:
                                        scam2 = True
                                        continue

                                if scam2:
                                    scam2=False
                                else:
                                    try:
                                        start = messageText.index('{badd2{') + len('{badd2{')
                                        end = messageText.index('}badd2}', start)
                                        badd2=messageText[start:end]
                                    except ValueError:
                                        badd2=""
                                    try:
                                        private2 = MyForm.conn.dumpprivkey(badd2)
                                    except:
                                        private2 = ""
                                    if private2!="":
                                        message = "alfa01{status{started-buyer45" + str(messageText[29:])
                                        subject = "cencel agree from buyer - private 2"
                                        self.sndmessage(message,subject,cont2,cont)
                                        del sh[ides]
                                        sh.sync()
                            sh.close()
                            self.rendertextbrowser2()


                    else:
                        proc=True

                if message[0:29] == "alfa01{status{started-buyer45":
                    addrbuyer = fromAddress
                    addrmerchant = toAddress
                    try:
                        start = messageText.index('{cont{') + len('{cont{')
                        end = messageText.index('}cont}', start)
                        cont=messageText[start:end]
                    except ValueError:
                        error="sm error"
                        proc=False
                    try:
                        start = messageText.index('{cont2{') + len('{cont2{')
                        end = messageText.index('}cont2}', start)
                        cont2=messageText[start:end]
                    except ValueError:
                        error="sm error"
                        proc=False
                    if cont2!=toAddress or cont!=fromAddress:
                        proc=False
                    try:
                        start = messageText.index('{id{') + len('{id{')
                        end = messageText.index('}id}', start)
                        ides=messageText[start:end]
                    except ValueError:
                        error="id error"
                        proc=False

                    try:
                        start = messageText.index('{private2{') + len('{private12{')
                        end = messageText.index('}private2}', start)
                        private2=messageText[start:end]
                    except ValueError:
                        error="id error"
                        proc=False


                    if proc:
                        if self.onlygoodsymbols(ides) and self.onlygoodsymbols(cont) and self.onlygoodsymbols(private2):
                            sh2 = shelve.open('escrowm.slv')
                            if sh2[ides][:29] == "alfa01{status{started-buyer44" or "alfa01{status{started-buyer40" or "alfa01{status{started-buyer41":
                                if self.ui.autorescan.isChecked():
                                    try:
                                        MyForm.conn.importprivkey(private2, "DO NOT USE THIS ADDRESS", True)
                                    except:
                                        error = ""
                                else:
                                    try:
                                        MyForm.conn.importprivkey(private2, "DO NOT USE THIS ADDRESS", False)
                                    except:
                                        error = ""


                                try:
                                    start = sh2[ides].index('{escrowaddr2{') + len('{escrowaddr2{')
                                    end = sh2[ides].index('}escrowaddr2}', start)
                                    esc2 = sh2[ides][start:end]
                                except ValueError:
                                    error = ""
                                    esc2 = ""

                                a2 = MyForm.conn.validateaddress(esc2)

                                scam2 = False
                                for addre2 in a2.addresses:
                                    b2 = MyForm.conn.validateaddress(addre2)
                                    if b2.ismine == False:
                                        scam2 = True
                                        continue

                                if scam2:
                                    scam2=False
                                else:
                                    del sh2[ides]
                                    sh2.sync()
                            sh2.close()
                            self.rendertextbrowser3()


                    else:
                        proc=True

                proc = True
                if message[0:29] == "alfa01{status{started-buyer54":
                    addrbuyer = fromAddress
                    addrmerchant = toAddress
                    try:
                        start = messageText.index('{cont{') + len('{cont{')
                        end = messageText.index('}cont}', start)
                        cont=messageText[start:end]
                    except ValueError:
                        error="cont error"
                        proc=False
                    try:
                        start = messageText.index('{cont2{') + len('{cont2{')
                        end = messageText.index('}cont2}', start)
                        cont2=messageText[start:end]
                    except ValueError:
                        error="cont2 error"
                        proc=False
                    try:
                        start = messageText.index('{id{') + len('{id{')
                        end = messageText.index('}id}', start)
                        ides=messageText[start:end]
                    except ValueError:
                        error="id error"
                        proc=False

                    try:
                        start = messageText.index('{private1{') + len('{private1{')
                        end = messageText.index('}private1}', start)
                        private1=messageText[start:end]
                    except ValueError:
                        error="id error"
                        proc=False

                    try:
                        start = messageText.index('{private3{') + len('{private3{')
                        end = messageText.index('}private3}', start)
                        private3 = messageText[start:end]
                    except ValueError:
                        error="id error"
                        proc=False

                    if proc:
                        if self.onlygoodsymbols(ides) and self.onlygoodsymbols(cont) and self.onlygoodsymbols(cont2) and self.onlygoodsymbols(private1) and self.onlygoodsymbols(private3):
                            sh = shelve.open('escrow.slv')
                            if sh[ides][:29] == "alfa01{status{started-buyer-4" or sh[ides][:29] == "alfa01{status{started-buyer-5" or sh[ides][:29] == "alfa01{status{started-buyer-6" or sh[ides][:29] == "alfa01{status{started-buyer-3" or sh[ides][:29] == "alfa01{status{started-buyer-2" or sh[ides][:29] == "alfa01{status{started-buyer50" or sh[ides][:29] == "alfa01{status{started-buyer51":
                                try:
                                    MyForm.conn.importprivkey(private1, "DO NOT USE THIS ADDRESS", False)
                                except:
                                    error=""
                                if self.ui.autorescan.isChecked():
                                    try:
                                        MyForm.conn.importprivkey(private3, "DO NOT USE THIS ADDRESS", True)
                                    except:
                                        error=""
                                else:
                                    try:
                                        MyForm.conn.importprivkey(private3, "DO NOT USE THIS ADDRESS", False)
                                    except:
                                        error=""

                                try:
                                    start = messageText.index('{badd2{') + len('{badd2{')
                                    end = messageText.index('}badd2}', start)
                                    badd2 = messageText[start:end]
                                except ValueError:
                                    error="id error"
                                    proc=False

                                message = "alfa01{status{started-buyer55" + str(messageText[29:])

                                subject = "cencel agree from buyer - private 2"
                                self.sndmessage(message,subject,cont2,cont)
                                del sh[ides]
                                sh.sync()
                            sh.close()
                            self.rendertextbrowser2()


                    else:
                        proc=True


                #when buyer cancel deal on step 3
                if message[0:29] == "alfa01{status{started-buyer40":
                    addrbuyer = fromAddress
                    addrmerchant = toAddress
                    try:
                        start = messageText.index('{cont{') + len('{cont{')
                        end = messageText.index('}cont}', start)
                        cont=messageText[start:end]
                    except ValueError:
                        error="sm error"
                        proc=False
                    try:
                        start = messageText.index('{cont2{') + len('{cont2{')
                        end = messageText.index('}cont2}', start)
                        cont2=messageText[start:end]
                    except ValueError:
                        error="sm error"
                        proc=False
                    if cont!=toAddress or cont2!=fromAddress:
                        proc=False
                    try:
                        start = messageText.index('{id{') + len('{id{')
                        end = messageText.index('}id}', start)
                        ides=messageText[start:end]
                    except ValueError:
                        error="id error"
                        proc=False

                    if proc:
                        if self.onlygoodsymbols(ides) and self.onlygoodsymbols(cont) and self.onlygoodsymbols(cont2):
                            sh2 = shelve.open('escrowm.slv')
                            if sh2[ides][:29] == "alfa01{status{started-buyer-4" or sh2[ides][:29] == "alfa01{status{started-buyer-5" or sh2[ides][:29] == "alfa01{status{started-buyer-3" or sh2[ides][:29] == "alfa01{status{started-buyer-2" or sh2[ides][:29] == "alfa01{status{started-buyer44":
                                try:
                                    start = messageText.index('{private2{') + len('{private2{')
                                    end = messageText.index('}private2}', start)
                                    private2=messageText[start:end]
                                except ValueError:
                                    error=""
                                    private2=""
                                if self.ui.autorescan.isChecked():
                                    try:
                                        MyForm.conn.importprivkey(private2, "DO NOT USE THIS ADDRESS", True)
                                    except:
                                        error=""
                                else:
                                    try:
                                        MyForm.conn.importprivkey(private2, "DO NOT USE THIS ADDRESS", False)
                                    except:
                                        error=""
                                messageText = sh2[ides]
                                try:
                                    start = messageText.index('{maddr1{') + len('{maddr1{')
                                    end = messageText.index('}maddr1}', start)
                                    maddr1=messageText[start:end]
                                except ValueError:
                                    error=""
                                    maddr1=""
                                try:
                                    private1 = MyForm.conn.dumpprivkey(maddr1)
                                except:
                                    private1=""
                                if private1!="":
                                    msg = "alfa01"+"{status{"+"started-buyer41"+"}status}" + str(messageText[37:]) + "{private1{" + str(private1) + "}private1}"

                                    subject = "cencel agree from merchant"

                                    self.sndmessage(msg,subject,cont,cont2)


                                    del sh2[ides]
                            sh2.close()

                            self.rendertextbrowser3()



                    else:
                        proc=True

                if message[0:29] == "alfa01{status{started-buyer50":
                    addrbuyer = fromAddress
                    addrmerchant = toAddress
                    try:
                        start = messageText.index('{cont{') + len('{cont{')
                        end = messageText.index('}cont}', start)
                        cont=messageText[start:end]
                    except ValueError:
                        error=""
                        proc=False
                    try:
                        start = messageText.index('{cont2{') + len('{cont2{')
                        end = messageText.index('}cont2}', start)
                        cont2=messageText[start:end]
                    except ValueError:
                        error=""
                        proc=False
                    if cont!=toAddress or cont2!=fromAddress:
                        proc=False
                    try:
                        start = messageText.index('{id{') + len('{id{')
                        end = messageText.index('}id}', start)
                        ides=messageText[start:end]
                    except ValueError:
                        error="id error"
                        proc=False

                    if proc:
                        if self.onlygoodsymbols(ides) and self.onlygoodsymbols(cont) and self.onlygoodsymbols(cont2):
                            sh2 = shelve.open('escrowm.slv')
                            if sh2[ides][:29] == "alfa01{status{started-buyer-5" or sh2[ides][:29] == "alfa01{status{started-buyer-4" or sh2[ides][:29] == "alfa01{status{started-buyer-6" or sh2[ides][:29] == "alfa01{status{started-buyer54":
                                try:
                                    start = messageText.index('{private2{') + len('{private2{')
                                    end = messageText.index('}private2}', start)
                                    private2=messageText[start:end]
                                except ValueError:
                                    error=""
                                    private2=""
                                if self.ui.autorescan.isChecked():
                                    try:
                                        MyForm.conn.importprivkey(private2, "DO NOT USE THIS ADDRESS", True)
                                    except:
                                        error=""
                                else:
                                    try:
                                        MyForm.conn.importprivkey(private2, "DO NOT USE THIS ADDRESS", False)
                                    except:
                                        error=""
                                messageText = sh2[ides]
                                try:
                                    start = messageText.index('{maddr1{') + len('{maddr1{')
                                    end = messageText.index('}maddr1}', start)
                                    maddr1=messageText[start:end]
                                except ValueError:
                                    error=""
                                    maddr1=""
                                try:
                                    private1 = MyForm.conn.dumpprivkey(maddr1)
                                except:
                                    private1 = ""
                                try:
                                    start = messageText.index('{maddr3{') + len('{maddr3{')
                                    end = messageText.index('}maddr3}', start)
                                    maddr3=messageText[start:end]
                                except ValueError:
                                    error=""
                                    maddr3=""
                                try:
                                    private3 = MyForm.conn.dumpprivkey(maddr3)
                                except:
                                    private3 = ""
                                if private1!="" and private3!="":
                                    msg = "alfa01"+"{status{"+"started-buyer51"+"}status}" + str(messageText[37:]) + "{private1{" + str(private1) + "}private1}"+"{private3{" + str(private3) + "}private3}"
                                    subject = "cencel agree from merchant"
                                    self.sndmessage(msg,subject,cont,cont2)
                                    del sh2[ides]
                            sh2.close()
                            self.rendertextbrowser3()


                    else:
                        proc=True


                if message[0:29] == "alfa01{status{started-buyer60":
                    addrbuyer = fromAddress
                    addrmerchant = toAddress
                    try:
                        start = messageText.index('{cont{') + len('{cont{')
                        end = messageText.index('}cont}', start)
                        cont=messageText[start:end]
                    except ValueError:
                        error=""
                        proc=False
                    try:
                        start = messageText.index('{cont2{') + len('{cont2{')
                        end = messageText.index('}cont2}', start)
                        cont2=messageText[start:end]
                    except ValueError:
                        error=""
                        proc=False
                    if cont!=toAddress or cont2!=fromAddress:
                        proc=False
                    try:
                        start = messageText.index('{id{') + len('{id{')
                        end = messageText.index('}id}', start)
                        ides=messageText[start:end]
                    except ValueError:
                        error="id error"
                        proc=False
                    if proc:
                        if self.onlygoodsymbols(ides) and self.onlygoodsymbols(cont) and self.onlygoodsymbols(cont2):
                            sh2 = shelve.open('escrowm.slv')
                            if sh2[ides][:29] == "alfa01{status{started-buyer-6" or sh2[ides][:29] == "alfa01{status{started-buyer-5" or sh2[ides][:29] == "alfa01{status{started-buyer64":
                                messageText = sh2[ides]
                                try:
                                    start = messageText.index('{maddr1{') + len('{maddr1{')
                                    end = messageText.index('}maddr1}', start)
                                    maddr1=messageText[start:end]
                                except ValueError:
                                    error=""
                                    maddr1=""
                                try:
                                    private3 = MyForm.conn.dumpprivkey(maddr1)
                                except:
                                    private3=""
                                if private3!="":
                                    msg = "alfa01"+"{status{"+"started-buyer61"+"}status}" + str(messageText[37:]) + "{private3{"+str(private3)+"}private3}"
                                    sh2[ides] = msg
                            sh2.close()
                            self.rendertextbrowser3()
                    else:
                        proc=True

                if message[0:29] == "alfa01{status{started-buyer61":
                    addrbuyer = toAddress
                    addrmerchant = fromAddress
                    try:
                        start = messageText.index('{cont{') + len('{cont{')
                        end = messageText.index('}cont}', start)
                        cont=messageText[start:end]
                    except ValueError:
                        error=""
                        proc=False
                    try:
                        start = messageText.index('{cont2{') + len('{cont2{')
                        end = messageText.index('}cont2}', start)
                        cont2=messageText[start:end]
                    except ValueError:
                        error=""
                        proc=False
                    if cont!=fromAddress or cont2!=toAddress:
                        proc=False
                    try:
                        start = messageText.index('{id{') + len('{id{')
                        end = messageText.index('}id}', start)
                        ides=messageText[start:end]
                    except ValueError:
                        error="id error"
                        proc=False
                    try:
                        start = messageText.index('{private3{') + len('{private3{')
                        end = messageText.index('}private3}', start)
                        private3=messageText[start:end]
                    except ValueError:
                        error="id error"
                        proc=False
                    if proc:
                        if self.onlygoodsymbols(ides) and self.onlygoodsymbols(cont) and self.onlygoodsymbols(cont2):
                            sh = shelve.open('escrow.slv')
                            if self.ui.autorescan.isChecked():
                                try:
                                    MyForm.conn.importprivkey(private3, "DO NOT USE THIS ADDRESS", True)
                                except:
                                    error=""
                            else:
                                try:
                                    MyForm.conn.importprivkey(private3, "DO NOT USE THIS ADDRESS", False)
                                except:
                                    error=""
                            if sh[ides][:29] == "alfa01{status{started-buyer60":
                                messageText = sh[ides]
                                try:
                                    start = messageText.index('{badd2{') + len('{badd2{')
                                    end = messageText.index('}badd2}', start)
                                    badd2=messageText[start:end]
                                except ValueError:
                                    error=""
                                    badd2=""
                                try:
                                    private2 = MyForm.conn.dumpprivkey(badd2)
                                except:
                                    private2=""
                                if private2!="":
                                    msg = "alfa01{status{started-buyer62}status}"+str(messageText[37:])+"{private2{"+str(private2)+"}private2}"
                                    self.sndmessage(msg,subject,cont2,cont)
                                    sh[ides] = msg
                                    sh.sync()
                            sh.close()
                            self.rendertextbrowser2()
                    else:
                        proc=True

                if message[0:29] == "alfa01{status{started-buyer62":
                    try:
                        start = messageText.index('{cont{') + len('{cont{')
                        end = messageText.index('}cont}', start)
                        cont=messageText[start:end]
                    except ValueError:
                        error=""
                        proc=False
                    try:
                        start = messageText.index('{cont2{') + len('{cont2{')
                        end = messageText.index('}cont2}', start)
                        cont2=messageText[start:end]
                    except ValueError:
                        error=""
                        proc=False
                    if cont!=toAddress or cont2!=fromAddress:
                        proc=False
                    try:
                        start = messageText.index('{id{') + len('{id{')
                        end = messageText.index('}id}', start)
                        ides=messageText[start:end]
                    except ValueError:
                        error="id error"
                        proc=False
                    try:
                        start = messageText.index('{private2{') + len('{private2{')
                        end = messageText.index('}private2}', start)
                        private2=messageText[start:end]
                    except ValueError:
                        error="id error"
                        proc=False

                    if proc:
                        if self.onlygoodsymbols(ides) and self.onlygoodsymbols(cont) and self.onlygoodsymbols(cont2):
                            sh2 = shelve.open('escrowm.slv')
                            if self.ui.autorescan.isChecked():
                                try:
                                    MyForm.conn.importprivkey(private2, "DO NOT USE THIS ADDRESS", True)
                                except:
                                    error=""
                            else:
                                try:
                                    MyForm.conn.importprivkey(private2, "DO NOT USE THIS ADDRESS", False)
                                except:
                                    error=""
                            if sh2[ides][:29] == "alfa01{status{started-buyer61":
                                messageText = sh2[ides]
                                try:
                                    start = messageText.index('{maddr1{') + len('{maddr1{')
                                    end = messageText.index('}maddr1}', start)
                                    badd1 = messageText[start:end]
                                except ValueError:
                                    error=""
                                    badd1=""
                                try:
                                    private1 = MyForm.conn.dumpprivkey(badd1)
                                except:
                                    private1 = ""
                                if private1!="":
                                    msg = "alfa01{status{started-buyer63}status}"+str(messageText[37:])+"{private1{"+str(private1)+"}private1}"
                                    self.sndmessage(msg,subject,cont,cont2)
                                    del sh2[ides]
                            sh2.close()
                            self.rendertextbrowser3()
                    else:
                        proc=True


                if message[0:29] == "alfa01{status{started-buyer63":
                    addrbuyer = toAddress
                    addrmerchant = fromAddress
                    try:
                        start = messageText.index('{cont{') + len('{cont{')
                        end = messageText.index('}cont}', start)
                        cont=messageText[start:end]
                    except ValueError:
                        error=""
                        proc=False
                    try:
                        start = messageText.index('{cont2{') + len('{cont2{')
                        end = messageText.index('}cont2}', start)
                        cont2=messageText[start:end]
                    except ValueError:
                        error=""
                        proc=False
                    if cont!=toAddress or cont2!=fromAddress:
                        proc=False
                    try:
                        start = messageText.index('{id{') + len('{id{')
                        end = messageText.index('}id}', start)
                        ides=messageText[start:end]
                    except ValueError:
                        error="id error"
                        proc=False
                    try:
                        start = messageText.index('{private1{') + len('{private1{')
                        end = messageText.index('}private1}', start)
                        private1=messageText[start:end]
                    except ValueError:
                        error="id error"
                        proc=False
                    if proc:
                        if self.onlygoodsymbols(ides) and self.onlygoodsymbols(cont) and self.onlygoodsymbols(cont2):
                            sh = shelve.open('escrow.slv')
                            if self.ui.autorescan.isChecked():
                                try:
                                    MyForm.conn.importprivkey(private1, "DO NOT USE THIS ADDRESS", True)
                                except:
                                    error=""
                            else:
                                try:
                                    MyForm.conn.importprivkey(private1, "DO NOT USE THIS ADDRESS", False)
                                except:
                                    error=""
                            if sh[ides][:29] == "alfa01{status{started-buyer62":
                                #if is mine
                                del sh[ides]
                                sh.sync()
                            sh.close()
                            self.rendertextbrowser2()
                    else:
                        proc=True


        #merchant cancel deal on lvl 6

                if message[0:29] == "alfa01{status{started-buyer64":
                    addrbuyer = toAddress
                    addrmerchant = fromAddress
                    try:
                        start = messageText.index('{cont{') + len('{cont{')
                        end = messageText.index('}cont}', start)
                        cont=messageText[start:end]
                    except ValueError:
                        error=""
                        proc=False
                    try:
                        start = messageText.index('{cont2{') + len('{cont2{')
                        end = messageText.index('}cont2}', start)
                        cont2=messageText[start:end]
                    except ValueError:
                        error=""
                        proc=False
                    if cont!=toAddress or cont2!=fromAddress:
                        proc=False
                    try:
                        start = messageText.index('{id{') + len('{id{')
                        end = messageText.index('}id}', start)
                        ides=messageText[start:end]
                    except ValueError:
                        error="id error"
                        proc=False
                    try:
                        start = messageText.index('{private1{') + len('{private1{')
                        end = messageText.index('}private1}', start)
                        private1=messageText[start:end]
                    except ValueError:
                        error="id error"
                        proc=False

                    try:
                        start = messageText.index('{private3{') + len('{private3')
                        end = messageText.index('}private3}', start)
                        private3=messageText[start:end]
                    except ValueError:
                        error="id error"
                        proc=False

                    if proc:
                        if self.onlygoodsymbols(ides) and self.onlygoodsymbols(cont) and self.onlygoodsymbols(cont2):
                            sh = shelve.open('escrow.slv')
                            if self.ui.autorescan.isChecked():
                                try:
                                    MyForm.conn.importprivkey(private1, "DO NOT USE THIS ADDRESS", True)
                                except:
                                    error=""
                            else:
                                try:
                                    MyForm.conn.importprivkey(private1, "DO NOT USE THIS ADDRESS", False)
                                except:
                                    error=""
                            if sh[ides][:29] == "alfa01{status{started-buyer-6" or "alfa01{status{started-buyer60":
                                #if is mine
                                try:
                                    start = messageText.index('{badd2{') + len('{badd2{')
                                    end = messageText.index('}badd2}', start)
                                    badd2=messageText[start:end]
                                except ValueError:
                                    error=""
                                    badd2=""
                                try:
                                    private2 = MyForm.conn.dumpprivkey(badd2)
                                except:
                                    private2 = ""
                                if private2!="":
                                    msg = "alfa01{status{started-buyer65}status}"+str(messageText[37:])+"{private2{"+str(private2)+"}private2}"
                                    self.sndmessage(msg,subject,cont2,cont)
                                    del sh[ides]
                                    sh.sync()
                            sh.close()
                            self.rendertextbrowser2()
                    else:
                        proc=True

                #merchant start cancel merchant recieve

                if message[0:29] == "alfa01{status{started-buyer65":
                    addrbuyer = toAddress
                    addrmerchant = fromAddress
                    try:
                        start = messageText.index('{cont{') + len('{cont{')
                        end = messageText.index('}cont}', start)
                        cont=messageText[start:end]
                    except ValueError:
                        error=""
                        proc=False
                    try:
                        start = messageText.index('{cont2{') + len('{cont2{')
                        end = messageText.index('}cont2}', start)
                        cont2=messageText[start:end]
                    except ValueError:
                        error=""
                        proc=False
                    if cont2!=toAddress or cont!=fromAddress:
                        proc=False
                    try:
                        start = messageText.index('{id{') + len('{id{')
                        end = messageText.index('}id}', start)
                        ides=messageText[start:end]
                    except ValueError:
                        error="id error"
                        proc=False
                    try:
                        start = messageText.index('{private2{') + len('{private2{')
                        end = messageText.index('}private2}', start)
                        private2=messageText[start:end]
                    except ValueError:
                        error="id error"
                        proc=False

                    if proc:
                        if self.onlygoodsymbols(ides) and self.onlygoodsymbols(cont) and self.onlygoodsymbols(cont2):
                            sh2 = shelve.open('escrowm.slv')
                            if self.ui.autorescan.isChecked():
                                try:
                                    MyForm.conn.importprivkey(private2, "DO NOT USE THIS ADDRESS", True)
                                except:
                                    error=""
                            else:
                                try:
                                    MyForm.conn.importprivkey(private2, "DO NOT USE THIS ADDRESS", False)
                                except:
                                    error=""
                            if sh2[ides][:29] == "alfa01{status{started-buyer64":
                                #if is mine
                                del sh2[ides]
                            sh2.close()
                            self.rendertextbrowser3()
                    else:
                        proc=True





                #when get message with addresses from merchant

                if message[0:29] == "alfa01{status{started-buyer-2":
                    addrbuyer = toAddress
                    addrmerchant = fromAddress

                    try:
                        start = messageText.index('{cont2{') + len('{cont2{')
                        end = messageText.index('}cont2}', start)
                        cont=messageText[start:end]
                    except ValueError:
                        error="sm error"
                        proc=False
                    if cont!=toAddress:
                        proc=False
                    try:
                        start = messageText.index('{bitadr{') + len('{bitadr{')
                        end = messageText.index('}bitadr}', start)
                        buy1=messageText[start:end]
                    except ValueError:
                        error="sm error"
                        proc=False
                    try:
                        start = messageText.index('{bitadins1{') + len('{bitadins1{')
                        end = messageText.index('}bitadins1}', start)
                        buy2=messageText[start:end]
                    except ValueError:
                        error="bitcoin address error"
                        proc=False
                    try:
                        start = messageText.index('{bitadins2{') + len('{bitadins2{')
                        end = messageText.index('}bitadins2}', start)
                        buy3=messageText[start:end]
                    except ValueError:
                        error="bitcoin address error"
                        proc=False
                    try:
                        start = messageText.index('{id{') + len('{id{')
                        end = messageText.index('}id}', start)
                        idescrow3=messageText[start:end]
                    except ValueError:
                        error="id error"
                        proc=False
                    try:
                        start = messageText.index('{amount{') + len('{amount{')
                        end = messageText.index('}amount}', start)
                        amount=messageText[start:end]
                    except ValueError:
                        error="id error"
                        proc=False
                    try:
                        start = messageText.index('{escrowaddr1{') + len('{escrowaddr1{')
                        end = messageText.index('}escrowaddr1}', start)
                        esc1=messageText[start:end]
                    except ValueError:
                        error="id error"
                        proc=False
                    try:
                        start = messageText.index('{escrowaddr2{') + len('{escrowaddr2{')
                        end = messageText.index('}escrowaddr2}', start)
                        esc2=messageText[start:end]
                    except ValueError:
                        error="id error"
                        proc=False
                    try:
                        start = messageText.index('{escrowaddr3{') + len('{escrowaddr3{')
                        end = messageText.index('}escrowaddr3}', start)
                        esc3=messageText[start:end]
                    except ValueError:
                        error="id error"
                        proc=False


                    data_file = 'escrow.slv'
                    sh = shelve.open(data_file)
                    asc = False
                    if idescrow3 in sh.keys():
                        if sh[idescrow3][0:29] == "alfa01{status{started-buyer-1":
                            asc = True
                        else:
                            asc = False
                            self.statusBar().showMessage(_translate(
                                    "MainWindow", "Warning: Your just received merchant escrow message with not exitsted id."))
                    sh.close()
                    if proc and asc:
                        if self.onlygoodsymbols(buy1) and self.onlygoodsymbols(buy2) and self.onlygoodsymbols(buy3) and self.onlygoodsymbols(idescrow3):
                            sh = shelve.open('escrow.slv')
                            if idescrow3 not in sh.keys():
                                self.statusBar().showMessage(_translate(
                                    "MainWindow", "Warning: Your just received merchant escrow message with not exitsted id."))
                                sh.close()
                            else:
                                verifyescrows = sh[idescrow3]

                                try:
                                    start = verifyescrows.index('{lbl{') + len('{lbl{')
                                    end = verifyescrows.index('}lbl}', start)
                                    lbl=verifyescrows[start:end]
                                except ValueError:
                                    lbl=""
                                try:
                                    start = messageText.index('{amount{') + len('{amount{')
                                    end = messageText.index('}amount}', start)
                                    amount11=messageText[start:end]
                                except ValueError:
                                    amount11=""
                                    proc = False

                                if amount11 != amount:
                                    proc = False

                                if len(lbl)>50:
                                    lbl = lbl[:50]

                                if self.onlygoodsymbols(lbl) and proc:
                                    proc2=True
                                    try:
                                        start = verifyescrows.index('{bitadr{') + len('{bitadr{')
                                        end = verifyescrows.index('}bitadr}', start)
                                        adr1=verifyescrows[start:end]
                                    except ValueError:
                                        error="sm error"
                                        proc2=False
                                    try:
                                        start = verifyescrows.index('{bitadins1{') + len('{bitadins1{')
                                        end = verifyescrows.index('}bitadins1}', start)
                                        adr2=verifyescrows[start:end]
                                    except ValueError:
                                        error="bitcoin address error"
                                        proc2=False
                                    try:
                                        start = verifyescrows.index('{bitadins2{') + len('{bitadins2{')
                                        end = verifyescrows.index('}bitadins2}', start)
                                        adr3=verifyescrows[start:end]
                                    except ValueError:
                                        error="bitcoin address error"
                                        proc2=False

                                    escrowaddr1=MyForm.conn.addmultisigaddress(2,[adr1,buy1],idescrow3)
                                    escrowaddr2=MyForm.conn.addmultisigaddress(2,[adr2,buy2],idescrow3)
                                    escrowaddr3=MyForm.conn.addmultisigaddress(2,[adr3,buy3],idescrow3)


                                    if escrowaddr1!=esc1 or escrowaddr2!=esc2 or escrowaddr3!=esc3:
                                        proc2=False
                                    else:
                                        savemsg=sh[idescrow3]
                                        try:
                                            start = savemsg.index('{badd3{') + len('{badd3{')
                                            end = savemsg.index('}badd3}', start)
                                            badd3 = savemsg[start:end]
                                        except ValueError:
                                            error=''
                                            proc2=False
                                        try:
                                            start = savemsg.index('{badd1{') + len('{badd1{')
                                            end = savemsg.index('}badd1}', start)
                                            badd1 = savemsg[start:end]
                                        except ValueError:
                                            error=''
                                            proc2=False
                                        try:
                                            start = savemsg.index('{badd2{') + len('{badd2{')
                                            end = savemsg.index('}badd2}', start)
                                            badd2 = savemsg[start:end]
                                        except ValueError:
                                            error=''
                                            proc2=False
                                        try:
                                            start = sh[idescrow3].index('{comment{') + len('{comment{')
                                            end = sh[idescrow3].index('}comment}', start)
                                            comment = sh[idescrow3][start:end]
                                        except ValueError:
                                            error=''
                                            proc2=False
                                        messageesc = "alfa01"+"{status{"+"started-buyer-3"+"}status}"+str(savemsg[37:])+"{cont2{"+str(cont)+"}cont2}"+"{escrowaddr1{"+str(escrowaddr1)+'}escrowaddr1}'+'{escrowaddr2{'+str(escrowaddr2)+'}escrowaddr2}'+'{escrowaddr3{'+str(escrowaddr3)+'}escrowaddr3}'+"{badd3{"+str(badd3)+"}badd3}"+"{badd1{"+str(badd1)+"}badd1}"+"{badd2{"+str(badd2)+"}badd2}"+ '{comment{' + comment + '}comment}'

                                        sh[idescrow3] = messageesc
                                        proc2=True
                                        sh.sync()
                                        #send 1st insurance payment from buyer
                                        blc=0
                                        txid=""
                                        try:
                                            blc=MyForm.conn.getbalance()
                                        except:
                                            blc=0
                                        sendResult1=False
                                        try:
                                            txid=MyForm.conn.sendtoaddress(esc1,float(amount11)*0.05)
                                            sendResult1=True
                                        except:
                                            sendResult1=False
                                        if sendResult1 and txid != "":
                                            messageesc = "alfa01"+"{status{"+"started-buyer-4"+"}status}" + str(messageesc[37:])+"{txid1{"+str(txid)+"}txid1}"
                                            sh[idescrow3] = messageesc
                                            sh.sync()
                                            self.buyerpay1(messageesc, fromAddress, toAddress)

                                        elif blc < float(amount11)*0.05:
                                            self.statusBar().showMessage(_translate(
                                                "MainWindow", "Insufficient funds! You can try pay manualy."))
                                            messageesc = "alfa01"+"{status{"+"started-buyer04"+"}status}" + str(messageesc[37:])
                                            sh[idescrow3] = messageesc
                                            sh.sync()

                                        else:
                                            messageesc = "alfa01"+"{status{"+"started-buyer04"+"}status}"+str(messageesc[37:])
                                            sh[idescrow3] = messageesc
                                            sh.sync()
                                            self.statusBar().showMessage(_translate(
                                                "MainWindow", "Warning: Bitcoin error. Try to restart bitcoin client."))
                                        sh.sync()
                                        self.rendertextbrowser2()
                                sh.close()




                    else:
                        proc=True
                        sh.close()

                #buyer send payment and merchant recieve message with txid
                if message[0:29] == "alfa01{status{started-buyer-4":
                    try:
                        start = messageText.index('{id{') + len('{id{')
                        end = messageText.index('}id}', start)
                        id = messageText[start:end]
                    except ValueError:
                        error = ''
                    try:
                        start = messageText.index('{txid1{') + len('{txid1{')
                        end = messageText.index('}txid1}', start)
                        txid = messageText[start:end]
                    except ValueError:
                        error = ''
                    try:
                        sh2 = shelve.open("escrowm.slv")
                        messageText = sh2[id]

                        if sh2[id][0:29] == "alfa01{status{started-buyer-2":
                            try:
                                start = messageText.index('{escrowaddr1{') + len('{escrowaddr1{')
                                end = messageText.index('}escrowaddr1}', start)
                                esc1 = messageText[start:end]
                            except ValueError:
                                error = ""
                            try:
                                start = messageText.index('{amount{') + len('{amount{')
                                end = messageText.index('}amount}', start)
                                amount = messageText[start:end]
                            except ValueError:
                                error = ""

                            chk1payment = shelve.open("chk1pay.slv")
                            chk1payment[id] = [txid, esc1, amount]
                            chk1payment.close()
                            sh2[id] = "alfa01{status{started-buyer-4" + str(sh2[id][29:]) + "{txid1{" + str(txid) + "}txid1}"
                        sh2.close()
                    except:
                        error=""




                #merchant send payment and buyer recieve message with txid
                if message[0:29] == "alfa01{status{started-buyer-5":
                    try:
                        start = messageText.index('{id{') + len('{id{')
                        end = messageText.index('}id}', start)
                        id = messageText[start:end]
                    except ValueError:
                        error = ''
                    try:
                        start = messageText.index('{txid2{') + len('{txid2{')
                        end = messageText.index('}txid2}', start)
                        txid2 = messageText[start:end]
                    except ValueError:
                        error = ''
                    sh = shelve.open("escrow.slv")
                    messageText = sh[id]

                    if sh[id][0:29] == "alfa01{status{started-buyer-4" or sh[id][0:29] == "alfa01{status{started-buyer-3" or sh[id][0:29] == "alfa01{status{started-buyer-04":
                        try:
                            start = messageText.index('{escrowaddr2{') + len('{escrowaddr2{')
                            end = messageText.index('}escrowaddr2}', start)
                            esc2 = messageText[start:end]
                        except ValueError:
                            error = ""
                        try:
                            start = messageText.index('{amount{') + len('{amount{')
                            end = messageText.index('}amount}', start)
                            amount = messageText[start:end]
                        except ValueError:
                            error = ""

                        chk2payment = shelve.open("chk2pay.slv")
                        chk2payment[id] = [txid2, esc2, amount]
                        chk2payment.close()
                        sh[id] = "alfa01{status{started-buyer-5" + str(sh[id][29:]) + "{txid2{" + str(txid2) + "}txid2}"
                    sh.close()

                #merchant get message main payment sent
                if message[0:29] == "alfa01{status{started-buyer-6":
                    try:
                        start = messageText.index('{id{') + len('{id{')
                        end = messageText.index('}id}', start)
                        id = messageText[start:end]
                    except ValueError:
                        error = ''
                    try:
                        start = messageText.index('{txid3{') + len('{txid3{')
                        end = messageText.index('}txid3}', start)
                        txid3 = messageText[start:end]
                    except ValueError:
                        error = ''
                    sh2 = shelve.open("escrowm.slv")
                    messageText = sh2[id]

                    if sh2[id][0:29] == "alfa01{status{started-buyer-5":
                        try:
                            start = messageText.index('{escrowaddr3{') + len('{escrowaddr3{')
                            end = messageText.index('}escrowaddr3}', start)
                            esc3 = messageText[start:end]
                        except ValueError:
                            error = ""
                        try:
                            start = messageText.index('{amount{') + len('{amount{')
                            end = messageText.index('}amount}', start)
                            amount = messageText[start:end]
                        except ValueError:
                            error = ""

                        chk3payment = shelve.open("chk3pay.slv")
                        chk3payment[id] = [txid3, esc3, amount]
                        chk3payment.close()
                        sh2[id] = "alfa01{status{started-buyer-6" + str(sh2[id][29:]) + "{txid3{" + str(txid3) + "}txid3}"
                    sh2.close()






                #when receive that buyer had signed deal
                if message[0:29] == "alfa01{status{started-buyer-7":
                    addrbuyer = toAddress
                    addrmerchant = fromAddress
                    try:
                        start = messageText.index('{id{') + len('{id{')
                        end = messageText.index('}id}', start)
                        ids = messageText[start:end]
                    except ValueError:
                        error = ''
                    try:
                        start = messageText.index('{private1{') + len('{private1{')
                        end = messageText.index('}private1}', start)
                        private1 = messageText[start:end]
                    except ValueError:
                        error = ''
                        private1 = ""
                    try:
                        start = messageText.index('{private3{') + len('{private3{')
                        end = messageText.index('}private3}', start)
                        private3 = messageText[start:end]
                    except ValueError:
                        error = ''
                        private3 = ""

                    sh2 = shelve.open("escrowm.slv")

                    if sh2[ids][0:29] == "alfa01{status{started-buyer-6":
                        try:
                            MyForm.conn.importprivkey(private1, "DO NOT USE THIS ADDRESS", False)
                        except:
                            error=''
                        if self.ui.autorescan.isChecked():
                            try:
                                MyForm.conn.importprivkey(private3, "DO NOT USE THIS ADDRESS", True)
                            except:
                                error=''
                        else:
                            try:
                                MyForm.conn.importprivkey(private3, "DO NOT USE THIS ADDRESS", False)
                            except:
                                error=''

                        messageText3 = sh2[ids]
                        try:
                            start = messageText3.index('{escrowaddr1{') + len('{escrowaddr1{')
                            end = messageText3.index('}escrowaddr1}', start)
                            esc1 = messageText3[start:end]
                        except ValueError:
                            error=""
                        try:
                            start = messageText3.index('{escrowaddr2{') + len('{escrowaddr2{')
                            end = messageText3.index('}escrowaddr2}', start)
                            esc2 = messageText3[start:end]
                        except ValueError:
                            error=""
                        try:
                            start = messageText3.index('{escrowaddr3{') + len('{escrowaddr3{')
                            end = messageText3.index('}escrowaddr3}', start)
                            esc3 = messageText3[start:end]
                        except ValueError:
                            error=""

                        try:
                            start = messageText3.index('{maddr2{') + len('{maddr2{')
                            end = messageText3.index('}maddr2}', start)
                            addrs2 = messageText3[start:end]
                        except ValueError:
                            error=""

                        a1 = MyForm.conn.validateaddress(esc1)
                        a3 = MyForm.conn.validateaddress(esc3)

                        scam = False
                        for addre in a1.addresses:
                            b1 = MyForm.conn.validateaddress(addre)
                            if b1.ismine == False:
                                scam = True
                                continue
                        for addre3 in a3.addresses:
                            b3 = MyForm.conn.validateaddress(addre3)
                            if b3.ismine == False:
                                scam = True
                                continue

                        if scam == False:
                            try:
                                private2 = MyForm.conn.dumpprivkey(addrs2)
                            except:
                                private2 = ""

                            if private2!="":
                                try:
                                    start = messageText3.index('{cont{') + len('{cont{')
                                    end = messageText3.index('}cont}', start)
                                    fromAddress=messageText3[start:end]
                                except ValueError:
                                    error=''
                                try:
                                    start = messageText3.index('{cont2{') + len('{cont2{')
                                    end = messageText3.index('}cont2}', start)
                                    toAddress=messageText3[start:end]
                                except ValueError:
                                    error=''
                                message = "alfa01{status{started-buyer-8"+ str(messageText3[29:])+"{private2{"+str(private2)+"}private2}"
                                subject = "Last actions for finish escrow deal"
                                sh2[ids] = message
                                sh2.sync()
                                status, addressVersionNumber, streamNumber, ripe = decodeAddress(toAddress)
                                ackdata = OpenSSL.rand(32)

                                t = ()
                                sqlExecute(
                                    '''INSERT INTO sent VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                                    '',
                                    toAddress,
                                    ripe,
                                    fromAddress,
                                    subject,
                                    message,
                                    ackdata,
                                    int(time.time()),
                                    'msgqueued',
                                    1,
                                    1,
                                    'sent',
                                    2)

                                toLabel = ''
                                queryreturn = sqlQuery('''select label from addressbook where address=?''',
                                                        toAddress)
                                if queryreturn != []:
                                    for row in queryreturn:
                                        toLabel, = row

                                self.displayNewSentMessage(
                                    toAddress, toLabel, fromAddress, subject, message, ackdata)
                                shared.workerQueue.put(('sendmessage', toAddress))
                                sh2[ids] = message
                                sh2.sync()
                    sh2.close()

                if message[0:29] == "alfa01{status{started-buyer-8":
                    addrbuyer = fromAddress
                    addrmerchant = toAddress
                    try:
                        start = messageText.index('{id{') + len('{id{')
                        end = messageText.index('}id}', start)
                        id = messageText[start:end]
                    except ValueError:
                        error = ''
                    try:
                        start = messageText.index('{private2{') + len('{private2{')
                        end = messageText.index('}private2}', start)
                        private2 = messageText[start:end]
                    except ValueError:
                        error = ''
                        private2 = ""
                    sh = shelve.open("escrow.slv")
                    sss = sh[id]
                    if sh[id][0:29] == "alfa01{status{started-buyer-7":
                        sh[id] = messageText
                        try:
                            start = messageText.index('{escrowaddr1{') + len('{escrowaddr1{')
                            end = messageText.index('}escrowaddr1}', start)
                            esc1 = messageText[start:end]
                        except ValueError:
                            error=""
                        try:
                            start = messageText.index('{escrowaddr2{') + len('{escrowaddr2{')
                            end = messageText.index('}escrowaddr2}', start)
                            esc2 = messageText[start:end]
                        except ValueError:
                            error=""
                        try:
                            start = messageText.index('{escrowaddr3{') + len('{escrowaddr3{')
                            end = messageText.index('}escrowaddr3}', start)
                            esc3 = messageText[start:end]
                        except ValueError:
                            error=""


                        if self.ui.autorescan.isChecked():
                            try:
                                MyForm.conn.importprivkey(private2, "DO NOT USE THIS ADDRESS", True)
                            except:
                                error=''
                        else:
                            try:
                                MyForm.conn.importprivkey(private2, "DO NOT USE THIS ADDRESS", False)
                            except:
                                error=''

                        a2 = MyForm.conn.validateaddress(esc2)

                        scam2 = False
                        for addre2 in a2.addresses:
                            b2 = MyForm.conn.validateaddress(addre2)
                            if b2.ismine == False:
                                scam2 = True
                                continue


                        if scam2 == False:
                            try:
                                start = messageText.index('{cont{') + len('{cont{')
                                end = messageText.index('}cont}', start)
                                toAddress=messageText[start:end]
                            except ValueError:
                                error=''
                            try:
                                start = messageText.index('{cont2{') + len('{cont2{')
                                end = messageText.index('}cont2}', start)
                                fromAddress=messageText[start:end]
                            except ValueError:
                                error=''
                            message = "alfa01{status{started-buyer-9"+ str(messageText[29:])
                            subject = "Last actions for finish escrow deal"
                            status, addressVersionNumber, streamNumber, ripe = decodeAddress(toAddress)
                            ackdata = OpenSSL.rand(32)
                            t = ()
                            sqlExecute(
                                '''INSERT INTO sent VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                                '',
                                toAddress,
                                ripe,
                                fromAddress,
                                subject,
                                message,
                                ackdata,
                                int(time.time()),
                                'msgqueued',
                                1,
                                1,
                                'sent',
                                2)

                            toLabel = ''
                            queryreturn = sqlQuery('''select label from addressbook where address=?''',
                                                    toAddress)
                            if queryreturn != []:
                                for row in queryreturn:
                                    toLabel, = row

                            self.displayNewSentMessage(
                                toAddress, toLabel, fromAddress, subject, message, ackdata)
                            shared.workerQueue.put(('sendmessage', toAddress))
                            sh[id] = message
                            sh.sync()
                    sh.close()

                self.rendertextbrowser2()
                self.rendertextbrowser3()
                #changes end



    def addtotemp(self, txid1, subject, senderaddress, messageText):
        tmp = shelve.open("temp.slv")
        if len(tmp)<100:
            now_time = str(datetime.datetime.now())
            tmp[senderaddress] = [txid1,subject,messageText, now_time]
        else:
            tmp.clear()
        tmp.close()

    def every600sec(self):
        try:
            tmp = shelve.open("temp.slv")
            for i in tmp:
                senderaddress = i
                now_time = datetime.datetime.now()
                time = datetime.datetime.strptime(tmp[senderaddress][3], '%Y-%m-%d %H:%M:%S.%f')
                dlt = now_time - time
                secs = dlt.seconds
                if secs > 36200:
                    del tmp[senderaddress]
                else:
                    messageText = tmp[senderaddress][2]
                    rightmess = True
                    #get bitcoin signing address and txid
                    try:
                        start = messageText.index('{t1{') + len('{t1{')
                        end = messageText.index('}t1}', start)
                        txid1=messageText[start:end]
                    except ValueError:
                        txid1=''
                    try:
                        start = messageText.index('{t2{') + len('{t2{')
                        end = messageText.index('}t2}', start)
                        txid2=messageText[start:end]
                    except ValueError:
                        txid2=''

                    if len(senderaddress)>40:
                        error="address too long"
                        rightmess = False
                    elif len(senderaddress)>20 and rightmess == True:
                        resl = self.inlist(txid1, senderaddress)
                        res2 = self.inlist(txid2, senderaddress)
                        reslt1 = resl["sum"]
                        reslt2 = res2["sum"]
                        summ = reslt1+reslt2
                        if summ > 0.00001:
                            try:
                                start = messageText.index('-++') + len('-++')
                                end = messageText.index('++-', start)
                                signature = messageText[start:end]
                            except ValueError:
                                signature = ''
                            try:
                                start = messageText.index('-{') + len('-{')
                                end = messageText.index('}-', start)
                                messagebody = messageText[start:end]
                            except ValueError:
                                messagebody = ''
                            if len(messagebody)>250001:
                                messagebody = messagebody[:250000]
                            try:
                                start = messageText.index('{p{') + len('{p{')
                                end = messageText.index('}p}', start)
                                price=messageText[start:end]
                            except ValueError:
                                price=''
                            try:
                                start = messageText.index('{c{') + len('{c{')
                                end = messageText.index('}c}', start)
                                cont = messageText[start:end]
                            except ValueError:
                                cont = ''
                            subject = tmp[i][1]
                            verif = False
                            try:
                                verif = MyForm.conn.verifymessage(senderaddress, signature, messagebody)
                            except:
                                verif = False
                            if verif == True:
                                try:
                                    start = messageText.index('{l{') + len('{l{')
                                    end = messageText.index('}l}', start)
                                    loc = messageText[start:end]
                                except ValueError:
                                    loc = ''
                                now_time = str(datetime.datetime.now())
                                if subject[:1]=="G":
                                    g = shelve.open("board-goods.slv")
                                    g[senderaddress] = [summ, subject[1:], price, messagebody, cont, now_time, loc]
                                    g.close()
                                elif subject[:1]=="S":
                                    s = shelve.open("board-services.slv")
                                    s[senderaddress] = [summ, subject[1:], price, messagebody, cont, now_time, loc]
                                    s.close()
                                elif subject[:1]=="C":
                                    c = shelve.open("board-currencies.slv")
                                    c[senderaddress] = [summ, subject[1:], price, messagebody, cont, now_time, loc]
                                    c.close()
                            del tmp[senderaddress]
            tmp.close()
        except:
            error=""

    def buyerpay1(self, message, toAddress, fromAddress):
        #first payment when buyer receive reply
            if toAddress != '':
                    status, addressVersionNumber, streamNumber, ripe = decodeAddress(
                        toAddress)
                    subject = "escrow deal message txid1"
                    if status != 'success':
                        with shared.printLock:
                            print 'Error: Could not decode', toAddress, ':', status

                        if status == 'missingbm':
                            self.statusBar().showMessage(_translate(
                                "MainWindow", "Error: Bitmessage addresses start with BM-   Please check %1").arg(toAddress))
                        elif status == 'checksumfailed':
                            self.statusBar().showMessage(_translate(
                                "MainWindow", "Error: The address %1 is not typed or copied correctly. Please check it.").arg(toAddress))
                        elif status == 'invalidcharacters':
                            self.statusBar().showMessage(_translate(
                                "MainWindow", "Error: The address %1 contains invalid characters. Please check it.").arg(toAddress))
                        elif status == 'versiontoohigh':
                            self.statusBar().showMessage(_translate(
                                "MainWindow", "Error: The address version in %1 is too high. Either you need to upgrade your Bitmessage software or your acquaintance is being clever.").arg(toAddress))
                        elif status == 'ripetooshort':
                            self.statusBar().showMessage(_translate(
                                "MainWindow", "Error: Some data encoded in the address %1 is too short. There might be something wrong with the software of your acquaintance.").arg(toAddress))
                        elif status == 'ripetoolong':
                            self.statusBar().showMessage(_translate(
                                "MainWindow", "Error: Some data encoded in the address %1 is too long. There might be something wrong with the software of your acquaintance.").arg(toAddress))
                        else:
                            self.statusBar().showMessage(_translate(
                                "MainWindow", "Error: Something is wrong with the address %1.").arg(toAddress))
                    elif fromAddress == '':
                        self.statusBar().showMessage(_translate(
                            "MainWindow", "Error: You must specify a From address. If you don\'t have one, go to the \'Your Identities\' tab."))
                    else:
                        toAddress = addBMIfNotPresent(toAddress)
                        if addressVersionNumber > 4 or addressVersionNumber <= 1:
                            QMessageBox.about(self, _translate("MainWindow", "Address version number"), _translate(
                                "MainWindow", "Concerning the address %1, Bitmessage cannot understand address version numbers of %2. Perhaps upgrade Bitmessage to the latest version.").arg(toAddress).arg(str(addressVersionNumber)))
                        if streamNumber > 1 or streamNumber == 0:
                            QMessageBox.about(self, _translate("MainWindow", "Stream number"), _translate("MainWindow", "Concerning the address %1, Bitmessage cannot handle stream numbers of %2. Perhaps upgrade Bitmessage to the latest version.").arg(toAddress).arg(str(streamNumber)))
                        self.statusBar().showMessage('')
                        if shared.statusIconColor == 'red':
                            self.statusBar().showMessage(_translate(
                                "MainWindow", "Warning: You are currently not connected. Bitmessage will do the work necessary to send the message but it won\'t send until you connect."))

                        ackdata = OpenSSL.rand(32)
                        t = ()
                        sqlExecute(
                            '''INSERT INTO sent VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                            '',
                            toAddress,
                            ripe,
                            fromAddress,
                            subject,
                            message,
                            ackdata,
                            int(time.time()),
                            'msgqueued',
                            1,
                            1,
                            'sent',
                            2)

                        toLabel = ''
                        queryreturn = sqlQuery('''select label from addressbook where address=?''',
                                               toAddress)
                        if queryreturn != []:
                            for row in queryreturn:
                                toLabel, = row

                        self.displayNewSentMessage(
                            toAddress, toLabel, fromAddress, subject, message, ackdata)
                        shared.workerQueue.put(('sendmessage', toAddress))




    def merchantreply(self, addrbuyer, addrmerchant, addr1, addr2, addr3, idescrow, amount, lbl):
        #create multisigs
        bitcoinaddr=str(MyForm.conn.getnewaddress("DO NOT USE THIS ADDRESS"))
        bitcoinaddrins1=str(MyForm.conn.getnewaddress("DO NOT USE THIS ADDRESS"))
        bitcoinaddrins2=str(MyForm.conn.getnewaddress("DO NOT USE THIS ADDRESS"))

        escrowaddr1=MyForm.conn.addmultisigaddress(2,[addr1,bitcoinaddr],idescrow)
        escrowaddr2=MyForm.conn.addmultisigaddress(2,[addr2,bitcoinaddrins1],idescrow)
        escrowaddr3=MyForm.conn.addmultisigaddress(2,[addr3,bitcoinaddrins2],idescrow)

        v1 = MyForm.conn.validateaddress(bitcoinaddr)
        v2 = MyForm.conn.validateaddress(bitcoinaddrins1)
        v3 = MyForm.conn.validateaddress(bitcoinaddrins2)
        pub1 = v1.pubkey
        pub2 = v2.pubkey
        pub3 = v3.pubkey

        chkaddr = shelve.open(MyForm.addr_file)
        MyForm.chkaddr["4merchant"]= MyForm.escrow4merchant
        chkaddr.close()

        #toAddressesEscrow = address
        toAddress=addrbuyer
        fromAddress = addrmerchant
        subject = "merchant reply escrow deal"


        if toAddress != '':
            status, addressVersionNumber, streamNumber, ripe = decodeAddress(
                toAddress)
            if status != 'success':
                with shared.printLock:
                    print 'Error: Could not decode', toAddress, ':', status

                if status == 'missingbm':
                    self.statusBar().showMessage(_translate(
                        "MainWindow", "Error: Bitmessage addresses start with BM-   Please check %1").arg(toAddress))
                elif status == 'checksumfailed':
                    self.statusBar().showMessage(_translate(
                        "MainWindow", "Error: The address %1 is not typed or copied correctly. Please check it.").arg(toAddress))
                elif status == 'invalidcharacters':
                    self.statusBar().showMessage(_translate(
                        "MainWindow", "Error: The address %1 contains invalid characters. Please check it.").arg(toAddress))
                elif status == 'versiontoohigh':
                    self.statusBar().showMessage(_translate(
                        "MainWindow", "Error: The address version in %1 is too high. Either you need to upgrade your Bitmessage software or your acquaintance is being clever.").arg(toAddress))
                elif status == 'ripetooshort':
                    self.statusBar().showMessage(_translate(
                        "MainWindow", "Error: Some data encoded in the address %1 is too short. There might be something wrong with the software of your acquaintance.").arg(toAddress))
                elif status == 'ripetoolong':
                    self.statusBar().showMessage(_translate(
                        "MainWindow", "Error: Some data encoded in the address %1 is too long. There might be something wrong with the software of your acquaintance.").arg(toAddress))
                else:
                    self.statusBar().showMessage(_translate(
                        "MainWindow", "Error: Something is wrong with the address %1.").arg(toAddress))
            elif fromAddress == '':
                self.statusBar().showMessage(_translate(
                    "MainWindow", "Error: You must specify a From address. If you don\'t have one, go to the \'Your Identities\' tab."))
            else:
                toAddress = addBMIfNotPresent(toAddress)
                if addressVersionNumber > 4 or addressVersionNumber <= 1:
                    QMessageBox.about(self, _translate("MainWindow", "Address version number"), _translate(
                        "MainWindow", "Concerning the address %1, Bitmessage cannot understand address version numbers of %2. Perhaps upgrade Bitmessage to the latest version.").arg(toAddress).arg(str(addressVersionNumber)))
                if streamNumber > 1 or streamNumber == 0:
                    QMessageBox.about(self, _translate("MainWindow", "Stream number"), _translate("MainWindow", "Concerning the address %1, Bitmessage cannot handle stream numbers of %2. Perhaps upgrade Bitmessage to the latest version.").arg(toAddress).arg(str(streamNumber)))
                    self.statusBar().showMessage('')
                if shared.statusIconColor == 'red':
                    self.statusBar().showMessage(_translate(
                        "MainWindow", "Warning: You are currently not connected. Bitmessage will do the work necessary to send the message but it won\'t send until you connect."))



                data_file2 = 'escrowm.slv'
                sh2 = shelve.open(data_file2)

                if idescrow in sh2:
                    if sh2[idescrow][:29] == "alfa01{status{started-buyer-1":
                        try:
                            start = sh2[idescrow].index('{comment{') + len('{comment{')
                            end = sh2[idescrow].index('}comment}', start)
                            comment = sh2[idescrow][start:end]
                        except ValueError:
                            error=''
                            comment = ""
                        try:
                            start = sh2[idescrow].index('{badd1{') + len('{badd1{')
                            end = sh2[idescrow].index('}badd1}', start)
                            badd1 = sh2[idescrow][start:end]
                        except ValueError:
                            error=''
                            badd1 = ""
                        try:
                            start = sh2[idescrow].index('{badd2{') + len('{badd2{')
                            end = sh2[idescrow].index('}badd2}', start)
                            badd2 = sh2[idescrow][start:end]
                        except ValueError:
                            error=''
                            badd2 = ""
                        try:
                            start = sh2[idescrow].index('{badd3{') + len('{badd3{')
                            end = sh2[idescrow].index('}badd3}', start)
                            badd3 = sh2[idescrow][start:end]
                        except ValueError:
                            error=''
                            badd3 = ""
                        if len(comment) > 550:
                            comment = comment[:550]
                        message = "alfa01"+"{status{"+"started-buyer-2"+"}status}"+"{cont{"+str(fromAddress)+"}cont}"+"{cont2{"+str(toAddress)+"}cont2}"+"{bitadr{"+str(pub1)+"}bitadr}"+"{bitadins1{"+str(pub2)+"}bitadins1}"+"{bitadins2{"+str(pub3)+"}bitadins2}"+"{amount{"+str(amount)+"}amount}"+"{id{"+str(idescrow)+"}id}"+"{escrowaddr1{"+str(escrowaddr1)+"}escrowaddr1}"+"{escrowaddr2{"+str(escrowaddr2)+"}escrowaddr2}"+"{escrowaddr3{"+str(escrowaddr3)+"}escrowaddr3}"+"{lbl{"+str(lbl)+"}lbl}"+"{maddr1{"+str(bitcoinaddr)+"}maddr1}"+"{maddr2{"+str(bitcoinaddrins1)+"}maddr2}" + "{maddr3{"+ str(bitcoinaddrins2)+"}maddr3}" + "{badd1{" + str(badd1) + "}badd1}" + "{badd2{" + str(badd2) + "}badd2}" + "{badd3{" + str(badd3) + "}badd3}" + "{comment{" + comment + "}comment}"


                        sh2[idescrow] = message
                sh2.close()




                ackdata = OpenSSL.rand(32)
                t = ()
                sqlExecute(
                    '''INSERT INTO sent VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                    '',
                    toAddress,
                    ripe,
                    fromAddress,
                    subject,
                    message,
                    ackdata,
                    int(time.time()),
                    'msgqueued',
                    1,
                    1,
                    'sent',
                    2)

                toLabel = ''
                queryreturn = sqlQuery('''select label from addressbook where address=?''',
                                        toAddress)
                if queryreturn != []:
                    for row in queryreturn:
                        toLabel, = row

                self.displayNewSentMessage(
                    toAddress, toLabel, fromAddress, subject, message, ackdata)
                shared.workerQueue.put(('sendmessage', toAddress))

                self.ui.comboBoxSendFrom.setCurrentIndex(0)
                self.ui.labelFrom.setText('')
                self.ui.lineEditTo.setText('')
                self.ui.lineEditSubject.setText('')
                self.ui.textEditMessage.setText('')
                self.ui.tabWidget.setCurrentIndex(2)
                self.ui.tableWidgetSent.setCurrentCell(0, 0)

    def inlist(self, txid, senderaddress):
        hlp = helper.sqlhelper()
        try:
            rtn = hlp.getsumnew(senderaddress)
        except:
            return {'inadresses': [u' '], 'sum': 0.0, 'out_address': ' ', 'text': ' '}
        #hlp = {'inadresses': [u' '], 'sum': 0.0, 'out_address': ' ', 'text': ' '}
        return rtn
    def click_pushButtonAddAddressBook(self):
        self.AddAddressDialogInstance = AddAddressDialog(self)
        if self.AddAddressDialogInstance.exec_():
            if self.AddAddressDialogInstance.ui.labelAddressCheck.text() == _translate("MainWindow", "Address is valid."):
                # First we must check to see if the address is already in the
                # address book. The user cannot add it again or else it will
                # cause problems when updating and deleting the entry.
                address = addBMIfNotPresent(str(
                    self.AddAddressDialogInstance.ui.lineEditAddress.text()))
                label = self.AddAddressDialogInstance.ui.newAddressLabel.text().toUtf8()
                self.addEntryToAddressBook(address,label)
            else:
                self.statusBar().showMessage(_translate(
                    "MainWindow", "The address you entered was invalid. Ignoring it."))

    def addEntryToAddressBook(self,address,label):
        queryreturn = sqlQuery('''select * from addressbook where address=?''', address)
        if queryreturn == []:
            self.ui.tableWidgetAddressBook.setSortingEnabled(False)
            self.ui.tableWidgetAddressBook.insertRow(0)
            newItem = QtGui.QTableWidgetItem(unicode(label, 'utf-8'))
            newItem.setIcon(avatarize(address))
            self.ui.tableWidgetAddressBook.setItem(0, 0, newItem)
            newItem = QtGui.QTableWidgetItem(address)
            newItem.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ui.tableWidgetAddressBook.setItem(0, 1, newItem)
            self.ui.tableWidgetAddressBook.setSortingEnabled(True)
            sqlExecute('''INSERT INTO addressbook VALUES (?,?)''', str(label), address)
            self.rerenderInboxFromLabels()
            self.rerenderSentToLabels()
        else:
            self.statusBar().showMessage(_translate(
                        "MainWindow", "Error: You cannot add the same address to your address book twice. Try renaming the existing one if you want."))

    def addSubscription(self, address, label):
        address = addBMIfNotPresent(address)
        #This should be handled outside of this function, for error displaying and such, but it must also be checked here.
        if shared.isAddressInMySubscriptionsList(address):
            return
        #Add to UI list
        self.ui.tableWidgetSubscriptions.setSortingEnabled(False)
        self.ui.tableWidgetSubscriptions.insertRow(0)
        newItem =  QtGui.QTableWidgetItem(unicode(label, 'utf-8'))
        newItem.setIcon(avatarize(address))
        self.ui.tableWidgetSubscriptions.setItem(0,0,newItem)
        newItem =  QtGui.QTableWidgetItem(address)
        newItem.setFlags( QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled )
        self.ui.tableWidgetSubscriptions.setItem(0,1,newItem)
        self.ui.tableWidgetSubscriptions.setSortingEnabled(True)
        #Add to database (perhaps this should be separated from the MyForm class)
        sqlExecute('''INSERT INTO subscriptions VALUES (?,?,?)''',str(label),address,True)
        self.rerenderInboxFromLabels()
        shared.reloadBroadcastSendersForWhichImWatching()

    def click_pushButtonAddSubscription(self):
        self.NewSubscriptionDialogInstance = NewSubscriptionDialog(self)
        if self.NewSubscriptionDialogInstance.exec_():
            if self.NewSubscriptionDialogInstance.ui.labelAddressCheck.text() != _translate("MainWindow", "Address is valid."):
                self.statusBar().showMessage(_translate("MainWindow", "The address you entered was invalid. Ignoring it."))
                return
            address = addBMIfNotPresent(str(self.NewSubscriptionDialogInstance.ui.lineEditSubscriptionAddress.text()))
            # We must check to see if the address is already in the subscriptions list. The user cannot add it again or else it will cause problems when updating and deleting the entry.
            if shared.isAddressInMySubscriptionsList(address):
                self.statusBar().showMessage(_translate("MainWindow", "Error: You cannot add the same address to your subsciptions twice. Perhaps rename the existing one if you want."))
                return
            label = self.NewSubscriptionDialogInstance.ui.newsubscriptionlabel.text().toUtf8()
            self.addSubscription(address, label)
            # Now, if the user wants to display old broadcasts, let's get them out of the inventory and put them 
            # in the objectProcessorQueue to be processed
            if self.NewSubscriptionDialogInstance.ui.checkBoxDisplayMessagesAlreadyInInventory.isChecked():
                status, addressVersion, streamNumber, ripe = decodeAddress(address)
                shared.flushInventory()
                doubleHashOfAddressData = hashlib.sha512(hashlib.sha512(encodeVarint(
                    addressVersion) + encodeVarint(streamNumber) + ripe).digest()).digest()
                tag = doubleHashOfAddressData[32:]
                queryreturn = sqlQuery(
                    '''select payload from inventory where objecttype='broadcast' and tag=?''', tag)
                for row in queryreturn:
                    payload, = row
                    objectType = 'broadcast'
                    with shared.objectProcessorQueueSizeLock:
                        shared.objectProcessorQueueSize += len(payload)
                        shared.objectProcessorQueue.put((objectType,payload))

    def loadBlackWhiteList(self):
        # Initialize the Blacklist or Whitelist table
        listType = shared.config.get('bitmessagesettings', 'blackwhitelist')
        if listType == 'black':
            queryreturn = sqlQuery('''SELECT label, address, enabled FROM blacklist''')
        else:
            queryreturn = sqlQuery('''SELECT label, address, enabled FROM whitelist''')
        for row in queryreturn:
            label, address, enabled = row
            self.ui.tableWidgetBlacklist.insertRow(0)
            newItem = QtGui.QTableWidgetItem(unicode(label, 'utf-8'))
            if not enabled:
                newItem.setTextColor(QtGui.QColor(128, 128, 128))
            newItem.setIcon(avatarize(address))
            self.ui.tableWidgetBlacklist.setItem(0, 0, newItem)
            newItem = QtGui.QTableWidgetItem(address)
            newItem.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            if not enabled:
                newItem.setTextColor(QtGui.QColor(128, 128, 128))
            self.ui.tableWidgetBlacklist.setItem(0, 1, newItem)

    def click_pushButtonStatusIcon(self):
        print 'click_pushButtonStatusIcon'
        self.iconGlossaryInstance = iconGlossaryDialog(self)
        if self.iconGlossaryInstance.exec_():
            pass

    def click_actionHelp(self):
        self.helpDialogInstance = helpDialog(self)
        self.helpDialogInstance.exec_()

    def click_actionAbout(self):
        self.aboutDialogInstance = aboutDialog(self)
        self.aboutDialogInstance.exec_()

    def click_actionSettings(self):
        self.settingsDialogInstance = settingsDialog(self)
        if self.settingsDialogInstance.exec_():
            shared.config.set('bitmessagesettings', 'startonlogon', str(
                self.settingsDialogInstance.ui.checkBoxStartOnLogon.isChecked()))
            shared.config.set('bitmessagesettings', 'minimizetotray', str(
                self.settingsDialogInstance.ui.checkBoxMinimizeToTray.isChecked()))
            shared.config.set('bitmessagesettings', 'showtraynotifications', str(
                self.settingsDialogInstance.ui.checkBoxShowTrayNotifications.isChecked()))
            shared.config.set('bitmessagesettings', 'startintray', str(
                self.settingsDialogInstance.ui.checkBoxStartInTray.isChecked()))
            shared.config.set('bitmessagesettings', 'willinglysendtomobile', str(
                self.settingsDialogInstance.ui.checkBoxWillinglySendToMobile.isChecked()))
            shared.config.set('bitmessagesettings', 'useidenticons', str(
                self.settingsDialogInstance.ui.checkBoxUseIdenticons.isChecked()))
                
            lang_ind = int(self.settingsDialogInstance.ui.languageComboBox.currentIndex())
            if not languages[lang_ind] == 'other':
                shared.config.set('bitmessagesettings', 'userlocale', languages[lang_ind])
            
            if int(shared.config.get('bitmessagesettings', 'port')) != int(self.settingsDialogInstance.ui.lineEditTCPPort.text()):
                if not shared.safeConfigGetBoolean('bitmessagesettings', 'dontconnect'):
                    QMessageBox.about(self, _translate("MainWindow", "Restart"), _translate(
                        "MainWindow", "You must restart Bitmessage for the port number change to take effect."))
                shared.config.set('bitmessagesettings', 'port', str(
                    self.settingsDialogInstance.ui.lineEditTCPPort.text()))
            #print 'self.settingsDialogInstance.ui.comboBoxProxyType.currentText()', self.settingsDialogInstance.ui.comboBoxProxyType.currentText()
            #print 'self.settingsDialogInstance.ui.comboBoxProxyType.currentText())[0:5]', self.settingsDialogInstance.ui.comboBoxProxyType.currentText()[0:5]
            if shared.config.get('bitmessagesettings', 'socksproxytype') == 'none' and self.settingsDialogInstance.ui.comboBoxProxyType.currentText()[0:5] == 'SOCKS':
                if shared.statusIconColor != 'red':
                    QMessageBox.about(self, _translate("MainWindow", "Restart"), _translate(
                        "MainWindow", "Bitmessage will use your proxy from now on but you may want to manually restart Bitmessage now to close existing connections (if any)."))
            if shared.config.get('bitmessagesettings', 'socksproxytype')[0:5] == 'SOCKS' and self.settingsDialogInstance.ui.comboBoxProxyType.currentText()[0:5] != 'SOCKS':
                self.statusBar().showMessage('')
            if self.settingsDialogInstance.ui.comboBoxProxyType.currentText()[0:5] == 'SOCKS':
                shared.config.set('bitmessagesettings', 'socksproxytype', str(
                    self.settingsDialogInstance.ui.comboBoxProxyType.currentText()))
            else:
                shared.config.set('bitmessagesettings', 'socksproxytype', 'none')
            shared.config.set('bitmessagesettings', 'socksauthentication', str(
                self.settingsDialogInstance.ui.checkBoxAuthentication.isChecked()))
            shared.config.set('bitmessagesettings', 'sockshostname', str(
                self.settingsDialogInstance.ui.lineEditSocksHostname.text()))
            shared.config.set('bitmessagesettings', 'socksport', str(
                self.settingsDialogInstance.ui.lineEditSocksPort.text()))
            shared.config.set('bitmessagesettings', 'socksusername', str(
                self.settingsDialogInstance.ui.lineEditSocksUsername.text()))
            shared.config.set('bitmessagesettings', 'sockspassword', str(
                self.settingsDialogInstance.ui.lineEditSocksPassword.text()))
            shared.config.set('bitmessagesettings', 'sockslisten', str(
                self.settingsDialogInstance.ui.checkBoxSocksListen.isChecked()))

            shared.config.set('bitmessagesettings', 'namecoinrpctype',
                self.settingsDialogInstance.getNamecoinType())
            shared.config.set('bitmessagesettings', 'namecoinrpchost', str(
                self.settingsDialogInstance.ui.lineEditNamecoinHost.text()))
            shared.config.set('bitmessagesettings', 'namecoinrpcport', str(
                self.settingsDialogInstance.ui.lineEditNamecoinPort.text()))
            shared.config.set('bitmessagesettings', 'namecoinrpcuser', str(
                self.settingsDialogInstance.ui.lineEditNamecoinUser.text()))
            shared.config.set('bitmessagesettings', 'namecoinrpcpassword', str(
                self.settingsDialogInstance.ui.lineEditNamecoinPassword.text()))

            if float(self.settingsDialogInstance.ui.lineEditTotalDifficulty.text()) >= 1:
                shared.config.set('bitmessagesettings', 'defaultnoncetrialsperbyte', str(int(float(
                    self.settingsDialogInstance.ui.lineEditTotalDifficulty.text()) * shared.networkDefaultProofOfWorkNonceTrialsPerByte)))
            if float(self.settingsDialogInstance.ui.lineEditSmallMessageDifficulty.text()) >= 1:
                shared.config.set('bitmessagesettings', 'defaultpayloadlengthextrabytes', str(int(float(
                    self.settingsDialogInstance.ui.lineEditSmallMessageDifficulty.text()) * shared.networkDefaultPayloadLengthExtraBytes)))
            if float(self.settingsDialogInstance.ui.lineEditMaxAcceptableTotalDifficulty.text()) >= 1 or float(self.settingsDialogInstance.ui.lineEditMaxAcceptableTotalDifficulty.text()) == 0:
                shared.config.set('bitmessagesettings', 'maxacceptablenoncetrialsperbyte', str(int(float(
                    self.settingsDialogInstance.ui.lineEditMaxAcceptableTotalDifficulty.text()) * shared.networkDefaultProofOfWorkNonceTrialsPerByte)))
            if float(self.settingsDialogInstance.ui.lineEditMaxAcceptableSmallMessageDifficulty.text()) >= 1 or float(self.settingsDialogInstance.ui.lineEditMaxAcceptableSmallMessageDifficulty.text()) == 0:
                shared.config.set('bitmessagesettings', 'maxacceptablepayloadlengthextrabytes', str(int(float(
                    self.settingsDialogInstance.ui.lineEditMaxAcceptableSmallMessageDifficulty.text()) * shared.networkDefaultPayloadLengthExtraBytes)))
            #start:UI setting to stop trying to send messages after X days/months
            # I'm open to changing this UI to something else if someone has a better idea.
            if ((self.settingsDialogInstance.ui.lineEditDays.text()=='') and (self.settingsDialogInstance.ui.lineEditMonths.text()=='')):#We need to handle this special case. Bitmessage has its default behavior. The input is blank/blank
                shared.config.set('bitmessagesettings', 'stopresendingafterxdays', '')
                shared.config.set('bitmessagesettings', 'stopresendingafterxmonths', '')
                shared.maximumLengthOfTimeToBotherResendingMessages = float('inf')
            try:
                float(self.settingsDialogInstance.ui.lineEditDays.text())
                lineEditDaysIsValidFloat = True
            except:
                lineEditDaysIsValidFloat = False
            try:
                float(self.settingsDialogInstance.ui.lineEditMonths.text())
                lineEditMonthsIsValidFloat = True
            except:
                lineEditMonthsIsValidFloat = False
            if lineEditDaysIsValidFloat and not lineEditMonthsIsValidFloat:
                self.settingsDialogInstance.ui.lineEditMonths.setText("0")
            if lineEditMonthsIsValidFloat and not lineEditDaysIsValidFloat:
                self.settingsDialogInstance.ui.lineEditDays.setText("0")
            if lineEditDaysIsValidFloat or lineEditMonthsIsValidFloat:
                if (float(self.settingsDialogInstance.ui.lineEditDays.text()) >=0 and float(self.settingsDialogInstance.ui.lineEditMonths.text()) >=0):
                    shared.maximumLengthOfTimeToBotherResendingMessages = (float(str(self.settingsDialogInstance.ui.lineEditDays.text())) * 24 * 60 * 60) + (float(str(self.settingsDialogInstance.ui.lineEditMonths.text())) * (60 * 60 * 24 *365)/12)
                    if shared.maximumLengthOfTimeToBotherResendingMessages < 432000: # If the time period is less than 5 hours, we give zero values to all fields. No message will be sent again.
                        QMessageBox.about(self, _translate("MainWindow", "Will not resend ever"), _translate(
                            "MainWindow", "Note that the time limit you entered is less than the amount of time Bitmessage waits for the first resend attempt therefore your messages will never be resent."))
                        shared.config.set('bitmessagesettings', 'stopresendingafterxdays', '0')
                        shared.config.set('bitmessagesettings', 'stopresendingafterxmonths', '0')
                        shared.maximumLengthOfTimeToBotherResendingMessages = 0
                    else:
                        shared.config.set('bitmessagesettings', 'stopresendingafterxdays', str(float(
                        self.settingsDialogInstance.ui.lineEditDays.text())))
                        shared.config.set('bitmessagesettings', 'stopresendingafterxmonths', str(float(
                        self.settingsDialogInstance.ui.lineEditMonths.text())))
            #end

            # if str(self.settingsDialogInstance.ui.comboBoxMaxCores.currentText()) == 'All':
            #    shared.config.set('bitmessagesettings', 'maxcores', '99999')
            # else:
            # shared.config.set('bitmessagesettings', 'maxcores',
            # str(self.settingsDialogInstance.ui.comboBoxMaxCores.currentText()))

            with open(shared.appdata + 'keys.dat', 'wb') as configfile:
                shared.config.write(configfile)

            if 'win32' in sys.platform or 'win64' in sys.platform:
            # Auto-startup for Windows
                RUN_PATH = "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"
                self.settings = QSettings(RUN_PATH, QSettings.NativeFormat)
                if shared.config.getboolean('bitmessagesettings', 'startonlogon'):
                    self.settings.setValue("PyBitmessage", sys.argv[0])
                else:
                    self.settings.remove("PyBitmessage")
            elif 'darwin' in sys.platform:
                # startup for mac
                pass
            elif 'linux' in sys.platform:
                # startup for linux
                pass

            if shared.appdata != '' and self.settingsDialogInstance.ui.checkBoxPortableMode.isChecked():  # If we are NOT using portable mode now but the user selected that we should...
                # Write the keys.dat file to disk in the new location
                sqlStoredProcedure('movemessagstoprog')
                with open('keys.dat', 'wb') as configfile:
                    shared.config.write(configfile)
                # Write the knownnodes.dat file to disk in the new location
                shared.knownNodesLock.acquire()
                output = open('knownnodes.dat', 'wb')
                pickle.dump(shared.knownNodes, output)
                output.close()
                shared.knownNodesLock.release()
                os.remove(shared.appdata + 'keys.dat')
                os.remove(shared.appdata + 'knownnodes.dat')
                previousAppdataLocation = shared.appdata
                shared.appdata = ''
                debug.restartLoggingInUpdatedAppdataLocation()
                try:
                    os.remove(previousAppdataLocation + 'debug.log')
                    os.remove(previousAppdataLocation + 'debug.log.1')
                except:
                    pass

            if shared.appdata == '' and not self.settingsDialogInstance.ui.checkBoxPortableMode.isChecked():  # If we ARE using portable mode now but the user selected that we shouldn't...
                shared.appdata = shared.lookupAppdataFolder()
                if not os.path.exists(shared.appdata):
                    os.makedirs(shared.appdata)
                sqlStoredProcedure('movemessagstoappdata')
                # Write the keys.dat file to disk in the new location
                with open(shared.appdata + 'keys.dat', 'wb') as configfile:
                    shared.config.write(configfile)
                # Write the knownnodes.dat file to disk in the new location
                shared.knownNodesLock.acquire()
                output = open(shared.appdata + 'knownnodes.dat', 'wb')
                pickle.dump(shared.knownNodes, output)
                output.close()
                shared.knownNodesLock.release()
                os.remove('keys.dat')
                os.remove('knownnodes.dat')
                debug.restartLoggingInUpdatedAppdataLocation()
                try:
                    os.remove('debug.log')
                    os.remove('debug.log.1')
                except:
                    pass

    def click_radioButtonBlacklist(self):
        if shared.config.get('bitmessagesettings', 'blackwhitelist') == 'white':
            shared.config.set('bitmessagesettings', 'blackwhitelist', 'black')
            with open(shared.appdata + 'keys.dat', 'wb') as configfile:
                shared.config.write(configfile)
            # self.ui.tableWidgetBlacklist.clearContents()
            self.ui.tableWidgetBlacklist.setRowCount(0)
            self.loadBlackWhiteList()
            self.ui.tabWidget.setTabText(6, 'Blacklist')

    def click_radioButtonWhitelist(self):
        if shared.config.get('bitmessagesettings', 'blackwhitelist') == 'black':
            shared.config.set('bitmessagesettings', 'blackwhitelist', 'white')
            with open(shared.appdata + 'keys.dat', 'wb') as configfile:
                shared.config.write(configfile)
            # self.ui.tableWidgetBlacklist.clearContents()
            self.ui.tableWidgetBlacklist.setRowCount(0)
            self.loadBlackWhiteList()
            self.ui.tabWidget.setTabText(6, 'Whitelist')

    def click_pushButtonAddBlacklist(self):
        self.NewBlacklistDialogInstance = AddAddressDialog(self)
        if self.NewBlacklistDialogInstance.exec_():
            if self.NewBlacklistDialogInstance.ui.labelAddressCheck.text() == _translate("MainWindow", "Address is valid."):
                address = addBMIfNotPresent(str(
                    self.NewBlacklistDialogInstance.ui.lineEditAddress.text()))
                # First we must check to see if the address is already in the
                # address book. The user cannot add it again or else it will
                # cause problems when updating and deleting the entry.
                t = (address,)
                if shared.config.get('bitmessagesettings', 'blackwhitelist') == 'black':
                    sql = '''select * from blacklist where address=?'''
                else:
                    sql = '''select * from whitelist where address=?'''
                queryreturn = sqlQuery(sql,*t)
                if queryreturn == []:
                    self.ui.tableWidgetBlacklist.setSortingEnabled(False)
                    self.ui.tableWidgetBlacklist.insertRow(0)
                    newItem = QtGui.QTableWidgetItem(unicode(
                        self.NewBlacklistDialogInstance.ui.newAddressLabel.text().toUtf8(), 'utf-8'))
                    newItem.setIcon(avatarize(address))
                    self.ui.tableWidgetBlacklist.setItem(0, 0, newItem)
                    newItem = QtGui.QTableWidgetItem(address)
                    newItem.setFlags(
                        QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    self.ui.tableWidgetBlacklist.setItem(0, 1, newItem)
                    self.ui.tableWidgetBlacklist.setSortingEnabled(True)
                    t = (str(self.NewBlacklistDialogInstance.ui.newAddressLabel.text().toUtf8()), address, True)
                    if shared.config.get('bitmessagesettings', 'blackwhitelist') == 'black':
                        sql = '''INSERT INTO blacklist VALUES (?,?,?)'''
                    else:
                        sql = '''INSERT INTO whitelist VALUES (?,?,?)'''
                    sqlExecute(sql, *t)
                else:
                    self.statusBar().showMessage(_translate(
                        "MainWindow", "Error: You cannot add the same address to your list twice. Perhaps rename the existing one if you want."))
            else:
                self.statusBar().showMessage(_translate(
                    "MainWindow", "The address you entered was invalid. Ignoring it."))

    def on_action_SpecialAddressBehaviorDialog(self):
        self.dialog = SpecialAddressBehaviorDialog(self)
        # For Modal dialogs
        if self.dialog.exec_():
            currentRow = self.ui.tableWidgetYourIdentities.currentRow()
            addressAtCurrentRow = str(
                self.ui.tableWidgetYourIdentities.item(currentRow, 1).text())
            if shared.safeConfigGetBoolean(addressAtCurrentRow, 'chan'):
                return
            if self.dialog.ui.radioButtonBehaveNormalAddress.isChecked():
                shared.config.set(str(
                    addressAtCurrentRow), 'mailinglist', 'false')
                # Set the color to either black or grey
                if shared.config.getboolean(addressAtCurrentRow, 'enabled'):
                    self.ui.tableWidgetYourIdentities.item(
                        currentRow, 1).setTextColor(QApplication.palette()
                        .text().color())
                else:
                    self.ui.tableWidgetYourIdentities.item(
                        currentRow, 1).setTextColor(QtGui.QColor(128, 128, 128))
            else:
                shared.config.set(str(
                    addressAtCurrentRow), 'mailinglist', 'true')
                shared.config.set(str(addressAtCurrentRow), 'mailinglistname', str(
                    self.dialog.ui.lineEditMailingListName.text().toUtf8()))
                self.ui.tableWidgetYourIdentities.item(currentRow, 1).setTextColor(QtGui.QColor(137, 04, 177)) # magenta
            with open(shared.appdata + 'keys.dat', 'wb') as configfile:
                shared.config.write(configfile)
            self.rerenderInboxToLabels()

    def click_NewAddressDialog(self):
        self.dialog = NewAddressDialog(self)
        # For Modal dialogs
        if self.dialog.exec_():
            # self.dialog.ui.buttonBox.enabled = False
            if self.dialog.ui.radioButtonRandomAddress.isChecked():
                if self.dialog.ui.radioButtonMostAvailable.isChecked():
                    streamNumberForAddress = 1
                else:
                    # User selected 'Use the same stream as an existing
                    # address.'
                    streamNumberForAddress = decodeAddress(
                        self.dialog.ui.comboBoxExisting.currentText())[2]
                shared.addressGeneratorQueue.put(('createRandomAddress', 4, streamNumberForAddress, str(
                    self.dialog.ui.newaddresslabel.text().toUtf8()), 1, "", self.dialog.ui.checkBoxEighteenByteRipe.isChecked()))
            else:
                if self.dialog.ui.lineEditPassphrase.text() != self.dialog.ui.lineEditPassphraseAgain.text():
                    QMessageBox.about(self, _translate("MainWindow", "Passphrase mismatch"), _translate(
                        "MainWindow", "The passphrase you entered twice doesn\'t match. Try again."))
                elif self.dialog.ui.lineEditPassphrase.text() == "":
                    QMessageBox.about(self, _translate(
                        "MainWindow", "Choose a passphrase"), _translate("MainWindow", "You really do need a passphrase."))
                else:
                    streamNumberForAddress = 1  # this will eventually have to be replaced by logic to determine the most available stream number.
                    shared.addressGeneratorQueue.put(('createDeterministicAddresses', 4, streamNumberForAddress, "unused deterministic address", self.dialog.ui.spinBoxNumberOfAddressesToMake.value(
                    ), self.dialog.ui.lineEditPassphrase.text().toUtf8(), self.dialog.ui.checkBoxEighteenByteRipe.isChecked()))
        else:
            print 'new address dialog box rejected'

    # Quit selected from menu or application indicator
    def quit(self):
        os.system("taskkill /im bitcoin-qt.exe")
        '''quit_msg = "Are you sure you want to exit Bitmessage?"
        reply = QtGui.QMessageBox.question(self, 'Message',
                         quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if reply is QtGui.QMessageBox.No:
            return
        '''
        shared.doCleanShutdown()
        self.tray.hide()
        # unregister the messaging system
        if self.mmapp is not None:
            self.mmapp.unregister()
        self.statusBar().showMessage(_translate(
            "MainWindow", "All done. Closing user interface..."))
        os._exit(0)

    # window close event
    def closeEvent(self, event):
        self.appIndicatorHide()
        minimizeonclose = False

        try:
            minimizeonclose = shared.config.getboolean(
                'bitmessagesettings', 'minimizeonclose')
        except Exception:
            pass

        if minimizeonclose:
            # minimize the application
            event.ignore()
        else:
            # quit the application
            event.accept()
            self.quit()

    def on_action_InboxMessageForceHtml(self):
        currentInboxRow = self.ui.tableWidgetInbox.currentRow()

        msgid = str(self.ui.tableWidgetInbox.item(
            currentInboxRow, 3).data(Qt.UserRole).toPyObject())
        queryreturn = sqlQuery(
            '''select message from inbox where msgid=?''', msgid)
        if queryreturn != []:
            for row in queryreturn:
                messageAtCurrentInboxRow, = row 

        lines = messageAtCurrentInboxRow.split('\n')
        for i in xrange(len(lines)):
            if 'Message ostensibly from ' in lines[i]:
                lines[i] = '<p style="font-size: 12px; color: grey;">%s</span></p>' % (
                    lines[i])
            elif lines[i] == '------------------------------------------------------':
                lines[i] = '<hr>'
        content = ''
        for i in xrange(len(lines)):
            content += lines[i]
        content = content.replace('\n\n', '<br><br>')
        self.ui.textEditInboxMessage.setHtml(QtCore.QString(content))

    def on_action_InboxMarkUnread(self):
        font = QFont()
        font.setBold(True)
        for row in self.ui.tableWidgetInbox.selectedIndexes():
            currentRow = row.row()
            inventoryHashToMarkUnread = str(self.ui.tableWidgetInbox.item(
                currentRow, 3).data(Qt.UserRole).toPyObject())
            sqlExecute('''UPDATE inbox SET read=0 WHERE msgid=?''', inventoryHashToMarkUnread)
            self.ui.tableWidgetInbox.item(currentRow, 0).setFont(font)
            self.ui.tableWidgetInbox.item(currentRow, 1).setFont(font)
            self.ui.tableWidgetInbox.item(currentRow, 2).setFont(font)
            self.ui.tableWidgetInbox.item(currentRow, 3).setFont(font)
        self.changedInboxUnread()
        # self.ui.tableWidgetInbox.selectRow(currentRow + 1) 
        # This doesn't de-select the last message if you try to mark it unread, but that doesn't interfere. Might not be necessary.
        # We could also select upwards, but then our problem would be with the topmost message.
        # self.ui.tableWidgetInbox.clearSelection() manages to mark the message as read again.

    def on_action_InboxReply(self):
        currentInboxRow = self.ui.tableWidgetInbox.currentRow()
        toAddressAtCurrentInboxRow = str(self.ui.tableWidgetInbox.item(
            currentInboxRow, 0).data(Qt.UserRole).toPyObject())
        fromAddressAtCurrentInboxRow = str(self.ui.tableWidgetInbox.item(
            currentInboxRow, 1).data(Qt.UserRole).toPyObject())
        msgid = str(self.ui.tableWidgetInbox.item(
            currentInboxRow, 3).data(Qt.UserRole).toPyObject())
        queryreturn = sqlQuery(
            '''select message from inbox where msgid=?''', msgid)
        if queryreturn != []:
            for row in queryreturn:
                messageAtCurrentInboxRow, = row
        if toAddressAtCurrentInboxRow == self.str_broadcast_subscribers:
            self.ui.labelFrom.setText('')
        elif not shared.config.has_section(toAddressAtCurrentInboxRow):
            QtGui.QMessageBox.information(self, _translate("MainWindow", "Address is gone"), _translate(
                "MainWindow", "Bitmessage cannot find your address %1. Perhaps you removed it?").arg(toAddressAtCurrentInboxRow), QMessageBox.Ok)
            self.ui.labelFrom.setText('')
        elif not shared.config.getboolean(toAddressAtCurrentInboxRow, 'enabled'):
            QtGui.QMessageBox.information(self, _translate("MainWindow", "Address disabled"), _translate(
                "MainWindow", "Error: The address from which you are trying to send is disabled. You\'ll have to enable it on the \'Your Identities\' tab before using it."), QMessageBox.Ok)
            self.ui.labelFrom.setText('')
        else:
            self.ui.labelFrom.setText(toAddressAtCurrentInboxRow)
            self.setBroadcastEnablementDependingOnWhetherThisIsAChanAddress(toAddressAtCurrentInboxRow)

        self.ui.lineEditTo.setText(str(fromAddressAtCurrentInboxRow))
        
        # If the previous message was to a chan then we should send our reply to the chan rather than to the particular person who sent the message.
        if shared.config.has_section(toAddressAtCurrentInboxRow):
            if shared.safeConfigGetBoolean(toAddressAtCurrentInboxRow, 'chan'):
                print 'original sent to a chan. Setting the to address in the reply to the chan address.'
                self.ui.lineEditTo.setText(str(toAddressAtCurrentInboxRow))
        
        listOfAddressesInComboBoxSendFrom = [str(self.ui.comboBoxSendFrom.itemData(i).toPyObject()) for i in range(self.ui.comboBoxSendFrom.count())]
        if toAddressAtCurrentInboxRow in listOfAddressesInComboBoxSendFrom:
            currentIndex = listOfAddressesInComboBoxSendFrom.index(toAddressAtCurrentInboxRow)
            self.ui.comboBoxSendFrom.setCurrentIndex(currentIndex)
        else:
            self.ui.comboBoxSendFrom.setCurrentIndex(0)
        
        self.ui.textEditMessage.setText('\n\n------------------------------------------------------\n' + unicode(messageAtCurrentInboxRow, 'utf-8)'))
        if self.ui.tableWidgetInbox.item(currentInboxRow, 2).text()[0:3] in ['Re:', 'RE:']:
            self.ui.lineEditSubject.setText(
                self.ui.tableWidgetInbox.item(currentInboxRow, 2).text())
        else:
            self.ui.lineEditSubject.setText(
                'Re: ' + self.ui.tableWidgetInbox.item(currentInboxRow, 2).text())
        self.ui.radioButtonSpecific.setChecked(True)
        self.ui.tabWidget.setCurrentIndex(1)

    def on_action_InboxAddSenderToAddressBook(self):
        currentInboxRow = self.ui.tableWidgetInbox.currentRow()
        # self.ui.tableWidgetInbox.item(currentRow,1).data(Qt.UserRole).toPyObject()
        addressAtCurrentInboxRow = str(self.ui.tableWidgetInbox.item(
            currentInboxRow, 1).data(Qt.UserRole).toPyObject())
        # Let's make sure that it isn't already in the address book
        queryreturn = sqlQuery('''select * from addressbook where address=?''',
                               addressAtCurrentInboxRow)
        if queryreturn == []:
            self.ui.tableWidgetAddressBook.insertRow(0)
            newItem = QtGui.QTableWidgetItem(
                '--New entry. Change label in Address Book.--')
            self.ui.tableWidgetAddressBook.setItem(0, 0, newItem)
            newItem.setIcon(avatarize(addressAtCurrentInboxRow))
            newItem = QtGui.QTableWidgetItem(addressAtCurrentInboxRow)
            newItem.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ui.tableWidgetAddressBook.setItem(0, 1, newItem)
            sqlExecute('''INSERT INTO addressbook VALUES (?,?)''',
                       '--New entry. Change label in Address Book.--',
                       addressAtCurrentInboxRow)
            self.ui.tabWidget.setCurrentIndex(5)
            self.ui.tableWidgetAddressBook.setCurrentCell(0, 0)
            self.statusBar().showMessage(_translate(
                "MainWindow", "Entry added to the Address Book. Edit the label to your liking."))
        else:
            self.statusBar().showMessage(_translate(
                "MainWindow", "Error: You cannot add the same address to your address book twice. Try renaming the existing one if you want."))

    # Send item on the Inbox tab to trash
    def on_action_InboxTrash(self):
        while self.ui.tableWidgetInbox.selectedIndexes() != []:
            currentRow = self.ui.tableWidgetInbox.selectedIndexes()[0].row()
            inventoryHashToTrash = str(self.ui.tableWidgetInbox.item(
                currentRow, 3).data(Qt.UserRole).toPyObject())
            sqlExecute('''UPDATE inbox SET folder='trash' WHERE msgid=?''', inventoryHashToTrash)
            self.ui.textEditInboxMessage.setText("")
            self.ui.tableWidgetInbox.removeRow(currentRow)
            self.statusBar().showMessage(_translate(
                "MainWindow", "Moved items to trash. There is no user interface to view your trash, but it is still on disk if you are desperate to get it back."))
        if currentRow == 0:
            self.ui.tableWidgetInbox.selectRow(currentRow)
        else:
            self.ui.tableWidgetInbox.selectRow(currentRow - 1)

    def on_action_InboxSaveMessageAs(self):
        currentInboxRow = self.ui.tableWidgetInbox.currentRow()
        try:
            subjectAtCurrentInboxRow = str(self.ui.tableWidgetInbox.item(currentInboxRow,2).text())
        except:
            subjectAtCurrentInboxRow = ''

        # Retrieve the message data out of the SQL database
        msgid = str(self.ui.tableWidgetInbox.item(
            currentInboxRow, 3).data(Qt.UserRole).toPyObject())
        queryreturn = sqlQuery(
            '''select message from inbox where msgid=?''', msgid)
        if queryreturn != []:
            for row in queryreturn:
                message, = row

        defaultFilename = "".join(x for x in subjectAtCurrentInboxRow if x.isalnum()) + '.txt'
        filename = QFileDialog.getSaveFileName(self, _translate("MainWindow","Save As..."), defaultFilename, "Text files (*.txt);;All files (*.*)")
        if filename == '':
            return
        try:
            f = open(filename, 'w')
            f.write(message)
            f.close()
        except Exception, e:
            sys.stderr.write('Write error: '+ e)
            self.statusBar().showMessage(_translate("MainWindow", "Write error."))

    # Send item on the Sent tab to trash
    def on_action_SentTrash(self):
        while self.ui.tableWidgetSent.selectedIndexes() != []:
            currentRow = self.ui.tableWidgetSent.selectedIndexes()[0].row()
            ackdataToTrash = str(self.ui.tableWidgetSent.item(
                currentRow, 3).data(Qt.UserRole).toPyObject())
            sqlExecute('''UPDATE sent SET folder='trash' WHERE ackdata=?''', ackdataToTrash)
            self.ui.textEditSentMessage.setPlainText("")
            self.ui.tableWidgetSent.removeRow(currentRow)
            self.statusBar().showMessage(_translate(
                "MainWindow", "Moved items to trash. There is no user interface to view your trash, but it is still on disk if you are desperate to get it back."))
        if currentRow == 0:
            self.ui.tableWidgetSent.selectRow(currentRow)
        else:
            self.ui.tableWidgetSent.selectRow(currentRow - 1)

    def on_action_ForceSend(self):
        currentRow = self.ui.tableWidgetSent.currentRow()
        addressAtCurrentRow = str(self.ui.tableWidgetSent.item(
            currentRow, 0).data(Qt.UserRole).toPyObject())
        toRipe = decodeAddress(addressAtCurrentRow)[3]
        sqlExecute(
            '''UPDATE sent SET status='forcepow' WHERE toripe=? AND status='toodifficult' and folder='sent' ''',
            toRipe)
        queryreturn = sqlQuery('''select ackdata FROM sent WHERE status='forcepow' ''')
        for row in queryreturn:
            ackdata, = row
            shared.UISignalQueue.put(('updateSentItemStatusByAckdata', (
                ackdata, 'Overriding maximum-difficulty setting. Work queued.')))
        shared.workerQueue.put(('sendmessage', ''))

    def on_action_SentClipboard(self):
        currentRow = self.ui.tableWidgetSent.currentRow()
        addressAtCurrentRow = str(self.ui.tableWidgetSent.item(
            currentRow, 0).data(Qt.UserRole).toPyObject())
        clipboard = QtGui.QApplication.clipboard()
        clipboard.setText(str(addressAtCurrentRow))

    # Group of functions for the Address Book dialog box
    def on_action_AddressBookNew(self):
        self.click_pushButtonAddAddressBook()

    def on_action_AddressBookDelete(self):
        while self.ui.tableWidgetAddressBook.selectedIndexes() != []:
            currentRow = self.ui.tableWidgetAddressBook.selectedIndexes()[
                0].row()
            labelAtCurrentRow = self.ui.tableWidgetAddressBook.item(
                currentRow, 0).text().toUtf8()
            addressAtCurrentRow = self.ui.tableWidgetAddressBook.item(
                currentRow, 1).text()
            sqlExecute('''DELETE FROM addressbook WHERE label=? AND address=?''',
                       str(labelAtCurrentRow), str(addressAtCurrentRow))
            self.ui.tableWidgetAddressBook.removeRow(currentRow)
            self.rerenderInboxFromLabels()
            self.rerenderSentToLabels()

    def on_action_AddressBookClipboard(self):
        fullStringOfAddresses = ''
        listOfSelectedRows = {}
        for i in range(len(self.ui.tableWidgetAddressBook.selectedIndexes())):
            listOfSelectedRows[
                self.ui.tableWidgetAddressBook.selectedIndexes()[i].row()] = 0
        for currentRow in listOfSelectedRows:
            addressAtCurrentRow = self.ui.tableWidgetAddressBook.item(
                currentRow, 1).text()
            if fullStringOfAddresses == '':
                fullStringOfAddresses = addressAtCurrentRow
            else:
                fullStringOfAddresses += ', ' + str(addressAtCurrentRow)
        clipboard = QtGui.QApplication.clipboard()
        clipboard.setText(fullStringOfAddresses)

    def on_action_AddressBookSend(self):
        listOfSelectedRows = {}
        for i in range(len(self.ui.tableWidgetAddressBook.selectedIndexes())):
            listOfSelectedRows[
                self.ui.tableWidgetAddressBook.selectedIndexes()[i].row()] = 0
        for currentRow in listOfSelectedRows:
            addressAtCurrentRow = self.ui.tableWidgetAddressBook.item(
                currentRow, 1).text()
            if self.ui.lineEditTo.text() == '':
                self.ui.lineEditTo.setText(str(addressAtCurrentRow))
            else:
                self.ui.lineEditTo.setText(str(
                    self.ui.lineEditTo.text()) + '; ' + str(addressAtCurrentRow))
        if listOfSelectedRows == {}:
            self.statusBar().showMessage(_translate(
                "MainWindow", "No addresses selected."))
        else:
            self.statusBar().showMessage('')
            self.ui.tabWidget.setCurrentIndex(1)

    def on_action_AddressBookSubscribe(self):
        listOfSelectedRows = {}
        for i in range(len(self.ui.tableWidgetAddressBook.selectedIndexes())):
            listOfSelectedRows[self.ui.tableWidgetAddressBook.selectedIndexes()[i].row()] = 0
        for currentRow in listOfSelectedRows:
            addressAtCurrentRow = str(self.ui.tableWidgetAddressBook.item(currentRow,1).text())
            # Then subscribe to it... provided it's not already in the address book
            if shared.isAddressInMySubscriptionsList(addressAtCurrentRow):
                self.statusBar().showMessage(QtGui.QApplication.translate("MainWindow", "Error: You cannot add the same address to your subsciptions twice. Perhaps rename the existing one if you want."))
                continue
            labelAtCurrentRow = self.ui.tableWidgetAddressBook.item(currentRow,0).text().toUtf8()
            self.addSubscription(addressAtCurrentRow, labelAtCurrentRow)
            self.ui.tabWidget.setCurrentIndex(4)

    def on_context_menuAddressBook(self, point):
        self.popMenuAddressBook.exec_(
            self.ui.tableWidgetAddressBook.mapToGlobal(point))

    # Group of functions for the Subscriptions dialog box
    def on_action_SubscriptionsNew(self):
        self.click_pushButtonAddSubscription()
        
    def on_action_SubscriptionsDelete(self):
        print 'clicked Delete'
        currentRow = self.ui.tableWidgetSubscriptions.currentRow()
        labelAtCurrentRow = self.ui.tableWidgetSubscriptions.item(
            currentRow, 0).text().toUtf8()
        addressAtCurrentRow = self.ui.tableWidgetSubscriptions.item(
            currentRow, 1).text()
        sqlExecute('''DELETE FROM subscriptions WHERE label=? AND address=?''',
                   str(labelAtCurrentRow), str(addressAtCurrentRow))
        self.ui.tableWidgetSubscriptions.removeRow(currentRow)
        self.rerenderInboxFromLabels()
        shared.reloadBroadcastSendersForWhichImWatching()

    def on_action_SubscriptionsClipboard(self):
        currentRow = self.ui.tableWidgetSubscriptions.currentRow()
        addressAtCurrentRow = self.ui.tableWidgetSubscriptions.item(
            currentRow, 1).text()
        clipboard = QtGui.QApplication.clipboard()
        clipboard.setText(str(addressAtCurrentRow))

    def on_action_SubscriptionsEnable(self):
        currentRow = self.ui.tableWidgetSubscriptions.currentRow()
        labelAtCurrentRow = self.ui.tableWidgetSubscriptions.item(
            currentRow, 0).text().toUtf8()
        addressAtCurrentRow = self.ui.tableWidgetSubscriptions.item(
            currentRow, 1).text()
        sqlExecute(
            '''update subscriptions set enabled=1 WHERE label=? AND address=?''',
            str(labelAtCurrentRow), str(addressAtCurrentRow))
        self.ui.tableWidgetSubscriptions.item(
            currentRow, 0).setTextColor(QApplication.palette().text().color())
        self.ui.tableWidgetSubscriptions.item(
            currentRow, 1).setTextColor(QApplication.palette().text().color())
        shared.reloadBroadcastSendersForWhichImWatching()

    def on_action_SubscriptionsDisable(self):
        currentRow = self.ui.tableWidgetSubscriptions.currentRow()
        labelAtCurrentRow = self.ui.tableWidgetSubscriptions.item(
            currentRow, 0).text().toUtf8()
        addressAtCurrentRow = self.ui.tableWidgetSubscriptions.item(
            currentRow, 1).text()
        sqlExecute(
            '''update subscriptions set enabled=0 WHERE label=? AND address=?''',
            str(labelAtCurrentRow), str(addressAtCurrentRow))
        self.ui.tableWidgetSubscriptions.item(
            currentRow, 0).setTextColor(QtGui.QColor(128, 128, 128))
        self.ui.tableWidgetSubscriptions.item(
            currentRow, 1).setTextColor(QtGui.QColor(128, 128, 128))
        shared.reloadBroadcastSendersForWhichImWatching()

    def on_context_menuSubscriptions(self, point):
        self.popMenuSubscriptions.exec_(
            self.ui.tableWidgetSubscriptions.mapToGlobal(point))

    # Group of functions for the Blacklist dialog box
    def on_action_BlacklistNew(self):
        self.click_pushButtonAddBlacklist()

    def on_action_BlacklistDelete(self):
        currentRow = self.ui.tableWidgetBlacklist.currentRow()
        labelAtCurrentRow = self.ui.tableWidgetBlacklist.item(
            currentRow, 0).text().toUtf8()
        addressAtCurrentRow = self.ui.tableWidgetBlacklist.item(
            currentRow, 1).text()
        if shared.config.get('bitmessagesettings', 'blackwhitelist') == 'black':
            sqlExecute(
                '''DELETE FROM blacklist WHERE label=? AND address=?''',
                str(labelAtCurrentRow), str(addressAtCurrentRow))
        else:
            sqlExecute(
                '''DELETE FROM whitelist WHERE label=? AND address=?''',
                str(labelAtCurrentRow), str(addressAtCurrentRow))
        self.ui.tableWidgetBlacklist.removeRow(currentRow)

    def on_action_BlacklistClipboard(self):
        currentRow = self.ui.tableWidgetBlacklist.currentRow()
        addressAtCurrentRow = self.ui.tableWidgetBlacklist.item(
            currentRow, 1).text()
        clipboard = QtGui.QApplication.clipboard()
        clipboard.setText(str(addressAtCurrentRow))

    def on_context_menuBlacklist(self, point):
        self.popMenuBlacklist.exec_(
            self.ui.tableWidgetBlacklist.mapToGlobal(point))

    def on_action_BlacklistEnable(self):
        currentRow = self.ui.tableWidgetBlacklist.currentRow()
        addressAtCurrentRow = self.ui.tableWidgetBlacklist.item(
            currentRow, 1).text()
        self.ui.tableWidgetBlacklist.item(
            currentRow, 0).setTextColor(QApplication.palette().text().color())
        self.ui.tableWidgetBlacklist.item(
            currentRow, 1).setTextColor(QApplication.palette().text().color())
        if shared.config.get('bitmessagesettings', 'blackwhitelist') == 'black':
            sqlExecute(
                '''UPDATE blacklist SET enabled=1 WHERE address=?''',
                str(addressAtCurrentRow))
        else:
            sqlExecute(
                '''UPDATE whitelist SET enabled=1 WHERE address=?''',
                str(addressAtCurrentRow))

    def on_action_BlacklistDisable(self):
        currentRow = self.ui.tableWidgetBlacklist.currentRow()
        addressAtCurrentRow = self.ui.tableWidgetBlacklist.item(
            currentRow, 1).text()
        self.ui.tableWidgetBlacklist.item(
            currentRow, 0).setTextColor(QtGui.QColor(128, 128, 128))
        self.ui.tableWidgetBlacklist.item(
            currentRow, 1).setTextColor(QtGui.QColor(128, 128, 128))
        if shared.config.get('bitmessagesettings', 'blackwhitelist') == 'black':
            sqlExecute(
                '''UPDATE blacklist SET enabled=0 WHERE address=?''', str(addressAtCurrentRow))
        else:
            sqlExecute(
                '''UPDATE whitelist SET enabled=0 WHERE address=?''', str(addressAtCurrentRow))

    # Group of functions for the Your Identities dialog box
    def on_action_YourIdentitiesNew(self):
        self.click_NewAddressDialog()

    def on_action_YourIdentitiesEnable(self):
        currentRow = self.ui.tableWidgetYourIdentities.currentRow()
        addressAtCurrentRow = str(
            self.ui.tableWidgetYourIdentities.item(currentRow, 1).text())
        shared.config.set(addressAtCurrentRow, 'enabled', 'true')
        with open(shared.appdata + 'keys.dat', 'wb') as configfile:
            shared.config.write(configfile)
        self.ui.tableWidgetYourIdentities.item(
            currentRow, 0).setTextColor(QApplication.palette().text().color())
        self.ui.tableWidgetYourIdentities.item(
            currentRow, 1).setTextColor(QApplication.palette().text().color())
        self.ui.tableWidgetYourIdentities.item(
            currentRow, 2).setTextColor(QApplication.palette().text().color())
        if shared.safeConfigGetBoolean(addressAtCurrentRow, 'mailinglist'):
            self.ui.tableWidgetYourIdentities.item(currentRow, 1).setTextColor(QtGui.QColor(137, 04, 177)) # magenta
        if shared.safeConfigGetBoolean(addressAtCurrentRow, 'chan'):
            self.ui.tableWidgetYourIdentities.item(currentRow, 1).setTextColor(QtGui.QColor(216, 119, 0)) # orange
        shared.reloadMyAddressHashes()

    def on_action_YourIdentitiesDisable(self):
        currentRow = self.ui.tableWidgetYourIdentities.currentRow()
        addressAtCurrentRow = str(
            self.ui.tableWidgetYourIdentities.item(currentRow, 1).text())
        shared.config.set(str(addressAtCurrentRow), 'enabled', 'false')
        self.ui.tableWidgetYourIdentities.item(
            currentRow, 0).setTextColor(QtGui.QColor(128, 128, 128))
        self.ui.tableWidgetYourIdentities.item(
            currentRow, 1).setTextColor(QtGui.QColor(128, 128, 128))
        self.ui.tableWidgetYourIdentities.item(
            currentRow, 2).setTextColor(QtGui.QColor(128, 128, 128))
        if shared.safeConfigGetBoolean(addressAtCurrentRow, 'mailinglist'):
            self.ui.tableWidgetYourIdentities.item(currentRow, 1).setTextColor(QtGui.QColor(137, 04, 177)) # magenta
        with open(shared.appdata + 'keys.dat', 'wb') as configfile:
            shared.config.write(configfile)
        shared.reloadMyAddressHashes()

    def on_action_YourIdentitiesClipboard(self):
        currentRow = self.ui.tableWidgetYourIdentities.currentRow()
        addressAtCurrentRow = self.ui.tableWidgetYourIdentities.item(
            currentRow, 1).text()
        clipboard = QtGui.QApplication.clipboard()
        clipboard.setText(str(addressAtCurrentRow))

    def on_action_YourIdentitiesClipboard2(self):
        currentRow2 = self.ui.youids.currentRow()
        addressAtCurrentRow2 = self.ui.youids.item(
            currentRow2, 0).text()
        clipboard2 = QtGui.QApplication.clipboard()
        clipboard2.setText(str(addressAtCurrentRow2))

    def on_action_YourAddressClipboard2(self):
        currentRow3 = self.ui.bitcoinaddresses.currentRow()
        addressAtCurrentRow3 = self.ui.bitcoinaddresses.item(
            currentRow3, 1).text()
        clipboard3 = QtGui.QApplication.clipboard()
        clipboard3.setText(str(addressAtCurrentRow3))

    def on_action_YourIdentitiesSetAvatar(self):
        self.on_action_SetAvatar(self.ui.tableWidgetYourIdentities)
        
    def on_action_AddressBookSetAvatar(self):
        self.on_action_SetAvatar(self.ui.tableWidgetAddressBook)
        
    def on_action_SubscriptionsSetAvatar(self):
        self.on_action_SetAvatar(self.ui.tableWidgetSubscriptions)
        
    def on_action_BlacklistSetAvatar(self):
        self.on_action_SetAvatar(self.ui.tableWidgetBlacklist)
        
    def on_action_SetAvatar(self, thisTableWidget):
        # thisTableWidget =  self.ui.tableWidgetYourIdentities
        if not os.path.exists(shared.appdata + 'avatars/'):
            os.makedirs(shared.appdata + 'avatars/')
        currentRow = thisTableWidget.currentRow()
        addressAtCurrentRow = thisTableWidget.item(
            currentRow, 1).text()
        hash = hashlib.md5(addBMIfNotPresent(addressAtCurrentRow)).hexdigest()
        extensions = ['PNG', 'GIF', 'JPG', 'JPEG', 'SVG', 'BMP', 'MNG', 'PBM', 'PGM', 'PPM', 'TIFF', 'XBM', 'XPM', 'TGA']
        # http://pyqt.sourceforge.net/Docs/PyQt4/qimagereader.html#supportedImageFormats
        names = {'BMP':'Windows Bitmap', 'GIF':'Graphic Interchange Format', 'JPG':'Joint Photographic Experts Group', 'JPEG':'Joint Photographic Experts Group', 'MNG':'Multiple-image Network Graphics', 'PNG':'Portable Network Graphics', 'PBM':'Portable Bitmap', 'PGM':'Portable Graymap', 'PPM':'Portable Pixmap', 'TIFF':'Tagged Image File Format', 'XBM':'X11 Bitmap', 'XPM':'X11 Pixmap', 'SVG':'Scalable Vector Graphics', 'TGA':'Targa Image Format'}
        filters = []
        all_images_filter = []
        current_files = []
        for ext in extensions:
            filters += [ names[ext] + ' (*.' + ext.lower() + ')' ]
            all_images_filter += [ '*.' + ext.lower() ]
            upper = shared.appdata + 'avatars/' + hash + '.' + ext.upper()
            lower = shared.appdata + 'avatars/' + hash + '.' + ext.lower()
            if os.path.isfile(lower):
                current_files += [lower]
            elif os.path.isfile(upper):
                current_files += [upper]
        filters[0:0] = ['Image files (' + ' '.join(all_images_filter) + ')']
        filters[1:1] = ['All files (*.*)']
        sourcefile = QFileDialog.getOpenFileName(self, _translate("MainWindow","Set avatar..."), filter = ';;'.join(filters))
        # determine the correct filename (note that avatars don't use the suffix)
        destination = shared.appdata + 'avatars/' + hash + '.' + sourcefile.split('.')[-1]
        exists = QtCore.QFile.exists(destination)
        if sourcefile == '':
            # ask for removal of avatar
            if exists | (len(current_files)>0):
                displayMsg = _translate("MainWindow", "Do you really want to remove this avatar?")
                overwrite = QtGui.QMessageBox.question(
                            self, 'Message', displayMsg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            else:
                overwrite = QtGui.QMessageBox.No
        else:
            # ask whether to overwrite old avatar
            if exists | (len(current_files)>0):
                displayMsg = _translate("MainWindow", "You have already set an avatar for this address. Do you really want to overwrite it?")
                overwrite = QtGui.QMessageBox.question(
                            self, 'Message', displayMsg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            else:
                overwrite = QtGui.QMessageBox.No
            
        # copy the image file to the appdata folder
        if (not exists) | (overwrite == QtGui.QMessageBox.Yes):
            if overwrite == QtGui.QMessageBox.Yes:
                for file in current_files:
                    QtCore.QFile.remove(file)
                QtCore.QFile.remove(destination)
            # copy it
            if sourcefile != '':
                copied = QtCore.QFile.copy(sourcefile, destination)
                if not copied:
                    print 'couldn\'t copy :('
                    return False
            # set the icon
            thisTableWidget.item(
                currentRow, 0).setIcon(avatarize(addressAtCurrentRow))
            self.rerenderSubscriptions()
            self.rerenderComboBoxSendFrom()
            self.rerenderFromBoxEscrow()
            self.rerenderYourIdentities_2()
            self.rerenderInboxFromLabels()
            self.rerenderInboxToLabels()
            self.rerenderSentFromLabels()
            self.rerenderSentToLabels()
        
    def on_context_menuYourIdentities(self, point):
        self.popMenu.exec_(
            self.ui.tableWidgetYourIdentities.mapToGlobal(point))
    def on_context_menuYourIdentities2(self, point):
        self.popMenu2.exec_(
            self.ui.youids.mapToGlobal(point))

    def on_context_menuYourAddress2(self, point):
        self.popMenu3.exec_(
            self.ui.bitcoinaddresses.mapToGlobal(point))

    def on_context_menuInbox(self, point):
        self.popMenuInbox.exec_(self.ui.tableWidgetInbox.mapToGlobal(point))

    def on_context_menuSent(self, point):
        self.popMenuSent = QtGui.QMenu(self)
        self.popMenuSent.addAction(self.actionSentClipboard)
        self.popMenuSent.addAction(self.actionTrashSentMessage)

        # Check to see if this item is toodifficult and display an additional
        # menu option (Force Send) if it is.
        currentRow = self.ui.tableWidgetSent.currentRow()
        ackData = str(self.ui.tableWidgetSent.item(
            currentRow, 3).data(Qt.UserRole).toPyObject())
        queryreturn = sqlQuery('''SELECT status FROM sent where ackdata=?''', ackData)
        for row in queryreturn:
            status, = row
        if status == 'toodifficult':
            self.popMenuSent.addAction(self.actionForceSend)
        self.popMenuSent.exec_(self.ui.tableWidgetSent.mapToGlobal(point))

    def inboxSearchLineEditPressed(self):
        searchKeyword = self.ui.inboxSearchLineEdit.text().toUtf8().data()
        searchOption = self.ui.inboxSearchOptionCB.currentText().toUtf8().data()
        self.ui.inboxSearchLineEdit.setText(QString(""))
        self.ui.textEditInboxMessage.setPlainText(QString(""))
        self.loadInbox(searchOption, searchKeyword)

    def sentSearchLineEditPressed(self):
        searchKeyword = self.ui.sentSearchLineEdit.text().toUtf8().data()
        searchOption = self.ui.sentSearchOptionCB.currentText().toUtf8().data()
        self.ui.sentSearchLineEdit.setText(QString(""))
        self.ui.textEditInboxMessage.setPlainText(QString(""))
        self.loadSent(searchOption, searchKeyword)


    def tableWidgetInboxItemClicked(self):
        currentRow = self.ui.tableWidgetInbox.currentRow()
        if currentRow >= 0:
            font = QFont()
            font.setBold(False)
            self.ui.textEditInboxMessage.setCurrentFont(font)
            
            fromAddress = str(self.ui.tableWidgetInbox.item(
                currentRow, 1).data(Qt.UserRole).toPyObject())
            msgid = str(self.ui.tableWidgetInbox.item(
                currentRow, 3).data(Qt.UserRole).toPyObject())
            queryreturn = sqlQuery(
                '''select message from inbox where msgid=?''', msgid)
            if queryreturn != []:
                for row in queryreturn:
                    messageText, = row
            messageText = shared.fixPotentiallyInvalidUTF8Data(messageText)
            messageText = unicode(messageText, 'utf-8)')
            if len(messageText) > 30000:
                messageText = (
                        messageText[:30000] + '\n' +
                        '--- Display of the remainder of the message ' +
                        'truncated because it is too long.\n' +
                        '--- To see the full message, right-click in the ' +
                        'Inbox view and select "View HTML code as formatted ' +
                        'text",\n' +
                        '--- or select "Save message as..." to save it to a ' +
                        'file, or select "Reply" and ' +
                        'view the full message in the quote.')
            # If we have received this message from either a broadcast address
            # or from someone in our address book, display as HTML
            if decodeAddress(fromAddress)[3] in shared.broadcastSendersForWhichImWatching or shared.isAddressInMyAddressBook(fromAddress):
                self.ui.textEditInboxMessage.setText(messageText)
            else:
                self.ui.textEditInboxMessage.setPlainText(messageText)

            self.ui.tableWidgetInbox.item(currentRow, 0).setFont(font)
            self.ui.tableWidgetInbox.item(currentRow, 1).setFont(font)
            self.ui.tableWidgetInbox.item(currentRow, 2).setFont(font)
            self.ui.tableWidgetInbox.item(currentRow, 3).setFont(font)

            inventoryHash = str(self.ui.tableWidgetInbox.item(
                currentRow, 3).data(Qt.UserRole).toPyObject())
            self.ubuntuMessagingMenuClear(inventoryHash)
            sqlExecute('''update inbox set read=1 WHERE msgid=?''', inventoryHash)
            self.changedInboxUnread()

    def tableWidgetSentItemClicked(self):
        currentRow = self.ui.tableWidgetSent.currentRow()
        if currentRow >= 0:
            ackdata = str(self.ui.tableWidgetSent.item(
                currentRow, 3).data(Qt.UserRole).toPyObject())
            queryreturn = sqlQuery(
                '''select message from sent where ackdata=?''', ackdata)
            if queryreturn != []:
                for row in queryreturn:
                    message, = row
            else:
                message = "Error occurred: could not load message from disk."
            message = unicode(message, 'utf-8)')
            self.ui.textEditSentMessage.setPlainText(message)

    def tableWidgetYourIdentitiesItemChanged(self):
        currentRow = self.ui.tableWidgetYourIdentities.currentRow()
        if currentRow >= 0:
            addressAtCurrentRow = self.ui.tableWidgetYourIdentities.item(
                currentRow, 1).text()
            shared.config.set(str(addressAtCurrentRow), 'label', str(
                self.ui.tableWidgetYourIdentities.item(currentRow, 0).text().toUtf8()))
            with open(shared.appdata + 'keys.dat', 'wb') as configfile:
                shared.config.write(configfile)
            self.rerenderComboBoxSendFrom()
            # self.rerenderInboxFromLabels()
            self.rerenderInboxToLabels()
            self.rerenderSentFromLabels()
            # self.rerenderSentToLabels()

    def tableWidgetAddressBookItemChanged(self):
        currentRow = self.ui.tableWidgetAddressBook.currentRow()
        if currentRow >= 0:
            addressAtCurrentRow = self.ui.tableWidgetAddressBook.item(
                currentRow, 1).text()
            sqlExecute('''UPDATE addressbook set label=? WHERE address=?''',
                       str(self.ui.tableWidgetAddressBook.item(currentRow, 0).text().toUtf8()),
                       str(addressAtCurrentRow))
        self.rerenderInboxFromLabels()
        self.rerenderSentToLabels()

    def tableWidgetSubscriptionsItemChanged(self):
        currentRow = self.ui.tableWidgetSubscriptions.currentRow()
        if currentRow >= 0:
            addressAtCurrentRow = self.ui.tableWidgetSubscriptions.item(
                currentRow, 1).text()
            sqlExecute('''UPDATE subscriptions set label=? WHERE address=?''',
                       str(self.ui.tableWidgetSubscriptions.item(currentRow, 0).text().toUtf8()),
                       str(addressAtCurrentRow))
        self.rerenderInboxFromLabels()
        self.rerenderSentToLabels()

    def writeNewAddressToTable(self, label, address, streamNumber):
        self.ui.tableWidgetYourIdentities.setSortingEnabled(False)
        self.ui.tableWidgetYourIdentities.insertRow(0)
        newItem = QtGui.QTableWidgetItem(unicode(label, 'utf-8'))
        newItem.setIcon(avatarize(address))
        self.ui.tableWidgetYourIdentities.setItem(
            0, 0, newItem)
        newItem = QtGui.QTableWidgetItem(address)
        newItem.setFlags(
            QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        if shared.safeConfigGetBoolean(address, 'chan'):
            newItem.setTextColor(QtGui.QColor(216, 119, 0)) # orange
        self.ui.tableWidgetYourIdentities.setItem(0, 1, newItem)
        newItem = QtGui.QTableWidgetItem(streamNumber)
        newItem.setFlags(
            QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        self.ui.tableWidgetYourIdentities.setItem(0, 2, newItem)
        # self.ui.tableWidgetYourIdentities.setSortingEnabled(True)
        self.rerenderComboBoxSendFrom()
        self.rerenderFromBoxEscrow()
        self.rerenderYourIdentities_2()

    def updateStatusBar(self, data):
        if data != "":
            with shared.printLock:
                print 'Status bar:', data

        self.statusBar().showMessage(data)


class helpDialog(QtGui.QDialog):

    def __init__(self, parent):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_helpDialog()
        self.ui.setupUi(self)
        self.parent = parent
        self.ui.labelHelpURI.setOpenExternalLinks(True)
        QtGui.QWidget.resize(self, QtGui.QWidget.sizeHint(self))
        
class connectDialog(QtGui.QDialog):

    def __init__(self, parent):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_connectDialog()
        self.ui.setupUi(self)
        self.parent = parent
        QtGui.QWidget.resize(self, QtGui.QWidget.sizeHint(self))

class aboutDialog(QtGui.QDialog):

    def __init__(self, parent):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_aboutDialog()
        self.ui.setupUi(self)
        self.parent = parent
        self.ui.labelVersion.setText('version ' + shared.softwareVersion)


class regenerateAddressesDialog(QtGui.QDialog):

    def __init__(self, parent):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_regenerateAddressesDialog()
        self.ui.setupUi(self)
        self.parent = parent
        QtGui.QWidget.resize(self, QtGui.QWidget.sizeHint(self))

class settingsDialog(QtGui.QDialog):

    def __init__(self, parent):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_settingsDialog()
        self.ui.setupUi(self)
        self.parent = parent
        self.ui.checkBoxStartOnLogon.setChecked(
            shared.config.getboolean('bitmessagesettings', 'startonlogon'))
        self.ui.checkBoxMinimizeToTray.setChecked(
            shared.config.getboolean('bitmessagesettings', 'minimizetotray'))
        self.ui.checkBoxShowTrayNotifications.setChecked(
            shared.config.getboolean('bitmessagesettings', 'showtraynotifications'))
        self.ui.checkBoxStartInTray.setChecked(
            shared.config.getboolean('bitmessagesettings', 'startintray'))
        self.ui.checkBoxWillinglySendToMobile.setChecked(
            shared.safeConfigGetBoolean('bitmessagesettings', 'willinglysendtomobile'))
        self.ui.checkBoxUseIdenticons.setChecked(
            shared.safeConfigGetBoolean('bitmessagesettings', 'useidenticons'))
        
        global languages 
        languages = ['system','en','eo','fr','de','es','ru','no','ar','zh_cn','en_pirate','other']
        user_countrycode = str(shared.config.get('bitmessagesettings', 'userlocale'))
        if user_countrycode in languages:
            curr_index = languages.index(user_countrycode)
        else:
            curr_index = languages.index('other')
        self.ui.languageComboBox.setCurrentIndex(curr_index)
        
        if shared.appdata == '':
            self.ui.checkBoxPortableMode.setChecked(True)
        if 'darwin' in sys.platform:
            self.ui.checkBoxStartOnLogon.setDisabled(True)
            self.ui.checkBoxStartOnLogon.setText(_translate(
                "MainWindow", "Start-on-login not yet supported on your OS."))
            self.ui.checkBoxMinimizeToTray.setDisabled(True)
            self.ui.checkBoxMinimizeToTray.setText(_translate(
                "MainWindow", "Minimize-to-tray not yet supported on your OS."))
            self.ui.checkBoxShowTrayNotifications.setDisabled(True)
            self.ui.checkBoxShowTrayNotifications.setText(_translate(
                "MainWindow", "Tray notifications not yet supported on your OS."))
        elif 'linux' in sys.platform:
            self.ui.checkBoxStartOnLogon.setDisabled(True)
            self.ui.checkBoxStartOnLogon.setText(_translate(
                "MainWindow", "Start-on-login not yet supported on your OS."))
            self.ui.checkBoxMinimizeToTray.setDisabled(True)
            self.ui.checkBoxMinimizeToTray.setText(_translate(
                "MainWindow", "Minimize-to-tray not yet supported on your OS."))
        # On the Network settings tab:
        self.ui.lineEditTCPPort.setText(str(
            shared.config.get('bitmessagesettings', 'port')))
        self.ui.checkBoxAuthentication.setChecked(shared.config.getboolean(
            'bitmessagesettings', 'socksauthentication'))
        self.ui.checkBoxSocksListen.setChecked(shared.config.getboolean(
            'bitmessagesettings', 'sockslisten'))
        if str(shared.config.get('bitmessagesettings', 'socksproxytype')) == 'none':
            self.ui.comboBoxProxyType.setCurrentIndex(0)
            self.ui.lineEditSocksHostname.setEnabled(False)
            self.ui.lineEditSocksPort.setEnabled(False)
            self.ui.lineEditSocksUsername.setEnabled(False)
            self.ui.lineEditSocksPassword.setEnabled(False)
            self.ui.checkBoxAuthentication.setEnabled(False)
            self.ui.checkBoxSocksListen.setEnabled(False)
        elif str(shared.config.get('bitmessagesettings', 'socksproxytype')) == 'SOCKS4a':
            self.ui.comboBoxProxyType.setCurrentIndex(1)
            self.ui.lineEditTCPPort.setEnabled(False)
        elif str(shared.config.get('bitmessagesettings', 'socksproxytype')) == 'SOCKS5':
            self.ui.comboBoxProxyType.setCurrentIndex(2)
            self.ui.lineEditTCPPort.setEnabled(False)

        self.ui.lineEditSocksHostname.setText(str(
            shared.config.get('bitmessagesettings', 'sockshostname')))
        self.ui.lineEditSocksPort.setText(str(
            shared.config.get('bitmessagesettings', 'socksport')))
        self.ui.lineEditSocksUsername.setText(str(
            shared.config.get('bitmessagesettings', 'socksusername')))
        self.ui.lineEditSocksPassword.setText(str(
            shared.config.get('bitmessagesettings', 'sockspassword')))
        QtCore.QObject.connect(self.ui.comboBoxProxyType, QtCore.SIGNAL(
            "currentIndexChanged(int)"), self.comboBoxProxyTypeChanged)

        self.ui.lineEditTotalDifficulty.setText(str((float(shared.config.getint(
            'bitmessagesettings', 'defaultnoncetrialsperbyte')) / shared.networkDefaultProofOfWorkNonceTrialsPerByte)))
        self.ui.lineEditSmallMessageDifficulty.setText(str((float(shared.config.getint(
            'bitmessagesettings', 'defaultpayloadlengthextrabytes')) / shared.networkDefaultPayloadLengthExtraBytes)))

        # Max acceptable difficulty tab
        self.ui.lineEditMaxAcceptableTotalDifficulty.setText(str((float(shared.config.getint(
            'bitmessagesettings', 'maxacceptablenoncetrialsperbyte')) / shared.networkDefaultProofOfWorkNonceTrialsPerByte)))
        self.ui.lineEditMaxAcceptableSmallMessageDifficulty.setText(str((float(shared.config.getint(
            'bitmessagesettings', 'maxacceptablepayloadlengthextrabytes')) / shared.networkDefaultPayloadLengthExtraBytes)))

        # Namecoin integration tab
        nmctype = shared.config.get('bitmessagesettings', 'namecoinrpctype')
        self.ui.lineEditNamecoinHost.setText(str(
            shared.config.get('bitmessagesettings', 'namecoinrpchost')))
        self.ui.lineEditNamecoinPort.setText(str(
            shared.config.get('bitmessagesettings', 'namecoinrpcport')))
        self.ui.lineEditNamecoinUser.setText(str(
            shared.config.get('bitmessagesettings', 'namecoinrpcuser')))
        self.ui.lineEditNamecoinPassword.setText(str(
            shared.config.get('bitmessagesettings', 'namecoinrpcpassword')))

        if nmctype == "namecoind":
            self.ui.radioButtonNamecoinNamecoind.setChecked(True)
        elif nmctype == "nmcontrol":
            self.ui.radioButtonNamecoinNmcontrol.setChecked(True)
            self.ui.lineEditNamecoinUser.setEnabled(False)
            self.ui.labelNamecoinUser.setEnabled(False)
            self.ui.lineEditNamecoinPassword.setEnabled(False)
            self.ui.labelNamecoinPassword.setEnabled(False)
        else:
            assert False

        QtCore.QObject.connect(self.ui.radioButtonNamecoinNamecoind, QtCore.SIGNAL(
            "toggled(bool)"), self.namecoinTypeChanged)
        QtCore.QObject.connect(self.ui.radioButtonNamecoinNmcontrol, QtCore.SIGNAL(
            "toggled(bool)"), self.namecoinTypeChanged)
        QtCore.QObject.connect(self.ui.pushButtonNamecoinTest, QtCore.SIGNAL(
            "clicked()"), self.click_pushButtonNamecoinTest)

        #Message Resend tab
        self.ui.lineEditDays.setText(str(
            shared.config.get('bitmessagesettings', 'stopresendingafterxdays')))
        self.ui.lineEditMonths.setText(str(
            shared.config.get('bitmessagesettings', 'stopresendingafterxmonths')))
        
        
        #'System' tab removed for now.
        """try:
            maxCores = shared.config.getint('bitmessagesettings', 'maxcores')
        except:
            maxCores = 99999
        if maxCores <= 1:
            self.ui.comboBoxMaxCores.setCurrentIndex(0)
        elif maxCores == 2:
            self.ui.comboBoxMaxCores.setCurrentIndex(1)
        elif maxCores <= 4:
            self.ui.comboBoxMaxCores.setCurrentIndex(2)
        elif maxCores <= 8:
            self.ui.comboBoxMaxCores.setCurrentIndex(3)
        elif maxCores <= 16:
            self.ui.comboBoxMaxCores.setCurrentIndex(4)
        else:
            self.ui.comboBoxMaxCores.setCurrentIndex(5)"""

        QtGui.QWidget.resize(self, QtGui.QWidget.sizeHint(self))

    def comboBoxProxyTypeChanged(self, comboBoxIndex):
        if comboBoxIndex == 0:
            self.ui.lineEditSocksHostname.setEnabled(False)
            self.ui.lineEditSocksPort.setEnabled(False)
            self.ui.lineEditSocksUsername.setEnabled(False)
            self.ui.lineEditSocksPassword.setEnabled(False)
            self.ui.checkBoxAuthentication.setEnabled(False)
            self.ui.checkBoxSocksListen.setEnabled(False)
            self.ui.lineEditTCPPort.setEnabled(True)
        elif comboBoxIndex == 1 or comboBoxIndex == 2:
            self.ui.lineEditSocksHostname.setEnabled(True)
            self.ui.lineEditSocksPort.setEnabled(True)
            self.ui.checkBoxAuthentication.setEnabled(True)
            self.ui.checkBoxSocksListen.setEnabled(True)
            if self.ui.checkBoxAuthentication.isChecked():
                self.ui.lineEditSocksUsername.setEnabled(True)
                self.ui.lineEditSocksPassword.setEnabled(True)
            self.ui.lineEditTCPPort.setEnabled(False)

    # Check status of namecoin integration radio buttons and translate
    # it to a string as in the options.
    def getNamecoinType(self):
        if self.ui.radioButtonNamecoinNamecoind.isChecked():
            return "namecoind"
        if self.ui.radioButtonNamecoinNmcontrol.isChecked():
            return "nmcontrol"
        assert False

    # Namecoin connection type was changed.
    def namecoinTypeChanged(self, checked):
        nmctype = self.getNamecoinType()
        assert nmctype == "namecoind" or nmctype == "nmcontrol"
            
        isNamecoind = (nmctype == "namecoind")
        self.ui.lineEditNamecoinUser.setEnabled(isNamecoind)
        self.ui.labelNamecoinUser.setEnabled(isNamecoind)
        self.ui.lineEditNamecoinPassword.setEnabled(isNamecoind)
        self.ui.labelNamecoinPassword.setEnabled(isNamecoind)

        if isNamecoind:
            self.ui.lineEditNamecoinPort.setText(shared.namecoinDefaultRpcPort)
        else:
            self.ui.lineEditNamecoinPort.setText("9000")

    # Test the namecoin settings specified in the settings dialog.
    def click_pushButtonNamecoinTest(self):
        self.ui.labelNamecoinTestResult.setText(_translate(
                "MainWindow", "Testing..."))
        options = {}
        options["type"] = self.getNamecoinType()
        options["host"] = self.ui.lineEditNamecoinHost.text()
        options["port"] = self.ui.lineEditNamecoinPort.text()
        options["user"] = self.ui.lineEditNamecoinUser.text()
        options["password"] = self.ui.lineEditNamecoinPassword.text()
        nc = namecoinConnection(options)
        response = nc.test()
        responseStatus = response[0]
        responseText = response[1]
        self.ui.labelNamecoinTestResult.setText(responseText)

        if responseStatus== 'success':
            self.parent.ui.pushButtonFetchNamecoinID.show()

class SpecialAddressBehaviorDialog(QtGui.QDialog):

    def __init__(self, parent):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_SpecialAddressBehaviorDialog()
        self.ui.setupUi(self)
        self.parent = parent
        currentRow = parent.ui.tableWidgetYourIdentities.currentRow()
        addressAtCurrentRow = str(
            parent.ui.tableWidgetYourIdentities.item(currentRow, 1).text())
        if not shared.safeConfigGetBoolean(addressAtCurrentRow, 'chan'):
            if shared.safeConfigGetBoolean(addressAtCurrentRow, 'mailinglist'):
                self.ui.radioButtonBehaviorMailingList.click()
            else:
                self.ui.radioButtonBehaveNormalAddress.click()
            try:
                mailingListName = shared.config.get(
                    addressAtCurrentRow, 'mailinglistname')
            except:
                mailingListName = ''
            self.ui.lineEditMailingListName.setText(
                unicode(mailingListName, 'utf-8'))
        else: # if addressAtCurrentRow is a chan address
            self.ui.radioButtonBehaviorMailingList.setDisabled(True)
            self.ui.lineEditMailingListName.setText(_translate(
                "MainWindow", "This is a chan address. You cannot use it as a pseudo-mailing list."))

        QtGui.QWidget.resize(self, QtGui.QWidget.sizeHint(self))


class AddAddressDialog(QtGui.QDialog):

    def __init__(self, parent):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_AddAddressDialog()
        self.ui.setupUi(self)
        self.parent = parent
        QtCore.QObject.connect(self.ui.lineEditAddress, QtCore.SIGNAL(
            "textChanged(QString)"), self.addressChanged)

    def addressChanged(self, QString):
        status, a, b, c = decodeAddress(str(QString))
        if status == 'missingbm':
            self.ui.labelAddressCheck.setText(_translate(
                "MainWindow", "The address should start with ''BM-''"))
        elif status == 'checksumfailed':
            self.ui.labelAddressCheck.setText(_translate(
                "MainWindow", "The address is not typed or copied correctly (the checksum failed)."))
        elif status == 'versiontoohigh':
            self.ui.labelAddressCheck.setText(_translate(
                "MainWindow", "The version number of this address is higher than this software can support. Please upgrade Bitmessage."))
        elif status == 'invalidcharacters':
            self.ui.labelAddressCheck.setText(_translate(
                "MainWindow", "The address contains invalid characters."))
        elif status == 'ripetooshort':
            self.ui.labelAddressCheck.setText(_translate(
                "MainWindow", "Some data encoded in the address is too short."))
        elif status == 'ripetoolong':
            self.ui.labelAddressCheck.setText(_translate(
                "MainWindow", "Some data encoded in the address is too long."))
        elif status == 'success':
            self.ui.labelAddressCheck.setText(
                _translate("MainWindow", "Address is valid."))

class NewSubscriptionDialog(QtGui.QDialog):

    def __init__(self, parent):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_NewSubscriptionDialog()
        self.ui.setupUi(self)
        self.parent = parent
        QtCore.QObject.connect(self.ui.lineEditSubscriptionAddress, QtCore.SIGNAL(
            "textChanged(QString)"), self.addressChanged)
        self.ui.checkBoxDisplayMessagesAlreadyInInventory.setText(
            _translate("MainWindow", "Enter an address above."))

    def addressChanged(self, QString):
        self.ui.checkBoxDisplayMessagesAlreadyInInventory.setEnabled(False)
        self.ui.checkBoxDisplayMessagesAlreadyInInventory.setChecked(False)
        status, addressVersion, streamNumber, ripe = decodeAddress(str(QString))
        if status == 'missingbm':
            self.ui.labelAddressCheck.setText(_translate(
                "MainWindow", "The address should start with ''BM-''"))
        elif status == 'checksumfailed':
            self.ui.labelAddressCheck.setText(_translate(
                "MainWindow", "The address is not typed or copied correctly (the checksum failed)."))
        elif status == 'versiontoohigh':
            self.ui.labelAddressCheck.setText(_translate(
                "MainWindow", "The version number of this address is higher than this software can support. Please upgrade Bitmessage."))
        elif status == 'invalidcharacters':
            self.ui.labelAddressCheck.setText(_translate(
                "MainWindow", "The address contains invalid characters."))
        elif status == 'ripetooshort':
            self.ui.labelAddressCheck.setText(_translate(
                "MainWindow", "Some data encoded in the address is too short."))
        elif status == 'ripetoolong':
            self.ui.labelAddressCheck.setText(_translate(
                "MainWindow", "Some data encoded in the address is too long."))
        elif status == 'success':
            self.ui.labelAddressCheck.setText(
                _translate("MainWindow", "Address is valid."))
            if addressVersion <= 3:
                self.ui.checkBoxDisplayMessagesAlreadyInInventory.setText(
                    _translate("MainWindow", "Address is an old type. We cannot display its past broadcasts."))
            else:
                shared.flushInventory()
                doubleHashOfAddressData = hashlib.sha512(hashlib.sha512(encodeVarint(
                    addressVersion) + encodeVarint(streamNumber) + ripe).digest()).digest()
                tag = doubleHashOfAddressData[32:]
                queryreturn = sqlQuery(
                    '''select hash from inventory where objecttype='broadcast' and tag=?''', tag)
                if len(queryreturn) == 0:
                    self.ui.checkBoxDisplayMessagesAlreadyInInventory.setText(
                        _translate("MainWindow", "There are no recent broadcasts from this address to display."))
                elif len(queryreturn) == 1:
                    self.ui.checkBoxDisplayMessagesAlreadyInInventory.setEnabled(True)
                    self.ui.checkBoxDisplayMessagesAlreadyInInventory.setText(
                        _translate("MainWindow", "Display the %1 recent broadcast from this address.").arg(str(len(queryreturn))))
                else:
                    self.ui.checkBoxDisplayMessagesAlreadyInInventory.setEnabled(True)
                    self.ui.checkBoxDisplayMessagesAlreadyInInventory.setText(
                        _translate("MainWindow", "Display the %1 recent broadcasts from this address.").arg(str(len(queryreturn))))


class NewAddressDialog(QtGui.QDialog):

    def __init__(self, parent):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_NewAddressDialog()
        self.ui.setupUi(self)
        self.parent = parent
        row = 1
        # Let's fill out the 'existing address' combo box with addresses from
        # the 'Your Identities' tab.
        while self.parent.ui.tableWidgetYourIdentities.item(row - 1, 1):
            self.ui.radioButtonExisting.click()
            # print
            # self.parent.ui.tableWidgetYourIdentities.item(row-1,1).text()
            self.ui.comboBoxExisting.addItem(
                self.parent.ui.tableWidgetYourIdentities.item(row - 1, 1).text())
            row += 1
        self.ui.groupBoxDeterministic.setHidden(True)
        QtGui.QWidget.resize(self, QtGui.QWidget.sizeHint(self))

class newChanDialog(QtGui.QDialog):

    def __init__(self, parent):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_newChanDialog()
        self.ui.setupUi(self)
        self.parent = parent
        self.ui.groupBoxCreateChan.setHidden(True)
        QtGui.QWidget.resize(self, QtGui.QWidget.sizeHint(self))

class sellDialog2(QtGui.QDialog):
    def __init__(self, parent):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_SellAlert()
        self.ui.setupUi(self)
        self.parent = parent

class litegrab(QtGui.QDialog):
    def __init__(self, parent):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_litegrab()
        self.ui.setupUi(self)
        self.parent = parent
        QtCore.QObject.connect(self.ui.liteonoff, QtCore.SIGNAL(
            "clicked()"), self.click_ok)
        QtCore.QObject.connect(self.ui.liteonoff, QtCore.SIGNAL("accepted()"), self.click_ok);
        QtCore.QObject.connect(self.ui.liteonoff, QtCore.SIGNAL("rejected()"), self.click_cancel);
    def click_ok(self):
        settings = shelve.open("settings.slv")
        settings["litemode"] = True
        settings.close()
        self.hide()
    def click_cancel(self):
        settings = shelve.open("settings.slv")
        settings["litemode"] = False
        settings.close()
        self.hide()

class sellDialog(QtGui.QDialog):
    def __init__(self, parent):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Sell()
        self.ui.setupUi(self)
        self.parent = parent
        QtCore.QObject.connect(self.ui.payandpost, QtCore.SIGNAL(
            "clicked()"), self.click_postandpay)
        QtCore.QObject.connect(self.ui.resend, QtCore.SIGNAL(
            "clicked()"), self.resending)
        self.rerenderBoxAddresses()
        QtCore.QObject.connect(self.ui.onlyreted, QtCore.SIGNAL(
            "clicked()"), self.click_rtd)
        QtCore.QObject.connect(self.ui.newsellcont, QtCore.SIGNAL(
            "clicked()"), self.click_newadr)
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL(
            "clicked()"), self.click_cancel)

        self.renderLocation()
    def resending(self):
        mform = MyForm()
        mform.rsend()
        self.ui.smthwrong.setText("Sending. Wait 20-40 minutes.")
    def click_postandpay(self):
        self.ui.smthwrong.setText("Wait please...")
        self.ui.payandpost.setEnabled(False)
        sndmess = MyForm()
        fraddress = str(self.ui.listaddresssell.currentText().toUtf8())
        accnt= "Address for post offers"
        subject = str(self.ui.categorytext.toPlainText().toUtf8())
        if self.ui.xcategory.currentText()=="Goods":
            subject = u"G"+subject
        elif self.ui.xcategory.currentText()=="Services":
            subject = u"S"+subject
        elif self.ui.xcategory.currentText()=="Currencies":
            subject = u"C"+subject
        fromAddress = str(self.ui.contactsell.currentText())

        if fraddress !="" and "Select bitcoin address for signing ad":
            if fromAddress != "" and "Contact address":
                amount=self.ui.doubleSpinBox.value()
                m = MyForm.addr1[4:6]+MyForm.addr2[4:7]
                if amount >= 0.0001:
                    try:
                        blnc = MyForm.conn.getbalance()
                    except:
                        blnc = -1
                    if blnc>=(amount+0.0005):
                        MyForm.conn.setaccount(fraddress, accnt)
                        list0 = MyForm.conn.listunspent(0)
                        elem = -1
                        for el in list0:
                            if el["address"] == fraddress:
                                if el["amount"]>=(amount+0.0001):
                                    elem = list0.index(el)
                                    list = list0
                                    continue
                        if elem == -1:
                            MyForm.conn.sendtoaddress(fraddress, amount+0.0005)
                            list = MyForm.conn.listunspent(0)
                            for el in list:
                                if el["address"] == fraddress:
                                    elem = list.index(el)
                                    continue
                            if elem ==-1:
                                time.sleep(5)
                                list = MyForm.conn.listunspent(0)
                                elem = -1
                                for el in list:
                                    if el["address"] == fraddress:
                                        elem = list.index(el)
                                        continue
                            if elem ==-1:
                                time.sleep(10)
                                list = MyForm.conn.listunspent(0)
                                elem = -1
                                for el in list:
                                    if el["address"] == fraddress:
                                        elem = list.index(el)
                                        continue
                        if elem!=-1 and m=="chEuR":
                            unsp = list[elem]
                            txid = unsp["txid"]
                            vout = unsp["vout"]
                            change = unsp["amount"] - (amount +0.0001)
                            address1 = MyForm.addr1
                            address2 = MyForm.addr2
                            amount = amount/2.0
                            if change == 0:
                                a = MyForm.conn.createrawtransaction(txid, vout, address1, address2, amount)
                            elif change < 0:
                                txid1=""
                                txid2=""
                                self.ui.smthwrong.setText("Have not unspent money...")
                            else:
                                a = MyForm.conn.createrawtransaction2(txid, vout, address1, address2, amount, fraddress, change)
                            a = MyForm.conn.signrawtransaction(a)
                            txid1 = MyForm.conn.sendrawtransaction(a["hex"])
                            txid2 = txid1
                        else:
                            self.ui.smthwrong.setText("Have not unspent money...")
                    elif blnc==-1:
                        self.ui.smthwrong.setText("Problem with bitcoin daemon.")
                    else:
                        self.ui.smthwrong.setText("Insufficient funds.")
                elif amount < 0.0001 and amount > 0:
                    self.ui.smthwrong.setText("Must be > 0.0001")
                else:
                    self.ui.smthwrong.setText("Try to update offer.")
                msg = str(self.ui.productdetails.toPlainText().toUtf8())
                loc = str(self.ui.location.currentText().toUtf8())
                sign = str(MyForm.conn.signmessage(fraddress,msg))
                messg = "+{" + str(fraddress) + "}+" + "-{"+str(msg)+"}-" + "-++"+str(sign)+"++-"+"{p{"+str(self.ui.sellprice.value())+"}p}"+"{t1{"+str(txid1)+"}t1}"+"{t2{"+str(txid2)+"}t2}"+"{c{"+str(fromAddress)+"}c}" + "{l{" + str(loc)+"}l}"
                #sellDialog.hide()
                self.hide()
                sndmess.sndmessage(messg,subject, fromAddress, MyForm.bitxbaychan)
                self.ui.smthwrong.setText("")
                resendoffer = shelve.open("lastoffer.slv")
                nowtime = str(datetime.datetime.now())
                resendoffer[fraddress] = {"message":messg,"subject":subject, "from":fromAddress, "btcfrom":fraddress, "resended":0, "time":nowtime}
                resendoffer.close()
                #self.close()
            else:
                self.ui.smthwrong.setText("Wrong contact address")
        else:
            self.ui.smthwrong.setText("Wrong address")
        self.ui.payandpost.setEnabled(True)
        self.newsellDialog2Instance = sellDialog2(self)
        if self.newsellDialog2Instance.exec_():
            return

    def click_cancel(self):
        self.hide()

    def click_newadr(self):
        try:
            mfrm = MyForm()
            mfrm.newaddressescrowbuyer()
            self.ui.smthwrong.setText("Done.Wait and reopen window.")
        except:
            self.ui.smthwrong.setText("Generating fail.")
        self.rerenderBoxAddresses()

    def renderLocation(self):
        if self.ui.location.currentText()=="":
            self.ui.location.clear()
            a = 0
            for i in MyForm.locations:
                self.ui.location.insertItem(a,i,i)
                self.ui.location.setCurrentIndex(0)
                a = a + 1


    def click_rtd(self):
        self.rerenderBoxAddresses()

    def rerenderBoxAddresses(self):
        if self.ui.onlyreted.isChecked():
            self.ui.listaddresssell.clear()
            #myratings = shelve.open("myratings.slv")
            mfrm = MyForm()
            for i in MyForm.allbtcaddreses:
                resl = mfrm.inlist(i)
                sum = resl["sum"]
                if sum > 0.00001:
                    self.ui.listaddresssell.insertItem(0,i,i)
                    self.ui.listaddresssell.setCurrentIndex(0)
        else:
            self.ui.listaddresssell.clear()
            self.ui.listaddresssell.insertItem(0, "Select bitcoin address for signing ad", "Select bitcoin address for signing ad")
            for i in MyForm.allbtcaddreses:
                self.ui.listaddresssell.insertItem(0,i,i)

            if(self.ui.listaddresssell.count() > 1):
                self.ui.listaddresssell.setCurrentIndex(1)
            else:
                self.ui.listaddresssell.setCurrentIndex(0)

        self.ui.contactsell.clear()
        configSections = shared.config.sections()
        for addressInKeysFile in configSections:
            if addressInKeysFile != 'bitmessagesettings' and addressInKeysFile!= MyForm.bitxbaychan:
                isEnabled = shared.config.getboolean(
                    addressInKeysFile, 'enabled')  # I realize that this is poor programming practice but I don't care. It's easier for others to read.
                if isEnabled:
                    self.ui.contactsell.insertItem(0, str(addressInKeysFile), addressInKeysFile)
        self.ui.contactsell.insertItem(0, "Select bitmessage sender's address", "Select bitmessage sender's address")
        if(self.ui.contactsell.count() > 1):
            self.ui.contactsell.setCurrentIndex(1)
        else:
            self.ui.contactsell.setCurrentIndex(0)


class iconGlossaryDialog(QtGui.QDialog):

    def __init__(self, parent):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_iconGlossaryDialog()
        self.ui.setupUi(self)
        self.parent = parent
        self.ui.labelPortNumber.setText(_translate(
            "MainWindow", "You are using TCP port %1. (This can be changed in the settings).").arg(str(shared.config.getint('bitmessagesettings', 'port'))))
        QtGui.QWidget.resize(self, QtGui.QWidget.sizeHint(self))


# In order for the time columns on the Inbox and Sent tabs to be sorted
# correctly (rather than alphabetically), we need to overload the <
# operator and use this class instead of QTableWidgetItem.
class myTableWidgetItem(QTableWidgetItem):

    def __lt__(self, other):
        return int(self.data(33).toPyObject()) < int(other.data(33).toPyObject())

class UISignaler(QThread):

    def __init__(self, parent=None):
        QThread.__init__(self, parent)

    def run(self):
        while True:
            command, data = shared.UISignalQueue.get()
            if command == 'writeNewAddressToTable':
                label, address, streamNumber = data
                self.emit(SIGNAL(
                    "writeNewAddressToTable(PyQt_PyObject,PyQt_PyObject,PyQt_PyObject)"), label, address, str(streamNumber))
            elif command == 'updateStatusBar':
                self.emit(SIGNAL("updateStatusBar(PyQt_PyObject)"), data)
            elif command == 'updateSentItemStatusByHash':
                hash, message = data
                self.emit(SIGNAL(
                    "updateSentItemStatusByHash(PyQt_PyObject,PyQt_PyObject)"), hash, message)
            elif command == 'updateSentItemStatusByAckdata':
                ackData, message = data
                self.emit(SIGNAL(
                    "updateSentItemStatusByAckdata(PyQt_PyObject,PyQt_PyObject)"), ackData, message)
            elif command == 'displayNewInboxMessage':
                inventoryHash, toAddress, fromAddress, subject, body = data
                self.emit(SIGNAL(
                    "displayNewInboxMessage(PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject)"),
                    inventoryHash, toAddress, fromAddress, subject, body)
            elif command == 'displayNewSentMessage':
                toAddress, fromLabel, fromAddress, subject, message, ackdata = data
                self.emit(SIGNAL(
                    "displayNewSentMessage(PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject)"),
                    toAddress, fromLabel, fromAddress, subject, message, ackdata)
            elif command == 'updateNetworkStatusTab':
                self.emit(SIGNAL("updateNetworkStatusTab()"))
            elif command == 'updateNumberOfMessagesProcessed':
                self.emit(SIGNAL("updateNumberOfMessagesProcessed()"))
            elif command == 'updateNumberOfPubkeysProcessed':
                self.emit(SIGNAL("updateNumberOfPubkeysProcessed()"))
            elif command == 'updateNumberOfBroadcastsProcessed':
                self.emit(SIGNAL("updateNumberOfBroadcastsProcessed()"))
            elif command == 'setStatusIcon':
                self.emit(SIGNAL("setStatusIcon(PyQt_PyObject)"), data)
            elif command == 'changedInboxUnread':
                self.emit(SIGNAL("changedInboxUnread(PyQt_PyObject)"), data)
            elif command == 'rerenderInboxFromLabels':
                self.emit(SIGNAL("rerenderInboxFromLabels()"))
            elif command == 'rerenderSentToLabels':
                self.emit(SIGNAL("rerenderSentToLabels()"))
            elif command == 'rerenderAddressBook':
                self.emit(SIGNAL("rerenderAddressBook()"))
            elif command == 'rerenderSubscriptions':
                self.emit(SIGNAL("rerenderSubscriptions()"))
            elif command == 'removeInboxRowByMsgid':
                self.emit(SIGNAL("removeInboxRowByMsgid(PyQt_PyObject)"), data)
            elif command == 'alert':
                title, text, exitAfterUserClicksOk = data
                self.emit(SIGNAL("displayAlert(PyQt_PyObject, PyQt_PyObject, PyQt_PyObject)"), title, text, exitAfterUserClicksOk)
            else:
                sys.stderr.write(
                    'Command sent to UISignaler not recognized: %s\n' % command)

def run():
    app = QtGui.QApplication(sys.argv)
    translator = QtCore.QTranslator()
    
    try:
        locale_countrycode = str(locale.getdefaultlocale()[0])
    except:
        # The above is not compatible with all versions of OSX.
        locale_countrycode = "en_US" # Default to english.
    locale_lang = locale_countrycode[0:2]
    user_countrycode = str(shared.config.get('bitmessagesettings', 'userlocale'))
    user_lang = user_countrycode[0:2]
    try:
        translation_path = os.path.join(sys._MEIPASS, "translations/bitmessage_")
    except Exception, e:
        translation_path = "translations/bitmessage_"
    
    if shared.config.get('bitmessagesettings', 'userlocale') == 'system':
        # try to detect the users locale otherwise fallback to English
        try:
            # try the users full locale, e.g. 'en_US':
            # since we usually only provide languages, not localozations
            # this will usually fail
            translator.load(translation_path + locale_countrycode)
        except:
            try:
                # try the users locale language, e.g. 'en':
                # since we usually only provide languages, not localozations
                # this will usually succeed
                translator.load(translation_path + locale_lang)
            except:
                # as English is already the default language, we don't
                # need to do anything. No need to translate.
                pass
    else:
        try:
            # check if the user input is a valid translation file:
            # since user_countrycode will be usually set by the combobox
            # it will usually just be a language code
            translator.load(translation_path + user_countrycode)
        except:
            try:
                # check if the user lang is a valid translation file:
                # this is only needed if the user manually set his 'userlocale'
                # in the keys.dat to a countrycode (e.g. 'de_CH')
                translator.load(translation_path + user_lang)
            except:
                # as English is already the default language, we don't
                # need to do anything. No need to translate.
                pass

    QtGui.QApplication.installTranslator(translator)
    app.setStyleSheet("QStatusBar::item { border: 0px solid black }")
    myapp = MyForm()

    if not shared.config.getboolean('bitmessagesettings', 'startintray'):
        myapp.show()

    myapp.appIndicatorInit(app)
    myapp.ubuntuMessagingMenuInit()
    myapp.notifierInit()
    if shared.safeConfigGetBoolean('bitmessagesettings', 'dontconnect'):
        myapp.showConnectDialog() # ask the user if we may connect
    sys.exit(app.exec_())
