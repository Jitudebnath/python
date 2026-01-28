"""make your own list .
print the largest number present in that list"""

my_list = [78, 89, 45, 86, 15, 26, 39, 52, 84, 52, 45]

largest = my_list[0]

for i in range(0, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(f"Largest number in this list is {largest}")
