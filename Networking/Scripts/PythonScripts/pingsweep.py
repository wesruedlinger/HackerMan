#!/Users/redspartan/Documents/Development/VirtualEnv/bin/python
import os
activeIP = []
subnet = input('Enter the first three octets: ')
while True:
    octet4 = int(input('Enter a starting octet: '))
    endOctet = int(input('Enter an ending octet: '))
    break

while octet4 <= endOctet:
    ipAddr = subnet + '.' + str(octet4)
    print("\nScanning " + ipAddr)
    pingResponse = os.system('ping ' + ipAddr + ' -c 4 -t 3' + " >/dev/null")
    if pingResponse == 0:
        print("Active IP")
        activeIP.append(ipAddr)
        octet4 += 1
    else:
        print("Inactive IP")
        octet4 += 1 
print("\n" + "Your Active IPs are:" + "\n" + ", ".join(activeIP) + "\n")
print('End of Script')
