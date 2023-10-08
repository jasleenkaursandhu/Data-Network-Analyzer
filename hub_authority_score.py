import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Define the adjacency matrix
adjacency_matrix = np.array([[0, 1, 1, 1, 1, 1, 1],
                             [1, 0, 1, 0, 0, 0, 0],
                             [1, 1, 0, 0, 0, 0, 0],
                             [1, 0, 0, 0, 1, 0, 0],
                             [1, 0, 0, 1, 0, 0, 0],
                             [1, 0, 0, 0, 0, 0, 0],
                             [1, 0, 0, 0, 0, 1, 0]])

# Create a graph from the adjacency matrix
G = nx.DiGraph()

# Add nodes to the graph
num_nodes = adjacency_matrix.shape[0]
G.add_nodes_from(range(num_nodes))

# Add edges based on the adjacency matrix
for i in range(num_nodes):
    for j in range(num_nodes):
        if adjacency_matrix[i, j] == 1:
            G.add_edge(i, j)

# Compute HITS (Hubs and Authorities) scores
hits_scores = nx.hits(G, max_iter=100)

# Print the Hub and Authority scores of each node
print("Hub Scores:")
for node, hub_score in hits_scores[0].items():
    print(f"Node {node}: {hub_score:.3f}")

print("\nAuthority Scores:")
for node, authority_score in hits_scores[1].items():
    print(f"Node {node}: {authority_score:.3f}")

# Visualize the graph
pos = nx.spring_layout(G, seed=42)
labels = {i: f"Node {i}" for i in range(num_nodes)}
nx.draw(G, pos, with_labels=True, labels=labels, node_size=500, node_color='lightblue', arrowsize=20)
plt.title("Graph Visualization")
plt.savefig('images/hits_centrality_graph.png')
plt.show()
