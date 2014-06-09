#!/usr/bin/env python
'''
Modified on Mar 30, 2014

@author: BitXBay
'''

from BCDataStream import *
from enumeration import Enumeration
from base58 import public_key_to_bc_address, hash_160_to_bc_address
import struct
import hashlib, binascii
import helper

def getTxId(_data):
    _temp = hashlib.sha256(hashlib.sha256(_data).digest()).hexdigest()
    _result = ''
    while _temp !='':
        _result = _result + _temp[-2:]
        _temp = _temp[:-2]
    return _result

def short_hex(bytes):
    t = bytes.encode('hex_codec')
    if len(t) < 11:
        return t
    return t[0:4]+"..."+t[-4:]

def parse_TxIn(vds):
    d = {}
    d['prevout_hash'] = vds.read_bytes(32)
    d['prevout_n'] = vds.read_uint32()
    d['scriptSig'] = vds.read_bytes(vds.read_compact_size())
    d['sequence'] = vds.read_uint32()
    return d

def deserialize_TxIn(d):
    if d['prevout_hash'] == "\x00"*32:
        result = {"address":'00000000'}
    else:
        pk = extract_public_key(d['scriptSig'])
        result = {"address":pk}
    return result

def parse_TxOut(vds):
    d = {}
    d['value'] = vds.read_int64()
    d['scriptPubKey'] = vds.read_bytes(vds.read_compact_size())
    return d

def deserialize_TxOut(d):
    pk = extract_public_key(d['scriptPubKey'])
    result = {"address":pk, "value":"%.8f"%(d['value']/1.0e8,)}
    return result

def parse_Transaction(vds):
    d = {}
    start_pos = vds.read_cursor
    d['version'] = vds.read_int32()
    n_vin = vds.read_compact_size()
    d['txIn'] = []
    for i in xrange(n_vin):
        d['txIn'].append(parse_TxIn(vds))
    n_vout = vds.read_compact_size()
    d['txOut'] = []
    for i in xrange(n_vout):
        d['txOut'].append(parse_TxOut(vds))
    d['lockTime'] = vds.read_uint32()
    d['__data__'] = vds.input[start_pos:vds.read_cursor]
    return d

def deserialize_Transaction(d, block_time, addresses):
    txIns = []
    txOuts = []

    ct = False
    for txIn in d['txIn']:
        txIns.append(deserialize_TxIn(txIn))
    for txOut in d['txOut']:
        res =   deserialize_TxOut(txOut)
        txOuts.append(res)
        if res["address"] in addresses:
            ct = True
    if ct:
        tx_id =  getTxId(d['__data__'])
        sql= helper.sqlhelper()
        if sql.testxtid(tx_id, int(block_time)):
            id = sql.inserttx(tx_id,int(block_time))
            for txI in txIns:
                sql.insert(int(block_time), txI["address"], 0, False, id)
            for txO in txOuts:
                sql.insert(int(block_time), txO["address"], txO["value"], True, id)

def deserialize_TransactionRaw(d):
    txIns = []
    txOuts = []
    for txIn in d['txIn']:
        txIns.append(deserialize_TxIn(txIn))
    for txOut in d['txOut']:
        res =   deserialize_TxOut(txOut)
        txOuts.append(res)
    return txIns

def parse_BlockHeader(vds):
    d = {}
    header_start = vds.read_cursor
    d['version'] = vds.read_int32()
    d['hashPrev'] = vds.read_bytes(32)
    d['hashMerkleRoot'] = vds.read_bytes(32)
    d['nTime'] = vds.read_uint32()
    d['nBits'] = vds.read_uint32()
    d['nNonce'] = vds.read_uint32()
    header_end = vds.read_cursor
    d['__header__'] = vds.input[header_start:header_end]
    return d

def parse_Block(vds):
    d = parse_BlockHeader(vds)
    d['transactions'] = []
    nTransactions = vds.read_compact_size()
    for i in xrange(nTransactions):
        d['transactions'].append(parse_Transaction(vds))
    return d
 
def deserialize_Block(d,  block_time, addresses):
    result = [] 
    for t in d['transactions']:
        deserialize_Transaction(t, block_time, addresses)

opcodes = Enumeration("Opcodes", [
    ("OP_0", 0), ("OP_PUSHDATA1",76), "OP_PUSHDATA2", "OP_PUSHDATA4", "OP_1NEGATE", "OP_RESERVED",
    "OP_1", "OP_2", "OP_3", "OP_4", "OP_5", "OP_6", "OP_7",
    "OP_8", "OP_9", "OP_10", "OP_11", "OP_12", "OP_13", "OP_14", "OP_15", "OP_16",
    "OP_NOP", "OP_VER", "OP_IF", "OP_NOTIF", "OP_VERIF", "OP_VERNOTIF", "OP_ELSE", "OP_ENDIF", "OP_VERIFY",
    "OP_RETURN", "OP_TOALTSTACK", "OP_FROMALTSTACK", "OP_2DROP", "OP_2DUP", "OP_3DUP", "OP_2OVER", "OP_2ROT", "OP_2SWAP",
    "OP_IFDUP", "OP_DEPTH", "OP_DROP", "OP_DUP", "OP_NIP", "OP_OVER", "OP_PICK", "OP_ROLL", "OP_ROT",
    "OP_SWAP", "OP_TUCK", "OP_CAT", "OP_SUBSTR", "OP_LEFT", "OP_RIGHT", "OP_SIZE", "OP_INVERT", "OP_AND",
    "OP_OR", "OP_XOR", "OP_EQUAL", "OP_EQUALVERIFY", "OP_RESERVED1", "OP_RESERVED2", "OP_1ADD", "OP_1SUB", "OP_2MUL",
    "OP_2DIV", "OP_NEGATE", "OP_ABS", "OP_NOT", "OP_0NOTEQUAL", "OP_ADD", "OP_SUB", "OP_MUL", "OP_DIV",
    "OP_MOD", "OP_LSHIFT", "OP_RSHIFT", "OP_BOOLAND", "OP_BOOLOR",
    "OP_NUMEQUAL", "OP_NUMEQUALVERIFY", "OP_NUMNOTEQUAL", "OP_LESSTHAN",
    "OP_GREATERTHAN", "OP_LESSTHANOREQUAL", "OP_GREATERTHANOREQUAL", "OP_MIN", "OP_MAX",
    "OP_WITHIN", "OP_RIPEMD160", "OP_SHA1", "OP_SHA256", "OP_HASH160",
    "OP_HASH256", "OP_CODESEPARATOR", "OP_CHECKSIG", "OP_CHECKSIGVERIFY", "OP_CHECKMULTISIG",
    "OP_CHECKMULTISIGVERIFY",
    "OP_NOP1", "OP_NOP2", "OP_NOP3", "OP_NOP4", "OP_NOP5", "OP_NOP6", "OP_NOP7", "OP_NOP8", "OP_NOP9", "OP_NOP10",
    ("OP_INVALIDOPCODE", 0xFF),
])

def script_GetOp(bytes):
    i = 0
    while i < len(bytes):
        vch = None
        opcode = ord(bytes[i])
        i += 1
        if opcode <= opcodes.OP_PUSHDATA4:
            nSize = opcode
            if opcode == opcodes.OP_PUSHDATA1:
                if i + 1 > len(bytes):
                    vch = "_INVALID_NULL"
                    i = len(bytes)
                else:
                    nSize = ord(bytes[i])
                    i += 1
            elif opcode == opcodes.OP_PUSHDATA2:
                if i + 2 > len(bytes):
                    vch = "_INVALID_NULL"
                    i = len(bytes)
                else:
                    (nSize,) = struct.unpack_from('<H', bytes, i)
                    i += 2
            elif opcode == opcodes.OP_PUSHDATA4:
                if i + 4 > len(bytes):
                    vch = "_INVALID_NULL"
                    i = len(bytes)
                else:
                    (nSize,) = struct.unpack_from('<I', bytes, i)
                    i += 4
            if i+nSize > len(bytes):
                vch = "_INVALID_"+bytes[i:]
                i = len(bytes)
            else:
                vch = bytes[i:i+nSize]
                i += nSize
        yield (opcode, vch)

def script_GetOpName(opcode):
    try:
        return (opcodes.whatis(opcode)).replace("OP_", "")
    except KeyError:
        return "InvalidOp_"+str(opcode)

def decode_script(bytes):
    result = ''
    for (opcode, vch) in script_GetOp(bytes):
        if len(result) > 0: result += " "
        if opcode <= opcodes.OP_PUSHDATA4:
            result += "%d:"%(opcode,)
            result += short_hex(vch)
        else:
            result += script_GetOpName(opcode)
    return result

def match_decoded(decoded, to_match):
    if len(decoded) != len(to_match):
        return False;
    for i in range(len(decoded)):
        if to_match[i] == opcodes.OP_PUSHDATA4 and decoded[i][0] <= opcodes.OP_PUSHDATA4:
            continue
        if to_match[i] != decoded[i][0]:
            return False
    return True

def extract_public_key(bytes, version='\x00'):
    try:
        decoded = [ x for x in script_GetOp(bytes) ]
    except struct.error:
        return "(None)"
    match = [ opcodes.OP_PUSHDATA4, opcodes.OP_PUSHDATA4 ]
    if match_decoded(decoded, match):
        return public_key_to_bc_address(decoded[1][1], version=version)
    match = [ opcodes.OP_PUSHDATA4, opcodes.OP_CHECKSIG ]
    if match_decoded(decoded, match):
        return public_key_to_bc_address(decoded[0][1], version=version)
    match = [ opcodes.OP_DUP, opcodes.OP_HASH160, opcodes.OP_PUSHDATA4, opcodes.OP_EQUALVERIFY, opcodes.OP_CHECKSIG ]
    if match_decoded(decoded, match):
        return hash_160_to_bc_address(decoded[2][1], version=version)
    multisigs = [
      [ opcodes.OP_1, opcodes.OP_PUSHDATA4, opcodes.OP_1, opcodes.OP_CHECKMULTISIG ],
      [ opcodes.OP_2, opcodes.OP_PUSHDATA4, opcodes.OP_PUSHDATA4, opcodes.OP_2, opcodes.OP_CHECKMULTISIG ],
      [ opcodes.OP_3, opcodes.OP_PUSHDATA4, opcodes.OP_PUSHDATA4, opcodes.OP_3, opcodes.OP_CHECKMULTISIG ]
    ]
    for match in multisigs:
        if match_decoded(decoded, match):
            return "["+','.join([public_key_to_bc_address(decoded[i][1]) for i in range(1,len(decoded)-1)])+"]"
    match = [ opcodes.OP_HASH160, 0x14, opcodes.OP_EQUAL ]
    if match_decoded(decoded, match):
        return hash_160_to_bc_address(decoded[1][1], version="\x05")
    return "(None)"
