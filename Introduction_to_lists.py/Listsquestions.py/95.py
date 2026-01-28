"""Make your own list.print all the elements
present at the even index"""

list=[45,78,45,"balaram",887,889,847]

#Iterate by index
for i in range(0,len(list)):
    if i%2 ==0:
        print(list[i],end=" ")