import random

def binary_search(array, look_up_val, left, right):
    if left <= right:
        mid = (right + left) // 2
        if array[mid] == look_up_val:
            return mid
        elif array[mid] > look_up_val:
            return binary_search(array, look_up_val, left, mid - 1)
        else:
            return binary_search(array, look_up_val, mid + 1, right)


def next(arr, target):
    start = 0
    end = len(arr) - 1

    ans = -1
    while (start <= end):
        mid = (start + end) // 2

        # Move to right side if target is
        # greater.
        if arr[mid] <= target:
            start = mid + 1

        # Move left side.
        else:
            ans = mid
            end = mid - 1

    return ans

a = [-10, 10, 10, 11, 100, 1000, 2000]
print(next(a, 11))
