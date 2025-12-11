n = int(input("Enter a positive number: "))

def math_sum(n):
    if n < 1:
        return 0
    return n * (n + 1) // 2

result = math_sum(n)
print(f"The final sum is: {result}")