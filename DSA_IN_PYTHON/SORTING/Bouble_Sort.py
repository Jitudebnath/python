"""This program is related to Boublesort"""


def Bubble_Sort(nums):
    n = len(nums)
    # Outer loop for passes
    for i in range(n - 1):
        # Inner loop for comparisons
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:  # Compare adjacent elements
                nums[j], nums[j + 1] = nums[j + 1], nums[j]  # Swap if needed
    return nums


# Taking input from the user
nums = list(map(int, input("Enter the numbers separated by space: ").split()))
print("Sorted list:", Bubble_Sort(nums))
