import matplotlib.pyplot as plt

labels = ["Face Auth", "AES Encrypt", "PQC KEM", "Signature", "Replication"]
times = [0.42, 0.03, 0.05, 0.02, 0.08]  # Measure once using time.time()

plt.bar(labels, times)
plt.ylabel("Time (seconds)")
plt.title("End-to-End Encryption Time Breakdown")
plt.xticks(rotation=30)
plt.grid(True)
plt.savefig("results/graphs/end_to_end.png")
plt.show()
