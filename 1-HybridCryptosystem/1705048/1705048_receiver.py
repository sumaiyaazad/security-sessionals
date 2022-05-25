# Import socket module
import socket
import importlib
from BitVector import *

rsa = importlib.import_module('1705048_rsa')
aes = importlib.import_module('1705048_aes')


def decrypt(message):
    print(message)
    cipher_text, cipher_key = message.split("\n")[0], message.split("\n")[1]
    return 0

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 12345

# connect to the server on local computer
s.connect(('127.0.0.1', port))
# message = s.recv(1024).decode()
# decrypt(message)

# receive data from the server and decoding to get the string.
# print(s.recv(1024).decode())
while 1:
    message = s.recv(1024).decode()
    if "established" in message:
        print(message)
    else:
        decrypt(message)
        # write text
        # send signal
        # close the connection
        s.send("close".encode())
        s.close()
        break

