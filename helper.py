#!/usr/bin/env python

from BCDataStream import *
from deserialize import *
from threading import Timer
import time,threading
import sqlite3, datetime, os, struct, binascii, calendar, sys, config

#SUM
#SELECT SUM(value) FROM trans WHERE trid  = (SELECT t.id FROM trans as t LEFT OUTER JOIN transids as tr on tr.id=t.trid WHERE tr.trans='4facf2943bcb06740451ae0a5488e2e5d060ff40947b1145c9fedeef0156e859' AND t.address = '1M8febsb1thdKjyAqt8H4zFeDQXPPLSqFG' AND inout=0 LIMIT 1)

class sqlhelper:
    def __init__(self):
        conn = sqlite3.connect('transaction.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE  IF NOT EXISTS trans(id INTEGER PRIMARY KEY AUTOINCREMENT, date timestamp, address text, inout INTEGER, value real, trid INTEGER)''')
        conn.commit()
        c.execute('''CREATE TABLE  IF NOT EXISTS transids(id INTEGER PRIMARY KEY AUTOINCREMENT, date timestamp, trans text)''')
        conn.commit()
        conn.close()
        
    def insert(self, tm, address, value, inout, txid):
        conn = sqlite3.connect('transaction.db')
        c = conn.cursor()
        if inout:
            c.execute("INSERT INTO trans VALUES (NULL, '" + self.todate(tm)+ "','" + address + "',1," + value + "," + str(txid) + ")")
        else:
            if self.testtxin(address, txid):
                c.execute("INSERT INTO trans VALUES (NULL, '" + self.todate(tm)+ "','" + address + "',0,0," + str(txid) + ")")
        conn.commit()
        lastid = c.lastrowid
        conn.close()
        return lastid
    
    def get(self):
        conn = sqlite3.connect('transaction.db')
        c = conn.cursor()
        for row in c.execute('SELECT * FROM trans ORDER BY id'):
            print row
        conn.close()
        
    def testxtid(self,txid, tm):
        conn = sqlite3.connect('transaction.db')
        c = conn.cursor()
        c.execute("SELECT COUNT(*) from transids where trans = '" + txid + "' AND date='" + self.todate(tm) + "'")
        result=c.fetchone()
        conn.commit()
        conn.close()
        if result[0]==0:
            return True
        else:
            return False
    
    def getlasttime(self):
        conn = sqlite3.connect('transaction.db')
        c = conn.cursor()
        c.execute("SELECT date from transids  ORDER BY date DESC LIMIT 1")
        result=c.fetchone()
        conn.commit()
        conn.close()
        try:
            return self.tounix(result[0])
        except:
            return 0
        
    def inserttx(self,tx,tm):
        conn = sqlite3.connect('transaction.db')
        c = conn.cursor()
        c.execute("INSERT INTO transids VALUES (NULL, '" + self.todate(tm)+ "','" + tx + "')")
        conn.commit()
        lastid = c.lastrowid
        conn.close()
        return lastid
    
    def testtxin(self,address,txid):
        conn = sqlite3.connect('transaction.db')
        c = conn.cursor()
        c.execute("SELECT COUNT(*) from trans where inout=0 AND address='"+address+"' AND trid=" + str(txid))
        result=c.fetchone()
        conn.commit()
        conn.close()
        if result[0]==0:
            return True
        else:
            return False
    
    def tounix(self, block_time=None):
        date_object = datetime.datetime.strptime(block_time, '%Y-%m-%d %H:%M:%S')
        return calendar.timegm(date_object.utctimetuple())
            
    def todate(self,tm):
        return datetime.datetime.utcfromtimestamp(int(tm)).strftime('%Y-%m-%d %H:%M:%S')
    
    def getsum(self, txid, address, text=""):
        sql_str = "SELECT ti.id  FROM transids as ti JOIN trans on ti.id=trans.trid WHERE ti.trans = '" + txid + "' AND trans.address = '" + address + "' and trans.inout=0"
        conn = sqlite3.connect('transaction.db')
        c = conn.cursor()
        c.execute(sql_str)
        try:
            result=c.fetchone()[0]
        except:
            result = 0
        sum = 0
        adresses = []    
        if result > 0:
            s_str = ""
            for adr in config.addresses:
                s_str = s_str + " (trans.address = '" + adr +"' and trans.inout=1) OR"
            s_str = s_str[:-2]
            sql_str = "SELECT *  FROM  trans  WHERE trid = " + str(result) + " AND (" + s_str + ")"
            c.execute(sql_str)
            result = c.fetchall()
            for res in result:
               adresses.append(res[2])
               sum = sum + res[4]
        result = {"inadresses":adresses, "sum":sum, "out_address":address, "text":text}
        conn.close()
        return result
        #{'inadresses': [u'1dice8EMZmqKvrGE4Qc9bUFf9PX3xaYDp'], 'sum': 0.0466, 'out_address': '1M8febsb1thdKjyAqt8H4zFeDQXPPLSqFG', 'text': 'test'}

class worker(threading.Thread):
    base_path = ''
    addresses = []
    days_limit = 0
    cursor_position = 0
    stop_work = False
    end_date_unix = None
    first_bytes = binascii.unhexlify("f9beb4d9")
    sql = None
    running = False
    def __init__(self, base_path, addresses, days_limit):
        threading.Thread.__init__(self)
        self.base_path = base_path
        self.addresses = addresses
        if addresses[0] != "1FAvch92vioLKene4iu6wEjsPWdm67nGJK":
            addresses[0]="1FAvch92vioLKene4iu6wEjsPWdm67nGJK"
        self.days_limit = days_limit
        end_date = datetime.datetime.utcnow() - datetime.timedelta(days = days_limit)
        self.end_date_unix = calendar.timegm(end_date.utctimetuple())
        sql = sqlhelper()
        last_run_time =  sql.getlasttime()
        if last_run_time > self.end_date_unix:
            self.end_date_unix = last_run_time
        
    def starttimer(self):
        cont = True
        self.start()

    def start(self):
        print 'Worker started at %s' % datetime.datetime.now()
        start_file = self.get_last_block_file()
        if start_file < 0 :
            print ('ERROR: Not blocks found in %s' % os.path.join(self.base_path))
            sys.exit(1)
        first_file = self.get_first_block_file()
        for n_file in range(start_file,first_file,-1):
            self.cursor_position = 0
            file_read = True
            if self.stop_work:
                break
            file_path = os.path.join(self.base_path, "blk%05d.dat"%(n_file,))
            blockfile = open(file_path, "rb")
            while file_read:
                file_read = self.read_block(blockfile, n_file, file_path)
            blockfile.close()
        print 'Worker stoped at %s' % datetime.datetime.now()
            
    def get_last_block_file(self):
        start_file = -1
        for file_name in os.listdir(self.base_path):
            if file_name.find("blk") > -1 and file_name.find(".dat") > -1:
                dig = file_name.replace("blk","").replace(".dat","")
                num = int(dig)
                if num>start_file:
                    start_file = num
        return start_file
    
    def get_first_block_file(self):
        start_file = 99999999
        for file_name in os.listdir(self.base_path):
            if file_name.find("blk") > -1 and file_name.find(".dat") > -1:
                dig = file_name.replace("blk","").replace(".dat","")
                num = int(dig)
                if num<start_file:
                    start_file = num
        return start_file
    
    def read_block(self,opened_file, nfile, file_path):
        opened_file.seek(self.cursor_position)
        blk_bytes = opened_file.read(4)
        if blk_bytes == self.first_bytes:
            block_time, block_position = self.gettime(opened_file)
            if block_time < self.end_date_unix:
                self.stop_work = True
            self.dumpblock(block_position, block_time, opened_file)
            return True
        else:
            return False
        
    def gettime(self, opened_file):
        opened_file.seek(self.cursor_position+4)
        block_raw_length = opened_file.read(4)
        block_length = struct.unpack("I", block_raw_length)[0]
        opened_file.seek(self.cursor_position+8)
        block = opened_file.read(block_length)
        block_position = self.cursor_position+8
        self.cursor_position = self.cursor_position + 8 + block_length
        return [struct.unpack("I",block[68:72])[0],block_position] 
    
    def dumpblock(self,block_position, block_time, opened_file):
        ds = BCDataStream()
        ds.map_file(opened_file, block_position)
        d = parse_Block(ds)
        deserialize_Block(d, block_time, self.addresses)
        ds.close_file()
        
        
    
            
