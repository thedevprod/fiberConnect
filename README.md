# fiberConnect

A Python utility for processing Wi-Fi SSIDs and viewing local network configurations via Termux.

# Features

- **Direct Generation:** Process a specific SSID passed directly as a command-line argument.
- **Scanning Mode:** View nearby network details using Termux API integrations.
- **Formatted Output:** Colored command-line interface for clear readability.

# Prerequisites

- Android device with **Termux** installed
- **Termux:API** app installed (from F-Droid or GitHub releases) with Location permissions enabled

# Installation

Run the following commands in Termux to clone the repository and set up dependencies:

```bash
# Clone the repository
git clone https://github.com/thedevprod/fiberConnect.git

# Navigate into the project directory
cd fiberConnect

# Run the setup script
bash setup.sh
```

# Usage
### 1. Direct Generation Mode
``` bash
python wifi.py fh_0123456789ab
```
### 2. Scanning Mode
``` bash
python wifi.py