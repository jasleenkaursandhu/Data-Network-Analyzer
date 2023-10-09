import networkx as nx
import numpy as np

# Define the adjacency matrix
adjacency_matrix = np.array([
    [0, 1, 0],
    [1, 0, 0],
    [0, 0, 0]
])

# Create a graph from the adjacency matrix
G = nx.Graph(adjacency_matrix)

# 1. Number of components in the graph
num_components = nx.number_connected_components(G)

# 2. Diagonal values of the Laplacian matrix
laplacian_matrix = nx.laplacian_matrix(G).toarray()
diagonal_values = laplacian_matrix.diagonal()

# Print the results
print("1. Number of components in the graph:", num_components)
print("2. Diagonal values of the Laplacian matrix:")
for i, value in enumerate(diagonal_values):
    print(f"   Diagonal element {i + 1}: {value}")
