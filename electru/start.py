import electrum_main
import threading, time, sys
from electrum import commands
from PyQt4 import QtGui, QtCore


class electrum_worker():
    gui = None
    thread = None
    monitor = None
    
    def __init__(self,password=''):
        self.thread = threading.Thread(target=electrum_main.main)
        self.thread.start()
        self.gui = None
        #self.password = password
        self.cmd = None
        while self.gui == None:
            self.gui = electrum_main.guiWindow
            time.sleep(0.1)
        while not self.gui.wallet:
                time.sleep(0.1)
        self.gui.wallet.create_master_keys('1of1',password)
        self.cmd = self.get_cmd(password)
            #self.monitor = threading.Thread(target=self._monitor)
    def get_cmd(self,password):
        cmd = commands.Commands(self.gui.wallet,self.gui.network)
        cmd.password = password
        return cmd 
    
    def _monitor(self):
        while self.thread.isAlive():
            time.sleep(0.1)
    
    def getnewaddress(self, length=1):
        gap_limit = ew.gui.wallet.gap_limit
        if self.gui.wallet.has_master_public_keys('1of1'):
            old_addrs = self.gui.wallet.addresses()
            self.gui.wallet.change_gap_limit(gap_limit+length)
            new_addrs = self.gui.wallet.addresses()
            while len(old_addrs)==len(new_addrs):
                new_addrs = self.gui.wallet.addresses()
                time.sleep(0.01)
            return [e for e in new_addrs if not e in old_addrs]
        else:
            return []
    
    def getaccountaddress(self):
        return self.gui.wallet.addresses() 
    
    def addmultisigaddress(self,num,pubkeys):
        return self.cmd.createmultisig(num, pubkeys)
    
    def createrawtransaction(self, inputs, outputs):
        return self.cmd.createrawtransaction(inputs, outputs)
    
    def decoderawtransaction(self, raw):
        return self.cmd.decoderawtransaction(raw)
    
    def signrawtransaction(self, raw_tx, input_info, private_keys):
        return self.cmd.signrawtransaction(raw_tx, input_info, private_keys)
    
    def sendrawtransaction(self, raw):
        return self.cmd.sendrawtransaction(raw)
        
    def listunspent(self):
        return self.cmd.listunspent()
        
    def dumpprivkey(self, addr):
        return self.cmd.dumpprivkey(addr)
    
    def importprivkey(self, sec):
        return self.cmd.importprivkey(sec)
    
    def sendtoaddress(self,to_address,amount):
        try:
            result = self.cmd.payto(to_address, amount)
        except:
            result = 'Not enough funds'
        return result
    
    def getrawtransaction(self, tx_hash):
        return self.cmd.getrawtransaction(tx_hash)
    
    def listtransactions(self, addr):
        return self.cmd.getaddresshistory(addr)
    
    def validateaddress(self, addr):
        return self.cmd.validateaddress(addr)['isvalid']
    
    def verifymessage(self, address, signature, message):
        return self.cmd.verifymessage(address, signature, message)
    
    def signmessage(self, address, message):
        return self.cmd.signmessage(address, message)
       
    def getbalance(self, account= None):
        return self.cmd.getbalance(account)['confirmed']
    
    def close(self):
        sys.exit(0)
        #self.gui.
        
    

#TEST
def elec():     
    ew = electrum_worker('Password')
    while True:
        print ew.getbalance()
        time.sleep(1)
        print ew.getbalance()
        ew.close()




from PyQt4.QtGui import QApplication, QLabel

def createLabel():
    label = QLabel("Hello, world!")
    t = threading.Thread(target=elec)
    t.start()
    print 1
    label.show()

app = QApplication([])
createLabel()

app.exec_()
#END_TEST





        
        
 
#win = HelloWorld()       
#t = threading.Thread(target=elec)
#t.start()
#print ew.validateaddress('1HpzuF4pPUUvGabbGR3DdHLW1RkHqgekKt')
#sign = ew.signmessage('1KYP3p6Eq73AEm7EHhQPCVNqSPL3rLnKLy', 'hello')
#print ew.verifymessage('1KYP3p6Eq73AEm7EHhQPCVNqSPL3rLnKLy', sign, 'hello')
#print ew.getrawtransaction('837dea37ddc8b1e3ce646f1a656e79bbd8cc7f558ac56a169626d649ebe2a3ba')
#print ew.sendtoaddress('1LT434odTUyrfm5RVBdsbQU3znPSAh4JRx',0.000001)
#print ew.decoderawtransaction('0100000001aca7f3b45654c230e0886a57fb988c3044ef5e8f7f39726d305c61d5e818903c00000000fd5d010048304502200187af928e9d155c4b1ac9c1c9118153239aba76774f775d7c1f9c3e106ff33c0221008822b0f658edec22274d0b6ae9de10ebf2da06b1bbdaaba4e50eb078f39e3d78014730440220795f0f4f5941a77ae032ecb9e33753788d7eb5cb0c78d805575d6b00a1d9bfed02203e1f4ad9332d1416ae01e27038e945bc9db59c732728a383a6f1ed2fb99da7a4014cc952410491bba2510912a5bd37da1fb5b1673010e43d2c6d812c514e91bfa9f2eb129e1c183329db55bd868e209aac2fbc02cb33d98fe74bf23f0c235d6126b1d8334f864104865c40293a680cb9c020e7b1e106d8c1916d3cef99aa431a56d253e69256dac09ef122b1a986818a7cb624532f062c1d1f8722084861c5c3291ccffef4ec687441048d2455d2403e08708fc1f556002f1b6cd83f992d085097f9974ab08a28838f07896fbab08f39495e15fa6fad6edbfb1e754e35fa1c7844c41f322a1863d4621353aeffffffff0140420f00000000001976a914ae56b4db13554d321c402db3961187aed1bbed5b88ac00000000') 
        


