Writeup 3 - OSINT II, OpSec and RE
======

Name: *Travis Burk*
Section: *0201*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Travis Burk*

## Assignment 3 Writeup

### Part 1 (100 pts)
*The three vulnerabilities I would choose to alert Fred Kruegster about would be weak username/password, social media, and his html source code. Starting with the main issue of his lack of privacy in his social media accounts, I was able to find most of what I needed from there. Once I found his twitter account, I found a link to his company page which I was able to find his personal email. To further the evidence, I used his username and email to find his Instagram. From there I was able to find the plane ticket that lead me to find the flag in his company server. His other Instagram post showed an interest in pokemon which would come in handy soon. My solution for this problem would be to remove his company’s page from his twitter and set all his accounts too private. Moving onto the next problem of weak username and password, I was able to guess his username by looking at his professional email. As for Fred’s password, it is extremely weak. A simple python script using the rockyou.txt file was able to find his password within minutes. Once finding the password to be “pokemon” this could be paired with his love of pokemon pictures on his Instagram. Another hacker could simply guess this password without even writing a script. To solve this I would recommend using a stronger encrypted password, mixing in numbers and symbols. For his username I would stray away from handles that can be linked to his social media and emails. Finally, the last vulnerability I would relay to Fred was his company’s page source code. I would tell him from just looking at his source code I was able to find secret directories, 2 flags, and the sites IP address that lead to me finding wasted ports to gain access to the server. I would recommend enhancing his html/JS code so that users could not see all the information in the source code. I would also recommend locking down the robots.txt file, and removing the flag. This will stop the users from poking into things and finding sensitive material.*
