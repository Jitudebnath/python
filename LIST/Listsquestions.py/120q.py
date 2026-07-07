"""Write a program in python that swaps
the first and last elements of a given list"""

my_list = [32, 10, "Jitu", 55.90, "xyz"]
first = my_list[-1]
# print(first)
last = my_list[0]
# print(last)
my_list[0] = first
my_list[-1] = last

print(f"Swap list is = {my_list}")
