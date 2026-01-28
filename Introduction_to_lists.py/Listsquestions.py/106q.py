"""Remove all the even numbers from the list"""

my_list = [45, 88, 77, 99, 55, 56, 44, 12, 99]

new_list = []

for i in my_list:
    if i % 2 != 0:
        new_list.append(i)

print(new_list)
