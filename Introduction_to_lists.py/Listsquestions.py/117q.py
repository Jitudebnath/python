"""
Write a python program for product of all elements in a list
"""

list = [10, 20, 3, 40, 5, 60, 20]

product = 1

for num in list:
    product = product * num


print(f"Product of all elements in the list is {product}")
