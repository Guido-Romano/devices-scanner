# Network Scanner V1.0

This script scans devices on an internal network. It is designed to be versatile, running on Linux distributions from a notebook via WiFi or a PC with Ethernet. The script detects active hosts within a Class C network and prints their private IP addresses.

## Features

- **Network Host Discovery**: Scans the network to identify active hosts.
- **Efficiency**: Uses multithreading to speed up the scanning process.
- **Cross-Platform Compatibility**: Functions seamlessly across multiple Linux distributions.

## Requirements

- Python 3.x
- `socket` (built-in)
- `subprocess` (built-in)
- `concurrent.futures` (built-in)
- `sys` (built-in)

## Installation & Use

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/network-scanner
    cd network-scanner
    ```

2. **Install required packages** (based on your distribution):

    ### Debian-based distributions (e.g., Ubuntu, Kali)
    ```bash
    sudo apt-get update
    sudo apt-get install python3 python3-pip
    ```

    ### Arch-based distributions (e.g., Arch Linux, BlackArch)
    ```bash
    sudo pacman -Syu
    sudo pacman -S python python-pip
    ```

3. **Run the script**:

    ```bash
    python3 network_scanner.py
    ```

## How It Works

1. **Local IP Detection**: The script retrieves the local private IP address.
2. **IP Generation**: Generates a list of all possible IPs within the detected Class C network.
3. **Host Discovery**: Pings each IP address concurrently to identify active hosts.
4. **Results**: Prints a list of detected IPs for active hosts.

## Compatibility

This script has been tested on the following Linux distributions:
- Debian-based (e.g., Ubuntu, Kali)
- Arch-based (e.g., BlackArch, Manjaro)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

Special thanks to the Python community for built-in libraries like `socket`, `subprocess`, and `concurrent.futures` for their robust utilities.
