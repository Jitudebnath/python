"""Use recursion and find the dibonacci series numbers"""


def fibonacci_number(num):
    if num == 0 or num == 1:
        return num
    return fibonacci_number(num - 1) + fibonacci_number(num - 2)


n = int(input("Enter a number :"))
print(f" {n} no fibonacci number is {fibonacci_number(n)}")
