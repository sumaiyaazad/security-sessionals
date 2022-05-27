import time
from BitVector import *
import random


def generate_prime(k):
    count = 0
    number = []
    low_limit = pow(2, k//2 - 1) + 1
    up_limit = pow(2, k//2) - 1
    random_num = low_limit
    while count != 2 and random_num <= up_limit:
        flag = prime(random_num)
        if flag != 0 and random_num not in number:
            count += 1
            number.append(random_num)
        random_num += 2
    return number


def prime(num):
    return 1 if BitVector(intVal=num).test_for_primality() > 0.0 else 0


def find_gcd(a, b):
    r = a % b
    while r:
        a = b
        b = r
        r = a % b
    return b


def find_e(co_prime1):
    co_prime2 = co_prime1 - 1
    while co_prime2 > 1:
        gcd = find_gcd(co_prime1, co_prime2)
        if gcd == 1:
            return co_prime2
        co_prime2 -= 1


def find_d(e, phi_n):
    return pow(e, -1, phi_n)


def rsa_encryption(e, n, plain_text):
    plain_text_int = [ord(i) for i in plain_text]
    cipher_int = [pow(i, e, n) for i in plain_text_int]
    cipher_text = " ".join(str(item) for item in cipher_int)
    return cipher_text


def rsa_decryption(d, n, cipher_text):
    cipher_int = cipher_text.split(" ")
    cipher_text_int = [int(i) for i in cipher_int]
    deciphered_int = [pow(i, d, n) for i in cipher_text_int]
    deciphered_text = [chr(i) for i in deciphered_int]
    deciphered_text = "".join(i for i in deciphered_text)
    return deciphered_text


def primality_test(prime_number, iteration):
    if prime_number < 2:
        return 0
    if prime_number != 2 and prime_number % 2 == 0:
        return 0
    if prime_number == 2 or prime_number == 3:
        return 1
    s = prime_number - 1
    while s % 2 == 0:
        s = s // 2
    for i in range(0, iteration):
        p = random.randint(2, prime_number - 2)
        a = p % (prime_number - 4) + 2
        temp = s
        modulus = pow(a, temp) % prime_number
        while temp != prime_number - 1 and modulus != 1 and modulus != prime_number - 1:
            modulus = (modulus * modulus) % prime_number
            temp *= 2
            if modulus != prime_number - 1:
                return 0
    return 1


def start_simulation():
    key_length = [16, 32, 64, 128, 192, 256]
    plain_text = input("Plain Text: \n")
    for k in key_length:
        key_generation_start_time = time.time()
        prime_numbers = generate_prime(k)
        n = prime_numbers[0] * prime_numbers[1]
        phi_n = (prime_numbers[0] - 1) * (prime_numbers[1] - 1)
        e = find_e(phi_n)
        d = find_d(e, phi_n)
        key_generation_end_time = time.time()
        encryption_start_time = time.time()
        cipher_text = rsa_encryption(e, n, plain_text)
        encryption_end_time = time.time()
        decryption_start_time = time.time()
        deciphered_text = rsa_decryption(int(d), int(n), cipher_text)
        decryption_end_time = time.time()
        print("e,d,n ", e,d,n)
        print("cipher-text ", cipher_text)
        print(deciphered_text)
        print("k= ", k, " key generation= %s seconds" % (key_generation_end_time - key_generation_start_time),
              " encryption time= %s seconds" % (encryption_end_time - encryption_start_time),
              " decryption time= %s seconds" % (decryption_end_time - decryption_start_time))


# start_simulation()
