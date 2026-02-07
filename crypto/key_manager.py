import hashlib
import os

BIOMETRIC_KEY_PATH = "biometric/biometric.key"

def load_biometric_key():
    if not os.path.exists(BIOMETRIC_KEY_PATH):
        raise Exception("Biometric key not found. Enroll face first.")
    with open(BIOMETRIC_KEY_PATH, "rb") as f:
        return f.read()

def derive_aes_key(seed: bytes) -> bytes:
    bio_key = load_biometric_key()
    combined = bytes(a ^ b for a, b in zip(seed, bio_key))
    return hashlib.sha256(combined).digest()  # AES-256
