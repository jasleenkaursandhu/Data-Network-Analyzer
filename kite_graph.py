import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# Create the kite graph based on your description
edges = [(1, 2), (1, 4), (2, 3), (3, 4), (3, 5), (5, 6), (6, 7), (7, 8)]
G = nx.Graph(edges)

# Compute the Fiedler vector (eigenvector corresponding to the second smallest eigenvalue)
fiedler_vector = nx.fiedler_vector(G)

# Normalize the eigenvector
normalized_fiedler_vector = fiedler_vector / np.linalg.norm(fiedler_vector)

# Round the values to three significant figures
rounded_normalized_fiedler_vector = [round(value, 3) for value in normalized_fiedler_vector]

# Visualization
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue")
plt.title("Kite Graph")
plt.axis('off')

# Save the visualization as an image
plt.savefig("images/kite_graph.png")

# Print the results for each node
for node, value in enumerate(rounded_normalized_fiedler_vector, start=1):
    print(f"Node {node}: {value}")

# Show the graph visualization (optional)
plt.show()