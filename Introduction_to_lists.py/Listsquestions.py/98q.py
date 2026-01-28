"""Make your own list . Count the numbers which are divisible by both 2 and five ,
numbers present in that list """

my_list = [45,88,66,22,44,41,50,55,47,54]

count=0

for i in my_list:
    if i%2==0:
        if i%5==0:
            count +=1


print(f"there are {count} numbers in list which are divisible by both 2&5.")