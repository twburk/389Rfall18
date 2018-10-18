Writeup 7 - Forensics I
======

Name: *Travis Burk*
Section: *0201*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Travis Burk*

## Assignment 7 writeup

### Part 1 (40 pts)

1. JPEG

2. This photo was taken in Chicago Illinois. The buildings that are in the photo "John Hancock Observatory" and "875 North Michigan Avenue" 

3. This Photo was taken 2018:08:22 11:33:24

4. This photo was taken on a Apple Iphone 8. It was taken on the back camera 3.99mm f/1.8. 

5. This photo was taken 539.5 m above sea level.

6. After using strings and the grep command i was able to find this flag: 
CMSC389R-{look_I_f0und_a_str1ng}

### Part 2 (60 pts)

*There is multiple steps one should take while trying to reverse engineer this binary file. To begin the first step one should take is to use radare2 and rabin2. By using these two tools, we will be able to find which C function this assembly code is using. The command I used is "rabin2 -i binary" which returns a list of functions the code is using. This particular command showed a list of 9 functions, but three of them stuck out to me the most. The three functions were "fopen" "fwrite" and "fclose". By seeing these three functions i know that some file is being opened and modified in this code. So, my next step was to use the debugging to GDB. I rab the command "gdb binary" and set breakpoints at "main", "fopen", "fwrite" and "fclose". After setting the break points I started the code, and stepped through in line by line. By doing this I found that the argument being passed into "fopen" as the file is "/tmp/.stego". My next instinct was to try printing the file in GDB, but after running that command I realized that was not possible. So, next I opened another terminal and CD back to this week’s write-up. After getting into that directory, I tried CDing to the files directory “cd /tmp/.stego”; however, this was unsuccessful too. Next, I just CD to the tmp directory, “cd tmp”, which contained more directories. All of which did not contain any information regarding the flag. I then was directed to download a hex editor, I choose hexcurse. Once downloaded I converted the .stego file to a JPG file by running the command "cp .stego stego.JPG" and viewed the file in hexcurse. I compared that file to the image.jpg provided to us in part 1. The key difference i noticed was that the image starts for FF while the stego file starts with 00.*
