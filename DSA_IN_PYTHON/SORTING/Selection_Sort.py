"""This is related toselection short using python"""


def SelectionSort(nums):
    n = len(nums)
    for i in range(n):
        mini_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[mini_index]:
                mini_index = j
        nums[i], nums[mini_index] = nums[mini_index], nums[i]
    return nums


nums = list(map(int, input("Enter the numbers separated by space: ").split()))
print("Sorted list:", SelectionSort(nums))
