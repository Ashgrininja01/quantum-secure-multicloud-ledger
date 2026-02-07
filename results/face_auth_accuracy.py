import numpy as np
import matplotlib.pyplot as plt

# Sample distances from real runs (collect 10–15 manually)
distances = [0.18, 0.21, 0.23, 0.19, 0.24, 0.22, 0.20]

plt.hist(distances, bins=5)
plt.xlabel("Face Embedding Distance")
plt.ylabel("Frequency")
plt.title("Face Authentication Distance Distribution")
plt.grid(True)
plt.savefig("results/graphs/face_distance.png")
plt.show()
