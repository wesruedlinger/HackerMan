#!/bin/bash
# syntax --> ./slow_scan.sh 192.168.1 1 254 
for i in `seq $2 $3`
do
	nc -nvz -w1 $1.$i 21 22 23 80 2&>1 |  grep -E 'succ|open$'
done


