#This fuction is all about sum of n natural number using recursive function
n=int(input("Enter a psositive natural number : "))

def sum_natural(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    else:
        return sum_natural(n-1)+n
    
print(sum_natural(n))
    
