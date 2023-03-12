from zad2testy import runtests


def partition_by_begging(L, p, r):
    x = L[r]
    i = p - 1
    for j in range(p, r):
        if L[j][0] < x[0] or (L[j][0] == x[0] and L[j][1] > x[1]):
            i += 1
            L[i], L[j] = L[j], L[i]
    L[i+1], L[r] = L[r], L[i+1]
    return i + 1


def quick_sort_by_begging(L, p, r):
    if p < r:
        q = partition_by_begging(L, p, r)
        quick_sort_by_begging(L, p, q-1)
        quick_sort_by_begging(L, q+1, r)


def depth(L):
    max_depth = 0
    n = len(L)
    quick_sort_by_begging(L, 0, n-1)

    for i in range(n):
        if n - i - 1 < max_depth:
            break
        curr_depth = 0
        for j in range(i+1, n):
            if L[j][0] > L[i][1]:
                break
            if L[j][1] <= L[i][1]:
                curr_depth += 1
        if curr_depth > max_depth:
            max_depth = curr_depth

    return max_depth


runtests(depth)
