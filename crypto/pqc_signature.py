import oqs
import hashlib

SIG_ALG = "ML-DSA-44"

def sign_metadata(data: bytes):
    """
    Signs ledger metadata using ML-DSA (Dilithium).
    """
    sig = oqs.Signature(SIG_ALG)
    public_key = sig.generate_keypair()
    signature = sig.sign(data)
    return public_key, signature


def verify_metadata(data: bytes, signature: bytes, public_key: bytes):
    """
    Verifies ML-DSA signature.
    """
    sig = oqs.Signature(SIG_ALG)
    return sig.verify(data, signature, public_key)

