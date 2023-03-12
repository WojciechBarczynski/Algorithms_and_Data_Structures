# Wojciech Barczynski 410754
'''
Robimy Edmondsa Karpa dla wszystkich kombinacji wierzchołków docelowych.
Złożoność obliczeniowa: jakbym nie używał pop-ów z listy i innych takich to O(E^2 V^3),
ale tutaj i tak liczy się minimalizowanie czasu testów i mojego czasu poświęconego na to zadanie, więc who cares.
Złożoność pamięcowa: O(V + E)
'''


from zad9testy import runtests
from collections import deque
import copy


def Edmonds_Karp(resnet, s, sink1, sink2):
    queue = deque()
    visited = [False for _ in range(len(resnet))]
    parents = [None for _ in range(len(resnet))]
    val = [None for _ in range(len(resnet))]
    val[s] = float('inf')
    queue.append(s)
    visited[s] = True
    flag = True
    while queue and flag:
        u = queue.popleft()
        for neighbour, flow in resnet[u]:
            if visited[neighbour] is False:
                visited[neighbour] = False
                val[neighbour] = min(val[u], flow)
                parents[neighbour] = u
                queue.append(neighbour)
                if neighbour == sink1 or neighbour == sink2:
                    flag = False
                    break
    if val[sink1] is not None:
        vertex = sink1
        parent = parents[sink1]
        augmented_flow = val[sink1]
    elif val[sink2] is not None:
        vertex = sink2
        parent = parents[sink2]
        augmented_flow = val[sink2]
    else:
        return None

    while parent is not None:
        for i in range(len(resnet[parent])):
            if resnet[parent][i][0] == vertex:
                if resnet[parent][i][1] - augmented_flow != 0:
                    resnet[parent][i] = (
                        resnet[parent][i][0], resnet[parent][i][1] - augmented_flow)
                else:
                    resnet[parent].pop(i)
                vertex = parent
                parent = parents[vertex]
                break
    return augmented_flow


def maxflow(G, s):
    vertex_count = 0
    for ver1, ver2, flow in G:
        vertex_count = max(vertex_count, ver1 + 1, ver2 + 1)
    graph = [[] for _ in range(vertex_count)]
    for ver1, ver2, flow in G:
        graph[ver1].append((ver2, flow))

    maximal_flow = 0

    for sink1 in range(vertex_count - 1):
        if sink1 != s:
            for sink2 in range(sink1 + 1, vertex_count):
                if sink2 != s:
                    resnet = [[el for el in graph[i]]
                              for i in range(vertex_count)]
                    current_flow = 0
                    while True:
                        augmented_flow = Edmonds_Karp(resnet, s, sink1, sink2)
                        if augmented_flow is None:
                            break
                        else:
                            current_flow += augmented_flow
                    maximal_flow = max(maximal_flow, current_flow)
    return maximal_flow


runtests(maxflow, all_tests=True)
