"""Create a list and promt the user for an 'oldnumber' followed by a
'new number'.If the 'old number' exists in the list,replace it with the 'new number'
provided by the user"""

my_list = [45, 96, 8, 96, 42, 75, 96, 85, 62, 31, 64, 67]

old = int(input("Enter the old number:"))
new = int(input("Enter the new number:"))

for i in range(0, len(my_list)):
    if my_list[i] == old:
        my_list[i] = new

print(my_list)
