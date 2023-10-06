# Read the directed graph from the file
with open("directed_graph.txt", "r") as file:
    lines = file.readlines()
    edges = [line.strip().split() for line in lines]

# Initialize variables to keep track of graph properties
nodes = set()
edge_count = 0
self_loops = False
in_degree = {}
out_degree = {}

# Iterate through the edges to calculate properties
for edge in edges:
    source, target = map(int, edge)
    nodes.add(source)
    nodes.add(target)
    edge_count += 1

    if source == target:
        self_loops = True

    if source in out_degree:
        out_degree[source] += 1
    else:
        out_degree[source] = 1

    if target in in_degree:
        in_degree[target] += 1
    else:
        in_degree[target] = 1

# 1. Number of nodes in the graph
num_nodes = len(nodes)

# 2. Number of edges in the graph
num_edges = edge_count

# 3. Does the graph contain self-loops?
contains_self_loops = "Yes" if self_loops else "No"

# 4. Does the graph have directed cycles not involving self-loops?
has_directed_cycles = "Yes" if any(in_degree[node] > 0 and out_degree[node] == 0 for node in nodes) else "No"

# 5. Maximum likelihood estimate of p
p_estimate = num_edges / (num_nodes * (num_nodes - 1))

# 6. p-value for the null hypothesis that p=0.1
from math import sqrt
from scipy.stats import norm

p_null_hypothesis = 0.1  # Null hypothesis value for p
sample_mean = num_edges / (num_nodes * (num_nodes - 1))
sample_variance = (p_null_hypothesis * (1 - p_null_hypothesis)) / (num_nodes * (num_nodes - 1))
z = abs((sample_mean - p_null_hypothesis) / sqrt(sample_variance))
p_value = 2 * (1 - norm.cdf(z))

# Print the results
print("1. Number of nodes in the graph:", num_nodes)
print("2. Number of edges in the graph:", num_edges)
print("3. Does the graph contain self-loops?", contains_self_loops)
print("4. Does the graph have directed cycles not involving self-loops?", has_directed_cycles)
print("5. Maximum likelihood estimate of p:", p_estimate)
print("6. p-value for the null hypothesis that p=0.1:", p_value)
