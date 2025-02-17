#!/usr/bin/env python3
import nmap
import concurrent.futures
import sys
import time
from termcolor import colored
from mac_vendor_lookup import MacLookup

start_time = time.time()


# Performs a network scan to discover active devices.
def scan_network():
    nm = nmap.PortScanner()
    ip_range = "192.168.100.1/24"

    print(colored("\n[*] Discovering devices on the network...", "blue"))

    all_results = {}
    total_attempts = 5  # Number of scan attempts
    mac_lookup = MacLookup()  # Load MAC database once

    # Repeat the scan `total_attempts` times
    for attempt in range(total_attempts):

        # Update progress bar
        progress = (
            colored(
                f"\033[3mProgress: [{'#' * (attempt + 1)}"
                f"{'.' * (total_attempts - attempt - 1)}] "
                f"{int((attempt + 1) / total_attempts * 100)}%\033[0m",
                "grey"))

        sys.stdout.write("\r" + progress)
        sys.stdout.flush()

        try:
            nm.scan(hosts=ip_range, arguments='-sn -PR -T4 -n')
        except Exception as e:
            print(colored(f"\n[!] Network scan error: {e}", "red"))
            continue

        hosts = nm.all_hosts()
        if not hosts:
            print(colored("\n[!] No active hosts found.", "red"))
            continue

        # Concurrent scanning using ThreadPoolExecutor
        with concurrent.futures.ThreadPoolExecutor(max_workers=256)as executor:
            future_to_host = {
                executor.submit(scan_host, nm, host, mac_lookup):
                    host for host in hosts}

            for future in concurrent.futures.as_completed(future_to_host):
                result = future.result()

                if result:
                    ip, mac, vendor, formatted_result = result
                    if (
                        ip not in all_results or
                        (all_results[ip][1] == 'Unknown' and mac != 'Unknown')
                    ):
                        all_results[ip] = (mac, vendor, formatted_result)

    # Print combined results
    if all_results:
        print(colored(
            f"\n\n[+] Found {len(all_results)}"
            " unique active devices.\n", "green"))
        for result in all_results.values():
            print(result[2])
    else:
        print(colored("\n[!] No active hosts found after 5 attempts.", "red"))

    print(colored("\n[*] Scan complete.", "green"))

    total_time = time.time() - start_time
    print(colored(
        f"\033[3mTotal execution time: {total_time:.2f} seconds\033[0m",
        'grey'))


# Scans a single host for open ports and retrieves hardware details.
def scan_host(nm, host, mac_lookup):
    try:
        nm.scan(
            hosts=host,
            arguments=(
                '-T4 -p 22,80,443,3389 --max-rtt-timeout 200ms '
                '--max-retries 2 -n'
                )
            )

        ip = nm[host]['addresses'].get('ipv4', host)
        mac = nm[host]['addresses'].get('mac', 'Unknown')
        vendor = 'Unknown'

        if mac != 'Unknown':
            try:
                vendor = mac_lookup.lookup(mac)
            except Exception:
                vendor = 'Unknown'

        formatted_result = (
            f"{colored(f'IP: {ip}', 'white')} | "
            f"{colored(f'MAC: {mac}', 'yellow')} | "
            f"{colored(f'{vendor}', 'white')}"
        )

        return (ip, mac, vendor, formatted_result)

    except Exception:

        # Return IP with 'Unknown' for MAC and vendor if there's an error
        formatted_result = (
            f"{colored(f'IP: {host}', 'white')} | "
            f"{colored(f'MAC: Unknown', 'yellow')} | "
            f"{colored(f'Unknown', 'white')}"
            )
        return (host, 'Unknown', 'Unknown', formatted_result)


if __name__ == "__main__":
    scan_network()
