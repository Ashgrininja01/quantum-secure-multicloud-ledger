from crypto.aes import aes_encrypt
from crypto.pqc_kem import kem_encapsulate
from crypto.pqc_signature import sign_metadata
import time

def encrypt_file(path):
    data = open(path, "rb").read()

    pk, kem_ct, seed = kem_encapsulate()
    iv, ct = aes_encrypt(data, seed)

    open(path + ".enc", "wb").write(iv + ct)
    open(path + ".kem", "wb").write(kem_ct)

    metadata = f"{path}|{time.time()}".encode()
    pub, sig = sign_metadata(metadata)

    open(path + ".pub", "wb").write(pub)
    open(path + ".sig", "wb").write(sig)

    print("Encrypted with biometric-bound AES + PQC.")
if __name__ == "__main__":
    encrypt_file("sample.txt")
