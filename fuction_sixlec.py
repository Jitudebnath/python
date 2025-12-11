#find the average of 3 numbers

def calc_avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)
    return(avg)
    

calc_avg(1,2,3)

#cities and heroes etc using function

cities=["pune","hydrabad","kolkata","bhubaneswar"]
heroes=["krish","superman","batman","ironman"]


def print_len(list):
    print(len(list))
        
def print_list(list):
    for item in list:
        print(item,end=" ")
        
        print_list(heroes)
print()