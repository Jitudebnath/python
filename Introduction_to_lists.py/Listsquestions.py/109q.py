"""Start by creating two separate lists with random numbers.Then
create a third list that merges the numbers from the first and second lists
together"""

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = []

for i in list1:
    result.append(i)

for j in list2:
    result.append(j)

print(result)
