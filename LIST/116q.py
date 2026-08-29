"""
Write a python code to find out the second largest
element present in that particular list
"""

my_list = [12, 36, 48, 60, 72, 24, 84, 96, 108, 120]

largest = float("-inf")
sec_largest = float("-inf")

for num in my_list:
    if num > largest:
        sec_largest = largest
        largest = num
    elif num > sec_largest and num < largest:
        sec_largest = num


print(sec_largest)
