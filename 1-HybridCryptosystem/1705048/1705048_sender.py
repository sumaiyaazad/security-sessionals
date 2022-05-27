# first of all import the socket library
import socket
import importlib
from BitVector import *
import os

rsa = importlib.import_module('1705048_rsa')
aes = importlib.import_module('1705048_aes')


def encrypt():
    plain_text = input("plain text: \n")
    plain_text, plain_text_hex = aes.fetch_text(plain_text)
    key = input("aes encryption key: \n")
    key = aes.fetch_key(key)
    round_key_byte_hex = aes.generate_round_key(key)
    cipher_text = aes.encrypt(plain_text, round_key_byte_hex)
    rsa_key_length = input("rsa encryption key: \n")
    prime_numbers = rsa.generate_prime(int(rsa_key_length))
    n = prime_numbers[0] * prime_numbers[1]
    phi_n = (prime_numbers[0] - 1) * (prime_numbers[1] - 1)
    e = rsa.find_e(phi_n)
    d = rsa.find_d(e, phi_n)
    cipher_key = rsa.rsa_encryption(e, n, key)
    return plain_text, cipher_text, cipher_key, d, n


s = socket.socket()
print("Socket successfully created")

port = 12345
s.bind(('', port))
print("socket binded to %s" % port)

s.listen(5)
print("socket is listening")


while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    c.send('connection established'.encode())
    plain_text, cipher_text, cipher_key, d, n = encrypt()
    file_name = "don't open this/PRK.txt"
    out_file = open(file_name, "wb")
    file_content = str(d)+"\n"+str(n)
    out_file.write(file_content.encode())
    out_file.close()
    message = str(cipher_text)+"\n"+str(cipher_key)
    c.send(message.encode())
    message = c.recv(4096).decode()
    if "close" in message:
        file_name = "don't open this/secret.txt"
        in_file = open(file_name, "r", encoding='utf-8')
        secret = in_file.read()
        in_file.close()
        if plain_text == secret:
            print("message sent successfully")
        else:
            print("error")
        c.close()
    break
