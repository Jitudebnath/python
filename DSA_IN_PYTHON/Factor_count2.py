"""Read a number from the user and print all the factors
of that particular number and count the number of factors"""


def print_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)

    print(f"Factors of {num} are {factors} ")
    print(f"Total number of factors:", len(factors))


n = int(input("Enter a number:"))
print_factors(n)
