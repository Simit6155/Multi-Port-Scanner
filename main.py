import socket
import colorama
from colorama import Fore,init

init(autoreset=True)

print(Fore.RED + "This Multi-Port tester was made by @Redsimit ")
ip = "127.0.0.1"
ports = [4444, 22, 8080, 443, 21, 22, 23, 25, 53, 80, 31337]

try:
    socket.create_connection((ip, ports[0]), timeout=3)
    print(Fore.GREEN + f"Port {ports[0]} open ")
except socket.error:
    print(Fore.GREEN + f"Port {ports[0]} closed ")

try:
    socket.create_connection((ip, ports[1]), timeout=3)
    print(Fore.GREEN + f"Port {ports[1]} open ")
except socket.error:
    print(Fore.GREEN + f"Port {ports[1]} closed ")

try:
    socket.create_connection((ip, ports[2]), timeout=3)
    print(Fore.GREEN + f"Port {ports[2]} open ")
except socket.error:
    print(Fore.GREEN + f"Port {ports[2]} closed ")

try:
    socket.create_connection((ip, ports[3]), timeout=3)
    print(Fore.GREEN + f"Port {ports[3]} open ")
except socket.error:
    print(Fore.GREEN + f"Port {ports[3]} closed ")

try:
    socket.create_connection((ip, ports[4]), timeout=3)
    print(Fore.GREEN + f"Port {ports[4]} open ")
except socket.error:
    print(Fore.GREEN + f"Port {ports[4]} closed ")

try:
    socket.create_connection((ip, ports[5]), timeout=3)
    print(Fore.GREEN + f"Port {ports[5]} open ")
except socket.error:
    print(Fore.GREEN + f"Port {ports[5]} closed ")

try:
    socket.create_connection((ip, ports[6]), timeout=3)
    print(Fore.GREEN + f"Port {ports[6]} open ")
except socket.error:
    print(Fore.GREEN + f"Port {ports[6]} closed ")

try:
    socket.create_connection((ip, ports[7]), timeout=3)
    print(Fore.GREEN + f"Port {ports[7]} open ")
except socket.error:
    print(Fore.GREEN + f"Port {ports[7]} closed ")

try:
    socket.create_connection((ip, ports[8]), timeout=3)
    print(Fore.GREEN + f"Port {ports[8]} open ")
except socket.error:
    print(Fore.GREEN + f"Port {ports[8]} closed ")

try:
    socket.create_connection((ip, ports[9]), timeout=3)
    print(Fore.GREEN + f"Port {ports[9]} open ")
except socket.error:
    print(Fore.GREEN + f"Port {ports[9]} closed ")

try:
    socket.create_connection((ip, ports[10]), timeout=3)
    print(Fore.GREEN + f"Port {ports[10]} open ")
except socket.error:
    print(Fore.GREEN + f"Port {ports[10]} closed ")
