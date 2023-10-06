import numpy as np
import matplotlib.pyplot as plt
import os

# Define the adjacency matrix of the graph
adjacency_matrix = np.array([
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0, 1, 0]
])

# Define the node types
node_types = [1, 2, 1, 2, 2, 1, 2, 2, 2, 1]

# Calculate the number of nodes
num_nodes = len(node_types)

# Calculate the total number of edges
num_edges = np.sum(adjacency_matrix) // 2  # Divide by 2 to avoid double counting

# Initialize variables to store modularity terms
Q = 0.0
total_degree = np.zeros(num_nodes)
total_degree_type = np.zeros(2)

# Calculate the total degree for each node and the total degree for each type
for i in range(num_nodes):
    for j in range(num_nodes):
        if i != j:
            if node_types[i] == node_types[j]:
                total_degree[i] += adjacency_matrix[i][j]
            total_degree_type[node_types[i] - 1] += adjacency_matrix[i][j]

# Calculate the modularity
for i in range(num_nodes):
    for j in range(num_nodes):
        if i != j:
            delta_type = int(node_types[i] == node_types[j])
            Q += (adjacency_matrix[i][j] - total_degree[i] * total_degree[j] / (2 * num_edges)) * delta_type

# Normalize the modularity
Q /= (2 * num_edges)

# Print the modularity
print(f"Modularity of the graph: {Q:.6f}")

# Create a bar chart visualization of node types
plt.figure(figsize=(6, 4))
plt.bar(["Type 1", "Type 2"], total_degree_type, color='skyblue')
plt.xlabel("Node Types")
plt.ylabel("Total Degree")
plt.title("Total Degree by Node Type")
plt.tight_layout()

# Create the "images" folder if it doesn't exist
if not os.path.exists("images"):
    os.makedirs("images")

# Save the visualization to the "images" folder
image_path = os.path.join("images", "node_type_degree.png")
plt.savefig(image_path)

# Show the visualization
plt.show()
