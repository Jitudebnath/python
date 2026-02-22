"""This is related toselection short using python"""


def SelectionShort(nums):
    n = len(nums)
    for i in range(0, n):
        mini_index = i
    for j in range(i + 1, n):
        if nums[j] < nums[mini_index]:
            mini_index = j
    nums[i], nums[mini_index] = nums[mini_index], nums[i]
    return nums


nums = list(map(int, (input("Enter the numbers seperated by space:").split())))
print("Sorted list:", SelectionShort(nums))
