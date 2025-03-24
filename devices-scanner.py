#!/usr/bin/env python3

import subprocess
import sys
import socket
from concurrent.futures import ThreadPoolExecutor


def get_local_ip():
    """Get the private IP address of the device."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.connect(("8.8.8.8", 80))
            return sock.getsockname()[0]
    except Exception as error:
        print(f"[-] Error obtaining the local IP: {error}")
        sys.exit(1)


def generate_class_c_ips(base_ip):
    """Generate all IPs in the Class C network based on the detected IP."""
    first_three_octets = '.'.join(base_ip.split('.')[:3])
    return [f"{first_three_octets}.{i}" for i in range(1, 256)]


def host_discovery(target_ip):
    """Ping an IP to verify if it is active."""
    ping_command = (
        ["ping", "-c", "1", target_ip]
        if sys.platform != "win32"
        else ["ping", "-n", "1", target_ip]
    )

    try:
        ping = subprocess.run(
            ping_command, timeout=1,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        if ping.returncode == 0:
            return target_ip
    except subprocess.TimeoutExpired:
        pass
    return None


def main():
    local_ip = get_local_ip()
    print(f"\n[+] Local IP detected: {local_ip}")

    targets = generate_class_c_ips(local_ip)
    print(
        "[+] Scanning the network in the range:",
        f"{'.'.join(local_ip.split('.')[:3])}.1 - {'.'.join(local_ip.split('.')[:3])}.255\n",
    )

    max_threads = 100
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        results = list(executor.map(host_discovery, targets))

    active_hosts = [ip for ip in results if ip]
    if active_hosts:
        print("[+] Active hosts detected:")
        for host in active_hosts:
            print(f"\t🔹 {host}")
    else:
        print("\t[-] No active hosts found.")


if __name__ == "__main__":
    main()
