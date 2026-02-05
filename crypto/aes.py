from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

def aes_encrypt(data, key):
    iv = os.urandom(12)
    enc = Cipher(algorithms.AES(key), modes.GCM(iv)).encryptor()
    ct = enc.update(data) + enc.finalize()
    return iv, ct, enc.tag

def aes_decrypt(iv, ct, tag, key):
    dec = Cipher(algorithms.AES(key), modes.GCM(iv, tag)).decryptor()
    return dec.update(ct) + dec.finalize()

