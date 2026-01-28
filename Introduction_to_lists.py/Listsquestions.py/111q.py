"""Make a list.Then ask a number from user .If number exist
in that list then print the position of the elements else print-1"""

my_list = [5, 1, 56.32, 5, 5, 1, 1, 78, 45, 12]

value = float(input("Enter the value :"))

if value in my_list:
    index = my_list.index(value)

    print(f"Index ={index}")
else:
    print(-1)
