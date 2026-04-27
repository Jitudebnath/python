# Using * for creatting another pattern
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    # print spaces before stars
    for j in range(n - i):
        print(" ", end="")
    # print stars with spaces between them
    for k in range(2 * i - 1):
        print("*", end="")
    print()
