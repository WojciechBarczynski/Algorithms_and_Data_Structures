# Wojciech Barczynski 410754
'''
Opis algorytmu:
Zauwazmy, ze aby wydluzyc najkrotsza sciezke z wierzcholka s do wierzcholka t musimy usunac krawedz znajdujaca
sie w kazdej z najkrotszych sciezek. Wiemy, ze odleglosc pomiedzy dwoma wierzcholkami jest metryka, wiec spelnia
tez ona warunek trojkata, wiec jesli jakas krawedz wystepuje we wszystkich najkrotszych sciezkach, to jest ona
w kazdej z tych sciezek rowno odlegla od s. Na poczatku wyznaczamy wiec zmodyfikowanym algorytmem BFS najkrotsze
sciezki z s do t (zapisujemy dla kazdego wierzcholka na najkrotszej sciezce w s do t z jakich wierzcholkow mozna
do niego dotrzec najszybciej). Nastepnie sprawdzamy czy na ktorejs "fali" BFSa do parentach od t do s
znajduje sie tylko jedna krawedz, jesli tak to oznacza to, ze krawedz ta wystepuje we wszystkich najkotszych sciezkach,
wiec jest ona odpowiedzia na nasze pytanie, jesli natomiast taka krawedz nie istnieje, to nie mozna wydluzyc
sciezki przez usuniecie tylko jednej krawedzi.
'''


from zad6testy import runtests
from collections import deque


def longer(G, s, t):
    if s == t:
        return None

    vertices_count = len(G)
    distance = [None for _ in range(vertices_count)]
    parents = [[] for _ in range(vertices_count)]
    parents[s] = [None]
    distance[s] = 0
    has_reached_t = False
    queue = deque()
    queue.append(s)

    while queue:
        u = queue.popleft()
        u_distance = distance[u]
        if has_reached_t:
            if u_distance + 1 > distance[t]:
                break
        for neighbour in G[u]:
            if distance[neighbour] is None:
                distance[neighbour] = u_distance + 1
                for i in range(len(parents[neighbour])):
                    if parents[neighbour][i] == u:
                        break
                else:
                    parents[neighbour].append(u)
                queue.append(neighbour)
            elif distance[neighbour] == u_distance + 1:
                for i in range(len(parents[neighbour])):
                    if parents[neighbour][i] == u:
                        break
                else:
                    parents[neighbour].append(u)
                queue.append(neighbour)
            if neighbour == t:
                has_reached_t = True

    if distance[t] is None:
        return None
    if distance[t] == 1:
        return (s, t)

    last_distance = distance[t]
    backward_ver_queue = deque()
    backward_edge_queue = deque()
    backward_ver_queue.append(t)

    while backward_ver_queue:
        u = backward_ver_queue.popleft()
        if u is None:
            break
        if distance[u] == last_distance - 1:
            is_only_one_edge = True
            a = backward_edge_queue.popleft()
            while backward_edge_queue:
                b = backward_edge_queue.popleft()
                if a != b:
                    is_only_one_edge = False
            if is_only_one_edge:
                return a
            last_distance -= 1

        for parent in parents[u]:
            backward_ver_queue.append(parent)
            backward_edge_queue.append((parent, u))

    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(longer, all_tests=True)
