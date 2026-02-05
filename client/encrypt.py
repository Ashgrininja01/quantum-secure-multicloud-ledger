from crypto.aes import aes_encrypt
from crypto.pqc_kem import kem_encapsulate
from crypto.pqc_signature import sign_metadata
import time

def encrypt_file(path):
    data = open(path, "rb").read()

    pk, kem_ct, aes_key = kem_encapsulate()
    iv, ct, tag = aes_encrypt(data, aes_key)

    open(path + ".enc", "wb").write(iv + tag + ct)
    open(path + ".kem", "wb").write(kem_ct)
    metadata = f"{path}|{time.time()}".encode()
    pub, sig = sign_metadata(metadata)

    open(path + ".pub", "wb").write(pub)
    open(path + ".sig", "wb").write(sig)

    print("Encrypted. Stored .enc and .kem (key capsule).")

if __name__ == "__main__":
    encrypt_file("sample.txt")
