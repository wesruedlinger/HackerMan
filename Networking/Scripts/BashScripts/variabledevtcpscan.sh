#!/bin/bash


for port in `seq $2 $3`
do
	echo > /dev/tcp/$1/$port &&
	echo "Port $port is open" ||
	echo "Port $port is closed"
done
