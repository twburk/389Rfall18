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

1. *The timestamp that was generated from the document is 1540428007. By plugging that timestamp into a website "epochconverter.com" I was able to convert the timestamp to an actual date and time. The time would be Wednesday, October 24, 2018 at 8:40 pm.*

2. *The author of the document is the user laz0rh4x.*

3. *The header of the document states that there is 9 sections in the document; however the actual section count is 11.*

4.

5.
