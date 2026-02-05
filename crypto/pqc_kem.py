import oqs

def kem_encapsulate():
    kem = oqs.KeyEncapsulation("Kyber512")
    pk = kem.generate_keypair()
    ct, ss = kem.encap_secret(pk)
    return pk, ct, ss

def kem_decapsulate(ct):
    kem = oqs.KeyEncapsulation("Kyber512")
    return kem.decap_secret(ct)

