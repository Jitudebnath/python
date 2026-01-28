"""make your own list. find the sum of all even 
numbers present in that list"""

my_list = [12,24,36,59,48,45,78]

total=0

for i in range(0,len(my_list)):
    if my_list[i]%2==0:
        total=total+my_list[i]

print(f"Sum of all even numbers is {total}")        