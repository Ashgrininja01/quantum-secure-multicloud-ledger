import time, matplotlib.pyplot as plt
from crypto.pqc_kem import kem_encapsulate, kem_decapsulate

enc_times = []
dec_times = []

for _ in range(5):
    t0 = time.time()
    ct, sk = kem_encapsulate()
    enc_times.append(time.time() - t0)

    t0 = time.time()
    kem_decapsulate(ct, sk)
    dec_times.append(time.time() - t0)

plt.bar(
    ["Encapsulation", "Decapsulation"],
    [sum(enc_times)/len(enc_times), sum(dec_times)/len(dec_times)]
)
plt.ylabel("Time (seconds)")
plt.title("PQC KEM Overhead (Kyber)")
plt.grid(True)
plt.savefig("results/plots/pqc_kem.png")
plt.show()
