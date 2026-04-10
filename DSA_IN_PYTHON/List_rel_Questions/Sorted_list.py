# write a program to check wether the list is sorted or not.
def sorted(nums):
    n = len(nums)
    for i in range(0, n - 1):
        if nums[i] > nums[i + 1]:
            return False

    return True


num = list(map(int, input("Enter a list of numbers:").split()))
print(sorted(num))
