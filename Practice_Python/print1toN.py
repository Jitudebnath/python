"""print 1 to N using function"""


def one_to_n(n):
    if n == 0:  # base case
        return
    one_to_n(n - 1)  # recursive call first
    print(n)  # print after recursion


n = int(input("Enter a number: "))
one_to_n(n)
