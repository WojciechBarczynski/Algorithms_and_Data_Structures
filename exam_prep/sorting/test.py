import random

def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2

        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right)

        left_index = 0
        right_index = 0
        merge_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index][0] <= right[right_index][0]:
                array[merge_index] = left[left_index]
                left_index += 1
            else:
                array[merge_index] = right[right_index]
                right_index += 1
            merge_index += 1

        while left_index < len(left):
            array[merge_index] = left[left_index]
            left_index += 1
            merge_index += 1

        while right_index < len(right):
            array[merge_index] = right[right_index]
            right_index += 1
            merge_index += 1


T = []
for i in range(1000):
    T.append((random.randint(-10, 10), i))

merge_sort(T)
print(T)