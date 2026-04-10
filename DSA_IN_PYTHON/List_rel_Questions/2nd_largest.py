# find second largest element in a list
def second_largest(nums):

    largest = float("-inf")
    Sec_largest = float("-inf")
    n = len(nums)

    for i in range(0, n):
        largest = max(largest, nums[i])

    for i in range(0, n):
        if nums[i] > Sec_largest and nums[i] != largest:
            Sec_largest = nums[i]

    return Sec_largest


num = list(map(int, input("Enter the list of numbers:").split()))
print(second_largest(num))
