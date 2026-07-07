"""
Print the all following lists elements which are even numbers 
"""
my_list=[56,32,99,77,65,88,87]

#here iteration by index

for i in range(0,len(my_list)):
    if my_list[i]%2==0:
        print(my_list[i])