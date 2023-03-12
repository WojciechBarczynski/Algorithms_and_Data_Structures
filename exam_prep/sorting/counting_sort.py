def counting_sort(array, lower_bound, upper_bound):
    number_range = upper_bound - lower_bound + 1
    n = len(array)
    count = [0 for _ in range(number_range)]
    sorted_array = [None for _ in range(n)]

    for x in array:
        count[x - lower_bound] += 1

    for i in range(1, number_range):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        sorted_array[count[array[i] - lower_bound] - 1] = array[i]
        count[array[i] - lower_bound] -= 1

    for i in range(n):
        array[i] = sorted_array[i]



