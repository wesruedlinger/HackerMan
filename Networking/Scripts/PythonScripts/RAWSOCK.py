import socket, sys, binascii
from struct import *

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
except socket.error as msg:
    print('Socket creation failed! \nError Code - ' + str(msg))
    sys.exit()

packet = ''

source_ip = '10.10.0.40'
dest_ip = '172.16.1.15'

"""
IP header info in decimal. You need to consider the full field size and the decimal therein. 
The ip_ihl_ver field for example is actually read as 2 nibbles, however for ease of coding, 
we're going to just use the decimal value of the entire byte, assuming that the packet is not using IP options.
"""

ip_ver_ihl = 69       # Decimal
ip_tos = 96
ip_len = 0       # kernel will fill this in
ip_id = 1984
ip_frag = 0
ip_ttl = 128
ip_proto = 16
ip_check = 0     # kernel will fill the correct checksum
ip_saddr = socket.inet_aton(source_ip)
ip_daddr = socket.inet_aton(dest_ip)

"""
This portion creates the header by packing the above variables into a structure. 
The ! in the string means network order, while the code following specifies how to store the info. 
These "?"'s should indicate the size of the field that the information contained in the corresponding variables should be stored in. 
The "?"'s should be replaces with B, H or 4s. B=Byte, H=Half-word, 4s=four bytes (a str is a byte long)
"""

ip_header = pack('!BBHHHBBH4s4s' , ip_ver_ihl, ip_tos, ip_len, ip_id, ip_frag, ip_ttl, ip_proto, ip_check, ip_saddr, ip_daddr)

"""
Your custom protocol fields or data. We are going to just insert data here. 
Replace your message where the "MESSAGEDATA" is. Ensure you obfuscate/encode your data! 
You can specify a function for "ENCODEFUNCTION" from the binascii module as in this example, or you can use something else.
b'' will convert the string into a bytes-like object, which is required
"""

user_data = b'Ruedlinger'
hidden_msg = binascii.b2a_hex(user_data)

packet = ip_header + hidden_msg

# Change OBJECT to the correct socket object)
s.sendto(packet, (dest_ip, 0))
