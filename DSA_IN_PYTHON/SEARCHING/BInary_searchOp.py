"""binaray search using recursion concepts"""


def binary_search(nums, low, high, target):
    if low < high:
        return -1

    mid = (low + high) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_search(nums, mid + 1, high)
    else:
        return binary_search(nums, low, mid - 1)
