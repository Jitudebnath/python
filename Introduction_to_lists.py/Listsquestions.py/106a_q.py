"""Remove all the odd numbers from the list"""

my_list = [45, 66, 66, 66, 78, 11, 11, 12, 12, 12]

for i in my_list:
    if i % 2 != 0:
        my_list.remove(i)

print(my_list)
