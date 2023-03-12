def insertion_sort(T):
    for i in range(1, len(T)):
        current_val = T[i]
        j = i - 1
        while j >= 0 and current_val < T[j]:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = current_val
    return T

T = [412, 213, 34, 2, 44, 5, 6, -1, 3]
print(insertion_sort(T))