import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import os

# Sample adjacency matrix [0, B; B^T, 0] (replace with your actual data)
m, n = 4, 4  # Number of areas and workers
B = np.array([
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1]
])

# Create a bipartite graph from the adjacency matrix
G = nx.Graph()
G.add_nodes_from(range(m), bipartite=0)  # Areas
G.add_nodes_from(range(m, m + n), bipartite=1)  # Workers
edges = [(i, j + m) for i in range(m) for j in range(n) if B[i, j] == 1]
G.add_edges_from(edges)

# 1. Minimum number of workers required to cover all areas
min_cover = nx.bipartite.minimum_cover(G, top_nodes=range(m))
min_cover_size = len(min_cover)

# 2. Areas served by the fewest workers
area_degree = G.degree(range(m))
areas_fewest_workers = [node for node, degree in area_degree if degree == min(area_degree.values())]

# Create a visualization of the bipartite graph
plt.figure(figsize=(10, 6))
pos = nx.bipartite_layout(G, range(m))
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, font_size=10)
plt.title("Bipartite Graph of Areas and Workers")
plt.axis('off')

# Save the visualization to the "images" folder
os.makedirs("images", exist_ok=True)
plt.savefig("images/bipartite_graph.png")

# Display the results
print(f"1. Minimum number of workers required to cover all areas: {min_cover_size}")
print("2. Areas served by the fewest workers:", areas_fewest_workers)
