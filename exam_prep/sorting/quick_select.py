def partition(array, left, right):
    x = array[right]
    i = left - 1
    for j in range(left, right):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[right] = array[right], array[i + 1]
    return i + 1


def quick_select(array, searched_index, left, right):
    if left == right:
        return array[left]
    if left < right:
        q = partition(array, left, right)
        if q == searched_index:
            return array[q]
        elif q < searched_index:
            return quick_select(array, searched_index, q + 1, right)
        else:
            return quick_select(array, searched_index, left, q - 1)
