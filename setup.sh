#!/bin/bash

echo -e "\033[96m[*] Updating packages and installing dependencies...\033[0m"
pkg update -y && pkg upgrade -y
pkg install python termux-api git -y

chmod +x wifi_script.py
echo -e "\033[92m[+] Setup complete! You can now run the script using:\033[0m"
echo -e "\033[93mpython wifi.py\033[0m"