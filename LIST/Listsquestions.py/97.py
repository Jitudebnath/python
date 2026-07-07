"""Make your own list . Count the numbers of even numbers present 
in that list """

my_list = [45,88,66,22,44,41,26,23,47,54]

count=0

for i in my_list:
    if i%2==0:
        
            count +=1


print(f"There are total {count} even numbers in list.")