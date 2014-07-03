#!/usr/bin/env python

import urllib2, json, datetime, calendar
import config, helper

def request(_query=''):
    code = 0
    result = None
    try:
        url = config.service  + _query
        req = urllib2.Request(url)
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

def get_last_block_height():
    result = request('latestblock')
    try:
        return result['height']
    except:
        print result
        return 0

def getpages(address,to_date,last_height,confirmations):
    page = 0
    while True:
        result = request('address/' + address + '?format=json&offset='+str(page))
        try:
            txs = result['txs']
            if len(txs) == 0:
                break
            else:
                if parse_transactions(address,to_date,last_height,confirmations,txs):
                    break
                else:
                    page=page+50
        except:
            print result
            break
     
def parse_transactions(address,to_date,last_height,confirmations,txs):
    for x in range(0,len(txs)):
        tx = txs[x]
        cfm = last_height - tx['block_height'] + 1
        tx_time = tx['time']
        if tx_time<to_date:
            return True
        if (cfm>=confirmations):
            ins = tx['inputs']
            outs = tx['out']
            tx_id = tx['hash']
            insert_adresses(ins,outs,address,tx_id,tx_time)
    return False


def insert_adresses(ins,outs,address,tx_id,tx_time):
    sql = None
    id = 0
    is_address = False
    for x in range(0,len(outs)):
        out = outs[x]
        if out['addr'] == address:
            sql = helper.sqlhelper()
            value = "%.8f"%(out['value']/1.0e8,)
            if sql.testxtid(tx_id):
                id = sql.inserttx(tx_id,int(tx_time))
                sql.insert(int(tx_time), address, value, True, id)
                is_address = True
                break
    if is_address:
        for x in range(0,len(ins)):
            input = ins[x]
            sql.insert(int(tx_time), input['prev_out']['addr'], 0, False, id)
        
def gettransactions(days_limit,confirmations):
    to_date = datetime.datetime.utcnow() - datetime.timedelta(days = days_limit)
    sqlhelper = helper.sqlhelper
    to_date_unix = calendar.timegm(to_date.utctimetuple())
    last_height = get_last_block_height()
    if last_height>0:
        for x in range(0,len(config.addresses)):
            getpages(config.addresses[x],to_date_unix,last_height,confirmations)
    else:
        print 'Error'
        return False
    return True                 
        
#gettransactions(5,40)
                    