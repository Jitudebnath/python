"""make your own list .
print how many positive and negative numbers are
there in that particular list"""

my_list = [12,24,36,48,50,21,31,43,45,47,79]

count = 0
count2=0

for i in my_list:
    if i%2==0:
        count+=1

print(f"There are {count} even numbers.")

for i in my_list:
    if i%2!=0:
        count2+=1

print(f"There are {count2} odd numbers.")        
    