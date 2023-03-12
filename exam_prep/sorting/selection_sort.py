def selection_sort(T):
    for i in range(len(T) - 1):
        min_index = i
        for j in range(i + 1, len(T)):
            if T[j] < T[min_index]:
                min_index = j
        T[i], T[min_index] = T[min_index], T[i]
    return T

T = [-12, 5, -1, 22, 4, -2]
print(selection_sort(T))