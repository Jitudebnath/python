# Number is perfect number or not a perfect number
def count_factors(n):
    result = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            result.append(i)
            if i != n // i:
                result.append(n // i)
    return sorted(result)


n = int(input("Enter a number : "))
print(f"Numbers of factors : ", count_factors(n))
