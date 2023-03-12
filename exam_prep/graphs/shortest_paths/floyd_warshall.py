def floyd_warshall(G):
    distance = [[edge for edge in vertex] for vertex in G]
    print(distance)

    for k in range(len(G)):
        for i in range(len(G)):
            for j in range(len(G)):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    return distance

INF = float('inf')
graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0,   1],
         [INF, INF, INF, 0]]

print(floyd_warshall(graph))