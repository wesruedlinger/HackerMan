#!/bin/bash
#scans a network for active IPs and and open ports
for i in {1..254}
do
	nc -nzvw1 $1.$i 20 21 22 23 80 443 2>&1
done | grep -E 'OK$|open$|succ'

# sends all scans to background, then greps from the entire loop, 
# looking for success or open at the end of the line
