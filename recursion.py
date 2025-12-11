#recursive function
#here this program is going to print the factorail of the number 
def fact(n):
    if n == 0 or n == 1:   # base case
        return 1
    else:                  # recursive case
        return n * fact(n - 1)
print(fact(5))