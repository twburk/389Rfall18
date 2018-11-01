Writeup 8 - Forensics II, Network Analysis and File Carving/Parsing
=====

Name: *Travis Burk*
Section: *0201*

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Travis Burk*

## Assignment 8 Writeup

### Part 1 (45 Pts)
1. *The attackers in fact did use trceroute. By doing a search for "icmp" in wireshark it pulled up multiple attemps to traceroute the same destination. The destination IP address is 142.93.118.186.*

2. *By following the TCP stream on the TCP packet 109 I was able to find the usernames of the two attackers. The two usernames are laz0rh4x and c0uchpot4doz*

3. *By doing the TCP stream on the TCP packets I was able to determine the two IP address that were used during this chat. The two IP addresses are 206.189.113.189 and 142.93.118.186. By doing an IP lookup on the two IP addresses I was able to find that the IP address 142.93.118.186 is from New Jersey and IP address 206.189.113.189 is from London.*

4. *Using the TCP Stream I was able to determine both ports that the attackers were using to communicate via the server. The two ports are 2749 and 53878.*

5. *By taking a look at the chat that the TCP stream was able to generate I was able to determine some useful information. The user laz0rh4x mentioned the "updated plans" and also brings up the time 1500 (3 pm) the next day.*

6. *I also was able to find a link in the chat window. The user laz0rh4x sent a link to a google doc with the file type fpff. He mentions that the document provides the updated plans. The link is : https://drive.google.com/file/d/1McOX5WjeVHNLyTBNXqbOde7l8SAQ3DoI/view?usp=sharing*

7. *As stated in question 5 the attackers plan to meet at 1500 the next day (3pm).*

### Part 2 (55 Pts)

*Report your answers to the questions about parsing update.fpff below.*

*By downloading the file from the sharedrive and placing it in the same directory as my parser I was able to determine the answers to these questions.*

*My thought process on coding stub.py was to handle the header first. By using the struct.unpack function I was able to get the author, timestamp, and section count. Once getting the timestamp, i went online to convert to a human readable date and time. The author is a list of chars, that once put together gave you the username of one of the attackers. I found data length by passing data into the len function. Next I wanted to test if the number of sections was correct. I set my offset to 24 and a counter to 0. Next I created a while loop that will be ran as long as the offset was less than the length of data. Each time the code entered the while loop the section count was increased by one. The offset variable is updated multiple times in the while loop depending on the data parsed (additional information will be found later on). After running the code I found that there was actually 2 more section in the document that the header did not count for. The meat of the code comes from printing the information of each section. I created a dictionary that ranged from 2 to 8 with 2 = DWORDS, 3 = UTF8, 4 = DOUBLES, 5 = WORDS, 6 = COORD, 7 = REFERENCE, 8 = ASCII. Each will also contain a function that will be called depending on the type. The three functions are print_char which will be used for 3, and 8. This will decode the characters depending on the encoding that is also kept in the dictionary. print_int will be used for 4,5,7. Finally, p, will be used for 2 and 6. You will unpack the infroamtion from data based on the current offset of the while loop, test if the type is defined in the dictionary, if so, parse the data and pass into there function to print the data while also updating the offset by adding the size of the data to the offset value. If the type is not in the dictionary but the type equals 1, then it is a png file. I will pass the data into the final function png_out which will create a png file and add the bytes to that file and save it to my directory. Finally, if that is not true then we will skip and check if the offset is still less than the length of data.*

1. *The timestamp that was generated from the document is 1540428007. By plugging that timestamp into a website "epochconverter.com" I was able to convert the timestamp to an actual date and time. The time would be Wednesday, October 24, 2018 at 8:40 pm.*

2. *The author of the document is the user laz0rh4x.*

3. *The header of the document states that there is 9 sections in the document; however the actual section count is 11.*

4. *After running my script and finding that there actually 11 sections, my next train of thought was to add functions to print the data of each section. Using 4 functions, I was able to handle every case. The file output.txt contains the information found in the document, also out.png is an PNG image that was parsed out of the document.*

5.
