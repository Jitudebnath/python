# MovesZero is a leetcode based question
def Moves_Zeros(nums):
    insert_pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:

            nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
            insert_pos += 1
    return nums


nums = list(map(int, input("Enter number using space:").split()))
print(Moves_Zeros(nums))
