from zad8testy import runtests
from math import ceil, sqrt
from collections import deque


def check_if_is_connected(edges, begging, ending, n):
    G = [[] for _ in range(n)]
    for i in range(begging, ending + 1):
        G[edges[i][0]].append(edges[i][1])
        G[edges[i][1]].append(edges[i][0])
    visited = [False for _ in range(n)]
    q = deque()
    q.append(edges[0][0])
    visited[edges[0][0]] = True
    number_of_visited = 1
    while q:
        u = q.popleft()
        for neighbour in G[u]:
            if not visited[neighbour]:
                number_of_visited += 1
                q.append(neighbour)
                visited[neighbour] = True
                if number_of_visited == n:
                    return True
    return False


def binary_search(edges, start, begging, ending, n):
    if begging == ending:
        return begging
    mid = (begging + ending) // 2
    if check_if_is_connected(edges, start, mid, n):
        return binary_search(edges, start, begging, mid, n)
    else:
        return binary_search(edges, start, mid + 1, ending, n)


def highway(A):
    n = len(A)
    distance = [[ceil(sqrt(pow(A[i][0] - A[j][0], 2) + pow(A[i][1] - A[j][1], 2)))
                 for i in range(j + 1)] for j in range(n)]
    edges = []
    for i in range(n):
        for j in range(i):
            edges.append((j, i, distance[i][j]))
    edges.sort(key=lambda x: x[2])

    minimal = edges[-1][2]
    for i in range(len(edges)):
        if check_if_is_connected(edges, i, len(edges) - 1, n):
            optimal = binary_search(edges, i, i, len(edges) - 1, n)
            if edges[optimal][2] - edges[i][2] < minimal:
                if check_if_is_connected(edges, i, optimal, n):
                    minimal = edges[optimal][2] - edges[i][2]

    return minimal


runtests(highway, all_tests=True)
