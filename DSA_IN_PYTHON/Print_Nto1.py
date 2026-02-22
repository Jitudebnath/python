"""PRint n to one using recursion"""


def print_numbers(n, current=1):
    if current > n:
        return
    print_numbers(n, current + 1)
    print(current)


n = int(input("Enter a number:"))
print_numbers(n)
