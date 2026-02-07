from crypto.aes import aes_encrypt
from crypto.pqc_kem import kem_encapsulate
from crypto.pqc_signature import sign_metadata
import time

def encrypt_file(path):
    # Read input file
    with open(path, "rb") as f:
        data = f.read()

    # PQC Key Encapsulation (Kyber)
    kem_ct, seed = kem_encapsulate()

    # AES-256 encryption (biometric-bound internally)
    iv, ct = aes_encrypt(data, seed)

    # Write encrypted file
    with open(path + ".enc", "wb") as f:
        f.write(iv + ct)

    # Write KEM ciphertext
    with open(path + ".kem", "wb") as f:
        f.write(kem_ct)

    # Sign metadata using ML-DSA
    metadata = f"{path}|{int(time.time())}".encode()

    with open(path + ".meta", "wb") as f:    
        f.write(metadata)

    pub, sig = sign_metadata(metadata)
    )

    with open(path + ".pub", "wb") as f:
        f.write(pub)

    with open(path + ".sig", "wb") as f:
        f.write(sig)

    print("Encrypted with biometric-bound AES + PQC.")

if __name__ == "__main__":
    encrypt_file("sample.txt")
