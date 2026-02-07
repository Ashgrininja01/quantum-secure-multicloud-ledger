from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
from crypto.key_manager import derive_aes_key

def aes_encrypt(data: bytes, seed: bytes):
    key = derive_aes_key(seed)
    iv = os.urandom(12)
    aesgcm = AESGCM(key)
    ct = aesgcm.encrypt(iv, data, None)
    return iv, ct

def aes_decrypt(iv: bytes, ct: bytes, seed: bytes):
    key = derive_aes_key(seed)
    aesgcm = AESGCM(key)
    return aesgcm.decrypt(iv, ct, None)
