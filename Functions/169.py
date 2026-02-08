"""Check whether number is prime or not"""


def prime_number(num):
    factors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factors += 1
    if factors == 2:
        print("It is a prime number")
    else:
        print("It is not a prime number")


prime_number(17)
