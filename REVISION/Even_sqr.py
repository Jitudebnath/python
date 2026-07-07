"""print the squares of all even numbers"""

n = int(input("Enter a number: "))

square_even = [x**2 for x in range(n + 1) if x % 2 == 0]

print(square_even)
