# Rotate an array by 1 place


def rotate_array(nums):
    n = len(nums)
    temp = nums[n - 1]
    for i in range(n - 2, -1, -1):
        nums[i + 1] = nums[i]
    nums[0] = temp
    return nums


nums = list(map(int, input("Enter the list of elements:").split()))
print(rotate_array(nums))
