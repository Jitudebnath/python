"""count odd and even in a list"""


def count_even_odd(nums):
    evencount = 0
    oddcount = 0
    for num in nums:
        if num % 2 == 0:
            evencount += 1
        else:
            oddcount += 1
    return evencount, oddcount


nums = list(map(int, input("Enter numbers separated by space: ").split()))
print("odd and even numbers are given below")
print(count_even_odd(nums))
