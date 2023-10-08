import networkx as nx

# Define the number of nodes (n) in the circle graph (ensure n is odd and >= 3)
n = 7

# Create a circle graph with n nodes
G = nx.cycle_graph(n)

# Compute closeness centrality for each node
closeness_centrality = nx.closeness_centrality(G)

# Print the closeness centrality for each node
for node, closeness in closeness_centrality.items():
    print(f"Node {node}: Closeness Centrality = {closeness:.4f}")
