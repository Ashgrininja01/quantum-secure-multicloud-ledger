import os, time, matplotlib.pyplot as plt
from crypto.aes import aes_encrypt, aes_decrypt
import os

sizes_kb = [1, 10, 50, 100, 500]
enc_times = []
dec_times = []

for size in sizes_kb:
    data = os.urandom(size * 1024)
    key = os.urandom(32)

    t0 = time.time()
    iv, ct = aes_encrypt(data, key)
    enc_times.append(time.time() - t0)

    t0 = time.time()
    aes_decrypt(iv, ct, key)
    dec_times.append(time.time() - t0)

plt.plot(sizes_kb, enc_times, label="Encryption")
plt.plot(sizes_kb, dec_times, label="Decryption")
plt.xlabel("File Size (KB)")
plt.ylabel("Time (seconds)")
plt.title("AES-256 Performance vs File Size")
plt.legend()
plt.grid(True)
plt.savefig("results/graphs/aes_performance.png")
plt.show()
