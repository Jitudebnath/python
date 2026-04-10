# Remove duplicate without changing that particular array
def remove_duplicate(nums):
    n = len(nums)
    if n == 1:
        return 1
    i = 0
    j = i + 1
    while j < n:
        if nums[j] != nums[i]:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
        j += 1
    return i + 1


num = list(map(int, input("Enter the list:").split()))
print(remove_duplicate(num))
