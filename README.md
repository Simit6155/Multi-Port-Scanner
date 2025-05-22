# 🔍 Multi-Port Scanner by @Redsimit

A simple multi-port scanner written in Python that checks the status (open/closed) of common TCP ports on a target IP. Great for beginners learning about networking and sockets!

---

## 🚀 Features

- Scans multiple ports on a target IP  
- Uses TCP connections to determine if ports are open  
- Color-coded output using `colorama` for better readability  
- Lightweight and easy to understand  

---

## 🧠 How It Works

This script attempts to create a TCP connection to each port in a predefined list using Python’s built-in `socket` module. If the connection is successful within the timeout limit, the port is marked as **open**, otherwise as **closed**.

---

## 📜 Example Output

This Multi-Port tester was made by @Redsimit
Port 4444 open
Port 22 open
Port 8080 closed

---

## 🛠 Requirements

- Python 3.x  
- `colorama` module (install via pip if not already installed):

pip install colorama
🧪 How to Use
Clone or download this repository.

Open the script and change the ip variable to your target IP (default is 127.0.0.1).

Run the script:

bash
Kopieren
Bearbeiten
python multi_port_scanner.py
🔧 Customization
You can change the list of ports to scan by modifying the ports list:

ports = [4444, 22, 8080, 443, 21, 23, 25, 53, 80, 31337]
⚠️ Disclaimer
This tool is intended only for educational and legal purposes.
Scanning systems without permission is illegal and unethical.
Always get authorization before using this on a network you do not own.

📫 Author
Made by @Redsimit
