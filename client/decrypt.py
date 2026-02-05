from biometric.face_auth import authenticate_face
from crypto.aes import aes_decrypt
from crypto.pqc_kem import kem_decapsulate

def decrypt_file(path):
    if not authenticate_face():
        print("Access denied.")
        return

    blob = open(path + ".enc", "rb").read()
    iv, tag, ct = blob[:12], blob[12:28], blob[28:]
    kem_ct = open(path + ".kem", "rb").read()

    aes_key = kem_decapsulate(kem_ct)
    pt = aes_decrypt(iv, ct, tag, aes_key)

    open(path + ".dec", "wb").write(pt)
    print("Decrypted successfully.")

if __name__ == "__main__":
    decrypt_file("sample.txt")

