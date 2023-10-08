import networkx as nx
import matplotlib.pyplot as plt

# Define the adjacency matrix A
A = [
    [1, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 0]
]

# Create a directed graph
G = nx.DiGraph()

# Add nodes to the graph
num_nodes = len(A)
G.add_nodes_from(range(num_nodes))

# Add edges to represent the adjacency matrix
for i in range(num_nodes):
    for j in range(num_nodes):
        if A[i][j] == 1:
            G.add_edge(i, j)

# Calculate the left eigenvector centrality
eigenvector_centrality = nx.eigenvector_centrality(G)

# Print the centrality values rounded to three significant figures
for node, centrality in eigenvector_centrality.items():
    print(f"Node {node}: {centrality:.3f}")

# Visualize the graph
pos = nx.spring_layout(G, seed=42)
labels = {i: f"Node {i}" for i in range(num_nodes)}
nx.draw(G, pos, with_labels=True, labels=labels, node_size=500, node_color='lightblue', arrowsize=20)
plt.title("Graph Visualization")
plt.savefig('images/left_eigenvector_centrality_iii.png')
plt.show()
