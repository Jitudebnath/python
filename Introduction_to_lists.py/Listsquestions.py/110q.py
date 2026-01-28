"""Make your own list of your own.And remove all the duplicate element
from that list"""

my_list = [75, 45, "Jitu debnath", 12.1, "Debnath", 1, 1, 75, 45]

result = []

for i in my_list:
    if i not in result:
        result.append(i)


print(result)
