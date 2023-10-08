import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Define the adjacency matrix
A = np.array([[0, 1, 1, 1, 1, 1, 1],
              [1, 0, 1, 0, 0, 0, 0],
              [1, 1, 0, 0, 0, 0, 0],
              [1, 0, 0, 0, 1, 0, 0],
              [1, 0, 0, 1, 0, 0, 0],
              [1, 0, 0, 0, 0, 0, 0],
              [1, 0, 0, 0, 0, 1, 0]])

# Create a directed graph from the adjacency matrix
G = nx.DiGraph(A)

# Compute the Katz centrality with default parameters
katz_centrality = nx.katz_centrality_numpy(G)

# Print the Katz centrality of each node
for i, kc in katz_centrality.items():
    print(f"Node {i}: {kc:.3f}")

# Visualize the graph
pos = nx.spring_layout(G, seed=42)
labels = {i: f"Node {i}" for i in range(len(A))}
nx.draw(G, pos, with_labels=True, labels=labels, node_size=500, node_color='lightblue', arrowsize=20)
plt.title("Graph Visualization")
plt.savefig('images/katz_centrality_graph.png')
plt.show()
