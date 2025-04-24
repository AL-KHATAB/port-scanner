# ALKHATAB'S CLI PORT SCANNER

Interactive multi-threaded TCP port scanner built in Python, featuring:

- ASCII-art banner on startup
- Colored output using `termcolor`
- IPv4 address validation via `ipaddress`
- Configurable maximum port number
- Multi-threaded scanning for high performance

---

## Features

1. **Interactive CLI**: Prompts for comma-separated targets and maximum port number (1–65535).  
2. **Validation**: Rejects invalid IP addresses before scanning begins.  
3. **Thread Pool**: Uses 30 daemon threads by default to scan ports 1→N concurrently.  
4. **Colorized Output**: Open ports highlighted in green; status/info lines in blue or yellow.  
5. **Easy to Run**: No extra flags—just run and follow the prompts.

---

## Requirements

- Python 3.6+  
- [`termcolor`](https://pypi.org/project/termcolor/)  
- [`pyfiglet`](https://pypi.org/project/pyfiglet/)  

Install dependencies via pip:

```bash
pip install termcolor pyfiglet
```

---

## Usage

```bash
git clone https://github.com/AL-KHATAB/port-scanner.git
cd port-scanner
python port_scanner.py
```

1. **Enter targets**: Provide one or more IPv4 addresses, comma-separated.
2. **Enter max port**: Specify an integer between 1 and 65535.
3. **Watch it scan**: Open ports will print in real time.

Example:

```text
[*] Enter targets (comma-separated IPs): 192.168.1.10,10.0.0.5
[*] Enter max port number to scan (1-65535): 1024
```

---

## License

This project is licensed under the MIT License—see [LICENSE](LICENSE) for details.


