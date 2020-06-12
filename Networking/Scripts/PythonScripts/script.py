#!/Users/redspartan/Documents/Development/VirtualEnv/bin/python
#!/usr/local/bin/nmap
import os

activeIP = []
while True:
    print("What would you like to do?")
    option = int(input("1.   Pingsweep \n2.   NMAP \n3.   Quit \n>>> "))

#Quit Option
    if option == 3:
        break

#Ping Sweep Option
    if option == 1:
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
        print('End of ping sweep')

#NMAP Option
    if option == 2:
        choice = int(input("Do you what to enter an IP (1) or scan Active IPs found from ping sweep (2)? "))
        if choice == 1:
            newIP = str(input("Enter IP: "))
            os.system('sudo nmap -O ' + newIP)
        if choice == 2:
            for x in activeIP:
                os.system("sudo nmap -O " + x)

print('GoodBye')
