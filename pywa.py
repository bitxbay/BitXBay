#!/usr/bin/env python
#-*- coding: utf-8 -*-
pywversion="2.1.7"
never_update=False

#
# jackjack's pywallet.py
# https://github.com/jackjack-jj/pywallet
# forked from Joric's pywallet.py
#




beta_version =  ('a' in pywversion.split('-')[0]) or ('b' in pywversion.split('-')[0])

missing_dep = []
from bsddb.db import *
import os, sys, time, re
pyw_filename = os.path.basename(__file__)
pyw_path = os.path.dirname(os.path.realpath(__file__))

try:
    import json
except:
    try:
        import simplejson as json
    except:
        print("Json or simplejson package is needed")

import logging
import struct
import StringIO
import traceback
import socket
import types
import string
import exceptions
import hashlib
import random
import urllib
import math

from datetime import datetime
from subprocess import *

import os
import os.path
import platform


max_version = 81000
addrtype = 0
json_db = {}
private_keys = []
private_hex_keys = []
passphrase = ""
global_merging_message = ["",""]

balance_site = 'http://jackjack.alwaysdata.net/balance/index.php?address'
aversions = {};
for i in range(256):
    aversions[i] = "version %d" % i;
aversions[0] = 'Bitcoin';
aversions[48] = 'Litecoin';
aversions[52] = 'Namecoin';
aversions[111] = 'Testnet';

wallet_dir = ""
wallet_name = ""

ko = 1e3
kio = 1024
Mo = 1e6
Mio = 1024 ** 2
Go = 1e9
Gio = 1024 ** 3
To = 1e12
Tio = 1024 ** 4

prekeys = ["308201130201010420".decode('hex'), "308201120201010420".decode('hex')]
postkeys = ["a081a530".decode('hex'), "81a530".decode('hex')]

def delete_from_wallet(db_env, walletfile, typedel, kd):
    db = open_wallet(db_env, walletfile, True)
    kds = BCDataStream()
    vds = BCDataStream()
    deleted_items = 0
    if not isinstance(kd, list):
        kd=[kd]
    if typedel=='tx' and kd!=['all']:
        for keydel in kd:
            db.delete('\x02\x74\x78'+keydel.decode('hex')[::-1])
            deleted_items+=1
    else:
        for i,keydel in enumerate(kd):
            for (key, value) in db.items():
                kds.clear(); kds.write(key)
                vds.clear(); vds.write(value)
                type = kds.read_string()
                if typedel == "tx" and type == "tx":
                    db.delete(key)
                    deleted_items+=1
                elif typedel == "key":
                    if type == "key" or type == "ckey":
                        if keydel == public_key_to_bc_address(kds.read_bytes(kds.read_compact_size())):
                            db.delete(key)
                            deleted_items+=1
                    elif type == "pool":
                        vds.read_int32()
                        vds.read_int64()
                        if keydel == public_key_to_bc_address(vds.read_bytes(vds.read_compact_size())):
                            db.delete(key)
                            deleted_items+=1
                    elif type == "name":
                        if keydel == kds.read_string():
                            db.delete(key)
                            deleted_items+=1

    db.close()
    return deleted_items

def open_wallet(db_env, walletfile, writable=False):
    db = DB(db_env)
    if writable:
        DB_TYPEOPEN = DB_CREATE
    else:
        DB_TYPEOPEN = DB_RDONLY
    flags = DB_THREAD | DB_TYPEOPEN
    try:
        r = db.open(walletfile, "main", DB_BTREE, flags)
    except DBError:
        r = True
    if r is not None:
        logging.error("Couldn't open wallet.dat/main. Try quitting Bitcoin and running this again.")
        sys.exit(1)
    return db



class BCDataStream(object):
    def __init__(self):
        self.input = None
        self.read_cursor = 0

    def clear(self):
        self.input = None
        self.read_cursor = 0

    def write(self, bytes):	# Initialize with string of bytes
        if self.input is None:
            self.input = bytes
        else:
            self.input += bytes
    def read_bytes(self, length):
        try:
            result = self.input[self.read_cursor:self.read_cursor+length]
            self.read_cursor += length
            return result
        except IndexError:
            raise SerializationError("attempt to read past end of buffer")
        return ''


    def read_string(self):
        # Strings are encoded depending on length:
        # 0 to 252 :	1-byte-length followed by bytes (if any)
        # 253 to 65,535 : byte'253' 2-byte-length followed by bytes
        # 65,536 to 4,294,967,295 : byte '254' 4-byte-length followed by bytes
        # ... and the Bitcoin client is coded to understand:
        # greater than 4,294,967,295 : byte '255' 8-byte-length followed by bytes of string
        # ... but I don't think it actually handles any strings that big.
        if self.input is None:
            raise SerializationError("call write(bytes) before trying to deserialize")
        try:
            length = self.read_compact_size()
        except IndexError:
            raise SerializationError("attempt to read past end of buffer")
        return self.read_bytes(length)

    def write_string(self, string):
        # Length-encoded as with read-string
        self.write_compact_size(len(string))
        self.write(string)
    def read_boolean(self): return self.read_bytes(1)[0] != chr(0)
    def read_int16(self): return self._read_num('<h')
    def read_uint16(self): return self._read_num('<H')
    def read_int32(self): return self._read_num('<i')
    def read_uint32(self): return self._read_num('<I')
    def read_int64(self): return self._read_num('<q')
    def read_uint64(self): return self._read_num('<Q')
    def write_boolean(self, val): return self.write(chr(bool_to_int(val)))
    def write_int16(self, val): return self._write_num('<h', val)
    def write_uint16(self, val): return self._write_num('<H', val)
    def write_int32(self, val): return self._write_num('<i', val)
    def write_uint32(self, val): return self._write_num('<I', val)
    def write_int64(self, val): return self._write_num('<q', val)
    def write_uint64(self, val): return self._write_num('<Q', val)
    def read_compact_size(self):
        size = ord(self.input[self.read_cursor])
        self.read_cursor += 1
        if size == 253:
            size = self._read_num('<H')
        elif size == 254:
            size = self._read_num('<I')
        elif size == 255:
            size = self._read_num('<Q')
        return size

    def write_compact_size(self, size):
        if size < 0:
            raise SerializationError("attempt to write size < 0")
        elif size < 253:
            self.write(chr(size))
        elif size < 2**16:
            self.write('\xfd')
            self._write_num('<H', size)
        elif size < 2**32:
            self.write('\xfe')
            self._write_num('<I', size)
        elif size < 2**64:
            self.write('\xff')
            self._write_num('<Q', size)
    def _read_num(self, format):
        (i,) = struct.unpack_from(format, self.input, self.read_cursor)
        self.read_cursor += struct.calcsize(format)
        return i

    def _write_num(self, format, num):
        s = struct.pack(format, num)
        self.write(s)

def hash_160(public_key):
    md = hashlib.new('ripemd160')
    md.update(hashlib.sha256(public_key).digest())
    return md.digest()

def public_key_to_bc_address(public_key, v=None):
    if v==None:
        v=addrtype
    h160 = hash_160(public_key)
    return hash_160_to_bc_address(h160, v)

def hash_160_to_bc_address(h160, v=None):
    if v==None:
        v=addrtype
    vh160 = chr(v) + h160
    h = Hash(vh160)
    addr = vh160 + h[0:4]
    return b58encode(addr)

def bc_address_to_hash_160(addr):
    bytes = b58decode(addr, 25)
    return bytes[1:21]

def Hash(data):
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()

__b58chars = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
__b58base = len(__b58chars)

def b58encode(v):
    """ encode v, which is a string of bytes, to base58.
    """

    long_value = 0L
    for (i, c) in enumerate(v[::-1]):
        long_value += (256**i) * ord(c)
    result = ''
    while long_value >= __b58base:
        div, mod = divmod(long_value, __b58base)
        result = __b58chars[mod] + result
        long_value = div
    result = __b58chars[long_value] + result