"""floor and ceil question using python programming language"""


def find_floor_ceil(nums, target):
    n = len(nums)
    high = n - 1
    target = 6
    floor = -1
    ceil = -1
    low = 0

    while low <= high:
        mid = (low + high) // 2
    if nums[mid] == target:
        return [nums[mid], nums[mid]]
    elif nums[mid] > target:
        ceil = nums[mid]
        high = mid - 1
    else:
        floor = nums[mid]
    low = mid + 1

    return [floor, ceil]
