# first of all import the socket library
import socket
import importlib
from BitVector import *
import os

rsa = importlib.import_module('1705048_rsa')
aes = importlib.import_module('1705048_aes')


def encrypt():
    # plain_text = input("Plain Text: \n")
    plain_text = "Two One Nine Two Four"
    # plain_text = "CanTheyDoTheirFest"
    if len(plain_text) % 16 != 0:
        extra = ((len(plain_text) // 16) + 1) * 16
        plain_text = plain_text.ljust(extra, "*")
    plain_text_hex = BitVector(textstring=plain_text).get_hex_string_from_bitvector()
    plain_text_word = [plain_text_hex[i:i + 8] for i in range(0, len(plain_text_hex), 8)]
    # key = input("Key: \n")
    key = "Thats my Kung Fu"
    # key = "BUET CSE17 Batch"
    if len(key) < 16:
        key = key.ljust(16, "*")
    else:
        key = key[:16]
    round_key_byte_hex = aes.generate_round_key(key)
    cipher_matrix = []
    for i in range(0, len(plain_text_word), 4):
        cipher_matrix += aes.aes_encryption(plain_text_word[i:i + 4], round_key_byte_hex)
    cipher, cipher_text = aes.print_matrix(cipher_matrix)
    # print("Cipher text: ", cipher_text)
    prime_numbers = rsa.generate_prime(len(key))
    n = prime_numbers[0] * prime_numbers[1]
    phi_n = (prime_numbers[0] - 1) * (prime_numbers[1] - 1)
    e = rsa.find_e(phi_n)
    d = rsa.find_d(e, phi_n)
    cipher_key = rsa.rsa_encryption(e, n, plain_text)
    # print("Cipher key: ", cipher_key)
    return plain_text, cipher_text, cipher_key, d, n

# # next create a socket object
s = socket.socket()
print("Socket successfully created")

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))
print("socket binded to %s" % port)

# put the socket into listening mode
s.listen(5)
print("socket is listening")

# a forever loop until we interrupt it or
# an error occurs
while True:
    # Establish connection with client.
    c, addr = s.accept()
    print('Got connection from', addr)

    # send a thank you message to the client. encoding to send byte type.
    c.send('connection established'.encode())
    plain_text, cipher_text, cipher_key, d, n = encrypt()
    script_dir = os.path.dirname(__file__)
    rel_path = "PRK.txt"
    # file_name = os.path.join(script_dir, rel_path)
    out_file = open(rel_path, "wb")
    # out_file = open(file_name, "wb")
    write_content = str(d)+"\n"+str(n)
    out_file.write(write_content.encode())
    out_file.close()
    cipher_key = " ".join([str(item) for item in cipher_key])
    message = str(cipher_text)+"\n"+str(cipher_key)
    c.send(message.encode())
    message = c.recv(1024).decode()
    if "close" in message:
        # read output
        # send feedback
        c.close()
    break
