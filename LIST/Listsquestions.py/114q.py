"""Write a python code to find the occurance of each element in a list
and print the element with the higest occurrance"""

my_list = [4, 5, 5, 5, 5, 5, 5, 8, 8, 8, 8, "jitu", "jitu", "code & debug"]
result = []

# Collect unique elements
for num in my_list:
    if num not in result:
        result.append(num)

highest_occ_element = 0
highest_occurence = 0

# Count occurrences
for num in result:
    c = my_list.count(num)
    print(f"{num} occurs {c} times")
    if c > highest_occurence:
        highest_occurence = c
        highest_occ_element = num

print(f"Highest occurrence element = {highest_occ_element}")
print(f"{highest_occurence} times it occurs")
