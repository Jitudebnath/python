"""Converting tuple in list and list in tuple"""

my_tuple = (45, 56, 67, 78, 89, 9, 34)

my_list = list(my_tuple)
my_list.append(100)

my_tuple = tuple(my_list)
print(my_list)
