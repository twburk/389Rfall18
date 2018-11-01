#!/usr/bin/env python2

import sys
import struct
from datetime import datetime
import codecs


# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0xdeadbeef
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python2 stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[0:8])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))

# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

def print_char_entry(entry, end, encoding):
	char, = entry
	char = char.decode(encoding)
	print(char, end)

def print_int_entry(entry, end):
	num, = entry
	print(num, end)

timestamp = struct.unpack("<L", data[8:12])
#print("TIMESTAMP: %d (%s)" %(timestamp, datetime.fromtimestamp(timestamp)))
print("TIMESTAMP: %d " % timestamp)

author = struct.unpack("<cccccccc", data[12:20])
print(author)

#print_char_entry(author, "\n", "ascii")

section_count, = struct.unpack("<L", data[20:24])
print("SECTION COUNT: %d" % section_count)

print("DATA LENGTH: %d" % len(data))

print("-------  BODY  -------")

def png_out(data, offset, s_length):
	filename = 'out.png'
	f = open(filename, mode='wb')
	header = [0x89,0x50,0x4E,0x47,0x0D,0x0A,0x1A,0x0A]
	f.write(bytes(header))
	f.write(data[offset:offset+s_length])
	f.close()

stype_dict = {
	1: (1, "<c", print_char_entry, {'end': "", 'encoding' : 'ascii'}),
	2: (1, "<c", print_char_entry, {'end' : "", 'encoding' : 'utf-8'}),
	3: (4, "<L", print_int_entry, {'end' : ""}),
	#4: (8, "<q", print, {'end': ""}),
	5: (8, "<d", print_int_entry, {'end' : ""}),
	#6: (16, "<dd", print, {'end' : ""}),
	7: (4, "<L", print_int_entry, {'end' : ""})
}

offset = 24
section_count = 0

while(offset < len(data)):
	section_count += 1
	
	stype, slength = struct.unpack_from("<LL", data, offset)

	print("SECTION TYPE: %d" % stype)
	print("SECTION LENGTH: %d" % slength)

	offset += 8
	startOff = offset

	if(stype in stype_dict):
		if(section_count == 9 or section_count == 10):
			decoded_str = codecs.decode(data[offset:offset + slength], 'base64')
			print(decoded_str)
		(size,format_str,output_fun,args) = stype_dict[stype]

		for i in range(0, int(slength/size)):
			entry = struct.unpack_from(format_str, data, offset)
			offset += size
			output_fun(entry, **args)

		print("")

	elif(stype == 8):
		png_out(data, offset, slength)

	if(offset != startOff + slength):
		print("SKIPPING")
		offset = startOff + slength

print("-------  BODY  -------")

print("Number OF SECTIONS %d" % section_count)
