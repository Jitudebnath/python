"""print all odd numbers from the lists which you have declared 
in the the program """

my_list = [45,12,45,87,89,59,56,75,24,25]

for i in my_list:
    if i % 2 != 0:   # check if odd
        print(i, end=" ")
