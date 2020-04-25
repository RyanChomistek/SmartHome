#!/usr/bin/env python3
from flask import Flask
from flask_ask import Ask, statement, convert_errors, question
import logging

app = Flask(__name__)
ask = Ask(app, '/')



logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch
def launched():
    return question('Welcome to Smart Mirror')

@ask.intent('HelloWorldIntent')
def hello():
    return statement('Hello, world')

@ask.intent('GPIOControlIntent', mapping={'status': 'status'})
def gpio_status(status):
    print(status)
    return statement('connected')

if __name__ == '__main__':
    port = 5000 #the custom port you want
    app.run(host='0.0.0.0', port=port)
    


# import socket

# HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
# PORT = 8888        # Port to listen on (non-privileged ports are > 1023)

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen()
#     conn, addr = s.accept()
#     with conn:
#         print('Connected by', addr)
#         while True:
#             data = conn.recv(1024)
#             print('Received', repr(data))
#             if not data:
#                 break
#             conn.sendall(data)