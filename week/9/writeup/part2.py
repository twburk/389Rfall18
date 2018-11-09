#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing useful libraries -- feel free to add any others you find necessary
import socket
import hashlib

host = "142.93.117.193"   # IP address or URL
port = 7331    # port

# use these to connect to the service
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

cmd = "no quit"
count = 0;
while(count != 10):
	# receive some data
	data = s.recv(1024)
	print(data)
	if(count == 0):
		arr = data.split(" ")
		sha = arr[9]
		passw = arr[12]
		count += 1;
	else:
		arr = data.split(" ")
		sha = arr[3]
		passw = arr[6]
		count += 1;

	sha = sha.rstrip();
	passw = passw.rstrip();

	passw = passw[0:10]

	print(passw)

	if(sha == "sha224"):
		m = hashlib.sha224()
		m.update(passw)
		h = m.hexdigest()
	elif(sha == "sha256"):
		m = hashlib.sha256()
		m.update(passw)
		h = m.hexdigest()
	elif(sha == "sha1"):
		m = hashlib.sha1()
		m.update(passw)
		h = m.hexdigest()
	elif(sha == "sha384"):
		m = hashlib.sha384()
		m.update(passw)
		h = m.hexdigest()
	elif(sha == "sha512"):
		m = hashlib.sha512()
		m.update(passw)
		h = m.hexdigest()
	elif(sha == "md5"):
		m = hashlib.md5()
		m.update(passw)
		h = m.hexdigest()

	s.send(h + "\n")

data = s.recv(1024)
print(data)

# close the connection
s.close()
