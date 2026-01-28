"""Write a program to splits list into two halves"""

my_list = [34, 45, 56, 67, 78, 34, 45, 56, 23]

first_half = []
second_half = []

middle_index = len(my_list) // 2

for i in range(0, middle_index):
    first_half.append(my_list[i])

for i in range(middle_index, len(my_list)):
    second_half.append(my_list[i])


print(f"First list ={first_half}")
print(f"Second list ={second_half}")
