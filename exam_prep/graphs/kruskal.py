def union(x, y):
    global P, R
    x = find(x)
    y = find(y)
    if R[x] > R[y]:
        P[y] = x
    else:
        P[x] = y
        if R[x] == R[y]:
            R[y] = R[y] + 1


def makesets(n):
    global P, R
    P = [i for i in range(n)]
    R = [0 for _ in range(n)]


def find(x):
    global P, R
    if x != P[x]:
        P[x] = find(P[x])
    return P[x]


def kruskal(G):  # (neighbour, weight)
    E = []

    for i in range(len(G)):
        for vertex_neighbour in G[i]:
            E.append((vertex_neighbour[1], i, vertex_neighbour[0]))

    E.sort()
    A = []
    makesets(len(G))
    for w, x, y in E:
        if find(x) != find(y):
            union(x, y)
            A.append((x, y))
    return A


G = [[(1, 4), (7, 8)],
     [(0, 4), (2, 8), (7, 11)],
     [(1, 8), (3, 7), (5, 4), (8, 2)],
     [(2, 7), (5, 14), (4, 9)],
     [(3, 9), (5, 10)],
     [(2, 4), (3, 14), (4, 10), (6, 2)],
     [(5, 2), (7, 1), (8, 6)],
     [(0, 8), (1, 11), (8, 7), (6, 1)],
     [(2, 2), (6, 6), (7, 7)]]

print(kruskal(G))