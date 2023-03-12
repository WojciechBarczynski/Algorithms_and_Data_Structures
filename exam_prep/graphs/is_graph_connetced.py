from collections import deque

def is_graph_connected(adjacency_list):
    vertex_count = len(adjacency_list)
    visited = [False for _ in range(vertex_count)]

    queue = deque()
    queue.append(0)
    visited[0] = True
    while queue:
        u = queue.popleft()
        for neighbour in adjacency_list[u]:
            if not visited[neighbour]:
                visited[neighbour] = True
                queue.append(neighbour)
    for is_visited in visited:
        if not is_visited:
            return False
    return True