#!/bin/bash

for i in {1..254}
do
	nc -nzvw1 $1.$i 0-65535 2>&1 &
done | grep -E 'succ|open$'

# sends all scans to background, then greps from the entire loop, 
# looking for success or open at the end of the line
