Writeup 10 - Crypto II
=====

Name: *Travis Burk*
Section: *0201*

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Travis Burk*

## Assignment 10 Writeup

### Part 1 (70 Pts)


### Part 2 (30 Pts)
*For this section I first had to install gpg to my laptop. The command for this is "brew install gnupg". Next I had to generate my own keys. The command for this is "gpg --gen-key". After hitting enter it will ask you several questions, Name, Email, Acceptance, and password. After completing the requirements, I was granted my public and private keys. Next on the to-do list was importing the public key given to us through the is exercise. By typing this command "gpg --import " followed by the .key file in the directory I now can encrypt a message to this recipient. After this I created a text file with my message inside, this can be found at myMessage.txt. After saving that file I ran this command from the command line "gpg -e -u "Travis Burk" -r "UMD Cybersecurity Club" myMessage.txt" and then I confirm with a "y". What this command did was encrypt my text file using the UMD Cybersecurity Club public key. This new file was placed in my directory as myMessage.txt.gpg. After that I just simply renamed the file to message.private by executing "mv myMessage.txt.gpg message.private" in the command line.*



