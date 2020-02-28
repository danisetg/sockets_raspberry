import socket
import sys

HOST, PORT = "192.168.43.20", 9999

# Create a socket (SOCK_STREAM means a TCP socket)
while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
    # Connect to server and send data
        data = input()
        sock.connect((HOST, PORT))       
        sock.sendall(data.encode())

    finally:
        sock.close()