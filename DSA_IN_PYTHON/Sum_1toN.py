"""Sumation of all numbers using recursion"""


def sum_fun(n):
    if n == 1:
        return 1
    return n + sum_fun(n - 1)


n = int(input("Enter a number:"))
print(f"sum of {n} is {sum_fun(n)}")
