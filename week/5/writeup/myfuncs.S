section .text         ;declare this section to include executable instructions

global my_memset      ;export the 'my_memset' symbol to be accessible outside of file
my_memset:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame

	mov rax, rsi  ;move the byte to al pointer
	mov rcx, rdx  ;move the counter to rcx
	rep stosb     ;repeat store byte from al to [rdi]
		      ;and increase rsi (if direction flag cleared)
    		      ;decrease rcx and if rcx is zero, break out

	leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!
	
	
	


global my_strncpy     ;export the 'my_strncpy' symbol to be accessible outside of file
my_strncpy:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame

	mov rcx, rdx  ;move third parameter to counter register

help:		      				     ;helper function
	mov rbx, rdx  				     ;rbx will be size of third parameter
	sub rbx, rcx  				     ;rbx will be distance of string to modify
	mov byte ptr[rdi + rbx], byte ptr[rsi + rbx] ;replace characters 
	loop help     				     ;decrease rcx by 1, if rcx != 0 then jump back to top of help.
        


        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!
