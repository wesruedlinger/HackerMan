#!/bin/bash
IP=$(for i in {1..254}; do (/bin/ping -c1 192.168.28.$i | egrep "bytes from" | cut -d' ' -f4 | cut -d':' -f1 &); done)
for j in $IP; do for k in {20..10000}; do nc -nzvw1 $j $k 2>&1 & done | grep -E 'succ|open' | cut -d' ' -f3-4; done

#run on remote system from OPS(or system that can see the network of interest)
#ssh student@10.50.28.45 -t /bin/bash < all24.sh
