import socket

#Create variable for socket function
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Connect to IP and port using data instead of variable
s.connect(("127.0.0.1", 10000))

#Send a message
s.send(b"Disturbed")

#split the recieved data into data and connection info
response, conn = s.recvfrom(1024)

#split connection info into ip and port
ipaddr, port = conn

#decode() is utf-8 by default
print(response.decode("utf-8"))
