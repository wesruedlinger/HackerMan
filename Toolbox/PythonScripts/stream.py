import socket

#Create Variable to open stream socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)

#By default
# s = socket.socket()

#Create socket IP and Port
ipaddr = "172.16.1.15"
port = 5309 #or hex number

# Connection setup
s.connect((ipaddr, port)) #or address = ipaddr, port

#to send a messsage it must be bits like format. To do that add the prefix 'b' to a string.
message = b"Jenny"

#send my message
s.send(message)

#you can receive a response by splitting the response into data and address information
# it is recommended that the buffer size for recieving is a power of 2 and not too large. (in bytes)
response, conn = s.recvfrom(1024)

#In oder to actually see the response you must print and decode the data into UTF-8.
#It does decode(UTF-8) by default
print(response.decode())

#always close TCP connection
s.close()
