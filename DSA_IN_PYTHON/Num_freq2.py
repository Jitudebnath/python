"""print the frequency of a number using hash map in python"""

nums = [1, 2, 3, 4, 5, 6, 7]
hash_map = dict()
n = len(nums)
for i in range(0, n):
    hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1

print(hash_map)
