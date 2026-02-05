from crypto.aes import aes_encrypt
from crypto.pqc_kem import kem_encapsulate

def encrypt_file(path):
    data = open(path, "rb").read()

    pk, kem_ct, aes_key = kem_encapsulate()
    iv, ct, tag = aes_encrypt(data, aes_key)

    open(path + ".enc", "wb").write(iv + tag + ct)
    open(path + ".kem", "wb").write(kem_ct)

    print("Encrypted. Stored .enc and .kem (key capsule).")

if __name__ == "__main__":
    encrypt_file("sample.txt")
