"""Bubble sort using python programing language"""

def Bubblesort(nums):
    n= len(nums)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return nums


nums = list(map(int, input("Enter the numbers separated by space: ").split()))
print("Sorted list using bubble sort :", Bubblesort(nums)) 

