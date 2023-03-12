def bubble_sort(T):
    for i in range(len(T)):
        were_swapped = False
        for j in range(i, len(T)):
            if T[j] <= T[i]:
                T[i], T[j] = T[j], T[i]
                were_swapped = True
        if not were_swapped:
            break
    return T

T = [2, 1, 4, 1, 3224, 45, 6]
print(bubble_sort(T))