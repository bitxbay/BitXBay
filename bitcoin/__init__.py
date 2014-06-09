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
bitcoin-python - Easy-to-use Bitcoin API client
"""
def connect_to_local():
    """
    Connect to default bitcoin instance owned by this user, on this machine.
    
    Returns a :class:`~bitcoin.connection.BitcoinConnection` object.
    """
    from bitcoin.connection import BitcoinConnection
    from bitcoin.config import read_default_config    

    cfg = read_default_config()
    port = int(cfg.get('rpcport', '8332'))
    return BitcoinConnection(cfg['rpcuser'],cfg['rpcpassword'],'localhost',port)
    
def connect_to_remote(user, password, host='localhost', port=8332):
    """
    Connect to remote or alternative local bitcoin client instance.

    Returns a :class:`~bitcoin.connection.BitcoinConnection` object.
    """
    from bitcoin.connection import BitcoinConnection

    return BitcoinConnection(user, password, host, port)

