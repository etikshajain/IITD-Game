#!/bin/bash

ipaddr="127.0.0.1"  # Default IP address
ip_output=$(ipconfig getifaddr en0)
if [ "$1" = "wifi" ]; then
  ipaddr="$ip_output" 
fi
sed -i '' "s/IP_ADDR = .*/IP_ADDR = \"$ipaddr\"/" config/server.py

echo "Running game client at IP: $ipaddr"
python3 main.py