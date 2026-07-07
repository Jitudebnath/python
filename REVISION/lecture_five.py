nums=(1,4,9,25,36,49,64,81,100)
x=36

i=0
while i<len(nums):
    if(nums[i]==x):
        print("Found at index",i)
    else:
        print("nothing is found")
    i+=1
#value vaariable

veggies=["potato","brinjal","ladyfinger","cucumber"]

for val in veggies:
    print(val)
#use of range function
for i in range (10):
    print(i)
    
    for i in range(2,10):
        print(i) 
        
        #using range print all even number
        for i in range(2,100,2):
            print(i) 
            
            
#multiplication using range 

n=int(input("enter a number:"))

for i in range(1,11):
    print(n*i)