# Wojciech Barczynski 410754
# Modified bucket sort with cumulative density function

from zad3testy import runtests


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)



def SortTab(T, P):
    n = len(T)
    probability = [0 for _ in range(n + 1)]
    for interval in P:
        probability_per_int = (interval[2] / (interval[1] - interval[0]))
        probability[interval[0]] += probability_per_int
        probability[interval[1]] -= probability_per_int
    for i in range(1, n):
        probability[i] += probability[i - 1]

    for i in range(1, n):
        probability[i] += probability[i - 1]

    buckets = [[] for _ in range(n // 10 + 1)]

    bucket_length = 1 / n
    for i in range(n):
        buckets[int(probability[int(T[i])] // bucket_length) // 10].append(T[i])

    L = []
    for bucket in buckets:
        length = len(bucket)
        if length < 10:
            for i in range(1, length):
                key = bucket[i]
                j = i - 1
                while j >= 0 and key < bucket[j]:
                    bucket[j + 1] = bucket[j]
                    j -= 1
                bucket[j + 1] = key
            L += bucket
        else:
            quick_sort(bucket, 0, length - 1)
            L += bucket
    return L


runtests(SortTab)
