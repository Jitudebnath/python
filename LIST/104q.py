"""Write a program that prmpts the user to specify the length of a list
and then requests numbers to populates that list.Display the final list as the output"""

list_length = int(input("Enter the length = "))
result = []

for i in range(0, list_length):
    num = int(input(f"Enter value at position {i} = "))
    result.append(num)

print(result)
