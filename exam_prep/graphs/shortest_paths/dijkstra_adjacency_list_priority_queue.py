# O(E*logV)
from queue import PriorityQueue


def dijkstra_list(adjacency_list, start):  # (destination, weight)
    q = PriorityQueue()
    distances = [float('inf') for _ in range(len(adjacency_list))]
    distances[start] = 0
    q.put((0, start))
    while not q.empty():
        v_distance, v = q.get()
        if v_distance > distances[v]:
            continue
        for neighbour, weight in adjacency_list[v]:
            distance = v_distance + weight
            if distance < distances[neighbour]:
                distances[neighbour] = distance
                q.put((distance, neighbour))
    return distances


G = [[(1, 4), (7, 8)],
     [(0, 4), (2, 8), (7, 11)],
     [(1, 8), (3, 7), (5, 4), (8, 2)],
     [(2, 7), (5, 14), (4, 9)],
     [(3, 9), (5, 10)],
     [(2, 4), (3, 14), (4, 10), (6, 2)],
     [(5, 2), (7, 1), (8, 6)],
     [(0, 8), (1, 11), (8, 7), (6, 1)],
     [(2, 2), (6, 6), (7, 7)]]

print(dijkstra_list(G, 0))