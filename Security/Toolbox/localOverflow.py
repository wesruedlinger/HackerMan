# Outlined below is the general process for performing a Local Buffer Overflow
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
# YOUR TURN, DEVELOP YOUR OWN EXPLOIT                                         #
#       - Identify and Add the expected variables to your exploit             #
###############################################################################
user@host:~# nano exploit.py


	buffer = "teststringvalue"

	shellcode = buffer
	print(shellcode)

user@host:~# python exploit.py > exploitstring
user@host:~# gdb filename
(gdb) run < exploitstring


###############################################################################
# Step 1: Find the Buffer Size/Offset (PATTERN)                               #
#       - use gdb to determine buffer size                                    #
###############################################################################
user@host:~# nano exploit.py


	shellcode = buffer +
	print(shellcode)

user@host:~# python exploit.py > exploitstring


###############################################################################
# Step 2: Validate EIP Overwrite                                              #
#       - Check that you can overwrite the EIP                                #
#       - Have you added any NOP's                                            #
###############################################################################
user@host:~# nano exploit.py


	shellcode = buffer +
	print(shellcode)

user@host:~# python exploit.py > exploitstring


###############################################################################
# Step 3: Identify Bad Characters to exclude during shellcode generation      #
#       - Generator a list of all hex chars 0x00 - 0xFF                       #
###############################################################################
user@host:~# nano exploit.py


	shellcode = buffer +
	print(shellcode)

user@host:~# python exploit.py > exploitstring


###############################################################################
# Step 4: Find a Valid JMP ESP (Assembly Instruction)                         #
#       - JMP ESP values are 0xff, 0xe4                                       #
#       - What Architecture is the Executable                                 #
#              Does the EIP need to be Little Endian                          #
###############################################################################
user@host:~# env - gdb filename
(gdb) unset env LINES
(gdb) unset env COLUMNS
(gdb) run < exploitstring
(gdb) info proc mapping


###############################################################################
# Step 5: Generate Shellcode & Run Exploit                                    #
#       - Using msfvenom or msfconsole generate an appropriate payload        #
#              linux/x86/exec                                                 #
###############################################################################
user@host:~# msfconsole
msf > use linux/x86/exec
msf > set CMD 'YOUR COMMAND'
msf > generate -b 'BAD CHARACTERS' -f python


user@host:~# nano exploit.py


	shellcode = buffer +
	print(shellcode)

user@host:~# python exploit.py > exploitstring
