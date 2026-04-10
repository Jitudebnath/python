"""Find out the largest element in a List."""


def largest_element(nums):
    n = len(nums)
    largest = nums[0]
    for i in range(0, len(nums)):
        largest = max(largest, nums[i])

    return largest


nums = list(map(int, input("Enter a list of numbers:").split()))
print("Largest element is:", largest_element(nums))
