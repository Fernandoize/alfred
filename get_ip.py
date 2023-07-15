import pyperclip
import socket


def main():
    hostname = socket.gethostname()
    # Get the IP address of the machine
    ip_address = socket.gethostbyname(hostname)
    print("result: {}".format(ip_address))
    pyperclip.copy(ip_address)


if __name__ == '__main__':
    main()