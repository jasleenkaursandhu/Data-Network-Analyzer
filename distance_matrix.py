import numpy as np

# Define the adjacency matrix
adjacency_matrix = np.array([
    [0, 3, 0, 5, 2, 0],
    [3, 0, 5, 0, 2, 0],
    [0, 5, 0, 3, 0, 2],
    [5, 0, 3, 0, 0, 2],
    [2, 2, 0, 0, 0, 2],
    [0, 0, 2, 2, 2, 0]
])

# Function to compute the distance matrix using Dijkstra's algorithm
def dijkstra(graph, start):
    n = len(graph)
    visited = [False] * n
    distance = [float('inf')] * n
    distance[start] = 0

    for _ in range(n):
        min_distance = float('inf')
        u = -1
        for v in range(n):
            if not visited[v] and distance[v] < min_distance:
                min_distance = distance[v]
                u = v

        visited[u] = True
        for v in range(n):
            if not visited[v] and graph[u][v] > 0 and distance[u] + graph[u][v] < distance[v]:
                distance[v] = distance[u] + graph[u][v]

    return distance

# Initialize the distance matrix D
n = len(adjacency_matrix)
D = np.zeros((n, n), dtype=int)

# Compute the distance matrix D for terminal nodes
terminals = [1, 2, 3, 4]
for i in range(n):
    for j in range(i+1, n):
        shortest_path_lengths = dijkstra(adjacency_matrix, i)
        D[i][j] = shortest_path_lengths[j]
        D[j][i] = D[i][j]

# Print the distance matrix D
print("Distance Matrix (D):")
print(D)
