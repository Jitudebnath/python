"""Print 1 to n using recursion"""


def print_numbers(n, current=1):
    if current > n:
        return
    print(current)
    print_numbers(n, current + 1)


n = int(input("Enter a number:"))
print_numbers(n)
