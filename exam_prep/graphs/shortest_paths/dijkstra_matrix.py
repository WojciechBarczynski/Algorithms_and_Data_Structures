# O(V^2)

def dijkstra_matrix(adjacency_matrix, source):
    vertex_count = len(adjacency_matrix)
    distances = [float('inf') for _ in range(vertex_count)]
    distances[source] = 0
    shortest_path_tree_set = [False for _ in range(vertex_count)]

    for _ in range(vertex_count):
        minimal = float('inf')

        for i in range(vertex_count):
            if distances[i] < minimal and shortest_path_tree_set[i] is False:
                minimal = distances[i]
                min_index = i

        shortest_path_tree_set[min_index] = True

        for i in range(vertex_count):
            if adjacency_matrix[min_index][i] > 0 and shortest_path_tree_set[i] is False \
                    and distances[i] > distances[min_index]:
                distances[i] = distances[min_index] + adjacency_matrix[min_index][i]
    return distances


g = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
   [4, 0, 8, 0, 0, 0, 0, 11, 0],
   [0, 8, 0, 7, 0, 4, 0, 0, 2],
   [0, 0, 7, 0, 9, 14, 0, 0, 0],
   [0, 0, 0, 9, 0, 10, 0, 0, 0],
   [0, 0, 4, 14, 10, 0, 2, 0, 0],
   [0, 0, 0, 0, 0, 2, 0, 1, 6],
   [8, 11, 0, 0, 0, 0, 1, 0, 7],
   [0, 0, 2, 0, 0, 0, 6, 7, 0]]

print(dijkstra_matrix(g, 0))
