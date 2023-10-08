import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Define the adjacency matrix
adjacency_matrix = np.array([
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 0]
])

# Create a directed graph from the adjacency matrix
G = nx.DiGraph(adjacency_matrix)

# Calculate left eigenvector centrality
eigenvector_centrality = nx.eigenvector_centrality(G, max_iter=1000)

# Visualize the graph with node sizes proportional to eigenvector centrality
node_sizes = [2000 * eigenvector_centrality[node] for node in G.nodes()]
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=node_sizes, node_color='skyblue', font_size=10, font_color='black')

# Save the visualization to the "images" folder
plt.title("Left Eigenvector Centrality Visualization")
plt.savefig("images/left_eigenvector_centrality.png")
plt.show()

# Print eigenvector centrality values (rounded to the nearest integer)
for node, centrality in eigenvector_centrality.items():
    print(f"Node {node}: {round(centrality)}")
