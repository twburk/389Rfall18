Writeup 10 - Crypto II
=====

Name: *Travis Burk*
Section: *0201*

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Travis Burk*

## Assignment 10 Writeup

### Part 1 (70 Pts)
*Flag Found - CMSC389R-{i_still_put_the_M_between_the_DV} . Output of script can be found in outputScript.txt. My thought process for this part was to first establish a connection to the server using socket and the given IP/port numbers. Once a connection is established my first thought was to get the legit hash. I did this by entering 1 into the server and sending in my created message, "testing". This will send back data that will contain my legit hash. This hash starts at index 40. My legit hash was "5137a1e7b1a3ce4cddf1871c7118c074". The next step was creating a fake hash. I entered a new malicious message, "badTesting", then got the md5 hexdigest. My fak hash was "abccdae236d2971e0e1d73f877a18c7e". Finally, for the hard part. After several days of trying I was able to come up with a good solution to break the server. For starters I created a for loop that will iterate from 6 to 15, since we do not know which bits the secret is. For each iteration we will get the length of the message plus the secret length (6-15). The padding length will change depending on the secret size, so 56 - the message length will give you the padding length. From there i created another for loop that will iterate from 1 to the padding legnth, taking on "\x00" to the padding at each iteration. Once the for loop is finished we will tak on the bits to the ending of the padding, by multipling 8 to the message size and passing that number into struct.pack("<q", <place it here"). After the padding is complete we construct the payload by appending message plus padding plus the malicious message. We enter 2 in the server and pass in the payload then the fake hash. We keep doing this until eventually the server realizes it has a bug. It then gives us the flag to keep quiet about this. The payload that was correct in making the server give us the flag is "testing\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x88\x00\x00\x00\x00\x00\x00\x00badTesting".*

### Part 2 (30 Pts)
*For this section I first had to install gpg to my laptop. The command for this is "brew install gnupg". Next I had to generate my own keys. The command for this is "gpg --gen-key". After hitting enter it will ask you several questions, Name, Email, Acceptance, and password. After completing the requirements, I was granted my public and private keys. Next on the to-do list was importing the public key given to us through the is exercise. By typing this command "gpg --import " followed by the .key file in the directory I now can encrypt a message to this recipient. After this I created a text file with my message inside, this can be found at myMessage.txt. After saving that file I ran this command from the command line "gpg -e -u "Travis Burk" -r "UMD Cybersecurity Club" myMessage.txt" and then I confirm with a "y". What this command did was encrypt my text file using the UMD Cybersecurity Club public key. This new file was placed in my directory as myMessage.txt.gpg. After that I just simply renamed the file to message.private by executing "mv myMessage.txt.gpg message.private" in the command line.*



