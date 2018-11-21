#!/usr/bin/env python2
# from the git repo
import md5py, socket, hashlib, string, sys, os, time, struct

f = open("output.txt", "w")

host = "142.93.118.186"   # IP address or URL
port = 1234 # port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
data = s.recv(1024)
print(data)

#####################################
### STEP 1: Calculate forged hash ###
#####################################

one = "1\n"
s.send(one)			     
data = s.recv(1024)
print(data)

message = 'testing'    # original message here

s.send(message + "\n")			     
data = s.recv(1024)
print(data)
temp = data[40:] 

legit = temp.strip()#a legit hash of secret + message goes here, obtained from signing a message

print("LEGIT : " + legit)
f.write("Legit hash: " + legit + "\n")

# initialize hash object with state of a vulnerable hash
fake_md5 = md5py.new('A' * 64)
fake_md5.A, fake_md5.B, fake_md5.C, fake_md5.D = md5py._bytelist2long(legit.decode('hex'))

malicious = 'testing2'  # put your malicious message here

# update legit hash with malicious message
fake_md5.update(malicious)

# fake_hash is the hash for md5(secret + message + padding + malicious)
fake_hash = fake_md5.hexdigest()
print(fake_hash)
f.write("Fake hash" + fake_hash + "\n")


#############################
### STEP 2: Craft payload ###
#############################

# TODO: calculate proper padding based on secret + message
# secret is <redacted> bytes long (48 bits)
# each block in MD5 is 512 bits long
# secret + message is followed by bit 1 then bit 0's (i.e. \x80\x00\x00...)
# after the 0's is a bye with message length in bits, little endian style
# (i.e. 20 char msg = 160 bits = 0xa0 = '\xa0\x00\x00\x00\x00\x00\x00\x00\x00')
# craft padding to align the block as MD5 would do it
# (i.e. len(secret + message + padding) = 64 bytes = 512 bits

for i in range(6,15):
	#pad = 64 - ((len(message)+14) %64)
	#bits = 8 * (len(message)+i)

	#temp = message
	#temp += '\x80' + '\000' * (pad - 1)
	#temp += struct.pack('<q', bits)


	#encrypt = temp + malicious

	#payload = ""
	#for c in encrypt:
	#	payload =  payload + '\\x%02X' % ord(c)

	null = "\x00" * 43
	end = "\x00" * 7
	padding = "\x80" + null + "\x60" + end

	payload = message + padding + malicious

	print("PAYLOAD: " + payload)
	# send `fake_hash` and `payload` to server (manually or with sockets)
	# REMEMBER: every time you sign new data, you will regenerate a new secret!
	f.write("PAYLOAD: " + payload + "\n")


	two = "2\n"
	s.send(two)	#test signature     
	data = s.recv(1024)
	print(data)

	s.send(fake_hash + "\n")	

	data = s.recv(1024)
	print(data)

	s.send(payload + "\n")	

	data = s.recv(1024)
	print(data)
	data = s.recv(1024)
	print(data)
	data = s.recv(1024)
	print(data)


s.close()# close the connection
f.close()#close the file
