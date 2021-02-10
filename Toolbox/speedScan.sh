#!/bin/bash

echo "Enter network's first three octets: "
read net
echo "Enter starting host range: "
read start
echo "Enter ending host range: "
read end
echo "Enter ports space-delimited: "
read ports
echo "File Name: "
read filename

clear

IFS=' '
read -ra ADDR <<< "$ports"

portsS=""

for u in "${ADDR[@]}"; do
    if [[ "$u" == "-" ]]; then
        IFS='-'
        read -ra TEMP <<< "$u"
        for o in $(seq ${TEMP[0]} ${TEMP[1]}); do
            portsS="$portsS$o"$'\n'
        done
    else
        portsS="$portsS$u"$'\n'
    fi
done

IFS=$'\n'
read -rd '' -a ADDRS <<< "$portsS"

for ((i=$start; $i<=$end;i++))
do
    for t in "${ADDRS[@]}"; do
        printf "\033[0;0HWorking on host $net.$i port $t"
        nc -nzv -w1 $net.$i $t 2>&1 | grep -E "succ|open$" >> $filename &
    done
done
echo -E "\n"
