"""return the consecutive numbers of ones in a given list"""


def longestOnes(self, nums, k):
    left = 0
    zeros = 0
    max_len = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1

        # shrink window if zeros exceed k
        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len
