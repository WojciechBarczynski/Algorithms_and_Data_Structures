def bellman_ford_edge_list(edge_list, vertex_count, source):  # (edge_start, edge_end, weight)
    edge_count = len(edge_list)

    distances = [float('inf') for _ in range(vertex_count)]
    distances[source] = 0

    for _ in range(vertex_count - 1):
        for edge_start, edge_end, weight in edge_list:
            if distances[edge_start] + weight < distances[edge_end]:
                distances[edge_end] = distances[edge_start] + weight

    return distances

G = [(0, 1, -1), (0, 2, 4), (1, 2, 3), (1, 3, 2), (1, 4, 2), (3, 2, 5), (3, 1, 1), (4, 3, -3)]

print(bellman_ford_edge_list(G, 5, 0))