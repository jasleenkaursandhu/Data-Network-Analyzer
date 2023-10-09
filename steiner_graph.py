import networkx as nx
import matplotlib.pyplot as plt

# Define the adjacency matrix
adjacency_matrix = [
    [0, 3, 0, 5, 2, 0],
    [3, 0, 5, 0, 2, 0],
    [0, 5, 0, 3, 0, 2],
    [5, 0, 3, 0, 0, 2],
    [2, 2, 0, 0, 0, 2],
    [0, 0, 2, 2, 2, 0]
]

# Create a graph from the adjacency matrix
G = nx.Graph()
for i in range(len(adjacency_matrix)):
    for j in range(i + 1, len(adjacency_matrix[i])):
        if adjacency_matrix[i][j] > 0:
            G.add_edge(i + 1, j + 1, weight=adjacency_matrix[i][j])

# Define the terminal nodes
terminals = [1, 2, 3, 4]

# Find the Steiner tree
steiner_tree = nx.algorithms.approximation.steiner_tree(G, terminals)

# Calculate the sum of edge weights in the Steiner tree
total_edge_weight = sum(steiner_tree[i][j]['weight'] for i, j in steiner_tree.edges)

# Visualize the graph and the Steiner tree
pos = nx.spring_layout(G)  # Position nodes using a spring layout
labels = {i: i for i in G.nodes()}

plt.figure(figsize=(10, 6))

# Draw the original graph
nx.draw(G, pos, with_labels=True, labels=labels, node_color='lightblue', node_size=500)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

# Highlight the Steiner tree
steiner_tree_edges = [(u, v) for u, v in steiner_tree.edges]
nx.draw_networkx_edges(G, pos, edgelist=steiner_tree_edges, edge_color='red', width=2)

# Save the visualization to the 'images' folder
plt.savefig('images/steiner_tree.png', format='png', dpi=300)
plt.show()

# Print the sum of edge weights in the Steiner tree
print("Sum of edge weights in the Steiner tree:", total_edge_weight)
