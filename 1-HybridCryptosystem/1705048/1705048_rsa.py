import random
import time
from BitVector import *


def generate_prime(k):
    count = 0
    number = []
    # random_num = pow(2, k//2 - 1)
    # while count != 2 and random_num != pow(2, k//2):
    while count != 2:
        random_num = random.getrandbits(k // 2)
        # print(random_num)
        # bv = BitVector(intVal=random_num)
        # bv = bv.gen_random_bits(32)
        # flag = bv.test_for_primality()
        # print("random_num= ", random_num, "flag= ", flag)
        flag = primality_test(random_num, 5)
        if flag != 0 and random_num not in number:
            # print(random_num)
            # print("random_num= ", random_num, "flag= ", flag)
            count += 1
            number.append(random_num)
    return number


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
    # print("s= ", s)
    for i in range(0, iteration):
        p = random.randint(2, prime_number - 2)
        # print("p= ", p)
        a = p % (prime_number - 4) + 2
        # print("a= ", a)
        temp = s
        # print("temp = ", s)
        modulus = pow(a, temp) % prime_number
        # print("modulus= ", modulus)
        while temp != prime_number - 1 and modulus != 1 and modulus != prime_number - 1:
            modulus = (modulus * modulus) % prime_number
            temp *= 2
            # print("modulus= ", modulus)
            # print("temp= ", temp)
            if modulus != prime_number - 1:
                return 0
    return 1


def find_gcd(a, b):
    r = a % b
    while r:
        a = b
        b = r
        r = a % b
    return b


def find_e(co_prime1):
    # for i in range(2, co_prime1):
    #     gcd = find_gcd(co_prime1, i)
    #     if gcd == 1:
    #         co_prime2 = i
    #         break

    while 1:
        co_prime2 = random.randint(2, co_prime1 - 1)
        gcd = find_gcd(co_prime1, co_prime2)
        if gcd == 1:
            return co_prime2


def find_d(e, phi_n):
    i = 1
    while 1:
        d = (phi_n * i) + 1
        if d % e == 0:
            return ((phi_n * i) + 1) // e
        i += 1


def rsa_encryption(e, n, plain_text):
    # print(plain_text)
    plain_text_int = [ord(i) for i in plain_text]
    # print(plain_text_int)
    cipher_int = [pow(i, e, n) for i in plain_text_int]
    return cipher_int


def rsa_decryption(d, n, cipher_text_int):
    deciphered_int = [pow(i, d, n) for i in cipher_text_int]
    deciphered_text = [chr(i) for i in deciphered_int]
    return deciphered_text


def start_simulation():
    # for k in range(32, 33, 16):
    key_length = [16, 32, 64, 128]
    for k in key_length:
        key_generation_start_time = time.time()
        # prime_numbers = generate_prime(k)
        # n = prime_numbers[0] * prime_numbers[1]
        # phi_n = (prime_numbers[0] - 1) * (prime_numbers[1] - 1)
        # e = find_e(phi_n)
        # d = find_d(e, phi_n)
        key_generation_end_time = time.time()
        plain_text = "CanTheyArrangeTheFest?"
        # plain_text = "13"
        # plain_text_hex = BitVector(textstring=plain_text).get_hex_string_from_bitvector()
        encryption_start_time = time.time()
        cipher_text = rsa_encryption(45097, 2571216841, plain_text)
        # cipher_text = rsa_encryption(e, n, plain_text)
        encryption_end_time = time.time()
        # print(cipher_text)
        decryption_start_time = time.time()
        deciphered_text = rsa_decryption(int(2123962321.0), 2571216841, cipher_text)
        # deciphered_text = rsa_decryption(d, n, cipher_text)
        deciphered_text = "".join(i for i in deciphered_text)
        decryption_end_time = time.time()
        # print(deciphered_text)
        print("k= ", k, " key generation= %s seconds" % (key_generation_start_time - key_generation_end_time),
              " encryption time= %s seconds" % (encryption_end_time - encryption_start_time),
              " decryption time= %s seconds" % (decryption_end_time - decryption_start_time))

# start_simulation()
