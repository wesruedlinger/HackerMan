#!/bin/bash

for i in {1..30}
do
	nc -nvz -w1 172.16.1.$i 21 22 23 80 443
done

