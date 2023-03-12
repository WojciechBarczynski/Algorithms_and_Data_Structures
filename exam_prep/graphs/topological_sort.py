def dfs_visit(adjacency_list, vertex, visited, topological_sorted_list):
    visited[vertex] = True
    for neighbour in adjacency_list[vertex]:
        if not visited[neighbour]:
            dfs_visit(adjacency_list, neighbour, visited, topological_sorted_list)
    topological_sorted_list.append(vertex)


def topological_sort_(adjacency_list):
    vertex_count = len(adjacency_list)
    visited = [False for _ in range(vertex_count)]

    topological_sorted_list = []
    for vertex in range(vertex_count):
        if not visited[vertex]:
            dfs_visit(adjacency_list, vertex, visited, topological_sorted_list)
    return topological_sorted_list[::-1]

G = [[3],
     [3, 4],
     [4, 7],
     [5, 6, 7],
     [6],
     [],
     [],
     []]

print(topological_sort_(G))