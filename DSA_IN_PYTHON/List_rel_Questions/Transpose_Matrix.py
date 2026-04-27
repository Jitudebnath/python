# print the transpose of a matrix

nums = [[5, 4, 8], [7, 6, 3], [2, 1, 9]]
rows = len(nums)
cols = len(nums[0])

result = [[0] * rows for _ in range(cols)]

for i in range(0, rows):
    for j in range(0, cols):
        result[j][i] = nums[i][j]

print(result)
