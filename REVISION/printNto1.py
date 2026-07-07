"""print n to 1 numbers"""


def n_to_1(n):
    if n == 0:  # base case
        return
    print(n)  # print before recursion
    n_to_1(n - 1)  # recursive call


n = int(input("Enter a number: "))
n_to_1(n)
