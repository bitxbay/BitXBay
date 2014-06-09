#!/usr/bin/env python


import urllib2, base64, json, binascii
import config
import deserialize
from BCDataStream import *
import helper


def request(_data=None):
    code = 0
    result = None
    try:
        url = 'http://' + config.server + ':' + config.port
        headers = {"Authorization":"Basic " + base64.b64encode(config.user + ':' +config.password),"Content-type":"application/json"}
        req = urllib2.Request(url, _data, headers)
        response = urllib2.urlopen(req)
        _str = response.read()
        result =  json.loads(_str)
    except urllib2.HTTPError, e:
        code = e.code
        if code == 500:
            result =  json.loads(e.read().decode(config.encoding).encode('utf-8'))  
        if code == 401:
            result = {"result":None,"error":{"code":code,"message":"Invalid username or password"}}
    except urllib2.URLError, e:
        code = 404
        result = {"result":None,"error":{"code":code,"message":"Not found"}}
    return result

def sendtoaddress(address, amount=0, comment="", comment_to=""):
    obj = {"method":"sendtoaddress","params": [address,amount,comment,comment_to],"id":"1"}
    _data = json.dumps(obj)
    result = request(_data)
    return result

def getrawtransaction(txid):
    obj = {"method":"getrawtransaction","params": [txid],"id":"1"}
    _data = json.dumps(obj)
    result = request(_data)
    return result
    
def sendbitcoin(address, amount=0, comment="", comment_to=""):
    txid = sendtoaddress(address, amount, comment, comment_to)
    if txid['result']:
        _raw = getrawtransaction(txid['result'])
        if _raw['result']:
            ds = BCDataStream()
            ds.write(binascii.unhexlify(_raw['result']))
            _raw['result'] = deserialize.deserialize_TransactionRaw(deserialize.parse_Transaction(ds))
        return _raw
    else:
        if txid['error']['code']==-4:
            txid['error']['message']="Insufficient funds"
    return txid
    #{u'id': u'1', u'result': [{'address': '1KYjbZUcVpxJjND8XdANqviKZGYFu34KZp'}], u'error': None}    

