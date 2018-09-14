OSINT (Open Source Intelligence)
======

## Assignment details

This assignment has two parts. It is due by Thursday, September 13 at 11:59 PM.

To submit your homework, please follow the guidelines posted under the grading section of the syllabus.

**There will be a late penalty of 5% off per day late! Submissions received more than 3 days late will receive a 0!**

### Part 1

In class you were given an online usertag: `kruegster1990`

NOTE: "briefly describe" = 2-3 sentences (and/or include screenshot(s))

Use OSINT techniques to learn as much as you can about `kruegster1990` and answer the following questions:

1. What is `kruegster1990`'s real name?
	*Kruester1990's real name is Fred Kruester. I found this by doing a quick google search. The search returned multiple websites, one of which included the UMD Cybersecurity stwity site.*

2. List all personal information (including social media accounts) you can find about him. For each, briefly detail how you discovered them.
	*Name : Fred Kruegster. Obtained by doing a quick google search.
	 Twiiter : Kruegster1990. In the process of doing the google search, i found a link to his personal twitter account.
	 Email : kruegster1990@tutanota.com. On his twitter account he had his work website listed. Once I navigated to this site, i 									 went to the 'About' section and found his email/user photo that matches his twitter.*

3. What is the IP address of the webserver hosting his company's site? How did you discover this?
	*IP Address: 142.93.117.193
	I got this by going to Krugsters company web page 'cornerstoneairlines.co' and navigating to the admin tab. Once I made it to that tab, i saw that the page was under construction, but the URL was this IP address. Additionally if you navigate
	back to the index.html file and view the source code you will find the IP adress there to.*

4. List any hidden files or directories you found on this website. Did you find any flags?
	*/Secret is a hidden directory of this site. I found this by navigating to the robots.txt file on this site. From there I saw 
	that the directory /secret was disallow. When i navigated to this directory, it was a blank page. However when you view the page source i found the first flag. CMSC389R-{fly_th3_sk1es_w1th_u5}*

5. Did you find any other IP addresses associated with this website? What do they link to, or where did you find them?
	*While navigating throughout the cornerstoneairlines.co page i did not find any other IP address other than the main one associated with the site. When i 	censys.io the address, it did not pull up any other IP address either.*

6. If you found any associated server(s), where are they located? How did you discover this?
	*Location : New York, New York. 
	Server : Apache httpd 2.4.18
	I got this by going to shodan.io and plugging in the IP address that i found. From There I discovered the location of the server is in the United States and in New York City. I confirmed this by going to censys.io and plugging in the same IP, the results showed that the server is located in New York, New York and labeled the Server.*

7. Which operating system is running on the associated server(s)? How did you discover this?
	*OS : Ubuntu. I gathered this information when I was searching for the location of the server. When i went to censys.io and plugged in the IP address the first column of the basic information listed the OS as ubuntu.*

8. **BONUS:** Did you find any other flags on your OSINT mission? (Up to 9 pts!)
	*Flag 1 : CMSC389R-{fly_th3_sk1es_w1th_u5}
	 Flag 2 : CMSC389R-{h1dden_fl4g_in_s0urce}*

### Part 2

Use the provided python stub code [('stub.py')](stub.py) or write your own program in another language to gain access to the Cornerstone Airlines administrator server via an open port that you should have found in Part 1. 

Once you have gained access to the Cornerstone Airlines administrator portal with the correct login credentials, you will have access to a system shell. 

Use your knowledge of Linux and OSINT techniques to locate a specific flight record, read it, and submit the flag inside.

Your response here should briefly document how you approached and solved this part of the assignment. You should also push your bruteforce program to the "week/2/writeup" folder of your GitHub repository.

Note: If you choose to write your own program in another language, please include instructions on how to execute your program, including what version of the language you are using. You will **NOT** receive credit if the TAs cannot run your program.

If you are stuck on this part of the assignment, let us know! The facilitator staff is here to help and teach, and we are open to releasing hints as time goes on!

*IP Address : 142.93.117.193 -- Found on the admin page of          			cornerstoneairlines.co

Port : 1337 -- After running an nmap on the above IP address I Found 				that there were several ports open. I knew this was the 				correct one because it was labeled as waste. 

User Name : kruegster -- Based off of trial an error, i determine to 			   use Fred's email adress as the username.

Password : pokemon -- After running the stub.py program, and waiting		   around 30 mins i determine that the password pokemon was a 
			success

In my terminal i ran nc 142.93.117.193 1337 and when promoted for the user name and password i entered the above and was successfully logged into the admin acount. I then cd'd to multiple directories, until i went into the home directory. Once i was in there i found another directory called flight_records. Once in there, there was a list of txt files that all contain flags. I determined *

### Format
In the "week/2/writeup" directory of our repository there is a README.md file for you to edit and submit your homework in. Use this as a template and directly edit it with your answers. Complete your bruteforce program in this directory as well. When you've finished the assignment, [Push it](https://github.com/UMD-CS-STICs/389Rfall18/blob/master/HW_Submit_Instructions.md) up to your personal GitHub for us to grade.

Your responses to every prompt in this assignment should include answers to any specific questions along with a brief explanation of your thought process and how you obtained the answer.

### Scoring

Part 1 is worth 45 points, and part 2 is worth 55 points.

### Tips

Reference the slides from lecture 2 to help you effectively utilize available OSINT techniques.
