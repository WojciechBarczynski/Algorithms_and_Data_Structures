def reverse_adjacency_list_representation(graph):
    new_graph = [[] for _ in range(len(graph))]
    for vertex_index, vertex in enumerate(graph):
        print(vertex_index)
        for neighbour, weight in vertex:
            new_graph[vertex_index].append((weight, neighbour))
    return new_graph
