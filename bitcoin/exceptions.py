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
Exception definitions.
"""
class BitcoinException(Exception):
    """
    Base class for exceptions received from Bitcoin server.
    
    - *code* -- Error code from ``bitcoind``.
    """
    # Bitcoin specific error codes
    GENERIC = -1
    SAFEMODE = -2
    INVALID_AMOUNT = -3
    SEND_ERROR = -4
    INVALID_TRANSACTION_ID = -5
    INSUFFICIENT_FUNDS = -6
    OUT_OF_MEMORY = -7
    INVALID_PARAMETER = -8
    NOT_CONNECTED = -9
    DOWNLOADING_BLOCKS = -10
    # General JSON error codes
    PARSE_ERROR = -32700
    MISSING_METHOD = -32600
    METHOD_MUST_BE_STRING = -32600
    PARAMS_MUST_BE_ARRAY = -32600
    METHOD_NOT_FOUND = -32601
    
    def __init__(self, error):
        Exception.__init__(self, error['message'])
        self.code = error['code']

class SafeMode(BitcoinException):
    """
    Operation denied in safe mode (run ``bitcoind`` with ``-disablesafemode``).
    """

class InvalidAmount(BitcoinException):
    """
    Invalid amount.
    """
        
class SendError(BitcoinException):
    """
    Error while sending coins.
    """

class InvalidTransactionID(BitcoinException):
    """
    Invalid transaction ID.
    """

class InsufficientFunds(BitcoinException):
    """
    Insufficient funds to complete transaction.
    """

class OutOfMemory(BitcoinException):
    """
    Out of memory during operation.
    """

class InvalidParameter(BitcoinException):
    """
    Invalid parameter provided to function.
    """
    
class NotConnected(BitcoinException):
    """
    Not connected to any peers.
    """

class DownloadingBlocks(BitcoinException):
     """
    Client is still downloading blocks.
    """

# For convenience, we define more specific exception classes
# for the more common errors.
_exception_map = {
    BitcoinException.SAFEMODE: SafeMode,
    BitcoinException.INVALID_AMOUNT: InvalidAmount,
    BitcoinException.SEND_ERROR: SendError,
    BitcoinException.INVALID_TRANSACTION_ID: InvalidTransactionID,
    BitcoinException.INSUFFICIENT_FUNDS: InsufficientFunds,
    BitcoinException.OUT_OF_MEMORY: OutOfMemory,
    BitcoinException.INVALID_PARAMETER: InvalidParameter,
    BitcoinException.NOT_CONNECTED: NotConnected,
    BitcoinException.DOWNLOADING_BLOCKS: DownloadingBlocks
}

def _wrap_exception(error):
    """
    Convert a JSON error object to a more specific Bitcoin exception.
    """
    return _exception_map.get(error['code'], BitcoinException)(error)   

