
def partition(array, left, right):
    x = array[right]
    i = left - 1
    for j in range(left, right):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[right] = array[right], array[i + 1]
    return i + 1


def quick_sort(array, left, right):
    if left < right:
        q = partition(array, left, right)
        quick_sort(array, left, q - 1)
        quick_sort(array, q + 1, right)

