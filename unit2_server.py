#!/usr/bin/env python3

from adxl345 import ADXL345
import socket
import numpy as np
import json
import time
import random

HOST = 'localhost'  # Standard loopback interface address (localhost)
PORT = 65431            # Port to listen on (non-privileged ports are > 1023)


def get_graph_data():

    adxl345 = ADXL345()
    axes = adxl345.getAxes(True)

    graph_to_send = json.dumps({
        'x':axes['x'],
        'y':axes['y'],
        'z':axes['z']
    })
    return graph_to_send

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            # unuse
            data = conn.recv(1024)
            
            data = get_graph_data()
            print(data)
            conn.sendall(data.encode('utf-8'))

