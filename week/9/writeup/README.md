Writeup 9 - Crypto I
=====

Name: *Travis Burk*
Section: *0201*

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Travis Burk*

## Assignment 9 Writeup

### Part 1 (60 Pts)
*The passwords and salts for each hash can be found in the part1_output.txt file. 
Process: To brute force this problem, we must first open the password file and the hash file. In my code the variable for each would be wordlist, and hashes. From there I nested three for loops. The outter most for loop will go through each hash in the file, h, and will execute the next two for loops on each hash. The second for loop will go through each password in the file. Before this happens we point the file back to the begginning by calling wordlist.seek(0). We do this because after going through the list for the first hash the file does not begin over for the next hash. After getting each password from the file we will append each lower case letter to the beggining by having the third for loop go through all 26 letters and append it to the begginning of that word. Each time we append the character to the word we will get the sha512 hash of the new word and compare it to the testing hash. If it is equal print the salt and password that passed this case if not try the remaining characters and passwords in the file.*

### Part 2 (40 Pts)
*Flag : CMSC389R-{H4sh-5l!ngInG-h@sH3r}*

*Process : My throught process of coding this script was to have a while loop to keep executing until the user types in "quit". In the beginning of the while loop it will print the data recieved from the server. Following the print of the data I put a raw_input command that will ask the user for the answer of the question. I then would go online and manually find the hash of the password. After running this twice i realized there was a time limit of 10 seconds to get the answers. I then changed my script to answer the questions automoatically. I start by modifying the while loop to online run while the counter does not equal 10 (since there is only 10 questions). Once in the while loop we will split the data by whitespaces. This will return an array of all the strings in the data. If the counter is 0, we will set sha to be the 9 index of the array and passw to the 12 index of the array, if the counter is anything other than 0 sha will be the 3 index and passw will be the 6 index. This is because the server returns more strings in data when the first question is asked. From there we will reset passw to be the first 10 characters of its string, passw at first will contain a new line char and >>> at the end of the string. We are only worried about the characters we need to hash. Next I created If/elif statement that compares sha to all the hashlib sha. Depending on what if statement is true we will hash passw with that hash function. Finally we will send the hash to the server to get a correct result for that question. After answer all 10 questions I recieve the flag stated above.*


