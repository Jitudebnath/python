"""print the numbers with in a range which having most numbers of factors"""


def count_factors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count


def numbers_with_max_factors(limit):
    max_factors = 0
    numbers = []
    for i in range(1, limit + 1):
        factors = count_factors(i)
        if factors > max_factors:
            max_factors = factors
            numbers = [i]
        elif factors == max_factors:
            numbers.append(i)
    return numbers, max_factors


limit = int(input("Enter a numbers:"))
nums, factors = numbers_with_max_factors(limit)
print(
    f"Numbers between 1 and {limit} with the most factors are {nums}, each with {factors} factors."
)
