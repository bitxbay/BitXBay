import bitcoin
import time
import sys
import shelve
from bitcoin.exceptions import InsufficientFunds
import os
conn = bitcoin.connect_to_remote('user', 'user123', host='127.0.0.1', port=19001)


#if additional payment option is checked. Call it if cant collect with unspent without change > 0.0009.
# If option disabled and change more this money can be frozen for long time befor buyer/merchant don't accept or you don't cancel.
def additionalpaymentbuyer(fullamount):
    new = conn.getnewaddress()
    conn.sendtoaddress(new, fullamount)
    list = conn.listunspent(0)
    elem = -1
    for el in list:
        if el["address"] == new:
            elem = list.index(el)
            break
    if elem ==-1:
        time.sleep(5)
        list = conn.listunspent(0)
        elem = -1
        for el in list:
            if el["address"] == fraddress:
                elem = list.index(el)
                break
    if elem ==-1:
        time.sleep(10)
        list = conn.listunspent(0)
        elem = -1
        for el in list:
            if el["address"] == fraddress:
                elem = list.index(el)
                break
    if elem!=-1:
        unsp = list[elem]
        txid = unsp["txid"]
        vout = unsp["vout"]
        adlist = [{u"txid":txid, u"vout":vout}]
        strg = str('[{\\"txid\\":\\"'+str(txid)+'\\",\\"vout\\":'+str(vout)+'}]')
        print strg
        conn.lockunspent(False, strg)
        return adlist
    else:
        return []

#def additionalpaymentmerchant(fullamount):



#collect unspent txs for insurance payment and main payment, and get change
def unspent4sent(namount):
    namount2 = float(namount)*0.05
    if namount2 < 0.0005:
        namount2 = 0.0005
    namount = namount + namount2
    ad0 = []
    try:
        listunspent = conn.listunspent(0)
        listunspent = sorted(listunspent, key=lambda k: k['amount'])
        amount = 0
        fee = 0.0002
        adlist = []

        for el in listunspent:
            adlist.append({"txid":el["txid"], "vout":el["vout"]})
            amount = amount + el["amount"]
            if amount >= namount + fee:
                if amount - namount - fee > 0:
                    change = amount - fee - namount
                    #if change > 0.0009:
                    #    adlist = additionalpaymentbuyer(amount+fee+namount)
                    #    return adlist
                    return adlist, change
                else:
                    return adlist, 0
    except:
        t=1
    return ad0, 0

    #calculate unspent for insurence escrow (merchant side)
def unspent4sentmerch(namount, buyertxs, msig, msig2,addressbuyer, addressmerchant, buyerchange):
    namount2 = float(namount)*0.05
    if namount2 < 0.0005:
        namount2 = 0.0005
    ad0 = {}
    fraud = False
    #here check and break if buyer sent merchant's unspent.
    try:
        listunspent = conn.listunspent(0)
        listunspent = sorted(listunspent, key=lambda k: k['amount'])
    except:
        listunspent = []
        fraud = True
    allmine = False
    try:
        for el in listunspent:
            for buyert in buyertxs:
                if el["txid"] in buyert["txid"]:
                    fraud = True
        #specialy if you create deal with yourself check is all addresses is your
        allmine = True
        try:
            try:
                a2 = conn.validateaddress(str(msig))
                if a2.ismine == False:
                    allmine = False
            except:
                error=""
                allmine = False
            try:
                a2 = conn.validateaddress(str(msig2))
                if a2.ismine == False:
                    allmine = False
            except:
                error=""
                allmine = False

            try:
                a2 = conn.validateaddress(str(addressbuyer))
                if a2.ismine == False:
                    allmine = False
            except:
                error=""
                allmine = False

            print allmine

            try:
                a2 = conn.validateaddress(str(addressmerchant))
                if a2.ismine == False:
                    allmine = False
            except:
                error=""
                allmine = False
        except:
            allmine =False

        if allmine == True:
            fraud = False
    except:
        allmine = False
        fraud = True
        listunspent = []
    #here is if all checks is passed, need hard audit this checks
    if fraud == False:
        amount = 0
        if allmine:
            amount = buyerchange + namount2 + namount
        fee = 0.0001
        adlist = buyertxs

        #create tx with 2 payments form buyer and 1 from merchant and get back change
        for el in listunspent:
            print '10'
            if {"txid":el["txid"], "vout":el["vout"]} in adlist:
                if allmine != True:
                    adlist=[]
                    addr = []
                    break
            if amount >= (namount+namount2*2+fee):
                #this code only for deal with yourself
                change = amount - namount - namount2*2 - fee
                if change > 0:
                    m = conn.validateaddress(addressbuyer)
                    if m.ismine:
                        addr = {msig:namount2*2, msig2:namount, addressbuyer:change}
                        try:
                            a = conn.createrawtransactionlist(adlist, addr)
                        except:
                            a = ""
                        try:
                            b = conn.signrawtransaction(a)
                        except:
                            b = ""
                        try:
                            bsz = sys.getsizeof(b["hex"])/1000
                        except:
                            bsz = 16
                        if bsz > 1 and bsz < 15:
                            d = bsz
                            fee = fee + 0.0001 * d
                            change = amount - namount2*2 -namount - fee

                            if change > 0:
                                addr[addressbuyer] = change
                                a = conn.createrawtransactionlist(adlist, addr)
                                b = conn.signrawtransaction(a)
                                return b
                            elif change == 0:
                                del addr[addressbuyer]
                                a = conn.createrawtransactionlist(adlist, addr)
                                b = conn.signrawtransaction(a)
                                return b
                            else:
                                continue
                        else:
                            return b
                elif change == 0:
                    m = conn.validateaddress(addressbuyer)
                    if m.ismine:
                        addr = {msig:namount2*2, msig2:namount}
                        try:
                            a = conn.createrawtransactionlist(adlist, addr)
                        except:
                            a = ""
                        try:
                            b = conn.signrawtransaction(a)
                        except:
                            b = ""
                        try:
                            bsz = sys.getsizeof(b["hex"])/1000
                        except:
                            bsz = 16
                        if bsz > 1 and bsz < 15:
                            d = bsz
                            fee = fee + 0.0001 * d
                            continue
                        else:
                            return b
                else:
                    continue
            elif {"txid":el["txid"], "vout":el["vout"]} not in adlist:
                adlist.append({"txid":el["txid"], "vout":el["vout"]})
                amount = amount + el["amount"]
            if amount >= namount2 + fee and allmine == False:
                if buyerchange > 0:
                    if amount - namount2 -fee > 0:
                        change = amount - fee - namount2
                        addr = {msig:namount2*2, msig2:namount, addressbuyer:buyerchange, addressmerchant:change}
                    else:
                        addr = {msig:namount2*2, msig2:namount, addressbuyer:buyerchange}
                else:
                    if amount - namount2 -fee > 0:
                        change = amount - fee - namount2
                        addr = {msig:namount2*2, msig2:namount,addressmerchant:change}
                    else:
                        addr = {msig:namount2*2, msig2:namount}
                try:
                    a = conn.createrawtransactionlist(adlist, addr)
                except:
                    a = ""
                try:
                    b = conn.signrawtransaction(a)
                except:
                    b = ""
                try:
                    bsz = sys.getsizeof(b["hex"])/1000
                except:
                    bsz = 16
                #buyer pay 0.0002 commission and marchant 0.0001 if size of tx not more then 1000
                if bsz > 1 and bsz < 15:
                    d = bsz
                    fee = fee + 0.0001 * d
                    change = amount - namount2 - fee
                    if change > 0:
                        addr[addressmerchant] = change
                        a = conn.createrawtransactionlist(adlist, addr)
                        b = conn.signrawtransaction(a)
                        return b
                    elif change == 0:
                        del addr[addressmerchant]
                        a = conn.createrawtransactionlist(adlist, addr)
                        b = conn.signrawtransaction(a)
                        return b
                    else:
                        continue
                elif bsz == 0:
                    return b
                else:
                    error=""
                return b
    return ad0

def buyerverify(tx, amount, change, msig1, msig2, chaddress):
    fraud = True
    scam = True
    try:
        a2 = conn.validateaddress(msig1)
        for addre2 in a2.addresses:
            b2 = conn.validateaddress(addre2)
            if b2.ismine == True:
                scam = False
                continue
    except:
        scam = True

    scam2 = True
    try:
        a2 = conn.validateaddress(msig2)
        for addre2 in a2.addresses:
            b2 = conn.validateaddress(addre2)
            if b2.ismine == True:
                scam2 = False
                continue
    except:
        scam2 = True

    listlock = conn.listlockunspent()
    listun = conn.listunspent()
    listintx = conn.decoderawtransaction(tx)
    vout = listintx["vout"]
    vin = listintx["vin"]
    #if you create deal with yourself and all addresses "ismine"
    all = True
    try:
        for i in vout:
            a = i["scriptPubKey"]
            q = a["addresses"]
            if len(q)>1:
                fraud = True
                all = False
                continue
            elif len(q)>0:
                a2 = conn.validateaddress(str(q[0]))
                if a2.ismine == False:
                    all = False
                    continue
    except:
        all = False


    newlist = {}
    ins = amount*0.1
    if ins < 0.001:
        ins = 0.001
    for i in listlock:
        if i["txid"] in listintx:
            conn.lockunspent(True, i)

    for i in vin:
        for b in listun:
            if i["txid"] in b["txid"]:
                newlist[i["txid"]] = b["amount"]
    summ = 0
    for i in newlist:
        summ = summ + newlist[i]
    m = False
    m2 = False
    ch = False
    chsum = 0

    for i in vout:
        value = i["value"]
        a = i["scriptPubKey"]
        q = a["addresses"]
        if len(q)>1:
            fraud = True
        elif len(q) != 0:
            if q[0] == msig1 and value == ins:
                chsum = chsum + value*0.5
                m = True
            if q[0] == msig2 and value == amount:
                chsum = chsum + value
                m2 = True
            if q[0] == chaddress and value == change:
                chsum = chsum + value
                ch = True
        if m and m2 and ch:
            if chsum >= ins*0.5 + amount + change + 0.0001999 and chsum <= ins*0.5 + amount + change + 0.00020001:
                fraud = False
    if scam or scam2:
        fraud = True
    #if deal with yourself we can hope it is trusted deal
    if all == True:
        fraud = False
    return fraud
