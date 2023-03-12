# Wojciech Barczyński
'''
Opis algorytmu:
Najpierw przechodzimy po drzewie zapisując w x-ie wysokość, na której znajduje się dany wierzchołek. Później przechodzimy
po drzewie jeszcze raz zapisując max wysokość drzewa. Następnie znowu przechodzimy po drzewie zapisując dla każdego
poziomu drzewa liczbę node-ów znajdujących się na tym poziomie. Sprawdzamy max liczbę node-ów na wszyskich poziomowach.
Wybieramy poziom z max liczbą node-ów i max wysokością. Przechodzimy po drzewie jeszcze raz zmieniając wartość pola x na
krotkę (left_val, right_val) gdzie left_val/right_val = True/False/None -> True - w lewym/prawym poddrzewie znajduje się
wierzchołek na wybranym poziomie (o max width i max height), False - nie znajduje się, None - nie ma poddrzewa.
Następnie przechodzimy po drzewie, gdy w poddrzewie znajduje się wiezchołek idziemy do tego poddrzewa, gdy nie ucinamy go,
gdy nie ma go nic nie robimy. Tym sposobem opytmalnie ucinamy wszyskie zbędne wierzchołki.

Złożoność czasowa: O(n) -> tylko przejścia po drzewie
Złośoność pamięciowa: O(n)
'''

from egz1btesty import runtests
from collections import deque


class Node:
    def __init__(self):
        self.left = None    # lewe poddrzewo
        self.right = None   # prawe poddrzewo
        self.x = None       # pole do wykorzystania przez studentow


def insert_height(parent_height, vertex):
    vertex.x = parent_height + 1
    if vertex.left is not None:
        insert_height(vertex.x, vertex.left)
    if vertex.right is not None:
        insert_height(vertex.x, vertex.right)


def change_x(vertex, max_height_max_width):
    if vertex.x == max_height_max_width:
        left_val, right_val = None, None
        if vertex.left is not None:
            left_val = False
        if vertex.right is not None:
            right_val = False
        vertex.x = (left_val, right_val)
        return True
    if vertex.x > max_height_max_width:
        return False
    else:
        if vertex.left is None:
            left_val = None
        else:
            left_val = change_x(vertex.left, max_height_max_width)
        if vertex.right is None:
            right_val = None
        else:
            right_val = change_x(vertex.right, max_height_max_width)
        vertex.x = (left_val, right_val)
        if right_val is True or left_val is True:
            return True
        else:
            return False


def wideentall(T):
    T.x = 0
    if T.left is not None:
        insert_height(0, T.left)
    if T.right is not None:
        insert_height(0, T.right)

    max_height = 0

    q = deque()
    q.append(T)

    while q:
        vertex = q.popleft()
        max_height = max(max_height, vertex.x)
        if vertex.left is not None:
            q.append(vertex.left)
        if vertex.right is not None:
            q.append(vertex.right)

    level_width = [0 for _ in range(max_height + 1)]

    q.append(T)
    while q:
        vertex = q.popleft()
        level_width[vertex.x] += 1
        if vertex.left is not None:
            q.append(vertex.left)
        if vertex.right is not None:
            q.append(vertex.right)

    max_width = max(level_width)
    max_height_max_width = 0
    for level_index, level_width_size in enumerate(level_width):
        if max_width == level_width_size:
            max_height_max_width = level_index

    # teraz x = (True/False/None, True/False/None) -> czy lewe, prawe dziecko ma potomka na poziomie o ladnosci max

    cut_edge_count = 0
    change_x(T, max_height_max_width)

    vertex_queue = deque()
    vertex_queue.append(T)

    while vertex_queue:
        vertex = vertex_queue.popleft()
        left_val, right_val = vertex.x
        if left_val is False:
            cut_edge_count += 1
        if left_val is True:
            vertex_queue.append(vertex.left)
        if right_val is False:
            cut_edge_count += 1
        if right_val is True:
            vertex_queue.append(vertex.right)
    return cut_edge_count


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(wideentall, all_tests=True)
