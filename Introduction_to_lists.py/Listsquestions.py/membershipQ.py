"""Example related to membership operator in python
Ask a number from the user
Print yes if number exists in list else print no"""

a = [45, 55, 100, 5, "Jitu debnath", True, 55, 55.556, "code"]
num = int(input("Enter a number :"))
if num in a:
    print("Yes,This number is present in that list")
else:
    print("No,This number is not present in that list")
