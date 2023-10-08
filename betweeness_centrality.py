def betweenness_centrality_line_graph(n, i):
    betweenness = 0.0
    
    for s in range(1, n+1):
        if s == i:
            continue
        for t in range(1, n+1):
            if t == i or t == s:
                continue
            num_paths_i_st = 0
            g_st = 0
            for j in range(1, n+1):
                if j != s and j != t:
                    num_paths_i_st += (n ** i) ** (abs(s - j) + abs(t - j))
                    g_st += (n ** (s - t)) ** (abs(j - s) + abs(j - t))
            
            betweenness += num_paths_i_st / g_st
    
    return betweenness

# Example usage:
n = 5  # Number of nodes in the line graph
i = 3  # Node for which you want to calculate betweenness centrality
result = betweenness_centrality_line_graph(n, i)
print(f"Betweenness Centrality of Node {i}: {result}")
