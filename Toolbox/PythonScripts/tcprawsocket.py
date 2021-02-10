# Begin imports
import socket
from struct import *
import sys
# Add array for TCP checksum
import array

# attempt tp create a raw socket with error handling
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
except socket.error as msg:
	print(msg)
	sys.exit()

# IP variable setup
src_ip = "10.10.0.40"
dst_ip = "172.16.40.10"

# Construct the IPv4 header variables
ip_ver = 4		#set to 4 for normal traffic
ip_ihl = 5 		#set to 5 for normal traffic
ip_dscp = 0		#set to the dscp value wanted
ip_ecn = 0 		#set to the value needed if ECE is set
ip_len = 0		#kernel will fill this in
ip_id = 12345		#set to what you want
ip_frag_res = 0		#used for the reserve frag flag
ip_frag_df = 0          #used for the DF frag flag
ip_frag_mf = 0          #used for the MF frag flag
ip_frag_offset = 0      #used for frag offset values
ip_ttl = 0		#set to TTL you want
ip_proto = 6		#set to 6 or socket.IPPROTO_TCP
ip_check = 0		#kernel will fill this in
ip_saddr = socket.inet_aton(src_ip)
ip_daddr = socket.inet_aton(dst_ip)

# Combined variables as needed
ip_ver_ihl = (ip_ver<<4) + ip_ihl	#left shift version by 4
ip_tos =  (ip_dscp<<2) + ip_ecn		#left shift dscp by 2

# Fragmentation field - combine frag flags then add to frag offset
ip_frag_flags = (ip_frag_res<<15) + (ip_frag_df<<14) + (ip_frag_mf<<13)
ip_frag = ip_frag_flags + ip_frag_offset

# Pack the header use the '!' for network order and using only complete variable
# After ! the values are 'B' (1 byte int), 'H' (2 Bytes int), 'L' (4 Bytes int), '4s' (4 Bytes strings)

ip_header = pack('!BBHHHBBH4s4s', ip_ver_ihl, ip_tos, ip_len, ip_id, ip_frag, ip_ttl, ip_proto, ip_check, ip_saddr, ip_daddr)

# Create TCP header variables
tcp_src_port = 48888		#set tcp source port - use RHP
tcp_dst_port = 3389 #RDP	#set tcp dest port - use 3389 for RDP
tcp_seq_num = 1			#set sequence number
tcp_ack_num = 0			#set to 0 unless used with ACK flag
tcp_offset = 5			#set to 5 for tcp with no options (offset * 4 for the tcp header size)
tcp_res = 0			#set to 0 as reserved

# Create tcp flag variables per bit location
tcp_cwr = 0		#TCP CWR Flag
tcp_ece = 0             #TCP ECE Flag
tcp_urg = 0             #TCP URG Flag
tcp_ack = 0             #TCP ACK Flag
tcp_psh = 0             #TCP PSH Flag
tcp_rst = 0             #TCP RST Flag
tcp_syn = 0             #TCP SYN Flag
tcp_fin = 0             #TCP FIN Flag

# Continue creating tcp header variables
#tcp_window = 5840
tcp_window = socket.htons(5840)
tcp_check = 0		#will be set below
tcp_urg_pointer = 0	#this will be set when URG flag is set

# Combine TCP fields into complete bytes as needed
tcp_off_res = (tcp_offset<<4) + tcp_res

tcp_flags = (tcp_cwr<<7) + (tcp_ece<<6) + (tcp_urg<<5) + (tcp_ack<<4) + (tcp_psh<<3) + (tcp_rst<<2) + (tcp_syn<<1) + tcp_fin

# Pack the TCP header IOT fill in the tcp checksum - tcp checksum is not in network order
# After ! the values are 'B' (1 byte int), 'H' (2 Bytes int), 'L' (4 Bytes int), '4s' (4 Bytes strings)
tcp_header = pack('!HHLLBBH', tcp_src_port, tcp_dst_port, tcp_seq_num, tcp_ack_num, tcp_off_res, tcp_flags, tcp_window) + pack('H', tcp_check) + pack('!H', tcp_urg_pointer)

# Create a varible for user data
user_data = b"Hello"

# Create Pseudo header for checksum calculation
src_address = socket.inet_aton(src_ip)		#from IP header
dst_address = socket.inet_aton(dst_ip)		#from IP header
reserved = 0					#8 bits reserved for padding
protocol = socket.IPPROTO_TCP			#from ip header = 6
tcp_lenght = len(tcp_header) + len(user_data)	#combined length of tcp header and tcp data (user data)

# Pack the pseudo header to combine with user data
# After ! the values are 'B' (1 byte int), 'H' (2 Bytes int), 'L' (4 Bytes int), '4s' (4 Bytes strings)
ps_header = pack('!4s4sBBH', src_address, dst_address, reserved, protocol, tcp_lenght)

# Combine Pseudo header with TCP header and user data
ps_header = ps_header + tcp_header + user_data

# Build def for TCP checksum calculation
def checksum(data):
	if len(data) % 2 !=0:
		data += b'\0'
	res = sum(array.array("H", data))
	res = (res >> 16) + (res & 0xffff)
	res += res >> 16
	return (~res) & 0xffff

# Recreate TCP checksum variable && repack tcp header including new checksum value (resue previous tcp header pack from above) 
tcp_check = checksum(ps_header)
tcp_header = pack('!HHLLBBH', tcp_src_port, tcp_dst_port, tcp_seq_num, tcp_ack_num, tcp_off_res, tcp_flags, tcp_window) + pack('H', tcp_check) + pack('!H', tcp_urg_pointer)

# Combine IP header with new TCP header and user data
packet = ip_header + tcp_header + user_data

# Send the packet to the destination
s.sendto(packet, (dst_ip, 0))
