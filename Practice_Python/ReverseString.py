"""Reverse a string using recursion method"""


def reverse_string(s):
    if len(s) <= 1:
        return s
    else:
        return reverse_string(s[1:]) + s[0]


s = input("Enter a string:")
print(reverse_string(s))
