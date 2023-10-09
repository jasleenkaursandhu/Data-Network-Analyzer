import numpy as np
import matplotlib.pyplot as plt
import os

# Create a sample dataset B (matrix)
B = np.array([
    [1, 0, 1, 0],
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [0, 1, 0, 1]
])

# 1. Entry (i, j), i != j of B*(B^T)
intersection_counts = np.dot(B, B.T)

# 2. Entry (i, i) of B*(B^T)
area_counts = np.dot(B.T, B)

# Create the "images" folder if it doesn't exist
os.makedirs("images", exist_ok=True)

# Visualize the results
plt.figure(figsize=(12, 5))

# 1. Entry (i, j), i != j of B*(B^T)
plt.subplot(1, 2, 1)
plt.imshow(intersection_counts, cmap='viridis', interpolation='none')
plt.title("Number of workers serving both areas")
plt.colorbar()
plt.xlabel("Worker")
plt.ylabel("Area")

# 2. Entry (i, i) of B*(B^T)
plt.subplot(1, 2, 2)
plt.imshow(area_counts, cmap='viridis', interpolation='none')
plt.title("Number of areas served by each worker")
plt.colorbar()
plt.xlabel("Worker")
plt.ylabel("Worker")

# Save visualizations to the "images" folder
plt.tight_layout()
plt.savefig("images/worker_area_visualizations.png")

# Show the visualizations
plt.show()
