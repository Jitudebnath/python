def sum_of_digits(n):
    # Base case
    if n == 0:
        return 0
    # Recursive case
    return (n % 10) + sum_of_digits(n // 10)


# Take input from the user
n = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(n))
