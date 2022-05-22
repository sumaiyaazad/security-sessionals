# -*- coding: utf-8 -*-
"""BitVectorDemo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NoLVEBqkvrHwoYoEuxX0BeJvaJ5MtVrA
"""

"""Tables"""
import time
from BitVector import *

Sbox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

InvSbox = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)

Mixer = [
    [BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03")],
    [BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02")]
]

InvMixer = [
    [BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09")],
    [BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D")],
    [BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B")],
    [BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E")]
]
round_constant = [BitVector(hexstring="0E")]
b = BitVector(hexstring="4E")
int_val = b.intValue()
s = Sbox[int_val]
s = BitVector(intVal=s, size=8)
# print(s.get_bitvector_in_hex())

AES_modulus = BitVector(bitstring='100011011')

bv1 = BitVector(hexstring="02")
bv2 = BitVector(hexstring="63")
bv3 = bv1.gf_multiply_modular(bv2, AES_modulus, 8)
# print(bv3)


# my portion

round_constant = [BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="04"),
                  BitVector(hexstring="08"),
                  BitVector(hexstring="10"), BitVector(hexstring="20"), BitVector(hexstring="40"),
                  BitVector(hexstring="80"),
                  BitVector(hexstring="1B"), BitVector(hexstring="36")]


def g(last_word_of_key, round_constant):
    # left shifting 8 bit
    last_word_of_key_shifted = last_word_of_key[8:] + last_word_of_key[0:8]
    # substitution box
    last_word_of_key_shifted[0:8] = BitVector(intVal=Sbox[last_word_of_key_shifted[0:8].intValue()], size=8)
    last_word_of_key_shifted[8:16] = BitVector(intVal=Sbox[last_word_of_key_shifted[8:16].intValue()], size=8)
    last_word_of_key_shifted[16:24] = BitVector(intVal=Sbox[last_word_of_key_shifted[16:24].intValue()], size=8)
    last_word_of_key_shifted[24:32] = BitVector(intVal=Sbox[last_word_of_key_shifted[24:32].intValue()], size=8)
    # xor operation
    last_word_of_key_shifted[0:8] = last_word_of_key_shifted[0:8].__xor__(round_constant)
    return last_word_of_key_shifted


def generate_round_key(primary_key):
    if len(primary_key) < 16:
        primary_key = primary_key.ljust(16, "*")
    else:
        primary_key = primary_key[:16]
    primary_key = BitVector(textstring=primary_key)
    primary_key_hex = primary_key.get_hex_string_from_bitvector()
    round_keys = [primary_key_hex]
    round_key_words_bin = [[primary_key[i:i + 32] for i in range(0, 128, 32)]]
    round_key_words_hex = [[primary_key_hex[i:i + 8] for i in range(0, 32, 8)]]
    round_key_byte_hex = [[[round_key_words_hex[0][j][i:i + 2] for i in range(0, 8, 2)] for j in range(0, 4)]]
    for i in range(0, 10):
        w0 = g(round_key_words_bin[i][3], round_constant[i])
        w0 = w0.__xor__(round_key_words_bin[i][0])
        w1 = w0.__xor__(round_key_words_bin[i][1])
        w2 = w1.__xor__(round_key_words_bin[i][2])
        w3 = w2.__xor__(round_key_words_bin[i][3])
        round_key_words_bin.append([w0, w1, w2, w3])
        round_key_words_hex.append(
            [w0.get_hex_string_from_bitvector(), w1.get_hex_string_from_bitvector(), w2.get_hex_string_from_bitvector(),
             w3.get_hex_string_from_bitvector()])
        round_keys.append((w0 + w1 + w2 + w3).get_hex_string_from_bitvector())
        round_key_byte_hex.append(
            [[round_key_words_hex[i + 1][k][j:j + 2] for j in range(0, 8, 2)] for k in range(0, 4)])
    return round_key_byte_hex


def add_round_key(key, plain_text):
    state_matrix = [
        [BitVector(hexstring=key[j][i]).__xor__(BitVector(hexstring=plain_text[j][i])).get_hex_string_from_bitvector()
         for i in range(0, 4)] for j in range(0, 4)]
    return state_matrix


def substitute(state_matrix, flag):
    if flag == 1:
        substitution_matrix = [[BitVector(intVal=Sbox[BitVector(hexstring=state_matrix[i][j]).intValue()],
                                          size=8).get_hex_string_from_bitvector() for j in range(0, 4)] for i in
                               range(0, 4)]
    else:
        substitution_matrix = [[BitVector(intVal=InvSbox[BitVector(hexstring=state_matrix[i][j]).intValue()],
                                          size=8).get_hex_string_from_bitvector() for j in range(0, 4)] for i in
                               range(0, 4)]
    return substitution_matrix


def shift_row(substituted_matrix, flag):
    if flag == 1:
        shifted_matrix = [
            [substituted_matrix[0][0], substituted_matrix[1][1], substituted_matrix[2][2], substituted_matrix[3][3]],
            [substituted_matrix[1][0], substituted_matrix[2][1], substituted_matrix[3][2], substituted_matrix[0][3]],
            [substituted_matrix[2][0], substituted_matrix[3][1], substituted_matrix[0][2], substituted_matrix[1][3]],
            [substituted_matrix[3][0], substituted_matrix[0][1], substituted_matrix[1][2], substituted_matrix[2][3]],
        ]
    else:
        shifted_matrix = [
            [substituted_matrix[0][0], substituted_matrix[3][1], substituted_matrix[2][2], substituted_matrix[1][3]],
            [substituted_matrix[1][0], substituted_matrix[0][1], substituted_matrix[3][2], substituted_matrix[2][3]],
            [substituted_matrix[2][0], substituted_matrix[1][1], substituted_matrix[0][2], substituted_matrix[3][3]],
            [substituted_matrix[3][0], substituted_matrix[2][1], substituted_matrix[1][2], substituted_matrix[0][3]],
        ]

    return shifted_matrix


def mix_column(shifted_matrix, flag):
    mixed_col_matrix = [[], [], [], []]
    for i in range(0, 4):
        for j in range(0, 4):
            xor_result = BitVector(hexstring="00")
            for k in range(0, 4):
                if flag == 1:
                    xor_result = xor_result.__xor__(BitVector(hexstring=shifted_matrix[j][k]).gf_multiply_modular(
                        BitVector(hexstring=Mixer[i][k].get_hex_string_from_bitvector()), AES_modulus, 8))
                else:
                    xor_result = xor_result.__xor__(BitVector(hexstring=shifted_matrix[j][k]).gf_multiply_modular(
                        BitVector(hexstring=InvMixer[i][k].get_hex_string_from_bitvector()), AES_modulus, 8))
            mixed_col_matrix[j].append(xor_result.get_hex_string_from_bitvector())
    return mixed_col_matrix


def aes_encryption(plain_text, round_key_byte_hex):
    plain_text_word_hex = [[plain_text[i][j:j + 2] for j in range(0, 8, 2)] for i in range(0, 4)]
    state_matrix = add_round_key(round_key_byte_hex[0], plain_text_word_hex)
    for i in range(1, 10):
        substituted_matrix = substitute(state_matrix, 1)
        shifted_matrix = shift_row(substituted_matrix, 1)
        mixed_col_matrix = mix_column(shifted_matrix, 1)
        state_matrix = add_round_key(round_key_byte_hex[i], mixed_col_matrix)
        # print(state_matrix)
    substituted_matrix = substitute(state_matrix, 1)
    shifted_matrix = shift_row(substituted_matrix, 1)
    state_matrix = add_round_key(round_key_byte_hex[10], shifted_matrix)
    return state_matrix


def aes_decryption(encrypted_matrix, round_key_byte_hex):
    mixed_column_matrix = add_round_key(round_key_byte_hex[10], encrypted_matrix)
    for i in range(9, 0, -1):
        shifted_matrix = shift_row(mixed_column_matrix, 0)
        substituted_matrix = substitute(shifted_matrix, 0)
        state_matrix = add_round_key(round_key_byte_hex[i], substituted_matrix)
        mixed_column_matrix = mix_column(state_matrix, 0)
    shifted_matrix = shift_row(mixed_column_matrix, 0)
    substituted_matrix = substitute(shifted_matrix, 0)
    state_matrix = add_round_key(round_key_byte_hex[0], substituted_matrix)
    return state_matrix


def print_matrix(matrix):
    cipher = "".join(i for j in matrix for i in j)
    cipher_text = BitVector(hexstring=cipher).get_text_from_bitvector()
    print(cipher)
    print(cipher_text)


def start_simulation():
    # plain_text = input("Plain Text: \n")
    plain_text = "Two One Nine Two"
    # plain_text = "CanTheyDoTheirFest"
    plain_text_hex = BitVector(textstring=plain_text).get_hex_string_from_bitvector()
    print(plain_text_hex)
    plain_text_word = [plain_text_hex[i:i + 8] for i in range(0, 32, 8)]
    # key = input("Key: \n")
    key = "Thats my Kung Fu"
    # key = "BUET CSE17 Batch"
    key_hex = BitVector(textstring=key).get_hex_string_from_bitvector()
    print(key_hex)
    # _start_time = time.time()
    round_key_byte_hex = generate_round_key(key)
    cipher_matrix = aes_encryption(plain_text_word, round_key_byte_hex)
    print_matrix(cipher_matrix)
    deciphered_text = aes_decryption(cipher_matrix, round_key_byte_hex)
    print_matrix(deciphered_text)


start_simulation()
