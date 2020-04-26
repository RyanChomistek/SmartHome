#!/usr/bin/env python3
import json

print("start")

import socket

HOST = '52.229.38.99'  # The server's hostname or IP address
PORT = 8888        # The port used by the server

print("start")

payload = {"status":"on", "r":0, "g":255, "b":0} 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("start connect")
    s.connect((HOST, PORT))

    s.sendall(bytes(json.dumps(payload), 'utf-8'))
    data = s.recv(1024)
    print('Received', repr(data))