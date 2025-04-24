#!/usr/bin/env python3
"""
Interactive Multi-threaded Port Scanner

This script scans one or multiple IPv4 hosts for open TCP ports interactively,
with ASCII art, IP validation, and colored output.

Usage (interactive):
    Just run `python port_scanner.py` and follow the prompts.
"""

import socket
import termcolor
import threading
from queue import Queue
import ipaddress
import sys
import pyfiglet

print_lock = threading.Lock()
q = None  # Will be set per-target
invalid_ips = []

def check_ips(targets):
    """Validate a list of IP addresses, returning True if all valid."""
    global invalid_ips
    invalid_ips = []
    for ip in targets:
        ip = ip.strip()
        try:
            ipaddress.ip_address(ip)
        except ValueError:
            invalid_ips.append(ip)
    return not invalid_ips


def scan_port(target, port):
    """Attempt to connect to target:port. Print if open."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    try:
        sock.connect((target, port))
        with print_lock:
            print(termcolor.colored(f"[+] {target}:{port} is open", 'green'))
    except Exception:
        pass
    finally:
        sock.close()


def scanner_worker(target):
    """Worker thread: fetch ports from queue and scan."""
    while True:
        try:
            port = q.get_nowait()
        except Exception:
            break
        scan_port(target, port)
        q.task_done()


def scan_target(target, max_port):
    """Scan ports 1..max_port on a single target."""
    print(termcolor.colored(f"\n[*] Starting scan for {target}", 'blue'))
    global q
    q = Queue()

    # Enqueue ports
    for port in range(1, max_port + 1):
        q.put(port)

    # Launch threads
    threads = []
    num_threads = 30
    for _ in range(num_threads):
        t = threading.Thread(target=scanner_worker, args=(target,))
        t.daemon = True
        t.start()
        threads.append(t)

    # Wait for completion
    q.join()
    for t in threads:
        t.join()


def main():
    # ASCII banner
    ascii_art = pyfiglet.figlet_format("ALKHATAB'S CLI PORT SCANNER")
    print(ascii_art)
    print('-' * 60)

    # Get targets
    targets_input = input("[*] Enter targets (comma-separated IPs): ")
    targets = [h.strip() for h in targets_input.split(',') if h.strip()]

    if not check_ips(targets):
        print(termcolor.colored(f"Invalid IPs found: {', '.join(invalid_ips)}", 'red'))
        sys.exit(1)

    # Get max port
    port_input = input("[*] Enter max port number to scan (1-65535): ")
    try:
        max_port = int(port_input)
        if not 1 <= max_port <= 65535:
            raise ValueError()
    except ValueError:
        print(termcolor.colored("Invalid port number. Must be 1-65535.", 'red'))
        sys.exit(1)

    # Scan each target
    if len(targets) > 1:
        print(termcolor.colored("[*] Scanning multiple targets...", 'yellow'))
    for tgt in targets:
        scan_target(tgt, max_port)

if __name__ == '__main__':
    main()
