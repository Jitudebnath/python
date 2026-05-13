"""Bnary search using python programming language"""


def binary_search(nums, target):
    n = len(nums)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


nums = list(map(int, input("Enter a series of numbers using spaces: ").split()))
target = int(input("Enter a number: "))

print(binary_search(nums, target))
