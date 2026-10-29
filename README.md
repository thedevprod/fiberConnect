# fiberConnect

A Python utility for managing local Wi-Fi connections via Termux using Android's native command-line interface.

## Prerequisites

- Android device with **Termux** installed
- **Termux:API** app installed (from F-Droid or GitHub releases) with Location permissions granted
- Root access (`su`) enabled on the device

## Installation

Run the following commands in Termux to clone the repository and run the automated setup:

```bash
# Clone the repository
git clone https://github.com/thedevprod/fiberConnect.git

# Navigate into the project directory
cd fiberConnect

# Run the setup script to install system dependencies
bash setup.sh