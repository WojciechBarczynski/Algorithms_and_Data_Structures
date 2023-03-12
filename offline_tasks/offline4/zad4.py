# Wojciech Barczynski
# O(nlogn + np)

from zad4testy import runtests


def max_val_from_index(cost, index, T, F):
    n = len(T)
    if F[cost][index] is not None:
        return F[cost][index]
    if T[index][3] > cost:
        max_val = max_val_from_index(cost, index + 1, T, F)
    else:
        current_val = T[index][0] * (T[index][2] - T[index][1])
        if T[index][2] >= T[n-1][1]:
            max_val_not_taking = max_val_from_index(cost, index + 1, T, F)
            max_val_taking = (current_val, [T[index][4]])
            if max_val_not_taking[0] >= max_val_taking[0]:
                max_val = max_val_not_taking
            else:
                max_val = max_val_taking
        else:
            next_el = index + 1
            while next_el < n and T[next_el][1] <= T[index][2]:
                next_el += 1
            max_val_not_taking = max_val_from_index(cost, index + 1, T, F)
            max_val_taking = max_val_from_index(
                cost - T[index][3], next_el, T, F)
            max_val_taking = (
                max_val_taking[0] + current_val, max_val_taking[1] + [T[index][4]])
            if max_val_not_taking[0] >= max_val_taking[0]:
                max_val = max_val_not_taking
            else:
                max_val = max_val_taking
            F[cost][index] = max_val
    return max_val


def select_buildings(T, p):
    n = len(T)

    for i in range(n):
        T[i] = (T[i][0], T[i][1], T[i][2], T[i][3], i)

    T.sort(key=lambda x: x[1])
    F = [[None for _ in range(n)] for _ in range(p+1)]

    for i in range(n):
        F[0][i] = (0, [])
    for i in range(min(T[n - 1][3], p + 1)):
        F[i][n - 1] = (0, [])
    last_val = T[n - 1][0] * (T[n - 1][2] - T[n - 1][1])
    for i in range(T[n - 1][3], p + 1):
        F[i][n - 1] = (last_val, [T[n - 1][4]])

    val = max_val_from_index(p, 0, T, F)
    output = val[1]
    output.sort()

    return output


runtests(select_buildings)
