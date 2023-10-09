import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Define the distance matrix (D) as given
D = np.array([
    [0, 3, 6, 5, 2, 4],
    [3, 0, 5, 6, 2, 4],
    [6, 5, 0, 3, 4, 2],
    [5, 6, 3, 0, 4, 2],
    [2, 2, 4, 4, 0, 2],
    [4, 4, 2, 2, 2, 0]
])

# Create a graph from the distance matrix D
G = nx.Graph()

# Add nodes to the graph
n = D.shape[0]
for i in range(n):
    G.add_node(i)

# Add edges to the graph with weights from the distance matrix
for i in range(n):
    for j in range(i + 1, n):
        G.add_edge(i, j, weight=D[i][j])

# Find the minimal spanning tree (MST) using NetworkX
mst = nx.algorithms.tree.minimum_spanning_tree(G)

# Calculate the sum of all edge weights in the MST
total_edge_weight_mst = sum(mst[i][j]['weight'] for i, j in mst.edges())

# Visualize the MST
pos = nx.spring_layout(G)  # Position nodes using a spring layout
labels = {i: i for i in G.nodes()}

plt.figure(figsize=(10, 6))
nx.draw(G, pos, with_labels=True, labels=labels, node_color='lightblue', node_size=500)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

# Draw the minimal spanning tree
mst_edges = [(i, j) for i, j in mst.edges]
nx.draw_networkx_edges(G, pos, edgelist=mst_edges, edge_color='green', width=2)

# Save the visualization to the 'images' folder
plt.savefig('images/minimal_spanning_tree.png', format='png', dpi=300)
plt.show()

# Print the sum of edge weights in the MST
print("Sum of edge weights in the minimal spanning tree (MST):", total_edge_weight_mst)
