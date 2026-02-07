from oqs import KeyEncapsulation
import os

KEM_ALG = "Kyber512"

def kem_encapsulate():
    kem = KeyEncapsulation(KEM_ALG)
    public_key = kem.generate_keypair()
    ciphertext, shared_secret = kem.encap_secret(public_key)
    return public_key, ciphertext, shared_secret

def kem_decapsulate(ciphertext, secret_key):
    kem = KeyEncapsulation(KEM_ALG)
    kem.secret_key = secret_key
    return kem.decap_secret(ciphertext)
