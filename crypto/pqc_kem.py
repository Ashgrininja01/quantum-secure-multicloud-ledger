from oqs import KeyEncapsulation
import os
import pickle

KEM_ALG = "Kyber512"
KEY_DIR = "crypto/keys"

def kem_encapsulate():
    os.makedirs(KEY_DIR, exist_ok=True)

    kem = KeyEncapsulation(KEM_ALG)
    public_key = kem.generate_keypair()
    secret_key = kem.secret_key

    ciphertext, shared_secret = kem.encap_secret(public_key)

    # Store keys for demo / prototype
    with open(f"{KEY_DIR}/kem_public.key", "wb") as f:
        f.write(public_key)

    with open(f"{KEY_DIR}/kem_secret.key", "wb") as f:
        f.write(secret_key)

    return ciphertext, shared_secret


def kem_decapsulate(ciphertext):
    with open(f"{KEY_DIR}/kem_secret.key", "rb") as f:
        secret_key = f.read()

    kem = KeyEncapsulation(KEM_ALG)
    kem.secret_key = secret_key

    return kem.decap_secret(ciphertext)
