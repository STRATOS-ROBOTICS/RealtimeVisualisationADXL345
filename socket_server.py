#!/usr/bin/env python3

import socket

import numpy as np
import json
import time
import random

HOST = '192.168.11.18'  # Standard loopback interface address (localhost)
PORT = 65431            # Port to listen on (non-privileged ports are > 1023)

sample = 0

def get_graph_data():

    global sample

    sample += 1

    graph_to_send = json.dumps({
        'x':random.uniform(-1,1),
        'y':random.uniform(-1,1),
        'z':random.uniform(-1,1),
        's':sample
    })
    return graph_to_send

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            conn.sendall(get_graph_data().encode('utf-8'))

