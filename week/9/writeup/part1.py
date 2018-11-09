#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing a useful library -- feel free to add any others you find necessary
import hashlib
import string

# this will work if you place this script in your writeup folder
wordlist = open("probable-v2-top1575.txt", 'r')

# a string equal to 'abcdefghijklmnopqrstuvwxyz'.
salts = string.ascii_lowercase

#get hashes from file
hashes = open("hashes", 'r')

for h in hashes:
	h = h.strip()
	print("Testing Hash: " + h)
	wordlist.seek(0)
	for password in wordlist:
		password = password.strip()
		for salt in salts:
			m = hashlib.sha512()
			m.update(salt)
			m.update(password)
			test = m.hexdigest()
			if(test == h):
				print("Salt : " + salt)
				print("password : " + password)

