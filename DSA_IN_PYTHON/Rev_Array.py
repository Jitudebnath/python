"""Reverse an array using recursion"""


def reverseArray(arr, left, right):
    if left >= right:
        return

    arr[left], arr[right] = arr[right], arr[left]
    reverseArray(arr, left + 1, right - 1)
    return arr


arr = [7, 2, 1, 6, 5, 3, 2]
print(reverseArray(arr, 0, 5))
