# Copyright (c) 2010 Witchspace <witchspace81@gmail.com>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
Connect to Bitcoin server via JSON-RPC.
"""
from bitcoin.proxy import JSONRPCException, ServiceProxy
from bitcoin.exceptions import _wrap_exception
from bitcoin.data import ServerInfo,AccountInfo,AddressInfo,TransactionInfo,AddressValidation,WorkItem,Verification

class BitcoinConnection(object):
    """
    A BitcoinConnection object defines a connection to a bitcoin server.
    It is a thin wrapper around a JSON-RPC API connection.
    
    Up-to-date for SVN revision 198.
    
    Arguments to constructor:
    
    - *user* -- Authenticate as user.
    - *password* -- Authentication password.
    - *host* -- Bitcoin JSON-RPC host.
    - *port* -- Bitcoin JSON-RPC port.
    """
    def __init__(self, user, password, host='localhost', port=8332):
        """
        Create a new bitcoin server connection.
        """
        url = 'http://%s:%s@%s:%s/' % (
            user, password, host, port
            )
        try:
            self.proxy = ServiceProxy(url)
        except JSONRPCException,e:
            raise _wrap_exception(e.error)

    def stop(self):
        """
        Stop bitcoin server.
        """
        try:
            self.proxy.stop()
        except JSONRPCException,e:
            raise _wrap_exception(e.error)
            
    def getblockcount(self):
        """
        Returns the number of blocks in the longest block chain.
        """
        try:
            return self.proxy.getblockcount()
        except JSONRPCException,e:
            raise _wrap_exception(e.error)

    def addmultisigaddress (self, n, key1, account=None):

        try:
            if account is None:
                return  self.proxy.addmultisigaddress(n,key1)
            else:
                return self.proxy.addmultisigaddress(n,key1,account)
        except JSONRPCException,e:
            raise _wrap_exception(e.error)

    def createrawtransaction (self, txid, vout, address1, address2, amount):

        try:
            return self.proxy.createrawtransaction([{"txid":txid, "vout":vout}],{address1:amount, address2:amount} )
        except JSONRPCException,e:
            raise _wrap_exception(e.error)

    def createrawtransaction2 (self, txid, vout, address1, address2, amount, address3, amount2):

        try:
            return self.proxy.createrawtransaction([{"txid":txid, "vout":vout}],{address1:amount, address2:amount, address3:amount2} )
        except JSONRPCException,e:
            raise _wrap_exception(e.error)

    def signrawtransaction (self, hexy):

        try:
            return self.proxy.signrawtransaction(hexy)
        except JSONRPCException,e:
            raise _wrap_exception(e.error)

    def sendrawtransaction (self, hexy):

        try:
            return self.proxy.sendrawtransaction(hexy)
        except JSONRPCException,e:
            raise _wrap_exception(e.error)

    def listunspent (self, verified=0):

        try:
            return self.proxy.listunspent(verified)
        except JSONRPCException,e:
            raise _wrap_exception(e.error)

    def getconnectioncount(self):
        """
        Returns the number of connections to other nodes.
        """
        try:
            return self.proxy.getconnectioncount()
        except JSONRPCException,e:
            raise _wrap_exception(e.error)

    def getdifficulty(self):
        """
        Returns the proof-of-work difficulty as a multiple of the minimum difficulty.
        """
        try:
            return self.proxy.getdifficulty()
        except JSONRPCException,e:
            raise _wrap_exception(e.error)

    def getgenerate(self):
        """
        Returns :const:`True` or :const:`False`, depending on whether generation is enabled.
        """
        try:
            return self.proxy.getgenerate()
        except JSONRPCException,e:
            raise _wrap_exception(e.error)

    def setgenerate(self, generate, genproclimit=None):
        """
        Enable or disable generation (mining) of coins.
        
        Arguments:

        - *generate* -- is :const:`True` or :const:`False` to turn generation on or off.
        - *genproclimit* -- Number of processors that are used for generation, -1 is unlimited.

        """
        try:
            if genproclimit is None:
                return self.proxy.setgenerate(generate)
            else:
                return self.proxy.setgenerate(generate, genproclimit)
        except JSONRPCException,e:
            raise _wrap_exception(e.error)

    def gethashespersec(self):
        """
        Returns a recent hashes per second performance measurement while generating.
        """
        try:
            return self.proxy.gethashespersec()
        except JSONRPCException,e:
            raise _wrap_exception(e.error)

    def getinfo(self):
        """
        Returns an :class:`~bitcoin.data.ServerInfo` object containing various state info.
        """
        try:
            return self.proxy.getinfo()
        except JSONRPCException,e:
            raise _wrap_exception(e.error)

    def getpeerinfo(self):
        """
        Returns an peer info.
        """
        try:
            return self.proxy.getpeerinfo()
        except JSONRPCException,e:
            raise _wrap_exception(e.error)

    def getnewaddress(self, account=None):
        """
        Returns a new bitcoin address for receiving payments.
        
        Arguments:

        - *account* -- If account is specified (recommended), it is added to the address book
          so that payments received with the address will be credited to it.

        """
        try:
            if account is None:
                return self.proxy.getnewaddress()
            else:
                return self.proxy.getnewaddress(account)
        except JSONRPCException,e:
            raise _wrap_exception(e.error)

    def getaccountaddress(self, account):
        """
        Returns the current bitcoin address for receiving payments to an account.
        
        Arguments:
        
        - *account* -- Account for which the address should be returned.

        """
        try:
            return self.proxy.getaccountaddress(account)
        except JSONRPCException,e:
            raise _wrap_exception(e.error)

    def setaccount(self, bitcoinaddress, account):
        """
        Sets the account associated with the given address.
        
        Arguments:

        - *bitcoinaddress* -- Bitcoin address to associate.
        - *account* -- Account to associate the address to.

        """
        try:
            return self.proxy.setaccount(bitcoinaddress, account)
        except JSONRPCException,e:
            raise _wrap_exception(e.error)

    def getaccount(self, bitcoinaddress):
        """
        Returns the account associated with the given address.
        
        Arguments:
        
        - *bitcoinaddress* -- Bitcoin address to get account for.
        """
        try:
            return self.proxy.getaccount(bitcoinaddress)
        except JSONRPCException,e:
            raise _wrap_exception(e.error)

    def getaddressesbyaccount(self, account):
        """
        Returns the list of addresses for the given account.
        
        Arguments:
        
        - *account* -- Account to get list of addresses for.
        """ 
        try:
            return self.proxy.getaddressesbyaccount(account) 
        except JSONRPCException,e:
            raise _wrap_exception(e.error)


    def dumpprivkey(self, address):
        """
        Returns the dump.
        
        """ 
        try:
            return self.proxy.dumpprivkey(address) 
        except JSONRPCException,e:
            raise _wrap_exception(e.error)

    def importprivkey(self, address, label=None, rescan=False):
        """
        import the dump.
        
        """ 
        try:
            if label is None:
                return self.proxy.importprivkey(address, rescan)
            else:
                return self.proxy.importprivkey(address, label, rescan)
        except JSONRPCException,e:
            raise _wrap_exception(e.error)

    def sendtoaddress(self, bitcoinaddress, amount, comment=None, comment_to=None):
        """
        Sends *amount* from the server's available balance to *bitcoinaddress*.
        
        Arguments:
        
        - *bitcoinaddress* -- Bitcoin address to send to.
        - *amount* -- Amount to send (float, rounded to the nearest 0.01).
        - *minconf* -- Minimum number of confirmations required for transferred balance.
        - *comment* -- Comment for transaction.
        - *comment_to* -- Comment for to-address.

        """
        try:
            if comment is None:
                return self.proxy.sendtoaddress(bitcoinaddress, amount)
            elif comment_to is None:
                return self.proxy.sendtoaddress(bitcoinaddress, amount, comment)
            else:
                return self.proxy.sendtoaddress(bitcoinaddress, amount, comment, comment_to)
        except JSONRPCException,e:
            raise _wrap_exception(e.error)
  
    def getreceivedbyaddress(self, bitcoinaddress, minconf=1):
        """
        Returns the total amount received by a bitcoin address in transactions with at least a
        certain number of confirmations.
        
        Arguments:

        - *bitcoinaddress* -- Address to query for total amount.

        - *minconf* -- Number of confirmations to require, defaults to 1.
        """
        try:
            return self.proxy.getreceivedbyaddress(bitcoinaddress, minconf)
        except JSONRPCException,e:
            raise _wrap_exception(e.error)

    def getrawtransaction(self, txid, verbose=1):
        try:
            return self.proxy.getrawtransaction(txid, verbose)
        except JSONRPCException,e:
            raise _wrap_exception(e.error)
        
    def getreceivedbyaccount(self, account, minconf=1):
        """
        Returns the total amount received by addresses with an account in transactions with 
        at least a certain number of confirmations.
        
        Arguments:
        
        - *account* -- Account to query for total amount.
        - *minconf* -- Number of confirmations to require, defaults to 1.

        """
        try:
            return self.proxy.getreceivedbyaccount(account, minconf)
        except JSONRPCException,e:
            raise _wrap_exception(e.error)

    def listreceivedbyaddress(self, minconf=1, includeempty=False):
        """
        Returns a list of addresses.
        
        Each address is represented with a :class:`~bitcoin.data.AddressInfo` object.

        Arguments:
        
        - *minconf* -- Minimum number of confirmations before payments are included.
        - *includeempty* -- Whether to include addresses that haven't received any payments.

        """
        try:
            return [AddressInfo(*x) for x in self.proxy.listreceivedbyaddress(minconf, includeempty)]
        except JSONRPCException,e:
            raise _wrap_exception(e.error)
        
    def listreceivedbyaccount(self, minconf=1, includeempty=False):
        """
        Returns a list of accounts.
        
        Each account is represented with a :class:`~bitcoin.data.AccountInfo` object.
        
        Arguments:
        
        - *minconf* -- Minimum number of confirmations before payments are included.
        
        - *includeempty* -- Whether to include addresses that haven't received any payments.
        """
        try:
            return [AccountInfo(**x) for x in self.proxy.listreceivedbyaccount(minconf, includeempty)]
        except JSONRPCException,e:
            raise _wrap_exception(e.error)

    def listtransactions(self):
        """
        Returns a list of the last transactions for an account.
        
        Each transaction is represented with a :class:`~bitcoin.data.TransactionInfo` object.
        
        Arguments:
        
        - *minconf* -- Minimum number of confirmations before payments are included.
        - *count* -- Number of transactions to return.

        """
        try:
            return self.proxy.listtransactions()
        except JSONRPCException,e:
            raise _wrap_exception(e.error)

    def listaddressgroupings(self):
        """
        Returns a list of the last transactions for an account.

        Each transaction is represented with a :class:`~bitcoin.data.TransactionInfo` object.

        Arguments:

        - *minconf* -- Minimum number of confirmations before payments are included.
        - *count* -- Number of transactions to return.

        """
        try:
            return self.proxy.listaddressgroupings()
        except JSONRPCException,e:
            raise _wrap_exception(e.error)

    def listaccounts(self):
        """
        Returns a list of the last transactions for an account.

        Each transaction is represented with a :class:`~bitcoin.data.TransactionInfo` object.

        Arguments:

        - *minconf* -- Minimum number of confirmations before payments are included.
        - *count* -- Number of transactions to return.

        """
        try:
            return self.proxy.listaccounts()
        except JSONRPCException,e:
            raise _wrap_exception(e.error)

    def backupwallet(self, destination):
        """
        Safely copies ``wallet.dat`` to *destination*, which can be a directory or a path with filename.
        
        Arguments:
        - *destination* -- directory or path with filename to backup wallet to.

        """
        try:
            return self.proxy.backupwallet(destination)
        except JSONRPCException,e:
            raise _wrap_exception(e.error)

    def validateaddress(self, validateaddress):
        """
        Validate a bitcoin address and return information for it.

        The information is represented by a :class:`~bitcoin.data.AddressValidation` object.
        
        Arguments:
        
        - *validateaddress* -- Address to validate.

        """
        try:
            return AddressValidation(**self.proxy.validateaddress(validateaddress))
        except JSONRPCException,e:
            raise _wrap_exception(e.error)
			

    def verifymessage(self, address, signature, message):
        try:
            return self.proxy.verifymessage(address, signature, message)
        except JSONRPCException,e:
            raise _wrap_exception(e.error)

    def signmessage(self, address, message):
        try:
            return self.proxy.signmessage(address, message)
        except JSONRPCException,e:
            raise _wrap_exception(e.error)
        
    def getbalance(self, account=None):
        """
        Get the current balance, either for an account or the total server balance.
        
        Arguments:
        - *account* -- If this parameter is specified, returns the balance in the account.

        """
        try:
            if account is None:
                return self.proxy.getbalance()
            else:
                return self.proxy.getbalance(account)
        except JSONRPCException,e:
            raise _wrap_exception(e.error)
        
    def move(self, fromaccount, toaccount, amount, minconf=1, comment=None):
        """
        Move from one account in your wallet to another.
        
        Arguments:
        
        - *fromaccount* -- Source account name.
        - *toaccount* -- Destination account name.
        - *amount* -- Amount to transfer.
        - *minconf* -- Minimum number of confirmations required for transferred balance.
        - *comment* -- Comment to add to transaction log.
        
        """
        try:
            if comment is None:
                return self.proxy.move(fromaccount, toaccount, amount, minconf)
            else:
                return self.proxy.move(fromaccount, toaccount, amount, minconf, comment)
        except JSONRPCException,e:
            raise _wrap_exception(e.error)

    def sendfrom(self, fromaccount, tobitcoinaddress, amount, minconf=1, comment=None, comment_to=None):
        """
        Sends amount from account's balance to bitcoinaddress. This method will fail 
        if there is less than amount bitcoins with minconf confirmations in the account's 
        balance (unless account is the empty-string-named default account; it 
        behaves like the sendtoaddress method). Returns transaction ID on success.
        
        Arguments:
        
        - *fromaccount* -- Account to send from.
        - *tobitcoinaddress* -- Bitcoin address to send to.
        - *amount* -- Amount to send (float, rounded to the nearest 0.01).
        - *minconf* -- Minimum number of confirmations required for transferred balance.
        - *comment* -- Comment for transaction.
        - *comment_to* -- Comment for to-address.

        """
        try:
            if comment is None:
                return self.proxy.sendfrom(fromaccount, tobitcoinaddress, amount, minconf)
            elif comment_to is None:
                return self.proxy.sendfrom(fromaccount, tobitcoinaddress, amount, minconf, comment)
            else:
                return self.proxy.sendfrom(fromaccount, tobitcoinaddress, amount, minconf, comment, comment_to)
        except JSONRPCException,e:
            raise _wrap_exception(e.error)

    def getwork(self, data=None):
        """
        Get work for remote mining, or submit result. 
        If data is specified, the server tries to solve the block 
        using the provided data and returns :const:`True` if it was successful.
        If not, the function returns formatted hash data (:class:`~bitcoin.data.WorkItem`) 
        to work on.
        
        Arguments:
        
        - *data* -- Result from remote mining.

        """
        try:
            if data is None:
                # Only if no data provided, it returns a WorkItem
                return WorkItem(**self.proxy.getwork())
            else:
                return self.proxy.getwork(data)
        except JSONRPCException,e:
            raise _wrap_exception(e.error)

