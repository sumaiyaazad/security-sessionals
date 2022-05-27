import socket
import importlib

rsa = importlib.import_module('1705048_rsa')
aes = importlib.import_module('1705048_aes')


def decrypt(message, private_key):
    d, n = private_key.split("\n")[0], private_key.split("\n")[1]
    cipher_text, cipher_key = message.split("\n")[0], message.split("\n")[1]
    deciphered_key = rsa.rsa_decryption(int(d), int(n), cipher_key)
    round_key_byte_hex = aes.generate_round_key(deciphered_key)
    deciphered_text = aes.decrypt(cipher_text, round_key_byte_hex)
    return deciphered_text


s = socket.socket()


port = 12345


s.connect(('127.0.0.1', port))

while 1:
    message = s.recv(4096).decode()
    if "established" in message:
        print(message)
    else:
        print("message received")
        file_name = "don't open this/PRK.txt"
        in_file = open(file_name, "r", encoding='utf-8')
        private_key = in_file.read()
        in_file.close()
        deciphered_text = decrypt(message, private_key)
        file_name = "don't open this/secret.txt"
        out_file = open(file_name, "wb")
        out_file.write(deciphered_text.encode())
        out_file.close()
        s.send("close".encode())
        print("write message done")
        s.close()
        break

