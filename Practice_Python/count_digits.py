"""Count the number of digits in a number"""

from math import *


def count_digits(n):
    return int(log10(n) + 1)


n = int(input("Enter a number : "))
print(f"number of digits in {n} number is ", count_digits(n))
