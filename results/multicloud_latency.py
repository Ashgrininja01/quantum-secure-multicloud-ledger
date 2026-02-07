import matplotlib.pyplot as plt

clouds = ["AWS", "Azure", "GCP"]
times = [0.08, 0.07, 0.09]  # Measure upload time once

plt.bar(clouds, times)
plt.ylabel("Upload Time (seconds)")
plt.title("Multi-Cloud Replication Latency")
plt.grid(True)
plt.savefig("results/graphs/multicloud_latency.png")
plt.show()
