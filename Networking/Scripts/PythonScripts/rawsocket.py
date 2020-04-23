#import for socket creation
import socket

#import for structuring the packet
from struct import *

#import for system level commands
import sys

#import for encoding / decoding binascii
#import binascii

### Create a raw socket with error handling ###
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
except socket.error as msg:
	print(msg)
	sys.exit()

### Create the variable for the IPv4 header ###
saddr = ""
daddr = ""

ip_ver_ihl = 0x45	#standard versoin and IHL
ip_tos = 0x60		# DSCP 24 and no ECN (or 96 for decimal)
ip_lenght = 0		#kernel will fill this in
ip_id = 12345		#pick one
ip_frag = 0x2000	#combination of frag flags and offset (for more frag bit set)
ip_ttl = 128 		#default ttl of a windows machine
ip_proto = 16		#IP protocols (no additional header) 16 is for chaos
ip_check = 0		#filled in by kernel
ip_saddr = socket.inet_aton("10.10.0.40")	#dotted decimal notation str converted to 32 bit data
ip_daddr = socket.inet_aton("172.16.1.15")	#dotted decimal notation str converted to 32 bit data

### Combine variables into network order to send ###
# format of '!' is determining if the variables are packed into Network Order.
# from characters after the '!', you can use 'B' (1 Byte as int), 'H' (2 Bytes as int), 'L' (4 Bytes as int), '4s' (4 Bytes as string)
ip_header = pack('!BBHHHBBH4s4s', ip_ver_ihl, ip_tos, ip_lenght, ip_id, ip_frag, ip_ttl, ip_proto, ip_check, ip_saddr, ip_daddr)

### Create a data variable to send a message ###
data = b"Hello World"

### Encode message with binascii ###
#encoded = binascii.b2a_uu(data)

### Combine ip header with data ###
packet = ip_header + data
#packet - ip_header + encoded

### Uses sendto() function since we are not establishing connection ###
s.sendto(packet, ("172.16.1.15", 0))
