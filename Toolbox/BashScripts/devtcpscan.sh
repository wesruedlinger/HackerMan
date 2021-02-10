#!/bin/bash
#single IP scan for open ports of interest
for port in {20..65535}
do
	>/dev/tcp/$1/$port 2>&1 &
done | grep -E 'succ|open$|OK$'

