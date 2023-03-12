def bellman_ford(adjacency_list, source):  # (weight, destination)
    vertex_count = len(adjacency_list)
    edge_count = 0
    for vertex in adjacency_list:
        for edge in vertex:
            edge_count += 1

    distances = [float('inf') for _ in range(vertex_count)]
    distances[source] = 0

    for _ in range(vertex_count - 1):
        for vertex_index, vertex in enumerate(adjacency_list):
            for edge_weight, destination_vertex in vertex:
                if distances[vertex_index] + edge_weight < distances[destination_vertex]:
                    distances[destination_vertex] = distances[vertex_index] + edge_weight

    for vertex_index, vertex in enumerate(adjacency_list):
        for edge_weight, destination_vertex in vertex:
            if distances[vertex_index] + edge_weight < distances[destination_vertex]:
                return None # contain negative cycle

    return distances

