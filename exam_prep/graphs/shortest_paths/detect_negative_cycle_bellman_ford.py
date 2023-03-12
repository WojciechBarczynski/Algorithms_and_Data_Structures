def negative_cycle_bellman_ford(adjacency_list, source):  # (weight, destination)
    vertex_count = len(adjacency_list)
    edge_count = 0
    for vertex in adjacency_list:
        for edge in vertex:
            edge_count += 1

    distances = [float('inf') for _ in range(vertex_count)]
    distances[source] = 0
    parent = [None for _ in range(vertex_count)]

    for _ in range(vertex_count - 1):
        for vertex_index, vertex in enumerate(adjacency_list):
            for edge_weight, destination_vertex in vertex:
                if distances[vertex_index] is not None and distances[vertex_index] + edge_weight < \
                        distances[destination_vertex]:
                    distances[destination_vertex] = distances[vertex_index] + edge_weight
                    parent[destination_vertex] = vertex_index

    tmp = None
    for vertex_index, vertex in enumerate(adjacency_list):
        for edge_weight, destination_vertex in vertex:
            if distances[vertex_index] + edge_weight < \
                    distances[destination_vertex]:
                tmp = destination_vertex

    if tmp is not None:
        for _ in range(vertex_count):
            tmp = parent[tmp]

        cycle = []
        v = tmp
        while True:
            cycle.append(v)
            v = parent[v]
            if v == tmp:
                break
        return cycle[::-1]
    return False

G = [[(10, 1), (3, 2), (2, 3)],
     [(7, 3)],
     [(6, 3)],
     []]

print(negative_cycle_bellman_ford(G, 0))
