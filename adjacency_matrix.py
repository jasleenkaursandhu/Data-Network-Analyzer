import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import os

# Define the adjacency matrix A
A = np.array([
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0, 1, 0]
])

# Create a directory to save images if it doesn't exist
os.makedirs("images", exist_ok=True)

# 1. Check if the adjacency matrix represents a simple graph
is_simple_graph = np.all(np.logical_or(A == 0, A == 1))
print("1. Is it a simple graph? ", is_simple_graph)

# 2. Check if the adjacency matrix can represent an undirected graph
is_undirected = np.array_equal(A, A.T)
print("2. Can it represent an undirected graph? ", is_undirected)

# Visualization of the graph
G = nx.Graph(A)
plt.figure(figsize=(6, 6))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=8)
plt.title("Graph Visualization (Undirected)")
plt.savefig("images/graph_undirected.png")
plt.show()

# 3. Check if the graph is connected using matrix exponentiation
n = A.shape[0]
is_connected = np.all(np.linalg.matrix_power(A, n) > 0)
print("3. Is the graph connected? ", is_connected)

# 4. Find the minimum k such that Ak contains no entry equal to 1
k = 1
while np.any(np.linalg.matrix_power(A, k) == 1):
    k += 1
min_k = k if k <= n else -1
print("4. Minimum k (Ak contains no entry equal to 1): ", min_k)

# 5. Find connected components (use depth-first search)
visited = np.zeros(n, dtype=bool)
components = []

def dfs(node):
    visited[node] = True
    component.append(node)
    for neighbor, connected in enumerate(A[node]):
        if connected and not visited[neighbor]:
            dfs(neighbor)

for node in range(n):
    if not visited[node]:
        component = []
        dfs(node)
        components.append(component)

print("5. Number of connected components: ", len(components))
print("Connected components: ", components)

# Visualization of connected components
plt.figure(figsize=(6, 6))
colors = plt.cm.tab20(np.linspace(0, 1, len(components)))
for i, component in enumerate(components):
    subgraph = G.subgraph(component)
    pos = nx.spring_layout(subgraph, seed=42)
    nx.draw(
        subgraph, pos, with_labels=True, node_size=500,
        node_color=colors[i], font_size=8, label=f"Component {i + 1}"
    )
plt.title("Connected Components Visualization")
plt.savefig("images/connected_components.png")
plt.show()

# 6. Find the maximum degree of a node
degrees = np.sum(A, axis=0)
max_degree = np.max(degrees)
print("6. Maximum degree of a node: ", max_degree)

# 7. Find the number of walks of length 5 from node 0 to itself
walk_length = 5
num_walks_from_0_to_0 = np.linalg.matrix_power(A, walk_length)[0, 0]
print(f"7. Number of walks of length {walk_length} from node 0 to itself: ", num_walks_from_0_to_0)

# 8. Check if the statement is True or False
diagonal_entries = np.diag(A)
is_statement_true = np.array_equal(diagonal_entries, degrees)
print("8. Is the statement True? ", is_statement_true)

# Visualization of the adjacency matrix
plt.figure(figsize=(6, 6))
plt.imshow(A, cmap='binary', interpolation='none')
plt.title("Adjacency Matrix")
plt.savefig("images/adjacency_matrix.png")
plt.show()
