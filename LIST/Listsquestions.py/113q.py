"""Write a program to  find the average of all numbers
presentin thatparticular list"""

n = int(input("How many numbers do you want enter:\n"))

numbers = []

for i in range(n):
    num = float(input(f"Enter number {i+1} :"))
    numbers.append(num)

average = sum(numbers) / len(numbers)

print("numbers in the list:", numbers)
print("Average of numbers:", average)
