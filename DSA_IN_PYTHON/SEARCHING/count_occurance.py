"""Count occurance in sorted Array"""


def lower_bound(arrr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


def upper_bound(arrr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left


def count_occurance(arr, target):
    return upper_bound(arr, target) - lower_bound(arr, target)


arr = list(map(int, input("Enter the numbers using space").split()))
target = int(input("Enter the target value:"))

print(count_occurance(arr, target))
