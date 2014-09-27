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

try:
	from bsddb.db import *
except:
	try:
		from bsddb3.db import *
	except:
		missing_dep.append('bsddb')

import os, sys, time, re
pyw_filename = os.path.basename(__file__)
pyw_path = os.path.dirname(os.path.realpath(__file__))

try:
	for i in os.listdir('C:/Python27/Lib/site-packages'):
		if 'Twisted' in i:
			sys.path.append('C:/Python27/Lib/site-packages'+i)
except:
	''

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

from twisted.internet import reactor
from twisted.web import server, resource
from twisted.web.static import File
from twisted.python import log


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

def iais(a):
	if a>= 2:
		return 's'
	else:
		return ''

def systype():
	if platform.system() == "Darwin":
		return 'Mac'
	elif platform.system() == "Windows":
		return 'Win'
	return 'Linux'

def determine_db_dir():
	if wallet_dir in "":
		if platform.system() == "Darwin":
			return os.path.expanduser("~/Library/Application Support/Bitcoin/")
		elif platform.system() == "Windows":
			return os.path.join(os.environ['APPDATA'], "Bitcoin")
		return os.path.expanduser("~/.bitcoin")
	else:
		return wallet_dir

def determine_db_name():
	if wallet_name in "":
		return "wallet.dat"
	else:
		return wallet_name

########################
# begin of aes.py code #
########################

# from the SlowAES project, http://code.google.com/p/slowaes (aes.py)

def append_PKCS7_padding(s):
	"""return s padded to a multiple of 16-bytes by PKCS7 padding"""
	numpads = 16 - (len(s)%16)
	return s + numpads*chr(numpads)

def strip_PKCS7_padding(s):
	"""return s stripped of PKCS7 padding"""
	if len(s)%16 or not s:
		raise ValueError("String of len %d can't be PCKS7-padded" % len(s))
	numpads = ord(s[-1])
	if numpads > 16:
		raise ValueError("String ending with %r can't be PCKS7-padded" % s[-1])
	return s[:-numpads]

class AES(object):
	# valid key sizes
	keySize = dict(SIZE_128=16, SIZE_192=24, SIZE_256=32)

	# Rijndael S-box
	sbox =  [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67,
			0x2b, 0xfe, 0xd7, 0xab, 0x76, 0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59,
			0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0, 0xb7,
			0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1,
			0x71, 0xd8, 0x31, 0x15, 0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05,
			0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75, 0x09, 0x83,
			0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29,
			0xe3, 0x2f, 0x84, 0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b,
			0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf, 0xd0, 0xef, 0xaa,
			0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c,
			0x9f, 0xa8, 0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc,
			0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2, 0xcd, 0x0c, 0x13, 0xec,
			0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19,
			0x73, 0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee,
			0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb, 0xe0, 0x32, 0x3a, 0x0a, 0x49,
			0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
			0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4,
			0xea, 0x65, 0x7a, 0xae, 0x08, 0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6,
			0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a, 0x70,
			0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9,
			0x86, 0xc1, 0x1d, 0x9e, 0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e,
			0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf, 0x8c, 0xa1,
			0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0,
			0x54, 0xbb, 0x16]

	# Rijndael Inverted S-box
	rsbox = [0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3,
			0x9e, 0x81, 0xf3, 0xd7, 0xfb , 0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f,
			0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb , 0x54,
			0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b,
			0x42, 0xfa, 0xc3, 0x4e , 0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24,
			0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25 , 0x72, 0xf8,
			0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d,
			0x65, 0xb6, 0x92 , 0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda,
			0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84 , 0x90, 0xd8, 0xab,
			0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3,
			0x45, 0x06 , 0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1,
			0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b , 0x3a, 0x91, 0x11, 0x41,
			0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6,
			0x73 , 0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9,
			0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e , 0x47, 0xf1, 0x1a, 0x71, 0x1d,
			0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b ,
			0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0,
			0xfe, 0x78, 0xcd, 0x5a, 0xf4 , 0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07,
			0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f , 0x60,
			0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f,
			0x93, 0xc9, 0x9c, 0xef , 0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5,
			0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61 , 0x17, 0x2b,
			0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55,
			0x21, 0x0c, 0x7d]

	def getSBoxValue(self,num):
		"""Retrieves a given S-Box Value"""
		return self.sbox[num]

	def getSBoxInvert(self,num):
		"""Retrieves a given Inverted S-Box Value"""
		return self.rsbox[num]

	def rotate(self, word):
		""" Rijndael's key schedule rotate operation.

		Rotate a word eight bits to the left: eg, rotate(1d2c3a4f) == 2c3a4f1d
		Word is an char list of size 4 (32 bits overall).
		"""
		return word[1:] + word[:1]

	# Rijndael Rcon
	Rcon = [0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36,
			0x6c, 0xd8, 0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97,
			0x35, 0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39, 0x72,
			0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f, 0x25, 0x4a, 0x94, 0x33, 0x66,
			0xcc, 0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04,
			0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d,
			0x9a, 0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3,
			0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61,
			0xc2, 0x9f, 0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a,
			0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
			0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc,
			0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef, 0xc5,
			0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f, 0x25, 0x4a,
			0x94, 0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d,
			0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c,
			0xd8, 0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35,
			0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39, 0x72, 0xe4,
			0xd3, 0xbd, 0x61, 0xc2, 0x9f, 0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc,
			0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04, 0x08,
			0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a,
			0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3, 0x7d,
			0xfa, 0xef, 0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2,
			0x9f, 0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a, 0x74,
			0xe8, 0xcb ]

	def getRconValue(self, num):
		"""Retrieves a given Rcon Value"""
		return self.Rcon[num]

	def core(self, word, iteration):
		"""Key schedule core."""
		# rotate the 32-bit word 8 bits to the left
		word = self.rotate(word)
		# apply S-Box substitution on all 4 parts of the 32-bit word
		for i in range(4):
			word[i] = self.getSBoxValue(word[i])
		# XOR the output of the rcon operation with i to the first part
		# (leftmost) only
		word[0] = word[0] ^ self.getRconValue(iteration)
		return word

	def expandKey(self, key, size, expandedKeySize):
		"""Rijndael's key expansion.

		Expands an 128,192,256 key into an 176,208,240 bytes key

		expandedKey is a char list of large enough size,
		key is the non-expanded key.
		"""
		# current expanded keySize, in bytes
		currentSize = 0
		rconIteration = 1
		expandedKey = [0] * expandedKeySize

		# set the 16, 24, 32 bytes of the expanded key to the input key
		for j in range(size):
			expandedKey[j] = key[j]
		currentSize += size

		while currentSize < expandedKeySize:
			# assign the previous 4 bytes to the temporary value t
			t = expandedKey[currentSize-4:currentSize]

			# every 16,24,32 bytes we apply the core schedule to t
			# and increment rconIteration afterwards
			if currentSize % size == 0:
				t = self.core(t, rconIteration)
				rconIteration += 1
			# For 256-bit keys, we add an extra sbox to the calculation
			if size == self.keySize["SIZE_256"] and ((currentSize % size) == 16):
				for l in range(4): t[l] = self.getSBoxValue(t[l])

			# We XOR t with the four-byte block 16,24,32 bytes before the new
			# expanded key.  This becomes the next four bytes in the expanded
			# key.
			for m in range(4):
				expandedKey[currentSize] = expandedKey[currentSize - size] ^ \
						t[m]
				currentSize += 1

		return expandedKey

	def addRoundKey(self, state, roundKey):
		"""Adds (XORs) the round key to the state."""
		for i in range(16):
			state[i] ^= roundKey[i]
		return state

	def createRoundKey(self, expandedKey, roundKeyPointer):
		"""Create a round key.
		Creates a round key from the given expanded key and the
		position within the expanded key.
		"""
		roundKey = [0] * 16
		for i in range(4):
			for j in range(4):
				roundKey[j*4+i] = expandedKey[roundKeyPointer + i*4 + j]
		return roundKey

	def galois_multiplication(self, a, b):
		"""Galois multiplication of 8 bit characters a and b."""
		p = 0
		for counter in range(8):
			if b & 1: p ^= a
			hi_bit_set = a & 0x80
			a <<= 1
			# keep a 8 bit
			a &= 0xFF
			if hi_bit_set:
				a ^= 0x1b
			b >>= 1
		return p

	#
	# substitute all the values from the state with the value in the SBox
	# using the state value as index for the SBox
	#
	def subBytes(self, state, isInv):
		if isInv: getter = self.getSBoxInvert
		else: getter = self.getSBoxValue
		for i in range(16): state[i] = getter(state[i])
		return state

	# iterate over the 4 rows and call shiftRow() with that row
	def shiftRows(self, state, isInv):
		for i in range(4):
			state = self.shiftRow(state, i*4, i, isInv)
		return state

	# each iteration shifts the row to the left by 1
	def shiftRow(self, state, statePointer, nbr, isInv):
		for i in range(nbr):
			if isInv:
				state[statePointer:statePointer+4] = \
						state[statePointer+3:statePointer+4] + \
						state[statePointer:statePointer+3]
			else:
				state[statePointer:statePointer+4] = \
						state[statePointer+1:statePointer+4] + \
						state[statePointer:statePointer+1]
		return state

	# galois multiplication of the 4x4 matrix
	def mixColumns(self, state, isInv):
		# iterate over the 4 columns
		for i in range(4):
			# construct one column by slicing over the 4 rows
			column = state[i:i+16:4]
			# apply the mixColumn on one column
			column = self.mixColumn(column, isInv)
			# put the values back into the state
			state[i:i+16:4] = column

		return state

	# galois multiplication of 1 column of the 4x4 matrix
	def mixColumn(self, column, isInv):
		if isInv: mult = [14, 9, 13, 11]
		else: mult = [2, 1, 1, 3]
		cpy = list(column)
		g = self.galois_multiplication

		column[0] = g(cpy[0], mult[0]) ^ g(cpy[3], mult[1]) ^ \
					g(cpy[2], mult[2]) ^ g(cpy[1], mult[3])
		column[1] = g(cpy[1], mult[0]) ^ g(cpy[0], mult[1]) ^ \
					g(cpy[3], mult[2]) ^ g(cpy[2], mult[3])
		column[2] = g(cpy[2], mult[0]) ^ g(cpy[1], mult[1]) ^ \
					g(cpy[0], mult[2]) ^ g(cpy[3], mult[3])
		column[3] = g(cpy[3], mult[0]) ^ g(cpy[2], mult[1]) ^ \
					g(cpy[1], mult[2]) ^ g(cpy[0], mult[3])
		return column

	# applies the 4 operations of the forward round in sequence
	def aes_round(self, state, roundKey):
		state = self.subBytes(state, False)
		state = self.shiftRows(state, False)
		state = self.mixColumns(state, False)
		state = self.addRoundKey(state, roundKey)
		return state

	# applies the 4 operations of the inverse round in sequence
	def aes_invRound(self, state, roundKey):
		state = self.shiftRows(state, True)
		state = self.subBytes(state, True)
		state = self.addRoundKey(state, roundKey)
		state = self.mixColumns(state, True)
		return state

	# Perform the initial operations, the standard round, and the final
	# operations of the forward aes, creating a round key for each round
	def aes_main(self, state, expandedKey, nbrRounds):
		state = self.addRoundKey(state, self.createRoundKey(expandedKey, 0))
		i = 1
		while i < nbrRounds:
			state = self.aes_round(state,
								   self.createRoundKey(expandedKey, 16*i))
			i += 1
		state = self.subBytes(state, False)
		state = self.shiftRows(state, False)
		state = self.addRoundKey(state,
								 self.createRoundKey(expandedKey, 16*nbrRounds))
		return state

	# Perform the initial operations, the standard round, and the final
	# operations of the inverse aes, creating a round key for each round
	def aes_invMain(self, state, expandedKey, nbrRounds):
		state = self.addRoundKey(state,
								 self.createRoundKey(expandedKey, 16*nbrRounds))
		i = nbrRounds - 1
		while i > 0:
			state = self.aes_invRound(state,
									  self.createRoundKey(expandedKey, 16*i))
			i -= 1
		state = self.shiftRows(state, True)
		state = self.subBytes(state, True)
		state = self.addRoundKey(state, self.createRoundKey(expandedKey, 0))
		return state

	# encrypts a 128 bit input block against the given key of size specified
	def encrypt(self, iput, key, size):
		output = [0] * 16
		# the number of rounds
		nbrRounds = 0
		# the 128 bit block to encode
		block = [0] * 16
		# set the number of rounds
		if size == self.keySize["SIZE_128"]: nbrRounds = 10
		elif size == self.keySize["SIZE_192"]: nbrRounds = 12
		elif size == self.keySize["SIZE_256"]: nbrRounds = 14
		else: return None

		# the expanded keySize
		expandedKeySize = 16*(nbrRounds+1)

		# Set the block values, for the block:
		# a0,0 a0,1 a0,2 a0,3
		# a1,0 a1,1 a1,2 a1,3
		# a2,0 a2,1 a2,2 a2,3
		# a3,0 a3,1 a3,2 a3,3
		# the mapping order is a0,0 a1,0 a2,0 a3,0 a0,1 a1,1 ... a2,3 a3,3
		#
		# iterate over the columns
		for i in range(4):
			# iterate over the rows
			for j in range(4):
				block[(i+(j*4))] = iput[(i*4)+j]

		# expand the key into an 176, 208, 240 bytes key
		# the expanded key
		expandedKey = self.expandKey(key, size, expandedKeySize)

		# encrypt the block using the expandedKey
		block = self.aes_main(block, expandedKey, nbrRounds)

		# unmap the block again into the output
		for k in range(4):
			# iterate over the rows
			for l in range(4):
				output[(k*4)+l] = block[(k+(l*4))]
		return output

	# decrypts a 128 bit input block against the given key of size specified
	def decrypt(self, iput, key, size):
		output = [0] * 16
		# the number of rounds
		nbrRounds = 0
		# the 128 bit block to decode
		block = [0] * 16
		# set the number of rounds
		if size == self.keySize["SIZE_128"]: nbrRounds = 10
		elif size == self.keySize["SIZE_192"]: nbrRounds = 12
		elif size == self.keySize["SIZE_256"]: nbrRounds = 14
		else: return None

		# the expanded keySize
		expandedKeySize = 16*(nbrRounds+1)

		# Set the block values, for the block:
		# a0,0 a0,1 a0,2 a0,3
		# a1,0 a1,1 a1,2 a1,3
		# a2,0 a2,1 a2,2 a2,3
		# a3,0 a3,1 a3,2 a3,3
		# the mapping order is a0,0 a1,0 a2,0 a3,0 a0,1 a1,1 ... a2,3 a3,3

		# iterate over the columns
		for i in range(4):
			# iterate over the rows
			for j in range(4):
				block[(i+(j*4))] = iput[(i*4)+j]
		# expand the key into an 176, 208, 240 bytes key
		expandedKey = self.expandKey(key, size, expandedKeySize)
		# decrypt the block using the expandedKey
		block = self.aes_invMain(block, expandedKey, nbrRounds)
		# unmap the block again into the output
		for k in range(4):
			# iterate over the rows
			for l in range(4):
				output[(k*4)+l] = block[(k+(l*4))]
		return output

class AESModeOfOperation(object):

	aes = AES()

	# structure of supported modes of operation
	modeOfOperation = dict(OFB=0, CFB=1, CBC=2)

	# converts a 16 character string into a number array
	def convertString(self, string, start, end, mode):
		if end - start > 16: end = start + 16
		if mode == self.modeOfOperation["CBC"]: ar = [0] * 16
		else: ar = []

		i = start
		j = 0
		while len(ar) < end - start:
			ar.append(0)
		while i < end:
			ar[j] = ord(string[i])
			j += 1
			i += 1
		return ar

	# Mode of Operation Encryption
	# stringIn - Input String
	# mode - mode of type modeOfOperation
	# hexKey - a hex key of the bit length size
	# size - the bit length of the key
	# hexIV - the 128 bit hex Initilization Vector
	def encrypt(self, stringIn, mode, key, size, IV):
		if len(key) % size:
			return None
		if len(IV) % 16:
			return None
		# the AES input/output
		plaintext = []
		iput = [0] * 16
		output = []
		ciphertext = [0] * 16
		# the output cipher string
		cipherOut = []
		# char firstRound
		firstRound = True
		if stringIn != None:
			for j in range(int(math.ceil(float(len(stringIn))/16))):
				start = j*16
				end = j*16+16
				if  end > len(stringIn):
					end = len(stringIn)
				plaintext = self.convertString(stringIn, start, end, mode)
				# print 'PT@%s:%s' % (j, plaintext)
				if mode == self.modeOfOperation["CFB"]:
					if firstRound:
						output = self.aes.encrypt(IV, key, size)
						firstRound = False
					else:
						output = self.aes.encrypt(iput, key, size)
					for i in range(16):
						if len(plaintext)-1 < i:
							ciphertext[i] = 0 ^ output[i]
						elif len(output)-1 < i:
							ciphertext[i] = plaintext[i] ^ 0
						elif len(plaintext)-1 < i and len(output) < i:
							ciphertext[i] = 0 ^ 0
						else:
							ciphertext[i] = plaintext[i] ^ output[i]
					for k in range(end-start):
						cipherOut.append(ciphertext[k])
					iput = ciphertext
				elif mode == self.modeOfOperation["OFB"]:
					if firstRound:
						output = self.aes.encrypt(IV, key, size)
						firstRound = False
					else:
						output = self.aes.encrypt(iput, key, size)
					for i in range(16):
						if len(plaintext)-1 < i:
							ciphertext[i] = 0 ^ output[i]
						elif len(output)-1 < i:
							ciphertext[i] = plaintext[i] ^ 0
						elif len(plaintext)-1 < i and len(output) < i:
							ciphertext[i] = 0 ^ 0
						else:
							ciphertext[i] = plaintext[i] ^ output[i]
					for k in range(end-start):
						cipherOut.append(ciphertext[k])
					iput = output
				elif mode == self.modeOfOperation["CBC"]:
					for i in range(16):
						if firstRound:
							iput[i] =  plaintext[i] ^ IV[i]
						else:
							iput[i] =  plaintext[i] ^ ciphertext[i]
					# print 'IP@%s:%s' % (j, iput)
					firstRound = False
					ciphertext = self.aes.encrypt(iput, key, size)
					# always 16 bytes because of the padding for CBC
					for k in range(16):
						cipherOut.append(ciphertext[k])
		return mode, len(stringIn), cipherOut

	# Mode of Operation Decryption
	# cipherIn - Encrypted String
	# originalsize - The unencrypted string length - required for CBC
	# mode - mode of type modeOfOperation
	# key - a number array of the bit length size
	# size - the bit length of the key
	# IV - the 128 bit number array Initilization Vector
	def decrypt(self, cipherIn, originalsize, mode, key, size, IV):
		# cipherIn = unescCtrlChars(cipherIn)
		if len(key) % size:
			return None
		if len(IV) % 16:
			return None
		# the AES input/output
		ciphertext = []
		iput = []
		output = []
		plaintext = [0] * 16
		# the output plain text string
		stringOut = ''
		# char firstRound
		firstRound = True
		if cipherIn != None:
			for j in range(int(math.ceil(float(len(cipherIn))/16))):
				start = j*16
				end = j*16+16
				if j*16+16 > len(cipherIn):
					end = len(cipherIn)
				ciphertext = cipherIn[start:end]
				if mode == self.modeOfOperation["CFB"]:
					if firstRound:
						output = self.aes.encrypt(IV, key, size)
						firstRound = False
					else:
						output = self.aes.encrypt(iput, key, size)
					for i in range(16):
						if len(output)-1 < i:
							plaintext[i] = 0 ^ ciphertext[i]
						elif len(ciphertext)-1 < i:
							plaintext[i] = output[i] ^ 0
						elif len(output)-1 < i and len(ciphertext) < i:
							plaintext[i] = 0 ^ 0
						else:
							plaintext[i] = output[i] ^ ciphertext[i]
					for k in range(end-start):
						stringOut += chr(plaintext[k])
					iput = ciphertext
				elif mode == self.modeOfOperation["OFB"]:
					if firstRound:
						output = self.aes.encrypt(IV, key, size)
						firstRound = False
					else:
						output = self.aes.encrypt(iput, key, size)
					for i in range(16):
						if len(output)-1 < i:
							plaintext[i] = 0 ^ ciphertext[i]
						elif len(ciphertext)-1 < i:
							plaintext[i] = output[i] ^ 0
						elif len(output)-1 < i and len(ciphertext) < i:
							plaintext[i] = 0 ^ 0
						else:
							plaintext[i] = output[i] ^ ciphertext[i]
					for k in range(end-start):
						stringOut += chr(plaintext[k])
					iput = output
				elif mode == self.modeOfOperation["CBC"]:
					output = self.aes.decrypt(ciphertext, key, size)
					for i in range(16):
						if firstRound:
							plaintext[i] = IV[i] ^ output[i]
						else:
							plaintext[i] = iput[i] ^ output[i]
					firstRound = False
					if originalsize is not None and originalsize < end:
						for k in range(originalsize-start):
							stringOut += chr(plaintext[k])
					else:
						for k in range(end-start):
							stringOut += chr(plaintext[k])
					iput = ciphertext
		return stringOut

######################
# end of aes.py code #
######################

###################################
# pywallet crypter implementation #
###################################

crypter = None

try:
	from Crypto.Cipher import AES
	crypter = 'pycrypto'
except:
	pass

class Crypter_pycrypto( object ):
	def SetKeyFromPassphrase(self, vKeyData, vSalt, nDerivIterations, nDerivationMethod):
		if nDerivationMethod != 0:
			return 0
		data = vKeyData + vSalt
		for i in xrange(nDerivIterations):
			data = hashlib.sha512(data).digest()
		self.SetKey(data[0:32])
		self.SetIV(data[32:32+16])
		return len(data)

	def SetKey(self, key):
		self.chKey = key

	def SetIV(self, iv):
		self.chIV = iv[0:16]

	def Encrypt(self, data):
		return AES.new(self.chKey,AES.MODE_CBC,self.chIV).encrypt(data)[0:32]

	def Decrypt(self, data):
		return AES.new(self.chKey,AES.MODE_CBC,self.chIV).decrypt(data)[0:32]

try:
	if not crypter:
		import ctypes
		import ctypes.util
		ssl = ctypes.cdll.LoadLibrary (ctypes.util.find_library ('ssl') or 'libeay32')
		crypter = 'ssl'
except:
	pass

class Crypter_ssl(object):
	def __init__(self):
		self.chKey = ctypes.create_string_buffer (32)
		self.chIV = ctypes.create_string_buffer (16)

	def SetKeyFromPassphrase(self, vKeyData, vSalt, nDerivIterations, nDerivationMethod):
		if nDerivationMethod != 0:
			return 0
		strKeyData = ctypes.create_string_buffer (vKeyData)
		chSalt = ctypes.create_string_buffer (vSalt)
		return ssl.EVP_BytesToKey(ssl.EVP_aes_256_cbc(), ssl.EVP_sha512(), chSalt, strKeyData,
			len(vKeyData), nDerivIterations, ctypes.byref(self.chKey), ctypes.byref(self.chIV))

	def SetKey(self, key):
		self.chKey = ctypes.create_string_buffer(key)

	def SetIV(self, iv):
		self.chIV = ctypes.create_string_buffer(iv)

	def Encrypt(self, data):
		buf = ctypes.create_string_buffer(len(data) + 16)
		written = ctypes.c_int(0)
		final = ctypes.c_int(0)
		ctx = ssl.EVP_CIPHER_CTX_new()
		ssl.EVP_CIPHER_CTX_init(ctx)
		ssl.EVP_EncryptInit_ex(ctx, ssl.EVP_aes_256_cbc(), None, self.chKey, self.chIV)
		ssl.EVP_EncryptUpdate(ctx, buf, ctypes.byref(written), data, len(data))
		output = buf.raw[:written.value]
		ssl.EVP_EncryptFinal_ex(ctx, buf, ctypes.byref(final))
		output += buf.raw[:final.value]
		return output

	def Decrypt(self, data):
		buf = ctypes.create_string_buffer(len(data) + 16)
		written = ctypes.c_int(0)
		final = ctypes.c_int(0)
		ctx = ssl.EVP_CIPHER_CTX_new()
		ssl.EVP_CIPHER_CTX_init(ctx)
		ssl.EVP_DecryptInit_ex(ctx, ssl.EVP_aes_256_cbc(), None, self.chKey, self.chIV)
		ssl.EVP_DecryptUpdate(ctx, buf, ctypes.byref(written), data, len(data))
		output = buf.raw[:written.value]
		ssl.EVP_DecryptFinal_ex(ctx, buf, ctypes.byref(final))
		output += buf.raw[:final.value]
		return output

class Crypter_pure(object):
	def __init__(self):
		self.m = AESModeOfOperation()
		self.cbc = self.m.modeOfOperation["CBC"]
		self.sz = self.m.aes.keySize["SIZE_256"]

	def SetKeyFromPassphrase(self, vKeyData, vSalt, nDerivIterations, nDerivationMethod):
		if nDerivationMethod != 0:
			return 0
		data = vKeyData + vSalt
		for i in xrange(nDerivIterations):
			data = hashlib.sha512(data).digest()
		self.SetKey(data[0:32])
		self.SetIV(data[32:32+16])
		return len(data)

	def SetKey(self, key):
		self.chKey = [ord(i) for i in key]

	def SetIV(self, iv):
		self.chIV = [ord(i) for i in iv]

	def Encrypt(self, data):
		mode, size, cypher = self.m.encrypt(data, self.cbc, self.chKey, self.sz, self.chIV)
		return ''.join(map(chr, cypher))

	def Decrypt(self, data):
		chData = [ord(i) for i in data]
		return self.m.decrypt(chData, self.sz, self.cbc, self.chKey, self.sz, self.chIV)

if crypter == 'pycrypto':
	crypter = Crypter_pycrypto()
#	print "Crypter: pycrypto"
elif crypter == 'ssl':
	crypter = Crypter_ssl()
#	print "Crypter: ssl"
else:
	crypter = Crypter_pure()
#	print "Crypter: pure"
	logging.warning("pycrypto or libssl not found, decryption may be slow")

##########################################
# end of pywallet crypter implementation #
##########################################

# secp256k1

try:
	_p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2FL
except:
	print "Python 3 is not supported, you need Python 2.7.x"
	exit(1)
_r = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141L
_b = 0x0000000000000000000000000000000000000000000000000000000000000007L
_a = 0x0000000000000000000000000000000000000000000000000000000000000000L
_Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798L
_Gy = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8L

try:
	import ecdsa
	from ecdsa import der
	curve_secp256k1 = ecdsa.ellipticcurve.CurveFp (_p, _a, _b)
	generator_secp256k1 = g = ecdsa.ellipticcurve.Point (curve_secp256k1, _Gx, _Gy, _r)
	randrange = random.SystemRandom().randrange
	secp256k1 = ecdsa.curves.Curve ( "secp256k1", curve_secp256k1, generator_secp256k1, (1, 3, 132, 0, 10) )
	ecdsa.curves.curves.append (secp256k1)
except:
	missing_dep.append('ecdsa')

# python-ecdsa code (EC_KEY implementation)

class CurveFp( object ):
	def __init__( self, p, a, b ):
		self.__p = p
		self.__a = a
		self.__b = b

	def p( self ):
		return self.__p

	def a( self ):
		return self.__a

	def b( self ):
		return self.__b

	def contains_point( self, x, y ):
		return ( y * y - ( x * x * x + self.__a * x + self.__b ) ) % self.__p == 0

class Point( object ):
	def __init__( self, curve, x, y, order = None ):
		self.__curve = curve
		self.__x = x
		self.__y = y
		self.__order = order
		if self.__curve: assert self.__curve.contains_point( x, y )
		if order: assert self * order == INFINITY

	def __add__( self, other ):
		if other == INFINITY: return self
		if self == INFINITY: return other
		assert self.__curve == other.__curve
		if self.__x == other.__x:
			if ( self.__y + other.__y ) % self.__curve.p() == 0:
				return INFINITY
			else:
				return self.double()

		p = self.__curve.p()
		l = ( ( other.__y - self.__y ) * \
					inverse_mod( other.__x - self.__x, p ) ) % p
		x3 = ( l * l - self.__x - other.__x ) % p
		y3 = ( l * ( self.__x - x3 ) - self.__y ) % p
		return Point( self.__curve, x3, y3 )

	def __mul__( self, other ):
		def leftmost_bit( x ):
			assert x > 0
			result = 1L
			while result <= x: result = 2 * result
			return result / 2

		e = other
		if self.__order: e = e % self.__order
		if e == 0: return INFINITY
		if self == INFINITY: return INFINITY
		assert e > 0
		e3 = 3 * e
		negative_self = Point( self.__curve, self.__x, -self.__y, self.__order )
		i = leftmost_bit( e3 ) / 2
		result = self
		while i > 1:
			result = result.double()
			if ( e3 & i ) != 0 and ( e & i ) == 0: result = result + self
			if ( e3 & i ) == 0 and ( e & i ) != 0: result = result + negative_self
			i = i / 2
		return result

	def __rmul__( self, other ):
		return self * other

	def __str__( self ):
		if self == INFINITY: return "infinity"
		return "(%d,%d)" % ( self.__x, self.__y )

	def double( self ):
		if self == INFINITY:
			return INFINITY

		p = self.__curve.p()
		a = self.__curve.a()
		l = ( ( 3 * self.__x * self.__x + a ) * \
					inverse_mod( 2 * self.__y, p ) ) % p
		x3 = ( l * l - 2 * self.__x ) % p
		y3 = ( l * ( self.__x - x3 ) - self.__y ) % p
		return Point( self.__curve, x3, y3 )

	def x( self ):
		return self.__x

	def y( self ):
		return self.__y

	def curve( self ):
		return self.__curve

	def order( self ):
		return self.__order

INFINITY = Point( None, None, None )

def inverse_mod( a, m ):
	if a < 0 or m <= a: a = a % m
	c, d = a, m
	uc, vc, ud, vd = 1, 0, 0, 1
	while c != 0:
		q, c, d = divmod( d, c ) + ( c, )
		uc, vc, ud, vd = ud - q*uc, vd - q*vc, uc, vc
	assert d == 1
	if ud > 0: return ud
	else: return ud + m

class Signature( object ):
	def __init__( self, r, s ):
		self.r = r
		self.s = s

class Public_key( object ):
	def __init__( self, generator, point, c=None ):
		self.curve = generator.curve()
		self.generator = generator
		self.point = point
		self.compressed = c
		n = generator.order()
		if not n:
			raise RuntimeError, "Generator point must have order."
		if not n * point == INFINITY:
			raise RuntimeError, "Generator point order is bad."
		if point.x() < 0 or n <= point.x() or point.y() < 0 or n <= point.y():
			raise RuntimeError, "Generator point has x or y out of range."

	def verifies( self, hash, signature ):
		G = self.generator
		n = G.order()
		r = signature.r
		s = signature.s
		if r < 1 or r > n-1: return False
		if s < 1 or s > n-1: return False
		c = inverse_mod( s, n )
		u1 = ( hash * c ) % n
		u2 = ( r * c ) % n
		xy = u1 * G + u2 * self.point
		v = xy.x() % n
		return v == r

	def ser(self):
		if self.compressed:
			pk=('%02x'%(2+(self.point.y()&1))) + '%064x' % self.point.x()
		else:
			pk='04%064x%064x' % (self.point.x(), self.point.y())

		return pk.decode('hex')

	def get_addr(self, v=0):
		return public_key_to_bc_address(self.ser(), v)

class Private_key( object ):
	def __init__( self, public_key, secret_multiplier ):
		self.public_key = public_key
		self.secret_multiplier = secret_multiplier

	def der( self ):
		hex_der_key = '06052b8104000a30740201010420' + \
			'%064x' % self.secret_multiplier + \
			'a00706052b8104000aa14403420004' + \
			'%064x' % self.public_key.point.x() + \
			'%064x' % self.public_key.point.y()
		return hex_der_key.decode('hex')

	def sign( self, hash, random_k ):
		G = self.public_key.generator
		n = G.order()
		k = random_k % n
		p1 = k * G
		r = p1.x()
		if r == 0: raise RuntimeError, "amazingly unlucky random number r"
		s = ( inverse_mod( k, n ) * \
					( hash + ( self.secret_multiplier * r ) % n ) ) % n
		if s == 0: raise RuntimeError, "amazingly unlucky random number s"
		return Signature( r, s )

class EC_KEY(object):
	def __init__( self, secret ):
		curve = CurveFp( _p, _a, _b )
		generator = Point( curve, _Gx, _Gy, _r )
		self.pubkey = Public_key( generator, generator * secret )
		self.privkey = Private_key( self.pubkey, secret )
		self.secret = secret

# end of python-ecdsa code

# pywallet openssl private key implementation

def i2d_ECPrivateKey(pkey, compressed=False):#, crypted=True):
	part3='a081a53081a2020101302c06072a8648ce3d0101022100'  # for uncompressed keys
	if compressed:
		if True:#not crypted:  ## Bitcoin accepts both part3's for crypted wallets...
			part3='a08185308182020101302c06072a8648ce3d0101022100'  # for compressed keys
		key = '3081d30201010420' + \
			'%064x' % pkey.secret + \
			part3 + \
			'%064x' % _p + \
			'3006040100040107042102' + \
			'%064x' % _Gx + \
			'022100' + \
			'%064x' % _r + \
			'020101a124032200'
	else:
		key = '308201130201010420' + \
			'%064x' % pkey.secret + \
			part3 + \
			'%064x' % _p + \
			'3006040100040107044104' + \
			'%064x' % _Gx + \
			'%064x' % _Gy + \
			'022100' + \
			'%064x' % _r + \
			'020101a144034200'

	return key.decode('hex') + i2o_ECPublicKey(pkey, compressed)

def i2o_ECPublicKey(pkey, compressed=False):
	# public keys are 65 bytes long (520 bits)
	# 0x04 + 32-byte X-coordinate + 32-byte Y-coordinate
	# 0x00 = point at infinity, 0x02 and 0x03 = compressed, 0x04 = uncompressed
	# compressed keys: <sign> <x> where <sign> is 0x02 if y is even and 0x03 if y is odd
	if compressed:
		if pkey.pubkey.point.y() & 1:
			key = '03' + '%064x' % pkey.pubkey.point.x()
		else:
			key = '02' + '%064x' % pkey.pubkey.point.x()
	else:
		key = '04' + \
			'%064x' % pkey.pubkey.point.x() + \
			'%064x' % pkey.pubkey.point.y()

	return key.decode('hex')

# bitcointools hashes and base58 implementation

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

	# Bitcoin does a little leading-zero-compression:
	# leading 0-bytes in the input become leading-1s
	nPad = 0
	for c in v:
		if c == '\0': nPad += 1
		else: break

	return (__b58chars[0]*nPad) + result

def b58decode(v, length):
	""" decode v into a string of len bytes
	"""
	long_value = 0L
	for (i, c) in enumerate(v[::-1]):
		long_value += __b58chars.find(c) * (__b58base**i)

	result = ''
	while long_value >= 256:
		div, mod = divmod(long_value, 256)
		result = chr(mod) + result
		long_value = div
	result = chr(long_value) + result

	nPad = 0
	for c in v:
		if c == __b58chars[0]: nPad += 1
		else: break

	result = chr(0)*nPad + result
	if length is not None and len(result) != length:
		return None

	return result

# end of bitcointools base58 implementation

# address handling code

def long_hex(bytes):
	return bytes.encode('hex_codec')

def Hash(data):
	return hashlib.sha256(hashlib.sha256(data).digest()).digest()

def EncodeBase58Check(secret):
	hash = Hash(secret)
	return b58encode(secret + hash[0:4])

def DecodeBase58Check(sec):
	vchRet = b58decode(sec, None)
	secret = vchRet[0:-4]
	csum = vchRet[-4:]
	hash = Hash(secret)
	cs32 = hash[0:4]
	if cs32 != csum:
		return None
	else:
		return secret

def str_to_long(b):
	res = 0
	pos = 1
	for a in reversed(b):
		res += ord(a) * pos
		pos *= 256
	return res

def PrivKeyToSecret(privkey):
	if len(privkey) == 279:
		return privkey[9:9+32]
	else:
		return privkey[8:8+32]

def SecretToASecret(secret, compressed=False):
	prefix = chr((addrtype+128)&255)
	if addrtype==48:  #assuming Litecoin
		prefix = chr(128)
	vchIn = prefix + secret
	if compressed: vchIn += '\01'
	return EncodeBase58Check(vchIn)

def ASecretToSecret(sec):
	vch = DecodeBase58Check(sec)
	if not vch:
		return False
	if vch[0] != chr((addrtype+128)&255):
		print 'Warning: adress prefix seems bad (%d vs %d)'%(ord(vch[0]), (addrtype+128)&255)
	return vch[1:]

def regenerate_key(sec):
	b = ASecretToSecret(sec)
	if not b:
		return False
	b = b[0:32]
	secret = int('0x' + b.encode('hex'), 16)
	return EC_KEY(secret)

def GetPubKey(pkey, compressed=False):
	return i2o_ECPublicKey(pkey, compressed)

def GetPrivKey(pkey, compressed=False):
	return i2d_ECPrivateKey(pkey, compressed)

def GetSecret(pkey):
	return ('%064x' % pkey.secret).decode('hex')

def is_compressed(sec):
	b = ASecretToSecret(sec)
	return len(b) == 33

# bitcointools wallet.dat handling code

def create_env(db_dir):
	db_env = DBEnv(0)
	r = db_env.open(db_dir, (DB_CREATE|DB_INIT_LOCK|DB_INIT_LOG|DB_INIT_MPOOL|DB_INIT_TXN|DB_THREAD|DB_RECOVER))
	return db_env

def parse_CAddress(vds):
	d = {'ip':'0.0.0.0','port':0,'nTime': 0}
	try:
		d['nVersion'] = vds.read_int32()
		d['nTime'] = vds.read_uint32()
		d['nServices'] = vds.read_uint64()
		d['pchReserved'] = vds.read_bytes(12)
		d['ip'] = socket.inet_ntoa(vds.read_bytes(4))
		d['port'] = vds.read_uint16()
	except:
		pass
	return d

def deserialize_CAddress(d):
	return d['ip']+":"+str(d['port'])

def parse_BlockLocator(vds):
	d = { 'hashes' : [] }
	nHashes = vds.read_compact_size()
	for i in xrange(nHashes):
		d['hashes'].append(vds.read_bytes(32))
		return d

def deserialize_BlockLocator(d):
  result = "Block Locator top: "+d['hashes'][0][::-1].encode('hex_codec')
  return result

def parse_setting(setting, vds):
	if setting[0] == "f":	# flag (boolean) settings
		return str(vds.read_boolean())
	elif setting[0:4] == "addr": # CAddress
		d = parse_CAddress(vds)
		return deserialize_CAddress(d)
	elif setting == "nTransactionFee":
		return vds.read_int64()
	elif setting == "nLimitProcessors":
		return vds.read_int32()
	return 'unknown setting'

class SerializationError(Exception):
	""" Thrown when there's a problem deserializing or serializing """


def search_patterns_on_disk(device, size, inc, patternlist):   # inc must be higher than 1k
	try:
		otype=os.O_RDONLY|os.O_BINARY
	except:
		otype=os.O_RDONLY
	try:
		fd = os.open(device, otype)
	except Exception as e:
		print "Can't open %s, check the path or try as root"%device
		print "  Error:", e.args
		exit(0)

	i = 0
	data=''

	tzero=time.time()
	sizetokeep=0
	BlocksToInspect=dict(map(lambda x:[x,[]], patternlist))
	syst=systype()
	lendataloaded=None
	writeProgressEvery=100*Mo
	while i < int(size) and (lendataloaded!=0 or lendataloaded==None):
		if int(i/writeProgressEvery)!=int((i+inc)/writeProgressEvery):
			print "%.2f Go read"%(i/1e9)
		try:
			datakept=data[-sizetokeep:]
			data = datakept+os.read(fd, inc)
			lendataloaded = len(data)-len(datakept)   #should be inc
			for text in patternlist:
				if text in data:
					BlocksToInspect[text].append([i-len(datakept), data, len(datakept)])
					pass
			sizetokeep=20   # 20 because all the patterns have a len<20. Could be higher.
			i += lendataloaded
		except Exception as exc:
			if lendataloaded%512>0:
				raise Exception("SPOD error 1: %d, %d"%(lendataloaded, i-len(datakept)))
			os.lseek(fd, lendataloaded, os.SEEK_CUR)
			print str(exc)
			i += lendataloaded
			continue
	os.close(fd)

	AllOffsets=dict(map(lambda x:[x,[]], patternlist))
	for text,blocks in BlocksToInspect.items():
		for offset,data,ldk in blocks:  #ldk = len(datakept)
			offsetslist=[offset+m.start() for m in re.finditer(text, data)]
			AllOffsets[text].extend(offsetslist)

	AllOffsets['PRFdevice']=device
	AllOffsets['PRFdt']=time.time()-tzero
	AllOffsets['PRFsize']=i
	return AllOffsets

def multiextract(s, ll):
	r=[]
	cursor=0
	for length in ll:
		r.append(s[cursor:cursor+length])
		cursor+=length
	if s[cursor:]!='':
		r.append(s[cursor:])
	return r

class RecovCkey(object):
	def __init__(self, epk, pk):
		self.encrypted_pk=epk
		self.public_key=pk
		self.mkey=None
		self.privkey=None


class RecovMkey(object):
	def __init__(self, ekey, salt, nditer, ndmethod, nid):
		self.encrypted_key=ekey
		self.salt=salt
		self.iterations=nditer
		self.method=ndmethod
		self.id=nid

def readpartfile(fd, offset, length):   #make everything 512*n because of windows...
	rest=offset%512
	new_offset=offset-rest
	big_length=512*(int((length+rest-1)/512)+1)
	os.lseek(fd, new_offset, os.SEEK_SET)
	d=os.read(fd, big_length)
	return d[rest:rest+length]

def recov_ckey(fd, offset):
	d=readpartfile(fd, offset-49, 122)
	me=multiextract(d, [1,48,4,4,1])

	checks=[]
	checks.append([0, '30'])
	checks.append([3, '636b6579'])
	if sum(map(lambda x:int(me[x[0]]!=x[1].decode('hex')), checks)):  #number of false statements
		return None

	return me

def recov_mkey(fd, offset):
	d=readpartfile(fd, offset-72, 84)
	me=multiextract(d, [4,48,1,8,4,4,1,2,8,4])

	checks=[]
	checks.append([0, '43000130'])
	checks.append([2, '08'])
	checks.append([6, '00'])
	checks.append([8, '090001046d6b6579'])
	if sum(map(lambda x:int(me[x[0]]!=x[1].decode('hex')), checks)):  #number of false statements
		return None

	return me

def recov_uckey(fd, offset):
	checks=[]

	d=readpartfile(fd, offset-217, 223)
	if d[-7]=='\x26':
		me=multiextract(d, [2,1,4,1,32,141,33,2,1,6])

		checks.append([0, '3081'])
		checks.append([2, '02010104'])
	elif d[-7]=='\x46':
		d=readpartfile(fd, offset-282, 286)

		me=multiextract(d, [2,1,4,1,32,173,65,1,2,5])

		checks.append([0, '8201'])
		checks.append([2, '02010104'])
		checks.append([-1, '460001036b'])
	else:
		return None


	if sum(map(lambda x:int(me[x[0]]!=x[1].decode('hex')), checks)):  #number of false statements
		return None

	return me

def starts_with(s, b):
	return len(s)>=len(b) and s[:len(b)]==b


def recov(device, passes, size=102400, inc=10240, outputdir='.'):
	if inc%512>0:
		inc-=inc%512   #inc must be 512*n on Windows... Don't ask me why...

	nameToDBName={'mkey':'\x09\x00\x01\x04mkey','ckey':'\x27\x00\x01\x04ckey','key':'\x00\x01\x03key',}


	if not starts_with(device, 'PartialRecoveryFile:'):
		r=search_patterns_on_disk(device, size, inc, map(lambda x:nameToDBName[x], ['mkey', 'ckey', 'key']))
		f=open(outputdir+'/pywallet_partial_recovery_%d.dat'%ts(), 'w')
		f.write(str(r))
		f.close()
		print "\nRead %.1f Go in %.1f minutes\n"%(r['PRFsize']/1e9, r['PRFdt']/60.0)
	else:
		prf=device[20:]
		f=open(prf, 'r')
		content=f.read()
		f.close()
		cmd=("z = "+content+"")
		exec cmd in locals()
		r=z
		device=r['PRFdevice']
		print "\nLoaded %.1f Go from %s\n"%(r['PRFsize']/1e9, device)


	try:
		otype=os.O_RDONLY|os.O_BINARY
	except:
		otype=os.O_RDONLY
	fd = os.open(device, otype)


	mkeys=[]
	crypters=[]
	syst=systype()
	for offset in r[nameToDBName['mkey']]:
		s=recov_mkey(fd, offset)
		if s==None:
			continue
		newmkey=RecovMkey(s[1],s[3],int(s[5][::-1].encode('hex'), 16),int(s[4][::-1].encode('hex'), 16),int(s[-1][::-1].encode('hex'), 16))
		mkeys.append([offset,newmkey])

	print "Found", len(mkeys), 'possible wallets'




	ckeys=[]
	for offset in r[nameToDBName['ckey']]:
		s=recov_ckey(fd, offset)
		if s==None:
			continue
		newckey=RecovCkey(s[1], s[5][:int(s[4].encode('hex'),16)])
		ckeys.append([offset,newckey])
	print "Found", len(ckeys), 'possible encrypted keys'


	uckeys=[]
	for offset in r[nameToDBName['key']]:
		s=recov_uckey(fd, offset)
		if s==None:
			continue
		uckeys.append(s[4])
	print "Found", len(uckeys), 'possible unencrypted keys'


	os.close(fd)


	list_of_possible_keys_per_master_key=dict(map(lambda x:[x[1],[]], mkeys))
	for cko,ck in ckeys:
		tl=map(lambda x:[abs(x[0]-cko)]+x, mkeys)
		tl=sorted(tl, key=lambda x:x[0])
		list_of_possible_keys_per_master_key[tl[0][2]].append(ck)

	cpt=0
	mki=1
	tzero=time.time()
	if len(passes)==0:
		if len(ckeys)>0:
			print "Can't decrypt them as you didn't provide any passphrase."
	else:
		for mko,mk in mkeys:
			list_of_possible_keys=list_of_possible_keys_per_master_key[mk]
			sys.stdout.write( "\nPossible wallet #"+str(mki))
			sys.stdout.flush()
			for ppi,pp in enumerate(passes):
				sys.stdout.write( "\n    with passphrase #"+str(ppi+1)+"  ")
				sys.stdout.flush()
				failures_in_a_row=0
#				print "SKFP params:", pp, mk.salt, mk.iterations, mk.method
				res = crypter.SetKeyFromPassphrase(pp, mk.salt, mk.iterations, mk.method)
				if res == 0:
					print "Unsupported derivation method"
					sys.exit(1)
				masterkey = crypter.Decrypt(mk.encrypted_key)
				crypter.SetKey(masterkey)
				for ck in list_of_possible_keys:
					if cpt%10==9 and failures_in_a_row==0:
						sys.stdout.write('.')
						sys.stdout.flush()
					if failures_in_a_row>5:
						break
					crypter.SetIV(Hash(ck.public_key))
					secret = crypter.Decrypt(ck.encrypted_pk)
					compressed = ck.public_key[0] != '\04'


					pkey = EC_KEY(int('0x' + secret.encode('hex'), 16))
					if ck.public_key != GetPubKey(pkey, compressed):
						failures_in_a_row+=1
					else:
						failures_in_a_row=0
						ck.mkey=mk
						ck.privkey=secret
					cpt+=1
			mki+=1
		print "\n"
		tone=time.time()
		try:
			calcspeed=1.0*cpt/(tone-tzero)*60  #calc/min
		except:
			calcspeed=1.0
		if calcspeed==0:
			calcspeed=1.0

		ckeys_not_decrypted=filter(lambda x:x[1].privkey==None, ckeys)
		refused_to_test_all_pps=True
		if len(ckeys_not_decrypted)==0:
			print "All the found encrypted private keys have been decrypted."
			return map(lambda x:x[1].privkey, ckeys)
		else:
			print "Private keys not decrypted: %d"%len(ckeys_not_decrypted)
			print "Trying all the remaining possibilities (%d) might take up to %d minutes."%(len(ckeys_not_decrypted)*len(passes)*len(mkeys),int(len(ckeys_not_decrypted)*len(passes)*len(mkeys)/calcspeed))
			cont=raw_input("Do you want to test them? (y/n): ")
			while len(cont)==0:
                                cont=raw_input("Do you want to test them? (y/n): ")
                        if cont[0]=='y':
                                refused_to_test_all_pps=False
                                cpt=0
                                for dist,mko,mk in tl:
                                        for ppi,pp in enumerate(passes):
                                                res = crypter.SetKeyFromPassphrase(pp, mk.salt, mk.iterations, mk.method)
                                                if res == 0:
                                                        logging.error("Unsupported derivation method")
                                                        sys.exit(1)
                                                masterkey = crypter.Decrypt(mk.encrypted_key)
                                                crypter.SetKey(masterkey)
                                                for cko,ck in ckeys_not_decrypted:
                                                        tl=map(lambda x:[abs(x[0]-cko)]+x, mkeys)
                                                        tl=sorted(tl, key=lambda x:x[0])
                                                        if mk==tl[0][2]:
                                                                continue         #because already tested
                                                        crypter.SetIV(Hash(ck.public_key))
                                                        secret = crypter.Decrypt(ck.encrypted_pk)
                                                        compressed = ck.public_key[0] != '\04'


                                                        pkey = EC_KEY(int('0x' + secret.encode('hex'), 16))
                                                        if ck.public_key == GetPubKey(pkey, compressed):
                                                                ck.mkey=mk
                                                                ck.privkey=secret
                                                        cpt+=1

		print
		ckeys_not_decrypted=filter(lambda x:x[1].privkey==None, ckeys)
		if len(ckeys_not_decrypted)==0:
			print "All the found encrypted private keys have been finally decrypted."
		elif not refused_to_test_all_pps:
			print "Private keys not decrypted: %d"%len(ckeys_not_decrypted)
			print "Try another password, check the size of your partition or seek help"


	uncrypted_ckeys=filter(lambda x:x!=None, map(lambda x:x[1].privkey, ckeys))
	uckeys.extend(uncrypted_ckeys)

	return uckeys




def ts():
	return int(time.mktime(datetime.now().timetuple()))

def check_postkeys(key, postkeys):
	for i in postkeys:
		if key[:len(i)] == i:
			return True
	return False

def one_element_in(a, string):
	for i in a:
		if i in string:
			return True
	return False

def first_read(device, size, prekeys, inc=10000):
	t0 = ts()-1
	try:
		fd = os.open (device, os.O_RDONLY)
	except:
		print("Can't open %s, check the path or try as root"%device)
		exit(0)
	prekey = prekeys[0]
	data = ""
	i = 0
	data = os.read (fd, i)
	before_contained_key = False
	contains_key = False
	ranges = []

	while i < int(size):
		if i%(10*Mio) > 0 and i%(10*Mio) <= inc:
			print("\n%.2f/%.2f Go"%(i/1e9, size/1e9))
			t = ts()
			speed = i/(t-t0)
			ETAts = size/speed + t0
			d = datetime.fromtimestamp(ETAts)
			print(d.strftime("   ETA: %H:%M:%S"))

		try:
			data = os.read (fd, inc)
		except Exception as exc:
			os.lseek(fd, inc, os.SEEK_CUR)
			print str(exc)
			i += inc
			continue

		contains_key = one_element_in(prekeys, data)

		if not before_contained_key and contains_key:
			ranges.append(i)

		if before_contained_key and not contains_key:
			ranges.append(i)

		before_contained_key = contains_key

		i += inc

	os.close (fd)
	return ranges

def shrink_intervals(device, ranges, prekeys, inc=1000):
	prekey = prekeys[0]
	nranges = []
	fd = os.open (device, os.O_RDONLY)
	for j in range(len(ranges)/2):
		before_contained_key = False
		contains_key = False
		bi = ranges[2*j]
		bf = ranges[2*j+1]

		mini_blocks = []
		k = bi
		while k <= bf + len(prekey) + 1:
			mini_blocks.append(k)
			k += inc
			mini_blocks.append(k)

		for k in range(len(mini_blocks)/2):
			mini_blocks[2*k] -= len(prekey) +1
			mini_blocks[2*k+1] += len(prekey) +1


			bi = mini_blocks[2*k]
			bf = mini_blocks[2*k+1]

			os.lseek(fd, bi, 0)

			data = os.read(fd, bf-bi+1)
			contains_key = one_element_in(prekeys, data)

			if not before_contained_key and contains_key:
				nranges.append(bi)

			if before_contained_key and not contains_key:
				nranges.append(bi+len(prekey) +1+len(prekey) +1)

			before_contained_key = contains_key

	os.close (fd)

	return nranges

def find_offsets(device, ranges, prekeys):
	prekey = prekeys[0]
	list_offsets = []
	to_read = 0
	fd = os.open (device, os.O_RDONLY)
	for i in range(len(ranges)/2):
		bi = ranges[2*i]-len(prekey)-1
		os.lseek(fd, bi, 0)
		bf = ranges[2*i+1]+len(prekey)+1
		to_read += bf-bi+1
		buf = ""
		for j in range(len(prekey)):
			buf += "\x00"
		curs = bi

		while curs <= bf:
			data = os.read(fd, 1)
			buf = buf[1:] + data
			if buf in prekeys:
				list_offsets.append(curs)
			curs += 1

	os.close (fd)

	return [to_read, list_offsets]

def read_keys(device, list_offsets):
	found_hexkeys = []
	fd = os.open (device, os.O_RDONLY)
	for offset in list_offsets:
		os.lseek(fd, offset+1, 0)
		data = os.read(fd, 40)
		hexkey = data[1:33].encode('hex')
		after_key = data[33:39].encode('hex')
		if hexkey not in found_hexkeys and check_postkeys(after_key.decode('hex'), postkeys):
			found_hexkeys.append(hexkey)

	os.close (fd)

	return found_hexkeys

def read_device_size(size):
	if size[-2] == 'i':
		unit = size[-3:]
		value = float(size[:-3])
	else:
		unit = size[-2:]
		value = float(size[:-2])
	exec 'unit = %s' % unit
	return int(value * unit)

def md5_2(a):
	return hashlib.md5(a).digest()

def md5_file(nf):
  try:
	fichier = file(nf, 'r').read()
	return md5_2(fichier)
  except:
	return 'zz'

def md5_onlinefile(add):
	page = urllib.urlopen(add).read()
	return md5_2(page)


class KEY:

	 def __init__ (self):
		  self.prikey = None
		  self.pubkey = None

	 def generate (self, secret=None):
		  if secret:
				exp = int ('0x' + secret.encode ('hex'), 16)
				self.prikey = ecdsa.SigningKey.from_secret_exponent (exp, curve=secp256k1)
		  else:
				self.prikey = ecdsa.SigningKey.generate (curve=secp256k1)
		  self.pubkey = self.prikey.get_verifying_key()
		  return self.prikey.to_der()

	 def set_privkey (self, key):
		  if len(key) == 279:
				seq1, rest = der.remove_sequence (key)
				integer, rest = der.remove_integer (seq1)
				octet_str, rest = der.remove_octet_string (rest)
				tag1, cons1, rest, = der.remove_constructed (rest)
				tag2, cons2, rest, = der.remove_constructed (rest)
				point_str, rest = der.remove_bitstring (cons2)
				self.prikey = ecdsa.SigningKey.from_string(octet_str, curve=secp256k1)
		  else:
				self.prikey = ecdsa.SigningKey.from_der (key)

	 def set_pubkey (self, key):
		  key = key[1:]
		  self.pubkey = ecdsa.VerifyingKey.from_string (key, curve=secp256k1)

	 def get_privkey (self):
		  _p = self.prikey.curve.curve.p ()
		  _r = self.prikey.curve.generator.order ()
		  _Gx = self.prikey.curve.generator.x ()
		  _Gy = self.prikey.curve.generator.y ()
		  encoded_oid2 = der.encode_oid (*(1, 2, 840, 10045, 1, 1))
		  encoded_gxgy = "\x04" + ("%64x" % _Gx).decode('hex') + ("%64x" % _Gy).decode('hex')
		  param_sequence = der.encode_sequence (
				ecdsa.der.encode_integer(1),
					der.encode_sequence (
					encoded_oid2,
					der.encode_integer (_p),
				),
				der.encode_sequence (
					der.encode_octet_string("\x00"),
					der.encode_octet_string("\x07"),
				),
				der.encode_octet_string (encoded_gxgy),
				der.encode_integer (_r),
				der.encode_integer (1),
		  );
		  encoded_vk = "\x00\x04" + self.pubkey.to_string ()
		  return der.encode_sequence (
				der.encode_integer (1),
				der.encode_octet_string (self.prikey.to_string ()),
				der.encode_constructed (0, param_sequence),
				der.encode_constructed (1, der.encode_bitstring (encoded_vk)),
		  )

	 def get_pubkey (self):
		  return "\x04" + self.pubkey.to_string()

	 def sign (self, hash):
		  sig = self.prikey.sign_digest (hash, sigencode=ecdsa.util.sigencode_der)
		  return sig.encode('hex')

	 def verify (self, hash, sig):
		  return self.pubkey.verify_digest (sig, hash, sigdecode=ecdsa.util.sigdecode_der)

def bool_to_int(b):
	if b:
		return 1
	return 0

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

	def map_file(self, file, start):	# Initialize with bytes from file
		self.input = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
		self.read_cursor = start
	def seek_file(self, position):
		self.read_cursor = position
	def close_file(self):
		self.input.close()

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

	def read_bytes(self, length):
		try:
			result = self.input[self.read_cursor:self.read_cursor+length]
			self.read_cursor += length
			return result
		except IndexError:
			raise SerializationError("attempt to read past end of buffer")

		return ''

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

def inversetxid(txid):
	if len(txid) is not 64:
		print("Bad txid")
		return "CORRUPTEDTXID:"+txid
#		exit(0)
	new_txid = ""
	for i in range(32):
		new_txid += txid[62-2*i];
		new_txid += txid[62-2*i+1];
	return new_txid

def parse_wallet(db, item_callback):
	kds = BCDataStream()
	vds = BCDataStream()


	def parse_TxIn(vds):
		d = {}
		d['prevout_hash'] = vds.read_bytes(32).encode('hex')
		d['prevout_n'] = vds.read_uint32()
		d['scriptSig'] = vds.read_bytes(vds.read_compact_size()).encode('hex')
		d['sequence'] = vds.read_uint32()
		return d


	def parse_TxOut(vds):
		d = {}
		d['value'] = vds.read_int64()/1e8
		d['scriptPubKey'] = vds.read_bytes(vds.read_compact_size()).encode('hex')
		return d


	for (key, value) in db.items():
		d = { }

		kds.clear(); kds.write(key)
		vds.clear(); vds.write(value)

		type = kds.read_string()

		d["__key__"] = key
		d["__value__"] = value
		d["__type__"] = type

		try:
			if type == "tx":
				d["tx_id"] = inversetxid(kds.read_bytes(32).encode('hex_codec'))
				start = vds.read_cursor
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
				d['tx'] = vds.input[start:vds.read_cursor].encode('hex_codec')
				d['txv'] = value.encode('hex_codec')
				d['txk'] = key.encode('hex_codec')
			elif type == "name":
				d['hash'] = kds.read_string()
				d['name'] = vds.read_string()
			elif type == "version":
				d['version'] = vds.read_uint32()
			elif type == "minversion":
				d['minversion'] = vds.read_uint32()
			elif type == "setting":
				d['setting'] = kds.read_string()
				d['value'] = parse_setting(d['setting'], vds)
			elif type == "key":
				d['public_key'] = kds.read_bytes(kds.read_compact_size())
				d['private_key'] = vds.read_bytes(vds.read_compact_size())
			elif type == "wkey":
				d['public_key'] = kds.read_bytes(kds.read_compact_size())
				d['private_key'] = vds.read_bytes(vds.read_compact_size())
				d['created'] = vds.read_int64()
				d['expires'] = vds.read_int64()
				d['comment'] = vds.read_string()
			elif type == "defaultkey":
				d['key'] = vds.read_bytes(vds.read_compact_size())
			elif type == "pool":
				d['n'] = kds.read_int64()
				d['nVersion'] = vds.read_int32()
				d['nTime'] = vds.read_int64()
				d['public_key'] = vds.read_bytes(vds.read_compact_size())
			elif type == "acc":
				d['account'] = kds.read_string()
				d['nVersion'] = vds.read_int32()
				d['public_key'] = vds.read_bytes(vds.read_compact_size())
			elif type == "acentry":
				d['account'] = kds.read_string()
				d['n'] = kds.read_uint64()
				d['nVersion'] = vds.read_int32()
				d['nCreditDebit'] = vds.read_int64()
				d['nTime'] = vds.read_int64()
				d['otherAccount'] = vds.read_string()
				d['comment'] = vds.read_string()
			elif type == "bestblock":
				d['nVersion'] = vds.read_int32()
				d.update(parse_BlockLocator(vds))
			elif type == "ckey":
				d['public_key'] = kds.read_bytes(kds.read_compact_size())
				d['encrypted_private_key'] = vds.read_bytes(vds.read_compact_size())
			elif type == "mkey":
				d['nID'] = kds.read_uint32()
				d['encrypted_key'] = vds.read_string()
				d['salt'] = vds.read_string()
				d['nDerivationMethod'] = vds.read_uint32()
				d['nDerivationIterations'] = vds.read_uint32()
				d['otherParams'] = vds.read_string()

			item_callback(type, d)

		except Exception, e:
			traceback.print_exc()
			print("ERROR parsing wallet.dat, type %s" % type)
			print("key data: %s"%key)
			print("key data in hex: %s"%key.encode('hex_codec'))
			print("value data in hex: %s"%value.encode('hex_codec'))
			sys.exit(1)

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

def merge_keys_lists(la, lb):
	lr={}
	llr=[]
	for k in la:
		lr[k[0]]=k[1]

	for k in lb:
		if k[0] in lr.keys():
			lr[k[0]]=lr[k[0]]+" / "+k[1]
		else:
			lr[k[0]]=k[1]

	for k,j in lr.items():
		llr.append([k,j])

	return llr

def merge_wallets(wadir, wa, wbdir, wb, wrdir, wr, passphrase_a, passphrase_b, passphrase_r):
	global passphrase
	passphrase_LAST=passphrase

	#Read Wallet 1
	passphrase=passphrase_a
	dba_env = create_env(wadir)
	crypted_a = read_wallet(json_db, dba_env, wa, True, True, "", None)['crypted']

	list_keys_a=[]
	for i in json_db['keys']:
		try:
			label=i['label']
		except:
			label="#Reserve"
		try:
			list_keys_a.append([i['secret'], label])
		except:
			pass

	if len(list_keys_a)==0:
		return [False, "Something went wrong with the first wallet."]


	#Read Wallet 2
	passphrase=passphrase_b
	dbb_env = create_env(wbdir)
	crypted_b = read_wallet(json_db, dbb_env, wb, True, True, "", None)['crypted']

	list_keys_b=[]
	for i in json_db['keys']:
		try:
			label=i['label']
		except:
			label="#Reserve"
		try:
			list_keys_b.append([i['secret'], label])
		except:
			pass
	if len(list_keys_b)==0:
		return [False, "Something went wrong with the second wallet."]

	m=merge_keys_lists(list_keys_a,list_keys_b)


	#Create new wallet
	dbr_env = create_env(wrdir)
	create_new_wallet(dbr_env, wr, 80100)

	dbr = open_wallet(dbr_env, wr, True)
	update_wallet(dbr, 'minversion', { 'minversion' : 60000})


	if len(passphrase_r)>0:
		NPP_salt=random_string(16).decode('hex')
		NPP_rounds=int(50000+random.random()*20000)
		NPP_method=0
		NPP_MK=random_string(64).decode('hex')

		crypter.SetKeyFromPassphrase(passphrase_r, NPP_salt, NPP_rounds, NPP_method)
		NPP_EMK = crypter.Encrypt(NPP_MK)

		update_wallet(dbr, 'mkey', {
		    "encrypted_key": NPP_EMK,
			'nDerivationIterations' : NPP_rounds,
			'nDerivationMethod' : NPP_method,
			'nID' : 1,
			'otherParams' : ''.decode('hex'),
		    "salt": NPP_salt
		})


	dbr.close()

	t='\n'.join(map(lambda x:';'.join(x), m))
	passphrase=passphrase_r

	global global_merging_message

	global_merging_message=["Merging...","Merging..."]
	thread.start_new_thread(import_csv_keys, ("\x00"+t, wrdir, wr,))
	t=""

	passphrase=passphrase_LAST

	return [True]

def random_string(l, alph="0123456789abcdef"):
	r=""
	la=len(alph)
	for i in range(l):
		r+=alph[int(la*(random.random()))]
	return r

def update_wallet(db, types, datas, paramsAreLists=False):
	"""Write a single item to the wallet.
	db must be open with writable=True.
	type and data are the type code and data dictionary as parse_wallet would
	give to item_callback.
	data's __key__, __value__ and __type__ are ignored; only the primary data
	fields are used.
	"""

	if not paramsAreLists:
		types=[types]
		datas=[datas]

	if len(types)!=len(datas):
		raise Exception("UpdateWallet: sizes are different")

	for it,type in enumerate(types):
		data=datas[it]

		d = data
		kds = BCDataStream()
		vds = BCDataStream()

		# Write the type code to the key
		kds.write_string(type)
		vds.write("")						 # Ensure there is something

		try:
			if type == "tx":
	#			raise NotImplementedError("Writing items of type 'tx'")
				kds.write(d['txi'][6:].decode('hex_codec'))
				vds.write(d['txv'].decode('hex_codec'))
			elif type == "name":
				kds.write_string(d['hash'])
				vds.write_string(d['name'])
			elif type == "version":
				vds.write_uint32(d['version'])
			elif type == "minversion":
				vds.write_uint32(d['minversion'])
			elif type == "setting":
				raise NotImplementedError("Writing items of type 'setting'")
				kds.write_string(d['setting'])
				#d['value'] = parse_setting(d['setting'], vds)
			elif type == "key":
				kds.write_string(d['public_key'])
				vds.write_string(d['private_key'])
			elif type == "wkey":
				kds.write_string(d['public_key'])
				vds.write_string(d['private_key'])
				vds.write_int64(d['created'])
				vds.write_int64(d['expires'])
				vds.write_string(d['comment'])
			elif type == "defaultkey":
				vds.write_string(d['key'])
			elif type == "pool":
				kds.write_int64(d['n'])
				vds.write_int32(d['nVersion'])
				vds.write_int64(d['nTime'])
				vds.write_string(d['public_key'])
			elif type == "acc":
				kds.write_string(d['account'])
				vds.write_int32(d['nVersion'])
				vds.write_string(d['public_key'])
			elif type == "acentry":
				kds.write_string(d['account'])
				kds.write_uint64(d['n'])
				vds.write_int32(d['nVersion'])
				vds.write_int64(d['nCreditDebit'])
				vds.write_int64(d['nTime'])
				vds.write_string(d['otherAccount'])
				vds.write_string(d['comment'])
			elif type == "bestblock":
				vds.write_int32(d['nVersion'])
				vds.write_compact_size(len(d['hashes']))
				for h in d['hashes']:
					vds.write(h)
			elif type == "ckey":
				kds.write_string(d['public_key'])
				vds.write_string(d['encrypted_private_key'])
			elif type == "mkey":
				kds.write_uint32(d['nID'])
				vds.write_string(d['encrypted_key'])
				vds.write_string(d['salt'])
				vds.write_uint32(d['nDerivationMethod'])
				vds.write_uint32(d['nDerivationIterations'])
				vds.write_string(d['otherParams'])

			else:
				print "Unknown key type: "+type

			# Write the key/value pair to the database
			db.put(kds.input, vds.input)

		except Exception, e:
			print("ERROR writing to wallet.dat, type %s"%type)
			print("data dictionary: %r"%data)
			traceback.print_exc()

def create_new_wallet(db_env, walletfile, version):
	db_out = DB(db_env)

	try:
		r = db_out.open(walletfile, "main", DB_BTREE, DB_CREATE)
	except DBError:
		r = True

	if r is not None:
		logging.error("Couldn't open %s."%walletfile)
		sys.exit(1)

	db_out.put("0776657273696f6e".decode('hex'), ("%08x"%version).decode('hex')[::-1])

	db_out.close()


def rewrite_wallet(db_env, walletfile, destFileName, pre_put_callback=None):
	db = open_wallet(db_env, walletfile)

	db_out = DB(db_env)
	try:
		r = db_out.open(destFileName, "main", DB_BTREE, DB_CREATE)
	except DBError:
		r = True

	if r is not None:
		logging.error("Couldn't open %s."%destFileName)
		sys.exit(1)

	def item_callback(type, d):
		if (pre_put_callback is None or pre_put_callback(type, d)):
			db_out.put(d["__key__"], d["__value__"])

	parse_wallet(db, item_callback)
	db_out.close()
	db.close()

# end of bitcointools wallet.dat handling code

# wallet.dat reader / writer

addr_to_keys={}
def read_wallet(json_db, db_env, walletfile, print_wallet, print_wallet_transactions, transaction_filter, include_balance, vers=-1, FillPool=False):
	global passphrase, addr_to_keys
	crypted=False

	private_keys = []
	private_hex_keys = []

	if vers > -1:
		global addrtype
		oldaddrtype = addrtype
		addrtype = vers

	db = open_wallet(db_env, walletfile, writable=FillPool)

	json_db['keys'] = []
	json_db['pool'] = []
	json_db['tx'] = []
	json_db['names'] = {}
	json_db['ckey'] = []
	json_db['mkey'] = {}

	def item_callback(type, d):
		if type == "tx":
			json_db['tx'].append({"tx_id" : d['tx_id'], "txin" : d['txIn'], "txout" : d['txOut'], "tx_v" : d['txv'], "tx_k" : d['txk']})

		elif type == "name":
			json_db['names'][d['hash']] = d['name']

		elif type == "version":
			json_db['version'] = d['version']

		elif type == "minversion":
			json_db['minversion'] = d['minversion']

		elif type == "setting":
			if not json_db.has_key('settings'): json_db['settings'] = {}
			json_db["settings"][d['setting']] = d['value']

		elif type == "defaultkey":
			json_db['defaultkey'] = public_key_to_bc_address(d['key'])

		elif type == "key":
			addr = public_key_to_bc_address(d['public_key'])
			compressed = d['public_key'][0] != '\04'
			sec = SecretToASecret(PrivKeyToSecret(d['private_key']), compressed)
			hexsec = ASecretToSecret(sec).encode('hex')[:32]
			private_keys.append(sec)
			addr_to_keys[addr]=[hexsec, d['public_key'].encode('hex')]
			json_db['keys'].append({'addr' : addr, 'sec' : sec, 'hexsec' : hexsec, 'secret' : hexsec, 'pubkey':d['public_key'].encode('hex'), 'compressed':compressed, 'private':d['private_key'].encode('hex')})

		elif type == "wkey":
			if not json_db.has_key('wkey'): json_db['wkey'] = []
			json_db['wkey']['created'] = d['created']

		elif type == "pool":
			"""	d['n'] = kds.read_int64()
				d['nVersion'] = vds.read_int32()
				d['nTime'] = vds.read_int64()
				d['public_key'] = vds.read_bytes(vds.read_compact_size())"""
			try:
				json_db['pool'].append( {'n': d['n'], 'addr': public_key_to_bc_address(d['public_key']), 'addr2': public_key_to_bc_address(d['public_key'].decode('hex')), 'addr3': public_key_to_bc_address(d['public_key'].encode('hex')), 'nTime' : d['nTime'], 'nVersion' : d['nVersion'], 'public_key_hex' : d['public_key'] } )
			except:
				json_db['pool'].append( {'n': d['n'], 'addr': public_key_to_bc_address(d['public_key']), 'nTime' : d['nTime'], 'nVersion' : d['nVersion'], 'public_key_hex' : d['public_key'].encode('hex') } )

		elif type == "acc":
			json_db['acc'] = d['account']
			print("Account %s (current key: %s)"%(d['account'], public_key_to_bc_address(d['public_key'])))

		elif type == "acentry":
			json_db['acentry'] = (d['account'], d['nCreditDebit'], d['otherAccount'], time.ctime(d['nTime']), d['n'], d['comment'])

		elif type == "bestblock":
			json_db['bestblock'] = d['hashes'][0][::-1].encode('hex_codec')

		elif type == "ckey":
			crypted=True
			compressed = d['public_key'][0] != '\04'
			json_db['keys'].append({ 'pubkey': d['public_key'].encode('hex'),'addr': public_key_to_bc_address(d['public_key']), 'encrypted_privkey':  d['encrypted_private_key'].encode('hex_codec'), 'compressed':compressed})

		elif type == "mkey":
			json_db['mkey']['nID'] = d['nID']
			json_db['mkey']['encrypted_key'] = d['encrypted_key'].encode('hex_codec')
			json_db['mkey']['salt'] = d['salt'].encode('hex_codec')
			json_db['mkey']['nDerivationMethod'] = d['nDerivationMethod']
			json_db['mkey']['nDerivationIterations'] = d['nDerivationIterations']
			json_db['mkey']['otherParams'] = d['otherParams']

			if passphrase:
				res = crypter.SetKeyFromPassphrase(passphrase, d['salt'], d['nDerivationIterations'], d['nDerivationMethod'])
				if res == 0:
					logging.error("Unsupported derivation method")
					sys.exit(1)
				masterkey = crypter.Decrypt(d['encrypted_key'])
				crypter.SetKey(masterkey)

		else:
			json_db[type] = 'unsupported'
			print "Wallet data not recognized: "+str(d)

	list_of_reserve_not_in_pool=[]
	parse_wallet(db, item_callback)


	nkeys = len(json_db['keys'])
	i = 0
	for k in json_db['keys']:
		i+=1
		addr = k['addr']
		if include_balance:
#			print("%3d/%d  %s  %s" % (i, nkeys, k["addr"], k["balance"]))
			k["balance"] = balance(balance_site, k["addr"])
#			print("  %s" % (i, nkeys, k["addr"], k["balance"]))

		if addr in json_db['names'].keys():
			k["label"] = json_db['names'][addr]
			k["reserve"] = 0
		else:
			k["reserve"] = 1
			list_of_reserve_not_in_pool.append(k['pubkey'])


	def rnip_callback(a):
		list_of_reserve_not_in_pool.remove(a['public_key_hex'])

	if FillPool:
		map(rnip_callback, json_db['pool'])

		cpt=1
		for p in list_of_reserve_not_in_pool:
			update_wallet(db, 'pool', { 'public_key' : p.decode('hex'), 'n' : cpt, 'nTime' : ts(), 'nVersion':80100 })
			cpt+=1



	db.close()

	crypted = 'salt' in json_db['mkey']

	if not crypted:
		print "The wallet is not encrypted"

	if crypted and not passphrase:
		print "The wallet is encrypted but no passphrase is used"

	if crypted and passphrase:
		check = True
		ppcorrect=True
		for k in json_db['keys']:
		  if 'encrypted_privkey' in k:
			ckey = k['encrypted_privkey'].decode('hex')
			public_key = k['pubkey'].decode('hex')
			crypter.SetIV(Hash(public_key))
			secret = crypter.Decrypt(ckey)
			compressed = public_key[0] != '\04'


			if check:
				check = False
				pkey = EC_KEY(int('0x' + secret.encode('hex'), 16))
				if public_key != GetPubKey(pkey, compressed):
					print "The wallet is encrypted and the passphrase is incorrect"
					ppcorrect=False
					break

			sec = SecretToASecret(secret, compressed)
			k['sec'] = sec
			k['hexsec'] = secret[:32].encode('hex')
			k['secret'] = secret.encode('hex')
			k['compressed'] = compressed
			addr_to_keys[k['addr']]=[sec, k['pubkey']]
#			del(k['ckey'])
#			del(k['secret'])
#			del(k['pubkey'])
			private_keys.append(sec)
		if ppcorrect:
			print "The wallet is encrypted and the passphrase is correct"

	for k in json_db['keys']:
		if k['compressed'] and 'secret' in k:
			k['secret']+="01"

#	del(json_db['pool'])
#	del(json_db['names'])
	if vers > -1:
		addrtype = oldaddrtype

	return {'crypted':crypted}



def importprivkey(db, sec, label, reserve, keyishex, verbose=True, addrv=addrtype):
	if keyishex is None:
		pkey = regenerate_key(sec)
		compressed = is_compressed(sec)
	elif len(sec) == 64:
		pkey = EC_KEY(str_to_long(sec.decode('hex')))
		compressed = False
	elif len(sec) == 66:
		pkey = EC_KEY(str_to_long(sec[:-2].decode('hex')))
		compressed = True
	else:
		print("Hexadecimal private keys must be 64 or 66 characters long (specified one is "+str(len(sec))+" characters long)")
		return False

	if not pkey:
		return False

	secret = GetSecret(pkey)
	private_key = GetPrivKey(pkey, compressed)
	public_key = GetPubKey(pkey, compressed)
	addr = public_key_to_bc_address(public_key, addrv)

	if verbose:
		print "Address (%s): %s"%(aversions[addrv], addr)
		print "Privkey (%s): %s"%(aversions[addrv], SecretToASecret(secret, compressed))
		print "Hexprivkey: %s"%(secret.encode('hex'))
		print "Hash160: %s"%(bc_address_to_hash_160(addr).encode('hex'))
		if not compressed:
			print "Pubkey: 04%.64x%.64x"%(pkey.pubkey.point.x(), pkey.pubkey.point.y())
		else:
			print "Pubkey: 0%d%.64x"%(2+(pkey.pubkey.point.y()&1), pkey.pubkey.point.x())
		if int(secret.encode('hex'), 16)>_r:
			print 'Beware, 0x%s is equivalent to 0x%.33x</b>'%(secret.encode('hex'), int(secret.encode('hex'), 16)-_r)



	global crypter, passphrase, json_db
	crypted = False
	if 'mkey' in json_db.keys() and 'salt' in json_db['mkey']:
		crypted = True
	if crypted:
		if passphrase:
			cry_master = json_db['mkey']['encrypted_key'].decode('hex')
			cry_salt   = json_db['mkey']['salt'].decode('hex')
			cry_rounds = json_db['mkey']['nDerivationIterations']
			cry_method = json_db['mkey']['nDerivationMethod']

			crypter.SetKeyFromPassphrase(passphrase, cry_salt, cry_rounds, cry_method)
#			if verbose:
#				print "Import with", passphrase, "", cry_master.encode('hex'), "", cry_salt.encode('hex')
			masterkey = crypter.Decrypt(cry_master)
			crypter.SetKey(masterkey)
			crypter.SetIV(Hash(public_key))
			e = crypter.Encrypt(secret)
			ck_epk=e

			update_wallet(db, 'ckey', { 'public_key' : public_key, 'encrypted_private_key' : ck_epk })
	else:
		update_wallet(db, 'key', { 'public_key' : public_key, 'private_key' : private_key })

	if not reserve:
		update_wallet(db, 'name', { 'hash' : addr, 'name' : label })


	return True

def balance(site, address):
	page=urllib.urlopen("%s=%s" % (site, address))
	json_acc = json.loads(page.read().split("<end>")[0])
	if json_acc['0'] == 0:
		return "Invalid address"
	elif json_acc['0'] == 2:
		return "Never used"
	else:
		return json_acc['balance']

def read_jsonfile(filename):
	filin = open(filename, 'r')
	txdump = filin.read()
	filin.close()
	return json.loads(txdump)

def write_jsonfile(filename, array):
	filout = open(filename, 'w')
	filout.write(json.dumps(array, sort_keys=True, indent=0))
	filout.close()

def keyinfo(sec, keyishex):
	if keyishex is None:
		pkey = regenerate_key(sec)
		compressed = is_compressed(sec)
	elif len(sec) == 64:
		pkey = EC_KEY(str_to_long(sec.decode('hex')))
		compressed = False
	elif len(sec) == 66:
		pkey = EC_KEY(str_to_long(sec[:-2].decode('hex')))
		compressed = True
	else:
		print("Hexadecimal private keys must be 64 or 66 characters long (specified one is "+str(len(sec))+" characters long)")
		exit(0)

	if not pkey:
		return False

	secret = GetSecret(pkey)
	private_key = GetPrivKey(pkey, compressed)
	public_key = GetPubKey(pkey, compressed)
	addr = public_key_to_bc_address(public_key)

	print "Address (%s): %s" % ( aversions[addrtype], addr )
	print "Privkey (%s): %s" % ( aversions[addrtype], SecretToASecret(secret, compressed) )
	print "Hexprivkey:   %s" % secret.encode('hex')
	print "Hash160:      %s"%(bc_address_to_hash_160(addr).encode('hex'))

	return True

def css_wui():
	return """html, body {
  height: 100%;
  width: 100%;
  padding: 0;
  margin: 0;
}

body {
	margin: 0px;
	padding: 0px;
	background: url(data:image/jpeg;base64,/9j/4QAYRXhpZgAASUkqAAgAAAAAAAAAAAAAAP/sABFEdWNreQABAAQAAABLAAD/4QMpaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLwA8P3hwYWNrZXQgYmVnaW49Iu+7vyIgaWQ9Ilc1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCI/PiA8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJBZG9iZSBYTVAgQ29yZSA1LjAtYzA2MSA2NC4xNDA5NDksIDIwMTAvMTIvMDctMTA6NTc6MDEgICAgICAgICI+IDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+IDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCBDUzUgV2luZG93cyIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDozRjJGNUI0ODZBN0YxMUUyQkZGRUNDQzgwNjYxQkJENCIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDozRjJGNUI0OTZBN0YxMUUyQkZGRUNDQzgwNjYxQkJENCI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOjNGMkY1QjQ2NkE3RjExRTJCRkZFQ0NDODA2NjFCQkQ0IiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOjNGMkY1QjQ3NkE3RjExRTJCRkZFQ0NDODA2NjFCQkQ0Ii8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+/+4ADkFkb2JlAGTAAAAAAf/bAIQAAwICAgICAwICAwUDAwMFBQQDAwQF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%3D%3D) repeat;
	font-family: 'Open Sans', sans-serif;
	font-size: 10pt;
	color: #B0B0B0;
}


h1, h2, h3 {
	margin: 0;
	padding: 0;
}

h2
{
	font-weight: 400;
	font-family: 'Archivo Narrow', sans-serif;
	font-size: 2.50em;
}

p, ol, ul {
	margin-top: 0px;
}

p {
	line-height: 180%;
}

strong {
}

a {
	color: #1492C4;
}

a:hover {
	text-decoration: none;
}

a img {
	border: none;
}

img.border {
	border: 10px solid rgba(255,255,255,.10);
}

img.alignleft {
	float: left;
	margin-right: 30px;
}

img.alignright {
	float: right;
}

img.aligncenter {
	margin: 0px auto;
}

hr {
	display: none;
}

#retour-pyw{
 overflow: auto;
}

#uptodate{
	position:absolute;
	top:0px;
	right:0px;
	background: rgba(0,0,0,0.70);
	padding:10px;
}

#full-screen-background-image {
  z-index: -999;
  min-height: 100%;
  min-width: 1024px;
  width: 100%;
  height: auto;
  position: fixed;
  top: 0;
  left: 0;
}

#wrapper {
  position: relative;
  width: 100%;
  min-height: 400px;
  #margin: 30px auto;
	margin-top:10px;  #decalage p/r haut
}

#wrapper {
	overflow: hidden;
}

.container {
	width: 1000px;
	margin: 0px auto;
}

.clearfix {
	clear: both;
}

/** HEADER */

#header-wrapper-title
{
	overflow: hidden;
	height: 80px;
	margin-bottom: 10px;
	background: rgba(0,0,0,0);
}

#header-wrapper
{
	overflow: hidden;
	height: 50px;
	margin-bottom: 20px;
	background: rgba(0,0,0,0.70);
}

#header {
	overflow: hidden;
}

/** LOGO */

#logo {
	float: left;
	#width: 300px;
	height: 50px;

}

#logo h1, #logo p {
	margin: 0px;
	line-height: normal;
}

#logo h1 a {
	padding-left: 00px;
	text-decoration: none;
	font-size: 2.50em;
	font-weight: 400;
	font-family: 'Archivo Narrow', sans-serif;
	color: #FFFFFF;
}

/** MENU */

#menu {
	float: left;
	height: 50px;
}

#menu ul {
	margin: 0px;
	padding: 0px;
	list-style: none;
	line-height: normal;
}

#menu li {
	float: left;
	margin-right: 10px;
	padding: 0px 5px 0px 5px;
}

#menu a {
	display: block;
	height: 50px;
	padding: 0px 10px;
	line-height: 50px;
	text-decoration: none;
	text-transform: uppercase;
	color: #FFFFFF;
}

#menu a:hover {
	text-decoration: none;
	background: rgba(0,0,0,0.70);
}

#menu .active
{
	background: rgba(0,0,0,0.70);
}

/** PAGE */

#page {
	overflow: hidden;
	margin-bottom: 20px;
}

/** CONTENT */

#content {
	float: left;
	width: 950px;
	padding: 40px;
	background: rgba(0,0,0,0.70);
}

#content h2 a
{
	display: block;
	padding: 0px 0px 20px 0px;
	text-decoration: none;
	color: #FFFFFF;
}

#content #box1
{
	margin-bottom: 0px;
}

/** SIDEBAR */

#sidebar {
	float: right;
	width: 350px;
	padding: 20px;
	background: rgba(0,0,0,0.70);
}

#sidebar h2
{
	padding: 0px 0px 00px 0px;
	color: #FFFFFF;
}

/* Footer */

#footer {
	overflow: hidden;
	margin: 00px auto 0px auto;
	padding: 10px 0px;
	background: rgba(0,0,0,0.70);
}

#footer p {
	text-align: center;
	font-size: 12px;
}

#footer a {
}

/** LIST STYLE 1 */

ul.style1 {
	margin: 0px;
	padding: 10px 0px 0px 0px;
	list-style: none;
}

ul.style1 li {
	clear: both;
	margin-bottom: 25px;
	padding: 30px 0px 40px 0px;
	border-top: 1px solid #000000;
	box-shadow: inset 0 1px 0 rgba(255,255,255,.10);
}

ul.style1 h3 {
	padding-bottom: 5px;
	font-size: 14px;
	color: #FFFFFF;
}

ul.style1 p {
	line-height: 150%;
}

ul.style1 .button-style {
	float: left;
	margin-top: 0px;
}

ul.style1 .first {
	padding-top: 0px;
	border-top: none;
	box-shadow: none;
}

/** LIST STYLE 3 */

ul.style3 {
	margin: 0px;
	padding: 0px;
	list-style: none;
}

ul.style3 li {
	padding: 10px 0px 10px 0px;
	border-top: 1px solid #000000;
	box-shadow: inset 0 1px 0 rgba(255,255,255,.10);
}

ul.style3 a {
	text-decoration: none;
	color: #949494;
}

ul.style3 a:hover {
	text-decoration: underline;
}

ul.style3 .first {
	padding-top: 0px;
	border-top: none;
	box-shadow: none;
}

ul.style3 .date {
	width: 87px;
	background-color: #1F768D;
	margin-top: 20px;
	height: 24px;
	line-height: 24px;
	text-align: center;
	font-size: 12px;
	color: #FFFFFF;
}

ul.style3 .first .date
{
	margin-top: 0px;
}

.button-style
{
	display: inline-block;
	background-color: #1F768D;
	margin-top: 0px;
	padding: 5px 30px;
	height: 24px;
	line-height: 24px;
	text-decoration: none;
	text-align: center;
	color: #FFFFFF;
}

.button-style-red
{
	color: #ffffff;
	display: inline-block;
	background-color: #a12323;
	margin-top: 20px;
	padding: 5px 30px;
	height: 24px;
	line-height: 24px;
	text-decoration: none;
	text-align: center;
}

.entry
{
	margin-bottom: 30px;
}
"""

def onclick_on_tab(page):
	list=['DumpPage','ImportPage','DeletePage','InfoPage','AboutPage','PassphrasePage','TxPage']
	r=''
	for p in list:
		if p!=page:
			r+="document.getElementById('"+p+"').style.display='none';"
			r+="document.getElementById('"+p+"Button').className='';"
	r+="document.getElementById('"+page+"').style.display='block';"
	r+="document.getElementById('"+page+"Button').className='active';"
	return r

def html_wui(listcontent,uptodate_text):
	global pywversion
	return """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Pywallet Web Interface - Pywallet """+pywversion+"""</title>
<!--link href='http://fonts.googleapis.com/css?family=Archivo+Narrow:400,700|Open+Sans:400,600,700' rel='stylesheet' type='text/css'-->
<!--link href="default.css" rel="stylesheet" type="text/css" media="all" /-->
<style type="text/css">
@font-face {
  font-family: 'Archivo Narrow';
  font-style: normal;
  font-weight: 400;
  src: local('Archivo Narrow Regular'), local('ArchivoNarrow-Regular'), url('data:application/x-font-woff;base64,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') format('woff');
}
@font-face {
  font-family: 'Archivo Narrow';
  font-style: normal;
  font-weight: 700;
  src: local('Archivo Narrow Bold'), local('ArchivoNarrow-Bold'), url('data:application/x-font-woff;base64,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') format('woff');
}
@font-face {
  font-family: 'Open Sans';
  font-style: normal;
  font-weight: 400;
  src: local('Open Sans'), local('OpenSans'), url('data:application/x-font-woff;base64,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') format('woff');
}
@font-face {
  font-family: 'Open Sans';
  font-style: normal;
  font-weight: 600;
  src: local('Open Sans Semibold'), local('OpenSans-Semibold'), url('data:application/x-font-woff;base64,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') format('woff');
}
@font-face {
  font-family: 'Open Sans';
  font-style: normal;
  font-weight: 700;
  src: local('Open Sans Bold'), local('OpenSans-Bold'), url('data:application/x-font-woff;base64,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') format('woff');
}

"""+css_wui()+"""
</style>
</head>
<body>
<div id="wrapper">
	<div id="header-wrapper-title">
		<div id="header" class="container">
			<div id="logo" style="height: 150px;">
				<h1><a href="#">Pywallet """+str(pywversion)+"""</a></h1>
			</div>
		</div>
	</div>
	<div id="header-wrapper">
			<div style="width:300px;float: left;">&nbsp;</div>
			<div id="menu">
				<ul>
					<li id="DumpPageButton" class="active"><a href="#" accesskey="1" title="" onclick=" """+onclick_on_tab('DumpPage')+""" " >Dump</a></li>
					<li id="ImportPageButton"><a href="#" accesskey="2" title="" onclick=" """+onclick_on_tab('ImportPage')+""" " >Import</a></li>
					<li id="InfoPageButton"><a href="#" accesskey="3" title="" onclick=" """+onclick_on_tab('InfoPage')+""" " >Info</a></li>
					<li id="DeletePageButton"><a href="#" accesskey="4" title="" onclick=" """+onclick_on_tab('DeletePage')+""" " >Delete</a></li>
					<li id="PassphrasePageButton"><a href="#" accesskey="5" title="" onclick=" """+onclick_on_tab('PassphrasePage')+""" " >Passphrase</a></li>
					<li id="TxPageButton"><a href="#" accesskey="6" title="" onclick=" """+onclick_on_tab('TxPage')+""" " >Transaction</a></li>
					<li id="AboutPageButton"><a href="#" accesskey="7" title="" onclick=" """+onclick_on_tab('AboutPage')+""" " >About</a></li>
					<li id="QuitPageButton"><a href="quit">Stop</a></li>
				</ul>
			</div>
	</div>
	<div id="page" class="container">
		<div id="content">
			"""+listcontent+"""
		</div>
		<div id="sidebar" style="display:none;">
			<a href="#" class="button-style-red" style="float:right;position:relative;top:-15px;" onclick="document.getElementById('content').style.width='950px';document.getElementById('content').style.display='block';document.getElementById('sidebar').style.display='none';document.getElementById('sidebar').style.width='350px';">Close</a>
			<a href="#" class="button-style" style="float:right;position:relative;top:5px;left:-10px;" onclick="
			if(document.getElementById('content').style.display=='none'){
				document.getElementById('sidebar').style.width='350px';
				document.getElementById('content').style.width='500px';
				document.getElementById('content').style.display='block';
				this.innerHTML='Full page';
			}else{
				document.getElementById('sidebar').style.width='970px';
				document.getElementById('content').style.display='none';
				this.innerHTML='Reduce';
			}
			document.getElementById('sidebar').style.display='block';
			">Full page</a>
			<h2 style="positive:relative;top:-20px;">Data</h2>
			<br />
			<br />
			<p id="retour-pyw">
			</p>
		</div>
	</div>
	<div id="footer">
		<p><a href="http://pywallet.tk">Instructions to use Pywallet</a></p>
	</div>
</div>
<div id="uptodate">"""+uptodate_text+"""</div>
</body>
</html>
"""

def WI_FormInit(title, action, divname):
	return "<li><h3>%s</h3>"%title
	return '<style>#h'+divname+':hover{color:red;}</style><h3 id="h'+divname+'" onClick="document.getElementById(\''+divname+'\').style.display=(document.getElementById(\''+divname+'\').style.display==\'none\')?\'block\':\'none\';document.getElementById(\'iconOF_'+divname+'\').innerHTML=image_showdiv(\''+divname+'\');"><span style="width:21px;" id="iconOF_'+divname+'"><img src="http://creation-entreprise.comprendrechoisir.com/img/puce_tab_down.png" /></span>&nbsp;&nbsp;'+title+'</h3><div id="'+divname+'"><form style="margin-left:15px;" action="'+action+'" method=get>'

def WI_InputText(label, name, id, value, size=30):
	return '%s<input type=text name="%s" id="%s" value="%s" size=%s /><br />'%(label, name, id, value, size)

def WI_InputPassword(label, name, id, value, size=30):
	return '%s<input type=password name="%s" id="%s" value="%s" size=%s /><br />'%(label, name, id, value, size)

def WI_Submit(value, local_block, local_button, function):
	return """<br /><a href="#" class="button-style"  onClick="document.getElementById('content').style.width='500px';document.getElementById('sidebar').style.display='block';%s();return false;">%s</a>"""%(function,value)

def WI_CloseButton(local_block, local_button):
	return '<input type=button value="Close" onClick="document.getElementById(\'%s\').style.display=\'none\';document.getElementById(\'%s\').style.display=\'none\';" id="%s" style="display:none;" />'%(local_block, local_button, local_button)

def WI_ReturnDiv(local_block):
	return '<div id="%s" style="display:none;margin:10px 3%% 10px;padding:10px;overflow:auto;width:90%%;max-height:600px;background-color:#fff8dd;"></div>'%(local_block)

def WI_FormEnd():
	return "</li>"

def WI_RadioButton(name, value, id, checked, label):
	return '&nbsp;&nbsp;&nbsp;<input type="radio" name="%s" value="%s" id="%s" %s >%s<br>'%(name, value, id, checked, label)

def WI_Checkbox(name, value, id, other, label):
	return '<input type="checkbox" name="%s" value="%s" id="%s" %s />%s'%(name, value, id, other, label)

def WI_Endiv(t,name,title, desc,hidden=False):
	return '<div id="'+name+'" style="display:'+X_if_else('none',hidden,'block')+';"><div id="box1"><h2 class="title"><a href="#">'+title+'</a></h2>'+X_if_else('<p>'+desc+'</p>',desc!='','')+'</div><div ><ul class="style1">'+t+'</ul></div></div>'

def WI_AjaxFunction(name, command_when_ready, query_string, command_until_ready):
	return '\n\
function ajax%s(){\n\
	var ajaxRequest;\n\
	try{\n\
		ajaxRequest = new XMLHttpRequest();\n\
	} catch (e){\n\
		try{\n\
			ajaxRequest = new ActiveXObject("Msxml2.XMLHTTP");\n\
		} catch (e) {\n\
			try{\n\
				ajaxRequest = new ActiveXObject("Microsoft.XMLHTTP");\n\
			} catch (e){\n\
				alert("Your browser broke!");\n\
				return false;\n\
			}\n\
		}\n\
	}\n\
	ajaxRequest.onreadystatechange = function(){\n\
		if(ajaxRequest.readyState == 4){\n\
			%s\n\
		}\n\
	};\n\
	var queryString = %s;\n\
	ajaxRequest.open("GET", queryString, true);\n\
	%s\n\
	ajaxRequest.send(null);\n\
}\n\
\n\
'%(name, command_when_ready, query_string, command_until_ready)

def X_if_else(iftrue, cond, iffalse):
	if cond:
		return iftrue
	return iffalse

def export_all_keys(db, ks, filename):
	txt=";".join(ks)+"\n"
	for i in db['keys']:
	  try:
		j=i.copy()
		if 'label' not in j:
			j['label']='#Reserve'
		t=";".join([str(j[k]) for k in ks])
		txt+=t+"\n"
	  except:
		return False

	try:
		myFile = open(filename, 'w')
		myFile.write(txt)
		myFile.close()
		return True
	except:
		return False

def import_csv_keys(filename, wdir, wname, nbremax=9999999):
	global global_merging_message
	if filename[0]=="\x00":    #yeah, dirty workaround
		content=filename[1:]
	else:
		filen = open(filename, "r")
		content = filen.read()
		filen.close()

	db_env = create_env(wdir)
	read_wallet(json_db, db_env, wname, True, True, "", None)
	db = open_wallet(db_env, wname, writable=True)

	content=content.split('\n')
	content=content[:min(nbremax, len(content))]
	for i in range(len(content)):
	  c=content[i]
	  global_merging_message = ["Merging: "+str(round(100.0*(i+1)/len(content),1))+"%" for j in range(2)]
	  if ';' in c and len(c)>0 and c[0]!="#":
		cs=c.split(';')
		sec,label=cs[0:2]
		v=addrtype
		if len(cs)>2:
			v=int(cs[2])
		reserve=False
		if label=="#Reserve":
			reserve=True
		keyishex=None
		if abs(len(sec)-65)==1:
			keyishex=True
		importprivkey(db, sec, label, reserve, keyishex, verbose=False, addrv=v)

	global_merging_message = ["Merging done.", ""]

	db.close()

	read_wallet(json_db, db_env, wname, True, True, "", None, -1, True)  #Fill the pool if empty

	return True

def dep_text_aboutpage(val):
	if val:
		return "<span style='color:#bb0000;'>Not found</span>"
	else:
		return "<span style='color:#00bb00;'>Found</span>"

CTX_adds=''

if 'twisted' not in missing_dep:
	class WIRoot(resource.Resource):

		 def render_GET(self, request):
				try:
					request.args['update'][0]
					return update_pyw()
				except:
					True

				uptodate=md5_last_pywallet[1]==md5_pywallet
				checking_finished=bool(md5_last_pywallet[0])

				color="#DDDDFF"
				if checking_finished:
					if uptodate:
						color="#DDFFDD"
					else:
						color="#FFDDDD"

				check_version_text = \
 X_if_else(
	X_if_else(
		'Pywallet is up-to-date',
		uptodate,
		'Pywallet is <span style="color:red;font-weight:none;">not</span> up-to-date<br /><a href="#" onclick="ajaxUpdatePyw();return false;">Click to update</a>'),
	checking_finished,
	'Checking version...'
 )

				if beta_version:
					check_version_text="You are using a beta version<br />Thank you for your help"
					color="#DDDDDD"

				global pywversion
				header = '<h1 title="'+pyw_filename+' in '+pyw_path+'">Pywallet Web Interface v'+pywversion+'</h1><h3>CLOSE BITCOIN BEFORE USE!</h3><div style="position:fixed;top:5px;right:5px;border:solid 1px black;padding:15px;background-color:'+color+';font-weight:bold;text-align:center;">' + check_version_text + '</div><br /><br />'

				CPPForm = WI_FormInit('Change passphrase:', 'ChangePP', 'divformcpp') + \
							WI_InputPassword('', 'pp', 'cppf-pp', '') + \
							WI_Submit('Change', 'CPPDiv', 'cppf-close', 'ajaxCPP') + \
							WI_CloseButton('CPPDiv', 'cppf-close') + \
							WI_ReturnDiv('CPPDiv') + \
							WI_FormEnd()

				DWForm = WI_FormInit('Dump your wallet:', 'DumpWallet', 'divformdw') + \
							WI_InputText('Wallet Directory: ', 'dir', 'dwf-dir', determine_db_dir()) + \
							WI_InputText('Wallet Filename: ', 'name', 'dwf-name', determine_db_name(), 20) + \
							WI_InputText('<span style="border: 0 dashed;border-bottom-width:1px;" title="0 for Bitcoin, 52 for Namecoin, 111 for testnets">Version</span>:', 'vers', 'dwf-vers', '0', 1) + \
							WI_Checkbox('bal', 'y', 'dwf-bal', '', ' Dump with balance (can take minutes)') + "<br />" + \
							WI_Submit('Dump wallet', 'DWDiv', 'dwf-close', 'ajaxDW') + \
							WI_CloseButton('DWDiv', 'dwf-close') + \
							WI_ReturnDiv('DWDiv') + \
							WI_FormEnd()

				MWForm = WI_FormInit('Merge two wallets:', 'MergeWallets', 'divformmw') + \
							WI_InputText('Wallet 1 Directory: ', 'dir1', 'mwf-dir1', determine_db_dir()) + \
							WI_InputText('Wallet 1 Filename: ', 'name1', 'mwf-name1', determine_db_name(), 20) + \
							WI_InputPassword('<span style="border: 0 dashed;border-bottom-width:1px;" title="empty if none">Wallet 1 Passphrase: </span>', 'pass1', 'mwf-pass1', '') + "<br />" + \
							WI_InputText('Wallet 2 Directory: ', 'dir2', 'mwf-dir2', determine_db_dir()) + \
							WI_InputText('Wallet 2 Filename: ', 'name2', 'mwf-name2', "", 20) + \
							WI_InputPassword('<span style="border: 0 dashed;border-bottom-width:1px;" title="empty if none">Wallet 2 Passphrase: </span>', 'pass2', 'mwf-pass2', '') + "<br />" + \
							WI_InputText('Merged Wallet Directory: ', 'dirm', 'mwf-dirm', determine_db_dir()) + \
							WI_InputText('Merged Wallet Filename: ', 'namem', 'mwf-namem', "", 20) + \
							WI_InputPassword('<span style="border: 0 dashed;border-bottom-width:1px;" title="empty if none">Merged Wallet Passphrase: </span>', 'passm1', 'mwf-passm1', '') + \
							WI_InputPassword('Repeat Wallet Passphrase: ', 'passm2', 'mwf-passm2', '') + \
							WI_Submit('Merge wallets', 'MWDiv', 'mwf-close', 'ajaxMW') + \
							WI_CloseButton('MWDiv', 'mwf-close') + \
							WI_ReturnDiv('MWDiv') + \
							WI_FormEnd()

				DKForm = WI_FormInit('Dump your keys:', 'DumpKeys', 'divformdk') + \
							WI_InputText('Wallet Directory: ', 'dir', 'dkf-dir', determine_db_dir()) + \
							WI_InputText('Wallet Filename: ', 'name', 'dkf-name', determine_db_name(), 20) + \
							WI_InputText('<span style="border: 0 dashed;border-bottom-width:1px;" title="0 for Bitcoin, 52 for Namecoin, 111 for testnets">Version</span>:', 'vers', 'dkf-vers', '0', 1) + \
							WI_InputText('Output file: ', 'file', 'dkf-file', '', 60) + \
							WI_InputText('<span style="border: 0 dashed;border-bottom-width:1px;" title="to be chosen from the ones in wallet dump, separated with \',\', e.g. \'addr,secret\'">Data to print: </span>', 'keys', 'dkf-keys', '') + \
							WI_Checkbox('bal', 'y', 'dkf-bal', '', ' Dump with balance (can take minutes)') + "<br />" + \
							WI_Submit('Dump keys', 'DKDiv', 'dkf-close', 'ajaxDK') + \
							WI_CloseButton('DKDiv', 'dkf-close') + \
							WI_ReturnDiv('DKDiv') + \
							WI_FormEnd()

				IKForm = WI_FormInit('Import keys:', 'ImportKeys', 'divformik') + \
"The CSV file must have the following format: '5PrivateKey;Label'<br />" + \
							WI_InputText('Wallet Directory: ', 'dir', 'ikf-dir', determine_db_dir()) + \
							WI_InputText('Wallet Filename: ', 'name', 'ikf-name', determine_db_name(), 20) + \
							WI_InputText('<span style="border: 0 dashed;border-bottom-width:1px;" title="Format: \'privkey;label\', label=\'#Reserve\' to make the key a pool one">CSV file path</span>: ', 'file', 'ikf-file', '', 60) + \
							WI_Submit('Import keys', 'IKDiv', 'ikf-close', 'ajaxIK') + \
							WI_CloseButton('IKDiv', 'ikf-close') + \
							WI_ReturnDiv('IKDiv') + \
							WI_FormEnd()

				DTxForm = WI_FormInit('Dump your transactions to a file:', 'DumpTx', 'divformdtx') + \
							WI_InputText('Wallet Directory: ', 'dir', 'dt-dir', determine_db_dir()) + \
							WI_InputText('Wallet Filename: ', 'name', 'dt-name', determine_db_name(), 20) + \
							WI_InputText('Output file: ', 'file', 'dt-file', '') + \
							WI_Submit('Dump tx\'s', 'DTxDiv', 'dt-close', 'ajaxDTx') + \
							WI_CloseButton('DTxDiv', 'dt-close') + \
							WI_ReturnDiv('DTxDiv') + \
							WI_FormEnd()

				prehide_ecdsa=""
				posthide_ecdsa=""
				if 'ecdsa' in missing_dep:
					prehide_ecdsa="<span style='display:none;'>"
					posthide_ecdsa="</span>"
				InfoForm = WI_FormInit('Get some info about one key'+X_if_else(' and sign/verify messages', 'ecdsa' not in missing_dep,'')+':', 'Info', 'divforminfo') + \
							WI_InputText('Key: ', 'key', 'if-key', '', 60) + \
							prehide_ecdsa + WI_InputText('Message: ', 'msg', 'if-msg', '', 30) + posthide_ecdsa + \
							prehide_ecdsa + WI_InputText('Signature: ', 'sig', 'if-sig', '', 30) + posthide_ecdsa + \
							prehide_ecdsa + WI_InputText('Pubkey: ', 'pubkey', 'if-pubkey', '', 30) + posthide_ecdsa + \
							WI_InputText('<span style="border: 0 dashed;border-bottom-width:1px;" title="0 for Bitcoin, 52 for Namecoin, 111 for testnets">Version</span>:', 'vers', 'if-vers', '0', 1) + \
							"Format:<br />" + \
							WI_RadioButton('format', 'reg', 'if-reg', 'CHECKED', ' Regular, base 58') + \
							WI_RadioButton('format', 'hex', 'if-hex', '', ' Hexadecimal, 64 characters long') + \
							"You want:<br />" + \
							WI_RadioButton('i-need', '1', 'if-n-info', 'CHECKED', ' Info') + \
							prehide_ecdsa + WI_RadioButton('i-need', '2', 'if-n-sv', '', ' Sign and verify') + posthide_ecdsa +\
							prehide_ecdsa + WI_RadioButton('i-need', '3', 'if-n-both', '', ' Both') + posthide_ecdsa + \
							WI_Submit('Get info', 'InfoDiv', 'if-close', 'ajaxInfo') + \
							WI_CloseButton('InfoDiv', 'if-close') + \
							WI_ReturnDiv('InfoDiv') + \
							WI_FormEnd()


				ImportForm = WI_FormInit('Import a key into your wallet:', 'Import', 'divformimport') + \
							WI_InputText('Wallet Directory: ', 'dir', 'impf-dir', determine_db_dir(), 30) + \
							WI_InputText('Wallet Filename:', 'name', 'impf-name', determine_db_name(), 20) + \
							WI_InputText('Key:', 'key', 'impf-key', '', 65) + \
							WI_InputText('Label:', 'label', 'impf-label', '') + \
							WI_Checkbox('reserve', 'true', 'impf-reserve', 'onClick="document.getElementById(\'impf-label\').disabled=document.getElementById(\'impf-reserve\').checked"', ' Reserve') + "<br />" + \
							WI_InputText('<span style="border: 0 dashed;border-bottom-width:1px;" title="0 for Bitcoin, 52 for Namecoin, 111 for testnets">Version</span>:', 'vers', 'impf-vers', '0', 1) + \
							"Format:<br />" + \
							WI_Checkbox('format', 'hex', 'impf-hex', '', ' Hexadecimal, instead of base58') + "<br />" + \
							WI_Checkbox('format', 'cry', 'impf-cry', 'hidden=true', '<!-- Crypt-->') + \
							WI_Checkbox('format', 'com', 'impf-com', 'hidden=true', '<!--Compressed key-->') + \
							WI_Submit('Import key', 'ImportDiv', 'impf-close', 'ajaxImport') + \
							WI_CloseButton('ImportDiv', 'impf-close') + \
							WI_ReturnDiv('ImportDiv') + \
							WI_FormEnd()
#							WI_RadioButton('format', 'reg', 'impf-reg', 'CHECKED', ' Regular, base 58') + \
#							WI_RadioButton('format', 'hex', 'impf-hex', '', ' Hexadecimal, 64 characters long') + \


				ImportROForm = WI_FormInit('Import a read-only address (encrypted wallets only):', 'Import', 'divformimportro') + \
							WI_InputText('Wallet Directory: ', 'dir', 'irof-dir', determine_db_dir(), 30) + \
							WI_InputText('Wallet Filename:', 'name', 'irof-name', determine_db_name(), 20) + \
							WI_InputText('Public key (starting with 04): ', 'pub', 'irof-pub', '', 40) + \
							WI_InputText('Label: ', 'label', 'irof-label', '') + \
							WI_Submit('Import address', 'ImportDiv', 'irof-close', 'ajaxImportRO') + \
							WI_CloseButton('ImportRODiv', 'irof-close') + \
							WI_ReturnDiv('ImportRODiv') + \
							WI_FormEnd()

				DeleteForm = WI_FormInit('Delete keys from your wallet:', 'Delete', 'divformdelete') + \
							WI_InputText('Wallet Directory: ', 'dir', 'd-dir', determine_db_dir(), 40) + \
							WI_InputText('Wallet Filename:', 'name', 'd-name', determine_db_name()) + \
							WI_InputText('<span style="border: 0 dashed;border-bottom-width:1px;" title="divided by \'-\'">Keys</span>:', 'key', 'd-key', '', 65) + \
							"Type:<br />" + \
							WI_RadioButton('d-type', 'tx', 'd-r-tx', 'CHECKED', ' Transaction (type "all" in "Keys" to delete them all)') + \
							WI_RadioButton('d-type', 'key', 'd-r-key', '', ' Bitcoin address') + \
							WI_Submit('Delete', 'DeleteDiv', 'd-close', 'ajaxDelete') + \
							WI_CloseButton('DeleteDiv', 'd-close') + \
							WI_ReturnDiv('DeleteDiv') + \
							WI_FormEnd()

				ImportTxForm = WI_FormInit('Import a transaction into your wallet:', 'ImportTx', 'divformimporttx') + \
							WI_InputText('Wallet Directory: ', 'dir', 'it-dir', determine_db_dir(), 40) + \
							WI_InputText('Wallet Filename:', 'name', 'it-name', determine_db_name()) + \
							WI_InputText('Txk:', 'key', 'it-txk', '', 65) + \
							WI_InputText('Txv:', 'label', 'it-txv', '', 65) + \
							WI_Submit('Import', 'ImportTxDiv', 'it-close', 'ajaxImportTx') + \
							WI_CloseButton('ImportTxDiv', 'it-close') + \
							WI_ReturnDiv('ImportTxDiv') + \
							WI_FormEnd()

				BalanceForm = WI_FormInit('Print the balance of a Bitcoin address:', 'Balance', 'divformbalance') + \
							WI_InputText('Key:', 'key', 'bf-key', '', 35) + \
							WI_Submit('Get balance', 'BalanceDiv', 'gb-close', 'ajaxBalance') + \
							WI_CloseButton('BalanceDiv', 'gb-close') + \
							WI_ReturnDiv('BalanceDiv') + \
							WI_FormEnd()

				global CTX_adds, addr_to_keys
				CTX_adds2=CTX_adds.split('|')+addr_to_keys.keys()


				CreateTxForm = WI_FormInit('Create transaction', 'CTX', 'divformctx') + \
							X_if_else("Additional addresses used: " + ', '.join(CTX_adds.split('|'))+"<br /><br />",len(CTX_adds)>0,"No additional addresses used<br /><br />") + \
							listtx_txt(CTX_adds) + \
							WI_FormEnd()

				CreateTxForm2 = WI_FormInit('Check addresses funds', 'ListTransactions', 'divformctx') + \
							WI_InputText('<span style="border: 0 dashed;border-bottom-width:1px;" title="Divided by a |">Addresses</span>: ', 'adds', 'ctx-adds', '', 35) + \
							WI_Submit('Check ', '', '', 'ajaxCTx') + \
							WI_FormEnd()

				Misc = ''

				Javascript = '<script language="javascript" type="text/javascript">interv1=0;\
					totalin=0;\
					totalout=0;\
					\
					function majfee(){\
						document.getElementById("tot_in").innerHTML=(totalin)/100000000;\
						document.getElementById("tot_out").innerHTML=(totalout)/100000000;\
						document.getElementById("tot_fee").innerHTML=(totalin-totalout)/100000000;\
					}\
					\
					function image_showdiv(a){\
						if(document.getElementById(a).style.display!="none")r="http://creation-entreprise.comprendrechoisir.com/img/puce_tab_down.png";\
						else{\
						r="http://creation-entreprise.comprendrechoisir.com/img/puce_tab.png";}\
						\
						return "<img src=\'"+r+"\' />";\
						\
					}\
					function get_radio_value(radioform){\
						var rad_val;\
						for (var i=0; i < radioform.length; i++){\
							if (radioform[i].checked){\
								rad_val = radioform[i].value;\
							}\
						}\
						return rad_val;\
					}' + \
				WI_AjaxFunction('UpdatePyw', 'document.getElementById("uptodate").innerHTML = ajaxRequest.responseText;setTimeout(function() {window.location.reload();}, 2000);', '"/?update=1"', 'document.getElementById("uptodate").innerHTML = "Updating...";') + \
				WI_AjaxFunction('CTx', 'document.getElementById("retour-pyw").innerHTML = ajaxRequest.responseText;', '"/ListTransactions?addresses="+document.getElementById("ctx-adds").value', 'document.getElementById("retour-pyw").innerHTML = "Loading...";') + \
				WI_AjaxFunction('CPP', 'document.getElementById("retour-pyw").innerHTML = ajaxRequest.responseText;', '"/ChangePP?pp="+document.getElementById("cppf-pp").value', 'document.getElementById("retour-pyw").innerHTML = "Loading...";') + \
				WI_AjaxFunction('DW', 'document.getElementById("retour-pyw").innerHTML = ajaxRequest.responseText;', '"/DumpWallet?dir="+document.getElementById("dwf-dir").value+"&name="+document.getElementById("dwf-name").value+"&bal="+document.getElementById("dwf-bal").checked+"&version="+document.getElementById("dwf-vers").value', 'document.getElementById("retour-pyw").innerHTML = "Loading...";') + \
				WI_AjaxFunction('MW', 'document.getElementById("retour-pyw").innerHTML = ajaxRequest.responseText;', '"/MergeWallets?dir1="+document.getElementById("mwf-dir1").value+"&name1="+document.getElementById("mwf-name1").value+"&pass1="+encodeURIComponent(document.getElementById("mwf-pass1").value)+"&dir2="+document.getElementById("mwf-dir2").value+"&name2="+document.getElementById("mwf-name2").value+"&pass2="+encodeURIComponent(document.getElementById("mwf-pass2").value)+"&dirm="+document.getElementById("mwf-dirm").value+"&namem="+document.getElementById("mwf-namem").value+"&passm1="+encodeURIComponent(document.getElementById("mwf-passm1").value)+"&passm2="+encodeURIComponent(document.getElementById("mwf-passm2").value)+""', 'document.getElementById("retour-pyw").innerHTML = "Merging wallets... This may take a few minutes.";interv1=setInterval(ajaxUpdateMW,300);') + \
				WI_AjaxFunction('UpdateMW', 'if(ajaxRequest.responseText.length>0){document.getElementById("retour-pyw").innerHTML = ajaxRequest.responseText;}else{clearInterval(interv1);}', '"/Others?action=update_mwdiv"', '') + \
				WI_AjaxFunction('DK', 'document.getElementById("retour-pyw").innerHTML = ajaxRequest.responseText;', '"/DumpWallet?dir="+document.getElementById("dkf-dir").value+"&filetw="+document.getElementById("dkf-file").value+"&keys="+document.getElementById("dkf-keys").value+"&bal="+document.getElementById("dkf-bal").checked+"&name="+document.getElementById("dkf-name").value+"&version="+document.getElementById("dkf-vers").value', 'document.getElementById("retour-pyw").innerHTML = "Loading...";') + \
				WI_AjaxFunction('IK', 'document.getElementById("retour-pyw").innerHTML = ajaxRequest.responseText;', '"/Import?dir="+document.getElementById("ikf-dir").value+"&file="+document.getElementById("ikf-file").value+"&name="+document.getElementById("ikf-name").value', 'document.getElementById("retour-pyw").innerHTML = "Loading...";') + \
				WI_AjaxFunction('DTx', 'document.getElementById("retour-pyw").innerHTML = ajaxRequest.responseText;', '"/DumpTx?dir="+document.getElementById("dt-dir").value+"&name="+document.getElementById("dt-name").value+"&file="+document.getElementById("dt-file").value', 'document.getElementById("retour-pyw").innerHTML = "Loading...";') + \
				WI_AjaxFunction('Info', 'document.getElementById("retour-pyw").innerHTML = ajaxRequest.responseText;', '"/Info?key="+document.getElementById("if-key").value+"&msg="+document.getElementById("if-msg").value+"&pubkey="+document.getElementById("if-pubkey").value+"&sig="+document.getElementById("if-sig").value+"&vers="+document.getElementById("if-vers").value+"&format="+(document.getElementById("if-hex").checked?"hex":"reg")+"&need="+get_radio_value(document.getElementsByName("i-need"))', 'document.getElementById("retour-pyw").innerHTML = "Loading...";') + \
				WI_AjaxFunction('Import', 'document.getElementById("retour-pyw").innerHTML = ajaxRequest.responseText;', '"/Import?dir="+document.getElementById("impf-dir").value+"&name="+document.getElementById("impf-name").value+"&key="+document.getElementById("impf-key").value+"&label="+document.getElementById("impf-label").value+"&vers="+document.getElementById("impf-vers").value+"&com="+document.getElementById("impf-com").checked+"&cry="+document.getElementById("impf-cry").checked+"&format="+document.getElementById("impf-hex").checked+(document.getElementById("impf-reserve").checked?"&reserve=1":"")', 'document.getElementById("retour-pyw").innerHTML = "Loading...";') + \
				WI_AjaxFunction('ImportRO', 'document.getElementById("retour-pyw").innerHTML = ajaxRequest.responseText;', '"/Import?dir="+document.getElementById("irof-dir").value+"&name="+document.getElementById("irof-name").value+"&pub="+document.getElementById("irof-pub").value+"&label="+document.getElementById("irof-label").value', 'document.getElementById("retour-pyw").innerHTML = "Loading...";') + \
				WI_AjaxFunction('Balance', 'document.getElementById("retour-pyw").innerHTML = "Balance of " + document.getElementById("bf-key").value + ": " + ajaxRequest.responseText;', '"/Balance?key="+document.getElementById("bf-key").value', 'document.getElementById("retour-pyw").innerHTML = "Loading...";') + \
				WI_AjaxFunction('Delete', 'document.getElementById("retour-pyw").innerHTML = ajaxRequest.responseText;', '"/Delete?dir="+document.getElementById("d-dir").value+"&name="+document.getElementById("d-name").value+"&keydel="+document.getElementById("d-key").value+"&typedel="+get_radio_value(document.getElementsByName("d-type"))', 'document.getElementById("retour-pyw").innerHTML = "Loading...";') + \
				WI_AjaxFunction('ImportTx', 'document.getElementById("retour-pyw").innerHTML = ajaxRequest.responseText;', '"/ImportTx?dir="+document.getElementById("it-dir").value+"&name="+document.getElementById("it-name").value+"&txk="+document.getElementById("it-txk").value+"&txv="+document.getElementById("it-txv").value', 'document.getElementById("retour-pyw").innerHTML = "Loading...";') + \
				'</script>'

#				WI_AjaxFunction('Import', 'document.getElementById("ImportDiv").innerHTML = ajaxRequest.responseText;', '"/Import?dir="+document.getElementById("impf-dir").value+"&name="+document.getElementById("impf-name").value+"&key="+document.getElementById("impf-key").value+"&label="+document.getElementById("impf-label").value+"&vers="+document.getElementById("impf-vers").value+"&format="+(document.getElementById("impf-hex").checked?"hex":"reg")+(document.getElementById("impf-reserve").checked?"&reserve=1":"")', 'document.getElementById("ImportDiv").innerHTML = "Loading...";') + \


				page = '<html><head><title>Pywallet Web Interface</title></head><body>' + header + Javascript + CPPForm + DWForm + MWForm + DKForm + IKForm + DTxForm + InfoForm + ImportForm + ImportTxForm + DeleteForm + BalanceForm + Misc + '</body></html>'

				AboutPage="\
Pywallet is a tool to manage wallet files, developped by jackjack. <a href='https://bitcointalk.org/index.php?topic=34028'>Support thread</a> is on bitcointalk.<br />\
<br />\
To support pywallet's development or if you think it's worth something, you can send anything you want to 1AQDfx22pKGgXnUZFL1e4UKos3QqvRzNh5.\
\
<br /><br /><br /><br /><b>Dependencies:</b><br />\
				\
				&nbsp;&nbsp;&nbsp;ecdsa: "+dep_text_aboutpage('ecdsa' in missing_dep)+"\
				\
<br /><br /><b>Pywallet path:</b>&nbsp;&nbsp;&nbsp;"+pyw_path+"/"+pyw_filename+"\
				"

				return html_wui(Javascript + \
					WI_Endiv(DWForm+DKForm+DTxForm, 'DumpPage', 'Dump', '') + \
					WI_Endiv(ImportForm+IKForm+MWForm+ImportTxForm+ImportROForm,'ImportPage', 'Import', "Don't forget to close Bitcoin when you modify your wallet", True) + \
					WI_Endiv(DeleteForm,'DeletePage', 'Delete', "Don't forget to close Bitcoin when you modify your wallet", True) + \
					WI_Endiv(CPPForm,'PassphrasePage', 'Change passphrase', '', True) + \
					WI_Endiv(InfoForm+BalanceForm,'InfoPage', 'Info', '', True) + \
					WI_Endiv(CreateTxForm2+CreateTxForm,'TxPage', 'Manage transactions', 'You can here create your own transactions. <br />By default, the unspent transactions from addresses previously dumped are shown, but you can add other addresses to check.<br />You can\'t create a transaction if you didn\'t dump the private keys of each input beforehand.', True) + \
					WI_Endiv(AboutPage,'AboutPage','About','', True)
				,check_version_text
				)


				return page

		 def getChild(self, name, request):
			 if name == '':
				 return self
			 else:
				 if name in VIEWS.keys():
					 return resource.Resource.getChild(self, name, request)
				 else:
					 return WI404()

	class WIDumpWallet(resource.Resource):

		 def render_GET(self, request):
			 try:

					wdir=request.args['dir'][0]
					wname=request.args['name'][0]
					version = int(request.args['version'][0])
					log.msg('Wallet Dir: %s' %(wdir))
					log.msg('Wallet Name: %s' %(wname))

					if not os.path.isfile(wdir+"/"+wname):
						return '%s/%s doesn\'t exist'%(wdir, wname)

					try:
						bal=request.args['bal'][0]=='true'
					except:
						bal=false
					read_wallet(json_db, create_env(wdir), wname, True, True, "", bal, version)

#					print wdir
#					print wname
#					print json_db  #json.dumps(json_db, sort_keys=True, indent=4)

					try:
						kfile=request.args['filetw'][0]
						kkeys=request.args['keys'][0]
#						print kkeys.split(',')
						reteak=export_all_keys(json_db, kkeys.split(','), kfile)
						return 'File'+X_if_else("",reteak," not")+' written'
					except:
						return 'Wallet: %s/%s<br />Dump:<pre>%s</pre>'%(wdir, wname, json.dumps(json_db, sort_keys=True, indent=4))
			 except:
				 log.err()
				 return 'Error in dump page'

			 def render_POST(self, request):
				 return self.render_GET(request)

	class WIDumpTx(resource.Resource):

		 def render_GET(self, request):
			 try:
					wdir=request.args['dir'][0]
					wname=request.args['name'][0]
					jsonfile=request.args['file'][0]
					log.msg('Wallet Dir: %s' %(wdir))
					log.msg('Wallet Name: %s' %(wname))

					if not os.path.isfile(wdir+"/"+wname):
						return '%s/%s doesn\'t exist'%(wdir, wname)
					if os.path.isfile(jsonfile):
						return '%s exists'%(jsonfile)

					read_wallet(json_db, create_env(wdir), wname, True, True, "", None)
					write_jsonfile(jsonfile, json_db['tx'])
					return 'Wallet: %s/%s<br />Transations dumped in %s'%(wdir, wname, jsonfile)
			 except:
				 log.err()
				 return 'Error in dumptx page'

			 def render_POST(self, request):
				 return self.render_GET(request)

	class WIMergeWallets(resource.Resource):

		 def render_GET(self, request):
			 try:
				dir1=request.args['dir1'][0]
				name1=request.args['name1'][0]
				pass1=request.args['pass1'][0]
				dir2=request.args['dir2'][0]
				name2=request.args['name2'][0]
				pass2=request.args['pass2'][0]
				dirm=request.args['dirm'][0]
				namem=request.args['namem'][0]
				passm1=request.args['passm1'][0]
				passm2=request.args['passm2'][0]
				if passm1!=passm2:
					return 'The passphrases for the merged wallet don\'t match. Aborted.'

				r=merge_wallets(dir1, name1, dir2, name2, dirm, namem, pass1, pass2, passm1)
				if r[0]:
					return "Merging in progress..."
				else:
					return r[1]

				return ret
			 except:
				 log.err()
				 return 'Error in mergewallets page'

			 def render_POST(self, request):
				 return self.render_GET(request)

	class WIChangePP(resource.Resource):

		 def render_GET(self, request):
			 try:
				global passphrase
				passphrase=request.args['pp'][0]
				return 'Done'
			 except:
				log.err()
				return 'Error while changing passphrase'

			 def render_POST(self, request):
				 return self.render_GET(request)

	class WIOthers(resource.Resource):

		 def render_GET(self, request):
			 try:
				global passphrase
				global global_merging_message

				action=request.args['action'][0]
				if action=="update_mwdiv":
					ret=global_merging_message[0]
					global_merging_message[0]=global_merging_message[1]
					global_merging_message[1]=""
					return ret
				return 'Done'
			 except:
				log.err()
				return 'Error while WIOthers'

			 def render_POST(self, request):
				 return self.render_GET(request)

	class WIBalance(resource.Resource):

		 def render_GET(self, request):
			 try:
					return "%s"%str(balance(balance_site, request.args['key'][0]).encode('utf-8'))
			 except:
				 log.err()
				 return 'Error in balance page'

			 def render_POST(self, request):
				 return self.render_GET(request)

	class WIDelete(resource.Resource):

		 def render_GET(self, request):
			 try:
					wdir=request.args['dir'][0]
					wname=request.args['name'][0]
					keydel=request.args['keydel'][0]
					typedel=request.args['typedel'][0]
					db_env = create_env(wdir)

					if not os.path.isfile(wdir+"/"+wname):
						return '%s/%s doesn\'t exist'%(wdir, wname)

					deleted_items = delete_from_wallet(db_env, wname, typedel, keydel.split('-'))

					return "%s:%s has been successfully deleted from %s/%s, resulting in %d deleted item%s"%(typedel, keydel, wdir, wname, deleted_items, iais(deleted_items))

			 except:
				 log.err()
				 return 'Error in delete page'

			 def render_POST(self, request):
				 return self.render_GET(request)

def message_to_hash(msg, msgIsHex=False):
	str = ""
#	str += '04%064x%064x'%(pubkey.point.x(), pubkey.point.y())
#	str += "Padding text - "
	str += msg
	if msgIsHex:
		str = str.decode('hex')
	hash = Hash(str)
	return hash

def sign_message(secret, msg, msgIsHex=False):
	k = KEY()
	k.generate(secret)
	return k.sign(message_to_hash(msg, msgIsHex))

def verify_message_signature(pubkey, sign, msg, msgIsHex=False):
	k = KEY()
	k.set_pubkey(pubkey.decode('hex'))
	return k.verify(message_to_hash(msg, msgIsHex), sign.decode('hex'))


OP_DUP = 118;
OP_HASH160 = 169;
OP_EQUALVERIFY = 136;
OP_CHECKSIG = 172;

XOP_DUP = "%02x"%OP_DUP;
XOP_HASH160 = "%02x"%OP_HASH160;
XOP_EQUALVERIFY = "%02x"%OP_EQUALVERIFY;
XOP_CHECKSIG = "%02x"%OP_CHECKSIG;

BTC = 1e8

def ct(l_prevh, l_prevn, l_prevsig, l_prevpubkey, l_value_out, l_pubkey_out, is_msg_to_sign=-1, oldScriptPubkey=""):
	scriptSig = True
	if is_msg_to_sign is not -1:
		scriptSig = False
		index = is_msg_to_sign

	ret = ""
	ret += inverse_str("%08x"%1)
	nvin = len(l_prevh)
	ret += "%02x"%nvin

	for i in range(nvin):
		txin_ret = ""
		txin_ret2 = ""

		txin_ret += inverse_str(l_prevh[i])
		txin_ret += inverse_str("%08x"%l_prevn[i])

		if scriptSig:
			txin_ret2 += "%02x"%(1+len(l_prevsig[i])/2)
			txin_ret2 += l_prevsig[i]
			txin_ret2 += "01"
			txin_ret2 += "%02x"%(len(l_prevpubkey[i])/2)
			txin_ret2 += l_prevpubkey[i]

			txin_ret += "%02x"%(len(txin_ret2)/2)
			txin_ret += txin_ret2

		elif index == i:
			txin_ret += "%02x"%(len(oldScriptPubkey)/2)
			txin_ret += oldScriptPubkey
		else:
			txin_ret += "00"

		ret += txin_ret
		ret += "ffffffff"


	nvout = len(l_value_out)
	ret += "%02x"%nvout
	for i in range(nvout):
		txout_ret = ""

		txout_ret += inverse_str("%016x"%(l_value_out[i]))
		txout_ret += "%02x"%(len(l_pubkey_out[i])/2+5)
		txout_ret += "%02x"%OP_DUP
		txout_ret += "%02x"%OP_HASH160
		txout_ret += "%02x"%(len(l_pubkey_out[i])/2)
		txout_ret += l_pubkey_out[i]
		txout_ret += "%02x"%OP_EQUALVERIFY
		txout_ret += "%02x"%OP_CHECKSIG
		ret += txout_ret

	ret += "00000000"
	if not scriptSig:
		ret += "01000000"
	return ret

def create_transaction(secret_key, hashes_txin, indexes_txin, pubkey_txin, prevScriptPubKey, amounts_txout, scriptPubkey):
	li1 = len(secret_key)
	li2 = len(hashes_txin)
	li3 = len(indexes_txin)
	li4 = len(pubkey_txin)
	li5 = len(prevScriptPubKey)

	if li1 != li2 or li2 != li3 or li3 != li4 or li4 != li5:
		print("Error in the number of tx inputs")
		exit(0)

	lo1 = len(amounts_txout)
	lo2 = len(scriptPubkey)

	if lo1 != lo2:
		print("Error in the number of tx outputs")
		exit(0)

	sig_txin = []
	i=0
	for cpt in hashes_txin:
		sig_txin.append(sign_message(secret_key[i].decode('hex'), ct(hashes_txin, indexes_txin, sig_txin, pubkey_txin, amounts_txout, scriptPubkey, i, prevScriptPubKey[i]), True)+"01")
		i+=1

	tx = ct(hashes_txin, indexes_txin, sig_txin, pubkey_txin, amounts_txout, scriptPubkey)
	hashtx = Hash(tx.decode('hex')).encode('hex')

	for i in range(len(sig_txin)):
		try:
			verify_message_signature(pubkey_txin[i], sig_txin[i][:-2], ct(hashes_txin, indexes_txin, sig_txin, pubkey_txin, amounts_txout, scriptPubkey, i, prevScriptPubKey[i]), True)
			print("sig %2d: verif ok"%i)
		except:
			print("sig %2d: verif error"%i)
			exit(0)

#	tx += end_of_wallettx([], int(time.time()))
#	return [inverse_str(hashtx), "027478" + hashtx, tx]
	return [inverse_str(hashtx), "", tx]

def inverse_str(string):
	ret = ""
	for i in range(len(string)/2):
		ret += string[len(string)-2-2*i];
		ret += string[len(string)-2-2*i+1];
	return ret

def read_table(table, beg, end):
	rows = table.split(beg)
	for i in range(len(rows)):
		rows[i] = rows[i].split(end)[0]
	return rows

def read_blockexplorer_table(table):
	cell = []
	rows = read_table(table, '<tr>', '</tr>')
	for i in range(len(rows)):
		cell.append(read_table(rows[i], '<td>', '</td>'))
		del cell[i][0]
	del cell[0]
	del cell[0]
	return cell

txin_amounts = {}

def bc_address_to_available_tx(address, testnet=False):
	TN=""
	if testnet:
		TN="testnet"

	blockexplorer_url = "http://blockexplorer.com/"+TN+"/address/"
	ret = ""
	txin = []
	txin_no = {}
	global txin_amounts
	txout = []
	balance = 0
	txin_is_used = {}

	page = urllib.urlopen("%s/%s" % (blockexplorer_url, address))
	try:
		table = page.read().split('<table class="txtable">')[1]
		table = table.split("</table>")[0]
	except:
		return {address:[]}

	cell = read_blockexplorer_table(table)

	for i in range(len(cell)):
		txhash = read_table(cell[i][0], '/tx/', '#')[1]
		post_hash = read_table(cell[i][0], '#', '">')[1]
		io = post_hash[0]
		no_tx = post_hash[1:]
		if io in 'i':
			txout.append([txhash, post_hash])
		else:
			txin.append(txhash+no_tx)
			txin_no[txhash+no_tx] = post_hash[1:]
			txin_is_used[txhash+no_tx] = 0

		#hashblock = read_table(cell[i][1], '/block/', '">')[1]
		#blocknumber = read_table(cell[i][1], 'Block ', '</a>')[1]

		txin_amounts[txhash+no_tx] = round(float(cell[i][2]), 8)

#		if cell[i][3][:4] in 'Sent' and io in 'o':
#			print(cell[i][3][:4])
#			print(io)
#			return 'error'
#		if cell[i][3][:4] in 'Rece' and io in 'i':
#			print(cell[i][3][:4])
#			print(io)
#			return 'error'

		balance = round(float(cell[i][5]), 8)


	for tx in txout:
		pagetx = urllib.urlopen("http://blockexplorer.com/"+TN+"/tx/"+tx[0])
		table_in = pagetx.read().split('<a name="outputs">Outputs</a>')[0].split('<table class="txtable">')[1].split("</table>")[0]

		cell = read_blockexplorer_table(table_in)
		for i in range(len(cell)):
			txhash = read_table(cell[i][0], '/tx/', '#')[1]
			no_tx = read_table(cell[i][0], '#', '">')[1][1:]

			if txhash+no_tx in txin:
				txin_is_used[txhash+no_tx] = 1

	ret = []
	for tx in txin:
		if not txin_is_used[tx]:
			ret.append([tx,txin_amounts[tx],txin_no[tx]])

	return {address : ret}

def write_avtx(list_avtx, testnet=False):
	TN=""
	if testnet:
		TN="testnet"
	gret = "<table border=1>"
	for add in list_avtx:
		notnull = False
		try:
			hexsec = " -> " + bc_address_to_sec[add]
		except:
			hexsec = ""
		ret = '<tr><td colspan=3 align="center" rowspan=1><a href="http://blockexplorer.com/'+TN+'/address/' +add + '">' + add + "</a>" + hexsec + '</td></tr>'
		a = list_avtx[add]
		for array in a:
			notnull = True
			no_tx = array[0][64:]
			array[0] = array[0][:64]
			link = "http://blockexplorer.com/"+TN+"/rawtx/"+array[0]
			pagetx = urllib.urlopen(link)
			ScriptPubkey = str(json.loads(pagetx.read())['out'][int(array[2])]['scriptPubKey'])
#			ret += '<a href="http://blockexplorer.com/tx/' +array[0] + '">' + array[0] + "#" + no_tx + "</a>: " + str(array[1]) + " & " + ScriptPubkey + "<br />"
			ret += '<tr><td><a href="http://blockexplorer.com/'+TN+'/tx/' +array[0] + '#' + no_tx + '">' + array[0] + "</a></td><td>" + str(array[1]) + "</td><td>" + ScriptPubkey + "</td></tr>"
		ret+="<tr><td colspan=3></td></tr>"
#		ret += "<br />" + "<br />"
		if notnull is False:
			ret = ""
		gret += ret
	gret=gret[:-len("<tr><td colspan=3></td></tr>")]

	return gret+"</table>"

ct_txin = []
ct_txout = []


empty_txin={'hash':'', 'index':'', 'sig':'##', 'pubkey':'', 'oldscript':'', 'addr':''}
empty_txout={'amount':'', 'script':''}

class tx():
	ins=[]
	outs=[]
	tosign=False

	def hashtypeone(index,script):
		global empty_txin
		for i in range(len(ins)):
			self.ins[i]=empty_txin
		self.ins[index]['pubkey']=""
		self.ins[index]['oldscript']=s
		self.tosign=True

	def copy():
		r=tx()
		r.ins=self.ins[:]
		r.outs=self.outs[:]
		return r

	def sign(n=-1):
		if n==-1:
			for i in range(len(ins)):
				self.sign(i)
				return "done"

		global json_db
		txcopy=self.copy()
		txcopy.hashtypeone(i, self.ins[n]['oldscript'])

		sec=''
		for k in json_db['keys']:
		  if k['addr']==self.ins[n]['addr'] and 'hexsec' in k:
			sec=k['hexsec']
		if sec=='':
			print "priv key not found (addr:"+self.ins[n]['addr']+")"
			return ""

		self.ins[n]['sig']=sign_message(sec.decode('hex'), txcopy.get_tx(), True)

	def ser():
		r={}
		r['ins']=self.ins
		r['outs']=self.outs
		r['tosign']=self.tosign
		return json.dumps(r)

	def unser(r):
		s=json.loads(r)
		self.ins=s['ins']
		self.outs=s['outs']
		self.tosign=s['tosign']

	def get_tx():
		r=''
		ret += inverse_str("%08x"%1)
		ret += "%02x"%len(self.ins)

		for i in range(len(self.ins)):
			txin=self.ins[i]
			ret += inverse_str(txin['hash'])
			ret += inverse_str("%08x"%txin['index'])

			if txin['pubkey']!="":
				tmp += "%02x"%(1+len(txin['sig'])/2)
				tmp += txin['sig']
				tmp += "01"
				tmp += "%02x"%(len(txin['pubkey'])/2)
				tmp += txin['pubkey']

				ret += "%02x"%(len(tmp)/2)
				ret += tmp

			elif txin['oldscript']!="":
				ret += "%02x"%(len(txin['oldscript'])/2)
				ret += txin['oldscript']

			else:
				ret += "00"

			ret += "ffffffff"

		ret += "%02x"%len(self.outs)

		for i in range(len(self.outs)):
			txout=self.outs[i]
			ret += inverse_str("%016x"%(txout['amount']))

			if txout['script'][:2]=='s:':  #script
				script=txout['script'][:2]
				ret += "%02x"%(len(script)/2)
				ret += script
			else:                         #address
				ret += "%02x"%(len(txout['script'])/2+5)
				ret += "%02x"%OP_DUP
				ret += "%02x"%OP_HASH160
				ret += "%02x"%(len(txout['script'])/2)
				ret += txout['script']
				ret += "%02x"%OP_EQUALVERIFY
				ret += "%02x"%OP_CHECKSIG

		ret += "00000000"
		if not self.tosign:
			ret += "01000000"
		return ret


def listtx_txt(adds):
			untx_site="http://blockchain.info/unspent?active="
			ret=''
			table="""<form action='CT' method=post><table border=1>"""
			utx=untx_site+adds
			try:
				utxs=json.loads(urllib.urlopen(utx).read())["unspent_outputs"]
			except:
				return "No inputs"

			table+="<tr>\
					<td>Use</td>\
					<td>Tx hash</td>\
					<td>Script</td>\
					<td>Amount</td>\
				</tr>"
			for tx in utxs:
				txhash=str(tx["tx_hash"]).decode('hex')[::-1].encode('hex')
				txn=int(tx["tx_output_n"])
				txscript=str(tx["script"])
				txvalue=int(tx["value"])
				table+="<tr>"
				table+="<td>\
							<input type=checkbox onchange='totalin+=(this.checked?1:-1)*"+str(txvalue)+";majfee();' value='' defaultChecked=false name='txin_"+txhash+"_use_"+random_string(6)+"' >\
							<input type=hidden name='txin_"+txhash+"_h' value='"+str(txhash)+"'>\
							<input type=hidden name='txin_"+txhash+"_n' value='"+str(txn)+"'>\
							<input type=hidden name='txin_"+txhash+"_script' value='"+txscript+"'>\
<input type=hidden name='txin_"+txhash+"_amin' value='"+str(txvalue)+"'>\
						</td>"
#				table+="<td>"+a+"</td>"
				table+="<td>"+txhash+"</td>"
				table+="<!--td>"+str(txn)+"</td-->"
				if txscript[:6]+txscript[-4:]=="76a91488ac":
					table+="<td>Address "+hash_160_to_bc_address(txscript[6:-4].decode('hex'))+"</td>"
					table+="<input type=hidden name='txin_"+txhash+"_add' value='"+hash_160_to_bc_address(txscript[6:-4].decode('hex'))+"'>"
				else:
					table+="<td>"+txscript+"</td>"

				table+="<td>"+str(txvalue/1e8)+"</td>"
				table+="</tr>\n"
			table+="</table>"
			ret+=table

			ret+="<span id='tot_in'>0</span> BTC (inputs) - <span id='tot_out'>0</span> BTC (outputs) = <span id='tot_fee'>0</span> BTC (fee)<br /><br />"

			txouts=""
			nbretxouts=30
			unserouts=["parseFloat(document.getElementById(\"txout_am_"+str(i)+"\").value)" for i in range(nbretxouts)]
			serouts="+".join(unserouts)
			for i in range(nbretxouts):
				txouts+="<span id='txout_"+str(i)+"' style='display:"+X_if_else("inline",i<3,"none")+";' >\
Amount: <input value='0' onchange='totalout=Math.round(("+serouts+")*100000000);majfee();' name='txout_am_"+str(i)+"' id='txout_am_"+str(i)+"' />&nbsp;&nbsp;&nbsp;&nbsp;Script: <input name='txout_script_"+str(i)+"' />\
\
\
\
<br />"+X_if_else("<input type=button id='button_txout_"+str(i)+"' value='Add a txout' onclick='document.getElementById(\"txout_"+str(i+X_if_else(0,i==nbretxouts-1,1))+"\").style.display=\"block\";document.getElementById(\"button_txout_"+str(i)+"\").style.display=\"none\";' />",i>=2,"")+"</span>"

			ret+=txouts
			ret+="<input type=submit value='Create' /></form>"
#			ret+=WI_Submit('Create', '', '', 'ajaxCTX2')

			return ret

if 'twisted' not in missing_dep:
	class WIInfo(resource.Resource):

		 def render_GET(self, request):
			 global addrtype
			 try:
					sec = request.args['key'][0]
					format = request.args['format'][0]
					addrtype = int(request.args['vers'][0])
					msgIsHex = False
					msgIsFile = False
					try:
						msg = request.args['msg'][0]
						if msg[0:4] == "Hex:":
							msg = msg[4:]
							msgIsHex = True
						elif msg[0:5] == "File:":
							msg = msg[5:]
							if not os.path.isfile(msg):
								return '%s doesn\'t exist'%(msg)
							filin = open(msg, 'r')
							msg = filin.read()
							filin.close()
							msgIsFile = True

						sig = request.args['sig'][0]
						pubkey = request.args['pubkey'][0]
						need = int(request.args['need'][0])
					except:
						need = 1

					ret = ""

					if sec is not '':
						if format in 'reg':
							pkey = regenerate_key(sec)
							compressed = is_compressed(sec)
						elif len(sec) == 64:
							pkey = EC_KEY(str_to_long(sec.decode('hex')))
							compressed = False
						elif len(sec) == 66:
							pkey = EC_KEY(str_to_long(sec[:-2].decode('hex')))
							compressed = True
						else:
							return "Hexadecimal private keys must be 64 characters long"

						if not pkey:
							return "Bad private key"


						secret = GetSecret(pkey)
						private_key = GetPrivKey(pkey, compressed)
						public_key = GetPubKey(pkey, compressed)
						addr = public_key_to_bc_address(public_key)

						if need & 1:
							ret += "Address (%s): %s<br />"%(aversions[addrtype], addr)
							ret += "Privkey (%s): %s<br />"%(aversions[addrtype], SecretToASecret(secret, compressed))
							ret += "Hexprivkey: %s<br />"%(secret.encode('hex'))
							ret += "Hash160: %s<br />"%(bc_address_to_hash_160(addr).encode('hex'))
	#						ret += "Inverted hexprivkey: %s<br />"%(inversetxid(secret.encode('hex')))
							ret += "Pubkey: <span style='font-size:60%%;'>04%.64x%.64x</span><br />"%(pkey.pubkey.point.x(), pkey.pubkey.point.y())
							ret += X_if_else('<br /><br /><b>Beware, 0x%s is equivalent to 0x%.33x</b>'%(secret.encode('hex'), int(secret.encode('hex'), 16)-_r), (int(secret.encode('hex'), 16)>_r), '')

					if 'ecdsa' not in missing_dep and need & 2:
						if sec is not '' and msg is not '':
							if need & 1:
								ret += "<br />"
							ret += "Signature of '%s' by %s: <span style='font-size:60%%;'>%s</span><br />Pubkey: <span style='font-size:60%%;'>04%.64x%.64x</span><br />"%(X_if_else(msg, not msgIsFile, request.args['msg'][0]), addr, sign_message(secret, msg, msgIsHex), pkey.pubkey.point.x(), pkey.pubkey.point.y())

						if sig is not '' and msg is not '' and pubkey is not '':
							addr = public_key_to_bc_address(pubkey.decode('hex'))
							try:
								verify_message_signature(pubkey, sig, msg, msgIsHex)
								ret += "<br /><span style='color:#005500;'>Signature of '%s' by %s is <span style='font-size:60%%;'>%s</span></span><br />"%(X_if_else(msg, not msgIsFile, request.args['msg'][0]), addr, sig)
							except:
								ret += "<br /><span style='color:#990000;'>Signature of '%s' by %s is NOT <span style='font-size:60%%;'>%s</span></span><br />"%(X_if_else(msg, not msgIsFile, request.args['msg'][0]), addr, sig)

					return ret

			 except:
				 log.err()
				 return 'Error in info page'

			 def render_POST(self, request):
				 return self.render_GET(request)


	class WIImportTx(resource.Resource):

		 def render_GET(self, request):
			 global addrtype
			 try:
					wdir=request.args['dir'][0]
					wname=request.args['name'][0]
					txk=request.args['txk'][0]
					txv=request.args['txv'][0]
					d = {}

					if not os.path.isfile(wdir+"/"+wname):
						return '%s/%s doesn\'t exist'%(wdir, wname)

					if txk not in "file":
						dd = [{'tx_k':txk, 'tx_v':txv}]
					else:
						if not os.path.isfile(txv):
							return '%s doesn\'t exist'%(txv)
						dd = read_jsonfile(txv)


					db_env = create_env(wdir)
					read_wallet(json_db, db_env, wname, True, True, "", None)
					db = open_wallet(db_env, wname, writable=True)

					i=0
					for tx in dd:
						d = {'txi':tx['tx_k'], 'txv':tx['tx_v']}
						print(d)
						update_wallet(db, "tx", d)
						i+=1

					db.close()

					return "<pre>hash: %s\n%d transaction%s imported in %s/%s<pre>" % (inverse_str(txk[6:]), i, iais(i), wdir, wname)

			 except:
				 log.err()
				 return 'Error in importtx page'

			 def render_POST(self, request):
				 return self.render_GET(request)

	class WIQuit(resource.Resource):
		def render_GET(self, request):
			reactor.stop()
		def render_POST(self, request):
			return self.render_GET(request)

	class WICTListTx(resource.Resource):
		def render_GET(self, request):
			global CTX_adds
			try:
				adds=request.args['addresses'][0]
				CTX_adds=adds
			except:
				return "You must provide at least one address to see the transaction you can spend. Divided by |"

			ret=""
			ret=listtx_txt(adds)
			return "Refresh to display available incoming transactions"

		def render_POST(self, request):
			return self.render_GET(request)

	class WICT(resource.Resource):
		def render_GET(self, request):
			#CT?sec=s&hashesin=h&indexes=1&pubkeys=p&prevspk=r&amounts=2453628&spk=spk#tbend
			global txin_amounts, json_db
			display = ""



			try:
				testnet=request.args['testnet'][0]
				TN="testnet"
			except:
				TN=""

			try:

				list_sec, list_hin, list_indexes, list_pubs, list_scriptin, list_outam, list_scriptout, list_amin = [[] for i in range(8)]

				txin_to_use=[]
				txouts_nos=[]
				txouts_not_empty=[]
				for i in request.args:
					if i[:4]=='txin' and i[-10:-7]=='use':
						txin_to_use.append(i.split('_')[1])
					if i[:4]=='txou' and i.split('_')[2] not in txouts_nos:
						p=i.split('_')[1]
						no=i.split('_')[2]
						txouts_nos.append(no)

				for no in txouts_nos:
				  if request.args['txout_am_'+no][0]!='' and request.args['txout_am_'+no][0]!='0':
					list_outam.append(request.args['txout_am_'+no][0])
					list_scriptout.append(request.args['txout_script_'+no][0])


				global addr_to_keys
				for h in txin_to_use:
					if request.args['txin_'+h+'_add'][0] not in addr_to_keys.keys():
						return "<br />No private key for "+request.args['txin_'+h+'_add'][0]+", please dump a wallet containing this address<br /><br /><a href='http://localhost:"+str(webport)+"'>Return to Pywallet</a>"

					list_hin.append(h)
					list_indexes.append(request.args['txin_'+h+'_n'][0])
					list_scriptin.append(request.args['txin_'+h+'_script'][0])
					list_sec.append(addr_to_keys[request.args['txin_'+h+'_add'][0]][0])
					list_pubs.append(addr_to_keys[request.args['txin_'+h+'_add'][0]][1])
					list_amin.append(request.args['txin_'+h+'_amin'][0])

				sec=",".join(list_sec)
				hashesin=",".join(list_hin)
				indexes=",".join(list_indexes)
				pubkeys=",".join(list_pubs)
				prevspk=",".join(list_scriptin)
				amins=",".join(list_amin)
				amounts=",".join(list_outam)
				spk=",".join(list_scriptout)


			except:
				display += "error"
				return display

			secret_key = sec.split(',')
			hashes_txin = hashesin.split(',')
			indexes_txin = indexes.split(',')
			for i in range(len(indexes_txin)):
				indexes_txin[i] = int(indexes_txin[i])
			pubkey_txin = pubkeys.split(',')
			am_txin = amins.split(',')
			prevScriptPubKey = prevspk.split(',')

			amounts_txout = amounts.split(',')
			for i in range(len(amounts_txout)):
				amounts_txout[i] = int(1e8*float(amounts_txout[i]))
			spk_txout = spk.split(',')

			tx = create_transaction(secret_key, hashes_txin, indexes_txin, pubkey_txin, prevScriptPubKey, amounts_txout, spk_txout)

			display += "Inputs: (go to <a href='CTTest'>CTTest</a> before)<br />"
			sum_in = 0
			for i in range(len(hashes_txin)):
				try:
#					ain = txin_amounts[hashes_txin[i] + ("%d"%indexes_txin[i])]
					ain=int(am_txin[i])/1e8
					aaa = ", %.8f BTC"%ain
					sum_in += ain
				except:
					aaa = ""
				display += ('%d: <a href="http://blockexplorer.com/'+TN+'/tx/%s#o%d">%s #%d</a>%s<br />')%(i, hashes_txin[i], indexes_txin[i], hashes_txin[i], indexes_txin[i], aaa)

			display += "<br /><br />Outputs:<br />"
			sum_out = 0
			for i in range(len(spk_txout)):
				sum_out += amounts_txout[i]/BTC
				display += '%.8f BTC to %s<br />'%(amounts_txout[i]/BTC, hash_160_to_bc_address(spk_txout[i].decode('hex')))

			display += "<br />"
			display += "<br />"
			display += "In: %.8f BTC"%sum_in
			display += "<br />"
			display += "Out: %.8f BTC"%sum_out
			display += "<br />"
			display += "Fee: %.8f BTC"%(sum_in-sum_out)
			display += "<br />"
			display += "<br />"
			display += "<br />"
			display += ("<pre>Transaction hash: "+tx[0])
			display += "<br />"
#			display += ("tx_k:    "+tx[1])
#			display += "<br />"
			display += ("Raw transaction:       "+tx[2])

			display += "</pre><br />"


			return display

		def render_POST(self, request):
			return self.render_GET(request)

	class WICTTest(resource.Resource):

		def render_GET(self, request):
			try:
				request.args['testnet'][0]
				testnet=True
			except:
				testnet=False
			list_avtx = {}
			i = 0

			try:
				for add in request.args['addresses'][0].split(','):
					print "Address %d: %s"%(i, add)
					list_avtx[add] = bc_address_to_available_tx(add, testnet)[add]
					i += 1

				print(list_avtx)

				display = ""
				display += write_avtx(list_avtx, testnet)
			except:
				display="You must provide at least one address to see the transaction you can spend.<br /><a href='CTTest?addresses=1BAdzvknPux2zqG2eNawvgitCW1aqwE4bb'>Like this</a>"

			return display

		def render_POST(self, request):
			return self.render_GET(request)


	class WIImport(resource.Resource):

		 def render_GET(self, request):
			 global addrtype
			 try:
                                pub=request.args['pub'][0]
                                try:
										wdir=request.args['dir'][0]
										wname=request.args['name'][0]
										label=request.args['label'][0]

										db_env = create_env(wdir)
										db = open_wallet(db_env, wname, writable=True)
										update_wallet(db, 'ckey', { 'public_key' : pub.decode('hex'), 'encrypted_private_key' : random_string(96).decode('hex') })
										update_wallet(db, 'name', { 'hash' : public_key_to_bc_address(pub.decode('hex')), 'name' : "Read-only: "+label })
										db.close()
										return "Read-only address "+public_key_to_bc_address(pub.decode('hex'))+" imported"
        			except:
										return "Read-only address "+public_key_to_bc_address(pub.decode('hex'))+" not imported"
			 except:
                                pass

			 try:

					wdir=request.args['dir'][0]
					wname=request.args['name'][0]

					try:		#Import a single key
						addrtype = int(request.args['vers'][0])
						format = X_if_else('hex', request.args['format'][0]=='true', 'reg')
						reserve=request.args.has_key('reserve')
						label=request.args['label'][0]
						compressed=request.args['com'][0]=='true'
						tocrypt=request.args['cry'][0]=='true'
						sec = request.args['key'][0]
					except:		#Import csv file
						ret=import_csv_keys(request.args['file'][0],wdir,wname)
						return "File "+X_if_else("", ret, "not ")+"imported"





					if format in 'reg':
						pkey = regenerate_key(sec)
						compressed = is_compressed(sec)
					elif len(sec) == 64:
						pkey = EC_KEY(str_to_long(sec.decode('hex')))
						compressed = False
					elif len(sec) == 66:
						pkey = EC_KEY(str_to_long(sec[:-2].decode('hex')))
						compressed = True
					else:
						return "Hexadecimal private keys must be 64 or 66 characters long"

					if not pkey:
						return "Bad private key"

					if not os.path.isfile(wdir+"/"+wname):
						return '%s/%s doesn\'t exist'%(wdir, wname)


					db_env = create_env(wdir)
					ret_read = read_wallet(json_db, db_env, wname, True, True, "", None)
					tocrypt = ret_read['crypted']
					db = open_wallet(db_env, wname, writable=True)


					secret = GetSecret(pkey)
					private_key = GetPrivKey(pkey, compressed)
					public_key = GetPubKey(pkey, compressed)
					addr = public_key_to_bc_address(public_key)



					if (format in 'reg' and sec in private_keys) or (format not in 'reg' and sec in private_hex_keys):
						return "Already exists"

					if not tocrypt:
						update_wallet(db, 'key', { 'public_key' : public_key, 'private_key' : private_key })
					else:
						cry_master = json_db['mkey']['encrypted_key'].decode('hex')
						cry_salt   = json_db['mkey']['salt'].decode('hex')
						cry_rounds = json_db['mkey']['nDerivationIterations']
						cry_method = json_db['mkey']['nDerivationMethod']

						crypter.SetKeyFromPassphrase(passphrase, cry_salt, cry_rounds, cry_method)
						masterkey = crypter.Decrypt(cry_master)
						crypter.SetKey(masterkey)
						crypter.SetIV(Hash(public_key))
						e = crypter.Encrypt(secret)
						ck_epk=e

						update_wallet(db, 'ckey', { 'public_key' : public_key, 'encrypted_private_key' : ck_epk })

					if not reserve:
						update_wallet(db, 'name', { 'hash' : addr, 'name' : label })

					db.close()

					return "<pre>Address: %s\nPrivkey: %s\nHexkey: %s\nKey (%scrypted, %scompressed) imported in %s/%s<pre>" % (addr, SecretToASecret(secret, compressed), secret.encode('hex'), X_if_else("",tocrypt,"un"), X_if_else("",compressed,"un"), wdir, wname)

			 except:
				 log.err()
				 return 'Error in import page'

			 def render_POST(self, request):
				 return self.render_GET(request)

	class WI404(resource.Resource):

		 def render_GET(self, request):
			 return 'Page Not Found'


def update_pyw():
	if md5_last_pywallet[0] and md5_last_pywallet[1] not in md5_pywallet:
		dl=urllib.urlopen('https://raw.github.com/jackjack-jj/pywallet/master/pywallet.py').read()
		if len(dl)>40 and md5_2(dl)==md5_last_pywallet[1]:
			filout = open(pyw_path+"/"+pyw_filename, 'w')
			filout.write(dl)
			filout.close()
			thread.start_new_thread(restart_pywallet, ())
			return "Updated, restarting..."
		else:
			return "Problem when downloading new version ("+md5_2(dl)+"/"+md5_last_pywallet[1]+")"

def restart_pywallet():
	thread.start_new_thread(start_pywallet, ())
	time.sleep(2)
	reactor.stop()

def start_pywallet():
	a=Popen("python "+pyw_path+"/"+pyw_filename+" --web --port "+str(webport)+" --wait 3", shell=True, bufsize=-1, stdout=PIPE).stdout
	a.close()

def clone_wallet(parentPath, clonePath):
	types,datas=[],[]
	parentdir,parentname=os.path.split(parentPath)
	wdir,wname=os.path.split(clonePath)

	db_env = create_env(parentdir)
	read_wallet(json_db, db_env, parentname, True, True, "", False)

	types.append('version')
	datas.append({'version':json_db['version']})
	types.append('defaultkey')
	datas.append({'key':json_db['defaultkey']})
	for k in json_db['keys']:
		types.append('ckey')
		datas.append({'public_key':k['pubkey'].decode('hex'),'encrypted_private_key':random_string(96).decode('hex')})
	for k in json_db['pool']:
		types.append('pool')
		datas.append({'n':k['n'],'nVersion':k['nVersion'],'nTime':k['nTime'],'public_key':k['public_key_hex'].decode('hex')})
	for addr,label in json_db['names'].items():
		types.append('name')
		datas.append({'hash':addr,'name':'Watch:'+label})

	db_env = create_env(wdir)
	create_new_wallet(db_env, wname, 60000)

	db = open_wallet(db_env, wname, True)
	NPP_salt=random_string(16).decode('hex')
	NPP_rounds=int(50000+random.random()*20000)
	NPP_method=0
	NPP_MK=random_string(64).decode('hex')
	crypter.SetKeyFromPassphrase(random_string(64), NPP_salt, NPP_rounds, NPP_method)
	NPP_EMK = crypter.Encrypt(NPP_MK)
	update_wallet(db, 'mkey', {
		"encrypted_key": NPP_EMK,
		'nDerivationIterations' : NPP_rounds,
		'nDerivationMethod' : NPP_method,
		'nID' : 1,
		'otherParams' : ''.decode('hex'),
		"salt": NPP_salt
	})
	db.close()

	read_wallet(json_db, db_env, wname, True, True, "", False)

	db = open_wallet(db_env, wname, writable=True)
	update_wallet(db, types, datas, True)
	db.close()
	print "Wallet successfully cloned to:\n   %s"%clonePath

import thread
md5_last_pywallet = [False, ""]

def retrieve_last_pywallet_md5():
	global md5_last_pywallet
	md5_last_pywallet = [True, md5_onlinefile('https://raw.github.com/jackjack-jj/pywallet/master/pywallet.py')]

from optparse import OptionParser

if __name__ == '__main__':


	parser = OptionParser(usage="%prog [options]", version="%prog 1.1")

	parser.add_option("--passphrase", dest="passphrase",
		help="passphrase for the encrypted wallet")

	parser.add_option("--dumpwallet", dest="dump", action="store_true",
		help="dump wallet in json format")

	parser.add_option("--dumpwithbalance", dest="dumpbalance", action="store_true",
		help="includes balance of each address in the json dump, takes about 2 minutes per 100 addresses")

	parser.add_option("--importprivkey", dest="key",
		help="import private key from vanitygen")

	parser.add_option("--importhex", dest="keyishex", action="store_true",
		help="KEY is in hexadecimal format")

	parser.add_option("--datadir", dest="datadir",
		help="wallet directory (defaults to bitcoin default)")

	parser.add_option("--wallet", dest="walletfile",
		help="wallet filename (defaults to wallet.dat)",
		default="wallet.dat")

	parser.add_option("--label", dest="label",
		help="label shown in the adress book (defaults to '')",
		default="")

	parser.add_option("--testnet", dest="testnet", action="store_true",
		help="use testnet subdirectory and address type")

	parser.add_option("--namecoin", dest="namecoin", action="store_true",
		help="use namecoin address type")

	parser.add_option("--otherversion", dest="otherversion",
		help="use other network address type, whose version is OTHERVERSION")

	parser.add_option("--info", dest="keyinfo", action="store_true",
		help="display pubkey, privkey (both depending on the network) and hexkey")

	parser.add_option("--reserve", dest="reserve", action="store_true",
		help="import as a reserve key, i.e. it won't show in the adress book")

	parser.add_option("--multidelete", dest="multidelete",
		help="deletes data in your wallet, according to the file provided")

	parser.add_option("--balance", dest="key_balance",
		help="prints balance of KEY_BALANCE")

	parser.add_option("--web", dest="web", action="store_true",
		help="run pywallet web interface")

	parser.add_option("--port", dest="port",
		help="port of web interface (defaults to 8989)")

	parser.add_option("--recover", dest="recover", action="store_true",
		help="recover your deleted keys, use with recov_size and recov_device")

	parser.add_option("--recov_device", dest="recov_device",
		help="device to read (e.g. /dev/sda1 or E: or a file)")

	parser.add_option("--recov_size", dest="recov_size",
		help="number of bytes to read (e.g. 20Mo or 50Gio)")

	parser.add_option("--recov_outputdir", dest="recov_outputdir",
		help="output directory where the recovered wallet will be put")

	parser.add_option("--clone_watchonly_from", dest="clone_watchonly_from",
		help="path of the original wallet")

	parser.add_option("--clone_watchonly_to", dest="clone_watchonly_to",
		help="path of the resulting watch-only wallet")

	parser.add_option("--dont_check_walletversion", dest="dcv", action="store_true",
		help="don't check if wallet version > %d before running (WARNING: this may break your wallet, be sure you know what you do)"%max_version)

	parser.add_option("--wait", dest="nseconds",
		help="wait NSECONDS seconds before launch")


#	parser.add_option("--forcerun", dest="forcerun",
#		action="store_true",
#		help="run even if pywallet detects bitcoin is running")

	(options, args) = parser.parse_args()

#	a=Popen("ps xa | grep ' bitcoin'", shell=True, bufsize=-1, stdout=PIPE).stdout
#	aread=a.read()
#	nl = aread.count("\n")
#	a.close()
#	if nl > 2:
#		print('Bitcoin seems to be running: \n"%s"'%(aread))
#		if options.forcerun is None:
#			exit(0)

	if options.nseconds:
		time.sleep(int(options.nseconds))

	if options.passphrase:
		passphrase = options.passphrase

	if options.clone_watchonly_from is not None and options.clone_watchonly_to:
		clone_wallet(options.clone_watchonly_from, options.clone_watchonly_to)
		exit(0)


	if options.recover:
		if options.recov_size is None or options.recov_device is None or options.recov_outputdir is None:
			print("You must provide the device, the number of bytes to read and the output directory")
			exit(0)
		device = options.recov_device
		if len(device) in [2,3] and device[1]==':':
			device="\\\\.\\"+device
		size = read_device_size(options.recov_size)

		passphraseRecov=''
		while passphraseRecov=='':
			passphraseRecov=raw_input("Enter the passphrase for the wallet that will contain all the recovered keys: ")
		passphrase=passphraseRecov

		passes=[]
		p=' '
		print '\nEnter the possible passphrases used in your deleted wallets.'
		print "Don't forget that more passphrases = more time to test the possibilities."
		print 'Write one passphrase per line and end with an empty line.'
		while p!='':
			p=raw_input("Possible passphrase: ")
			if p!='':
				passes.append(p)

		print "\nStarting recovery."
		recoveredKeys=recov(device, passes, size, 10240, options.recov_outputdir)
		recoveredKeys=list(set(recoveredKeys))
#		print recoveredKeys[0:5]


		db_env = create_env(options.recov_outputdir)
		recov_wallet_name = "recovered_wallet_%s.dat"%ts()

		create_new_wallet(db_env, recov_wallet_name, 32500)

		if passphraseRecov!="I don't want to put a password on the recovered wallet and I know what can be the consequences.":
			db = open_wallet(db_env, recov_wallet_name, True)

			NPP_salt=random_string(16).decode('hex')
			NPP_rounds=int(50000+random.random()*20000)
			NPP_method=0
			NPP_MK=random_string(64).decode('hex')
			crypter.SetKeyFromPassphrase(passphraseRecov, NPP_salt, NPP_rounds, NPP_method)
			NPP_EMK = crypter.Encrypt(NPP_MK)
			update_wallet(db, 'mkey', {
				"encrypted_key": NPP_EMK,
				'nDerivationIterations' : NPP_rounds,
				'nDerivationMethod' : NPP_method,
				'nID' : 1,
				'otherParams' : ''.decode('hex'),
				"salt": NPP_salt
			})
			db.close()

		read_wallet(json_db, db_env, recov_wallet_name, True, True, "", False)

		db = open_wallet(db_env, recov_wallet_name, True)

		print "\n\nImporting:"
		for i,sec in enumerate(recoveredKeys):
			sec=sec.encode('hex')
			print("\nImporting key %4d/%d:"%(i+1, len(recoveredKeys)))
			importprivkey(db, sec, "recovered: %s"%sec, None, True)
			importprivkey(db, sec+'01', "recovered: %s"%sec, None, True)
		db.close()

		print("\n\nThe new wallet %s/%s contains the %d recovered key%s"%(options.recov_outputdir, recov_wallet_name, len(recoveredKeys), iais(len(recoveredKeys))))

		exit(0)


	if 'bsddb' in missing_dep:
		print("pywallet needs 'bsddb' package to run, please install it")
		exit(0)

	if 'twisted' in missing_dep and options.web is not None:
		print("'twisted' package is not installed, pywallet web interface can't be launched")
		exit(0)

	if 'ecdsa' in missing_dep:
		print("'ecdsa' package is not installed, pywallet won't be able to sign/verify messages")

	if 'twisted' not in missing_dep:
		VIEWS = {
			 'DumpWallet': WIDumpWallet(),
			 'MergeWallets': WIMergeWallets(),
			 'Import': WIImport(),
			 'ImportTx': WIImportTx(),
			 'DumpTx': WIDumpTx(),
			 'Info': WIInfo(),
			 'Delete': WIDelete(),
			 'Balance': WIBalance(),
			 'ChangePP': WIChangePP(),
			 'Others': WIOthers(),
			 'LoadBalances': WICTTest(),
			 'CTTest': WICTTest(),
			 'ListTransactions': WICTListTx(),
			 'CreateTransaction': WICT(),
			 'CT': WICT(),
			 'quit': WIQuit()

		}

	if options.dcv is not None:
		max_version = 10 ** 9

	if options.datadir is not None:
		wallet_dir = options.datadir

	if options.walletfile is not None:
		wallet_name = options.walletfile

	if 'twisted' not in missing_dep and options.web is not None:
		md5_pywallet = md5_file(pyw_path+"/"+pyw_filename)
		thread.start_new_thread(retrieve_last_pywallet_md5, ())

		webport = 8989
		if options.port is not None:
			webport = int(options.port)
		root = WIRoot()
		for viewName, className in VIEWS.items():
			root.putChild(viewName, className)
		log.startLogging(sys.stdout)
		log.msg('Starting server: %s' %str(datetime.now()))
		server = server.Site(root)
		reactor.listenTCP(webport, server)
		reactor.run()
		exit(0)

	if options.key_balance is not None:
		print(balance(balance_site, options.key_balance))
		exit(0)

	if options.dump is None and options.key is None and options.multidelete is None:
		print "A mandatory option is missing\n"
		parser.print_help()
		exit(0)

	if options.testnet:
		db_dir += "/testnet"
		addrtype = 111

	if options.namecoin or options.otherversion is not None:
		if options.datadir is None and options.keyinfo is None:
			print("You must provide your wallet directory")
			exit(0)
		else:
			if options.namecoin:
				addrtype = 52
			else:
				addrtype = int(options.otherversion)

	if options.keyinfo is not None:
		if not keyinfo(options.key, options.keyishex):
			print "Bad private key"
		exit(0)

	db_dir = determine_db_dir()

	db_env = create_env(db_dir)

	if options.multidelete is not None:
		filename=options.multidelete
		filin = open(filename, 'r')
		content = filin.read().split('\n')
		filin.close()
		typedel=content[0]
		kd=filter(bool,content[1:])
		try:
			r=delete_from_wallet(db_env, determine_db_name(), typedel, kd)
			print '%d element%s deleted'%(r, 's'*(int(r>1)))
		except:
			print "Error: do not try to delete a non-existing transaction."
			exit(1)
		exit(0)


	read_wallet(json_db, db_env, determine_db_name(), True, True, "", options.dumpbalance is not None)

	if json_db.get('minversion') > max_version:
		print "Version mismatch (must be <= %d)" % max_version
		#exit(1)

	if options.dump:
		print json.dumps(json_db, sort_keys=True, indent=4)
	elif options.key:
		if json_db['version'] > max_version:
			print "Version mismatch (must be <= %d)" % max_version
		elif (options.keyishex is None and options.key in private_keys) or (options.keyishex is not None and options.key in private_hex_keys):
			print "Already exists"
		else:
			db = open_wallet(db_env, determine_db_name(), writable=True)

			if importprivkey(db, options.key, options.label, options.reserve, options.keyishex):
				print "Imported successfully"
			else:
				print "Bad private key"

			db.close()





