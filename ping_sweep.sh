#!/bin/bash
if [ $# -ne 1 ]
then
echo "usage $0 <interface>"
fi
ip_address=$(ifconfig $1 | awk '/inet / {print $2; exit}' | cut -d '.' -f 1,2,3)
if [ -z "$ip_address" ]
then
echo "Unable to determine ip address"
fi


for x in {1..255}; do
  if ping -i 0.1 -c 1 -I "$interface" "$ip_address.$x" &>/dev/null; then
    echo "$ip_address.$x is up!"
  else
    echo "$ip_address.$x is down"
  fi
done
