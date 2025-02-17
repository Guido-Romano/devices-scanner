# Devices Scanner V1.0

This script scans devices on an internal network. It is designed to be run from a notebook via WiFi, but it can also be used perfectly from a PC with Ethernet. The script is intended for network audits and returns the private IP address of devices, their MAC address, and in some cases, the manufacturer brand.

## Features

- **Network Device Discovery**: Scans the network to discover active devices.
- **Device Details**: Retrieves private IP addresses, MAC addresses, and sometimes the manufacturer brand.
- **Concurrent Scanning**: Uses multithreading to speed up the scanning process.
- **Progress Updates**: Provides real-time progress updates during the scan.

## Requirements

- Python 3.x
- `nmap` (install via pip)
- `concurrent.futures` (built-in)
- `sys` (built-in)
- `time` (built-in)
- `termcolor` (install via pip)
- `mac_vendor_lookup` (install via pip)

## Installation & Use

1. **Clone the repository**:

    ```bash
    git clone https://github.com/tu-usuario/devices-scanner
    cd devices-scanner
    ```

2. **Install the required packages**:

    ### Debian-based distributions (e.g., Kali)

    ```bash
    sudo apt-get update
    sudo apt-get install python3 python3-pip nmap
    pip3 install termcolor mac_vendor_lookup
    ```

    ### Arch-based distributions (e.g., BlackArch)

    ```bash
    sudo pacman -Syu
    sudo pacman -S python python-pip nmap
    pip install termcolor mac_vendor_lookup
    ```

3. **Run the script**:

    ```bash
    python3 devices-scanner.py
    ```

## How It Works

1. **Network Scan**: The script performs a network scan to discover active devices.
2. **Device Information**: For each device, the script retrieves the private IP address, MAC address, and, if available, the manufacturer brand.
3. **Progress Updates**: The script provides real-time progress updates to keep you informed during the scan.
4. **Results**: The script prints the details of the discovered devices, including IP and MAC addresses and the manufacturer brand.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

Special thanks to the developers of the Nmap, `termcolor`, and `mac_vendor_lookup` libraries for their excellent tools.





