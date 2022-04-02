import time
import json
import socket

HOST = 'localhost'  # The server's hostname or IP address
PORT = 65431        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        s.sendall(b'get-data')
        data = s.recv(1024).decode('utf-8')
        print('Received from socket server : ', data)
        time.sleep(0.5)
