#!/bin/bash
# Written by Kenton Groombridge
# Scanner using bash sockets 

# Enter info
set -e # Return immediately from error

printf "Enter three octet prefix: "
read -r prefix

printf "Enter first IP: "
read -r startip

printf "Enter last IP: "
read -r endip

printf "Enter first port: "
read -r startport

printf "Enter last port: "
read -r endport

# Used to speed up scan, but remember proxychains doesn't support ICMP, so you will need to say 'n' here for that.
printf "Trust ping? (y/n): "
read -r ping

printf "Use netcat? (y/n): "
read -r nc

for (( host=startip ; host<=endip ; host++ )) # Scan range of IPs
do
	ip=${prefix}.${host}

	if [[ $ping == "y" || $ping == "Y" ]] # If ping is used, then set 
	then
		if ping -W 1 -c 1 -q ${ip} > /dev/null 2>&1 # ping with wait 1 sec, count 1, quietly, and print nothing, just need return code.
		then
			pingresponse=1
			printf "********** ${ip} is up **********\n"  # this is good to know as if it is pingable and no ports are listed
		else
			pingresponse=0
		fi
	else
		pingresponse=1 # If ping is used, set pingresponse to 1 so we can reguardless
	fi
	
	if [ ${pingresponse} -eq 1 ] # If ping is good, or ping not used
	then
		for (( port=startport ; port<=endport ; port++ )) # scan range of ports
		do
			ip=${prefix}.${host}
			
			if [[ $nc == "y" || $nc == "Y" ]] # Use netcat or bash to scan
			then
				nc -nzvw1 ${ip} ${port} 2>&1 | grep -E 'succ|open' &
			else
				timeout 0.5 bash -c "> /dev/tcp/${ip}/${port}" > /dev/null 2>&1 && printf "${ip} ${port} is open\n" &  # Use bash to touch port and print message if open
			fi
		done
	fi
done
