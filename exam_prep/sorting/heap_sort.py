def heapify(T, length, insertion_index):
    left = 2 * insertion_index + 1
    right = 2 * insertion_index + 2
    max_index = insertion_index
    if left < length and T[left] > T[max_index]:
        max_index = left
    if right < length and T[right] > T[max_index]:
        max_index = right
    if max_index != insertion_index:
        T[insertion_index], T[max_index] = T[max_index], T[insertion_index]
        heapify(T, length, max_index)


def build_heap(T):
    n = len(T)
    parent = (n - 2) // 2
    for i in range(parent, -1, -1):
        heapify(T, n, i)


def heap_sort(T):
    n = len(T)
    build_heap(T)
    for i in range(n - 1, 0, -1):
        T[0], T[i] = T[i], T[0]
        heapify(T, i, 0)
    return T


T = [123, 1, -2, 3, -8, 23]
print(heap_sort(T))
