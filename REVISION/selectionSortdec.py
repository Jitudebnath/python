"""selection sort in descending order"""

def SelectionSort(nums):
    n=len(nums)
    for i in range (n):
        max_index = i
        for j in range (i+1,n):
            if nums[j] > nums[max_index]:
                max_index = j 
        nums[i],nums[max_index] = nums[max_index],nums[i]
    return nums

nums = list(map(int, input("Enter the numbers separated by space: ").split()))
print("Sorted list:", SelectionSort(nums)) 