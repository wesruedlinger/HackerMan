#!/bin/bash

echo "File to Scan: "
read filename

# Get all IPs with port 80 open
website=$(awk '{print $3,$4}' $filename | grep -E '80$' | awk '{print $1}')
for i in $website
    do
        wget -r $i
    done

# Get all IPs with port 21 open
ftpserver=$(awk '{print $3,$4}' $filename | grep -E '21$' | awk '{print $1}')
for i in $ftpserver
    do
        wget -r ftp://$i
    done
