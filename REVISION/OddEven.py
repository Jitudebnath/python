#include retirn odd in case of odd and return even in case of even
n=int (input("Enter a positive integer number : "))
def num_check(n):
    if (n%2==0):
        print(" This is an EVEN number")
    else:
        print(" This is an ODD number")
        return(num_check)
num_check(n)