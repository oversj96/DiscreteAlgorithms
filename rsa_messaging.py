#!/usr/bin/env python

"""rsa_messaging.py: Using public key encryption, send encrypted messages and then decrypt them."""

__author__ = "Justin Overstreet"
__copyright__ = "oversj96.github.io"


from public_key_encryption import public_key_decrypt, public_key_encrypt


def make_cipher(text):
    if type(text) is str:
        characters = list(text)
        message = [ord(i) for i in characters]
    elif type(text) is list and text[0] is int:
        message = text
    else:
        return None
    return public_key_encrypt(1901, 4507, message, 2**16 + 1)

def decipher(message, number, e):
    decrypted_message = public_key_decrypt(number, e, message)
    return [chr(i) for i in decrypted_message]

if __name__ == "__main__":
    message, number, e = make_cipher("with spaces?")
    print(message)
    print(number)
    print(e)
    print(decipher(message, number, e))
