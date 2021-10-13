import socket
import colorama
from colorama import *
from IPy import IP


def scan(target):
    converted_ip = check_ip(target)
    print('\n' + f'{Fore.LIGHTGREEN_EX}P_SCAN EM: {Fore.LIGHTWHITE_EX}' + str(target))
    for port in range(1,100):
        scan_port(converted_ip, port)


def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)


def get_banner(s):
    return s.recv(1024)


def scan_port(ipaddres, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddres,port))
        try:
            banner = get_banner(sock)
            print(f'{Fore.GREEN}PORTA ABERTA: ' + str(port) + ' : '+  str(banner.decode().strip('\n')))
        except:
            print(f'{Fore.GREEN}PORTA ABERTA: ' + str(port))
    except:
        pass


if __name__ == "__main__":
    print(colorama.Fore.LIGHTRED_EX +
'\n ________'
'\n|\   __  \ '
'\n\ \  \|\  \ '
'\n \ \   ____\ '
'\n  \ \  \___|'
'\n   \ \__\ ' +
colorama.Fore.MAGENTA +
'\n ________       ________      ________      _________'
'\n|\   ____\     |\   ____\    |\   __  \    |\   ___   \ '
'\n\ \  \___|_    \ \  \___|    \ \  \|\  \   \ \  \ \ \  \ '
'\n \ \_____  \    \ \  \        \ \   __  \   \ \  \ \ \  \ '
'\n  \|____|\  \    \ \  \____    \ \  \ \  \   \ \  \ \ \  \ '
'\n    ____\_\  \    \ \_______\   \ \__\ \__\   \ \__\ \ \__\ '
'\n   |\_________\    \|_______|    \|__|\|__|    \|__|  \|__|'
'\n   \|_________| '
'\n'


)
    targets = input(colorama.Fore.RED + f"===========> {Fore.LIGHTWHITE_EX}  DIGITE UM ALVO PARA O SCAN {Fore.LIGHTRED_EX}  <=========== \n"
                                        f"             Caso queira fazer mais de um SCAN,                                                   \n"
                                        f"            coloque um {Fore.LIGHTWHITE_EX}-{Fore.LIGHTRED_EX} após o primeiro alvo             \n"
                                        "\n"
                                        f"            {Fore.RED}[-> ")
    if '-' in targets:
        for ip_add in targets.strip('-'):
            scan(ip_add.strip(' '))
    else:
        scan(targets)