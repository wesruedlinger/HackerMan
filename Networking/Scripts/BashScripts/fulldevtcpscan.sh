#!/bin/bash

for i in {1980..1989}
do
	echo >/dev/tcp/172.16.182.110/$i &&
	echo "Port $i is open" || echo "Port $i is closed"
done
