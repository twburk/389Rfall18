Writeup 5 - Binaries I
======

Name: *Travis Burk*
Section: *0102*

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Travis Burk*

## Assignment 5 Writeup

*Converting memcpy into assembly x88-64 only requires a few lines of code. To start you need to allocate space for the stack frame. Then while working with intel assembly the parameters will be placed in rdi, rsi, and rdx. You will move rsi to rax, which is the return pointer. Next you will move rdx to rcx, which is the counter variable. Finally I took advantage of the rep and stosb commands. Rep allows the code to keep executing until the counter pointer, rcx, reaches zero. The command that will execute until the counter reaches zero is stosb. This allows the code to move a byte to rdi. After rep finishes the function will then return the rax pointer. For the strncpy function, I wanted to do this differently so, I chose to use a helper function. I started the function by moving the stack pointer up to create a new frame. Next, i moved the parameter from rdx into the counter variable, rcx. After this executes, the code will enter into the loop. Once in the loop, I save rdx in rbx. This will be done every time the helper function runs. Rbx will always be the size of the third parameter. Next we will subtract the current counter variable from rbx. This will be used to move the pointer of the two string variables. The next two lines I moved the character from the src string into a variable, then moved that variable into the same location in the dst variable. Finally i use the loop command to decrease the counter variable and recall the loop if rcx does not equal zero. The toughest challenge i faced this week was moving the character pointer into a variable. I kept moving them into a register that saves 64 bits, and then i get error messages when trying to move that register into a byte. I found that we have to utilize the register al, to store a byte and avoid these error messages.*

























     *

