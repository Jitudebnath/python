"""Make your own list and find out the
smallest number from that numbers list in python programming
language"""

my_list = [45, -90, -78, 67, 45, 45, 889, 0, -999]

smallest = my_list[0]

for i in range(0, len(my_list)):
    if my_list[i] < smallest:
        smallest = my_list[i]

print(f"The smallest number is {smallest}")
