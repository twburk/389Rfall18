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
# the rest of the header and the actual RCFF body. Good luck!                                                                                                                                                      
                                                                                                                                                                                                                   
i = 8                                                                                                                                                                                                              
timestamp, = struct.unpack("<L", data[i:i+4]); i += 4                                                                                                                                                              
author, = struct.unpack("<8s", data[i:i+8]); i += 8                                                                                                                                                                
section_count, = struct.unpack("<L", data[i:i+4]); i += 4                                                                                                                                                          
print("TIMESTAMP: " + str(timestamp))                                                                                                                                                                              
print("AUTHOR: " + str(author))                                                                                                                                                                                    
print("SECTION COUNT: " + str(section_count))                                                                                                                                                                      
print
print("-------  BODY  -------")                                                                                                                                                                                    
for j in range(0, section_count + 2):                                                                                                                                                                              
    section_type, = struct.unpack("<L", data[i:i+4]); i += 4                                                                                                                                                       
    section_length, = struct.unpack("<i", data[i:i+4]); i += 4                                                                                                                                                     
    print("SECTION " + str(j + 1))                                                                                                                                                                                 
    print("SECTION TYPE: " + str(section_type))                                                                                                                                                                    
    print("SECTION LENGTH: " + str(section_length))                                                                                                                                                                
    if section_type == 3 or section_type == 8:                                                                                                                                                                     
        fmt = "<" + str(section_length) + "c"                                                                                                                                                                      
        section_value, = struct.unpack(fmt, data[i:i+section_length]); i += section_length                                                                                                                         
    elif section_type == 5:                                                                                                                                                                                        
        section_value = []                                                                                                                                                                                         
        for k in range(0, section_length / 4):                                                                                                                                                                     
            word, = struct.unpack("<L", data[i:i+4]); i += 4                                                                                                                                                       
            section_value.append(word)                                                                                                                                                                             
    elif section_type == 2:                                                                                                                                                                                        
        section_value = []                                                                                                                                                                                         
        for k in range(0, section_length / 8):                                                                                                                                                                     
            word, = struct.unpack("<q", data[i:i+8]); i += 8                                                                                                                                                       
            section_value.append(word)                                                                                                                                                                             
    elif section_type == 4:                                                                                                                                                                                        
        section_value = []                                                                                                                                                                                         
        for k in range(0, section_length / 8):                                                                                                                                                                     
            dbl, = struct.unpack("<d", data[i:i+8]); i += 8                                                                                                                                                        
            section_value.append(dbl)                                                                                                                                                                              
    elif section_type == 6:                                                                                                                                                                                        
        latitude, longitude, = struct.unpack("<dd", data[i:i+16]); i += 16                                                                                                                                         
        section_value = (latitude, longitude)                                                                                                                                                                      
    elif section_type == 7:                                                                                                                                                                                        
        section_value, = struct.unpack("<L", data[i:i+4]); i += 4                                                                                                                                                  
        if section_value < 0 or section_value >= section_count:                                                                                                                                                    
            section_value = "INVALID SECTION"
    elif section_type == 1:                                                                                                                                                                                        
        section_value = "PNG IMAGE. WRITING TO FILE IMAGE.PNG"                                                                                                                                                     
        raw_data = data[i:i+section_length]; i += section_length                                                                                                                                                   
        magic_bytes = "89504E470D0A1A0A"                                                                                                                                                                           
        total_data = magic_bytes.decode("hex") + raw_data                                                                                                                                                          
        png = open("image.png", "w")                                                                                                                                                                               
        png.write(total_data)                                                                                                                                                                                      
    else:                                                                                                                                                                                                          
        section_value = "INVALID SECTION"                                                                                                                                                                          
    print("SECTION VALUE: " + str(section_value))                                                                                                                                                                  
    print