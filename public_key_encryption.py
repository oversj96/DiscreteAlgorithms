#!/usr/bin/env python

"""public_key_encryption.py: Build and test the concept behind public key encryption"""

__author__ = "Justin Overstreet"
__copyright__ = "oversj86.github.io"


from fermat_factorization import fermat_factorization
from linear_combination import gcd_linear_combo


def decipher_private_key(multiple, e):
    factor, quotient = gcd_linear_combo(multiple, e)
    return factor - quotient


def public_key_encrypt(p, q, t, e):
    decremented_p = p - 1
    decremented_q = q - 1
    multiple = decremented_p * decremented_q
    d = decipher_private_key(multiple, e)
    if type(t) is list:
        message = [(m ** e) % (p*q) for m in t]
    else:
        message = (t ** e) % (p*q)
    return message


def public_key_decrypt(pq, e, t):
    p, q = fermat_factorization(pq)
    d = decipher_private_key((p-1)*(q-1), e)
    if type(t) is list:
        message = [(m ** d) % (p*q) for m in t]
    else:
        message = (t ** d) % (p*q)
    return message


def find_key(input_dict, value):
    return next((k for k, v in input_dict.items() if v == value), None)


if __name__ == "__main__":
    # Test encryption
    print(public_key_encrypt(1901, 4507, 10, 17))
    # Test decryption
    decrypted_info = public_key_decrypt(247, 5, [161, 212, 161, 212, 164, 119, 203, 32, 97, 32])
    alpha_dict = {'a': 2, 'b': 3, 'c': 4, 'd': 5, 'e': 6, 'f': 7, 'g': 8, 'h': 9, 'i': 10, 'j': 11, 'k': 12, 'l': 13,
                  'm': 14, 'n': 15, 'o': 16, 'p': 17, 'q': 18, 'r': 19, 's': 20, 't': 21, 'u': 22, 'v': 23, 'w': 24,
                  'x': 25, 'y': 26, 'z': 27}
    message = []
    for info in decrypted_info:
        message.append(find_key(alpha_dict, info))
    print(' '.join(message))
