def solution(a, b, c):
    s = a + b + c
    return min(s // 2, s - max(a, b, c))


# Taking input from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Result:", solution(a, b, c))
