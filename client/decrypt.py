from biometric.face_auth import authenticate_face
from crypto.aes import aes_decrypt
from crypto.pqc_kem import kem_decapsulate
from crypto.pqc_signature import verify_metadata

def decrypt_file(path):
    # Step 1: Face authentication gate
    if not authenticate_face():
        print("Access denied.")
        return

    # Step 2: Verify PQC signature (ledger check)
    metadata = None
    with open(path + ".pub", "rb") as f:
        pub = f.read()
    with open(path + ".sig", "rb") as f:
        sig = f.read()

    if not verify_metadata(pub, sig, metadata):
        print("Ledger signature verification failed.")
        return

    print("Ledger signature verified")

    # Step 3: Load encrypted data
    blob = open(path + ".enc", "rb").read()
    iv, ct = blob[:12], blob[12:]

    # Step 4: Load KEM ciphertext and decapsulate
    kem_ct = open(path + ".kem", "rb").read()
    seed = kem_decapsulate(kem_ct)

    print("PQC decapsulation successful")

    # Step 5: AES decryption
    plaintext = aes_decrypt(iv, ct, seed)

    with open(path + ".dec", "wb") as f:
        f.write(plaintext)

    print("Decrypted successfully")

if __name__ == "__main__":
    decrypt_file("sample.txt")
