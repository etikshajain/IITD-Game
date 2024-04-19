#!/bin/bash

if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <ip_address> <arg2>"
  exit 1
fi

ipaddr="$1"
sed -i '' "s/IP_ADDR = .*/IP_ADDR = \"$ipaddr\"/" config/server.py

echo -e "Running game client at IP:  \033[0;32m$ipaddr\033[0m"
python3 main.py "$2"