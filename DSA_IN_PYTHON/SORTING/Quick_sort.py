# This program is related to Quick sort implementation


def partition(nums, low, high):
    pivot = nums[low]
    i = low + 1
    j = high

    while True:
        while i <= high and nums[i] <= pivot:
            i += 1
        while j >= low and nums[j] > pivot:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            break

    nums[low], nums[j] = nums[j], nums[low]
    return j


def quick_sort(nums, low, high):
    if low < high:
        p_index = partition(nums, low, high)
        quick_sort(nums, low, p_index - 1)
        quick_sort(nums, p_index + 1, high)


# Taking input from the user
nums = list(map(int, input("Enter the numbers using space: ").split()))
quick_sort(nums, 0, len(nums) - 1)
print("Sorted list:", nums)
