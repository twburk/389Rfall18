Writeup 2 - OSINT (Open Source Intelligence)
======

Name: *PTravis Burk*
Section: *0201*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Travis Burk*

## Assignment 2 writeup

### Part 1 (45 pts)

1. *Kruester1990's real name is Fred Kruester. I found this by doing a quick google 	search. The search returned multiple websites, one of which included the UMD 		Cybersecurity stwity site.*

2. *Name : Fred Kruegster. Obtained by doing a quick google search.
	 Twiiter : Kruegster1990. In the process of doing the google search, i found a link to his personal twitter account.
	 Email : kruegster1990@tutanota.com. On his twitter account he had his work website listed. Once I navigated to this site, i went to the 'About' section and found his email/user photo that matches his twitter.
	 Another Email : KRUEGSTER1990@GMAIL.COM. I found this on spokeo.com, with the same profile pic as his twitter.
	 Instagram : Kruegster1990. Using intelteqniques.com I managed to find Freds IG profile.*

3. *IP Address: 142.93.117.193
	I got this by going to Krugsters company web page 'cornerstoneairlines.co' and navigating to the admin tab. Once I made it to that tab, i saw that the page was under construction, but the URL was this IP address. Additionally if you navigate
	back to the index.html file and view the source code you will find the IP adress there to.*

4. */Secret is a hidden directory of this site. I found this by navigating to 			robots.txt file on this site. From there I saw that the directory /secret was 		disallow. When i navigated to this directory, it was a blank page. However When 	you view the page source i found the first flag. 									CMSC389R-{fly_th3_sk1es_w1th_u5}*

5. *While navigating throughout the cornerstoneairlines.co page i did not find			another IP address other than the main one associated with the site. When I 		censys.io the address, it did not pull up any other IP address either.*

6. *Location : New York, New York. 
	Server : Apache httpd 2.4.18
	I got this by going to shodan.io and plugging in the IP address that i found. From There I discovered the location of the server is in the United States and in New York City. I confirmed this by going to censys.io and plugging in the same IP, the results showed that the server is located in New York, New York and labeled the Server.*

7. *OS : Ubuntu. I gathered this information when I was searching for the location 		of the server. When i went to censys.io and plugged in the IP address the first 	column of the basic information listed the OS as ubuntu.*

8. *(BONUS)*
	*Flag 1 : CMSC389R-{fly_th3_sk1es_w1th_u5}
	 Flag 2 : CMSC389R-{h1dden_fl4g_in_s0urce}*

### Part 2 (55 pts)

*IP Address : 142.93.117.193 -- Found on the admin page of          			cornerstoneairlines.co

Port : 1337 -- After running an nmap on the above IP address I Found 				that there were several ports open. I knew this was the correct one because it was labeled as waste. 

User Name : kruegster -- Based off of trial an error, i determine to 			   use Fred's email adress as the username.

Password : pokemon -- After running the stub.py program, and waiting		   around 30 mins i determine that the password pokemon was a success

In my terminal i ran nc 142.93.117.193 1337 and when promoted for the user name and password i entered the above and was successfully logged into the admin acount. I then cd'd to multiple directories, until i went into the home directory. Once i was in there i found another directory called flight_records. Once in there, there was a list of txt files that all contain flags. I determined that the final flag is CMSC389R-{c0rn3rstone-air-27670}. I got this by going on his IG and finding his flight ticket. On the third pic of the ticket i found AAC27670, which is in the flight record directory.*
