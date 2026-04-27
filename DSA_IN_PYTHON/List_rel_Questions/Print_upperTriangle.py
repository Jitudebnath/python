# print the upper triangle of a matrix
nums = [[5, 4, 8], [7, 6, 3], [2, 1, 9]]
rows = len(nums)
cols = len(nums[0])

for i in range(0, rows):
    for j in range(0, cols):
        if j >= i:
            print(nums[i][j], end="  ")
        else:
            print("*", end="  ")
    print()
