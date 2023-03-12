# Wojciech Barczynski
# Szukanie cyklu hamiltona - problem NP trudny
# rozwazanie wszystkich sciezek

from zad7testy import runtests


def rekur(G, n, vertex, steps, visited, gate):
    if steps == n - 1:
        if 0 in G[vertex][(gate + 1) % 2]:
            return [vertex]
        else:
            return None
    else:
        for i in range(len(G[vertex][(gate + 1) % 2]) - 1, -1, -1):
            el = G[vertex][(gate + 1) % 2][i]
            if visited[el] is False:
                visited[el] = True
                if vertex in G[el][0]:
                    path = rekur(G, n, el, steps + 1, visited, 0)
                    if path is not None:
                        return path + [vertex]
                if vertex in G[el][1]:
                    path = rekur(G, n, el, steps + 1, visited, 1)
                if path is None:
                    visited[el] = False
                else:
                    return path + [vertex]
        return None


def droga(G):
    visited = [False for _ in range(len(G))]
    visited[0] = True
    a = rekur(G, len(G), 0, 0, visited, 0)
    if a is not None:
        return a
    a = rekur(G, len(G), 0, 0, visited, 1)
    if a is not None:
        return a
    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(droga, all_tests=True)
