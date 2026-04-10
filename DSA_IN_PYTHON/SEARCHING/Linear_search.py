# python program for linear search


def linear_search(nums):
    target = 4
    n = len(nums)
    for i in range(0, n):
        if nums[i] == target:
            return i

    return -1


nums = list(map(int, input("Enter the list of numbers using space:").split()))
print(linear_search(nums))
