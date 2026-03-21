"""print the frequency of the numbers"""

nums = [2, 3, 4, 5, 6, 7, 8, 9, 6, 4, 3, 2, 5, 4, 5, 6, 6, 6]
freq_map = dict()
for i in range(0, len(nums)):
    if nums[i] in freq_map:
        freq_map[nums[i]] += 1
    else:
        freq_map[nums[i]] = 1

print(freq_map[6])
