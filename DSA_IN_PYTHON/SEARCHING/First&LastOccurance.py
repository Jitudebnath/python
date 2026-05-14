"""first and last occurance of a number using python programming language"""


def first_list(nums):
    target = 3
    first = -1
    last = -1
    for i in range(len(nums)):
        if nums[i] == target:
            if first == -1:
                first = i
            last = i
    return [first, last]


nums = list(map(int, input("Enter the numbers using space :").split()))
print(first_list(nums))
