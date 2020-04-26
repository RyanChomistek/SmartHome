#!/usr/bin/env python3
import json
import socket

HOST = '52.229.38.99'  # The server's hostname or IP address
PORT = 8888        # The port used by the server

deviceConnectionPayload = "start consumer connection"

#print(str(bytes(deviceConnectionPayload, 'utf-8')))

def setupSocket():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("start connect")
        s.connect((HOST, PORT))
        
        # Send initial handshake
        s.sendall(bytes(deviceConnectionPayload, 'utf-8'))
        data = s.recv(1024)
        dataStr = data.decode('utf-8')

        print("hand shake response " + dataStr)
        if(dataStr != "success"):
            return None

        while True:
            data = s.recv(1024)
            print('Received', repr(data))

setupSocket()