"""Ask a string from user,remove all the duplicate
from that string and print that string again
(order doesn't matter)"""

my_string = "aaaeerrooplanne"

result = set(my_string)
print(result)

joined_string = " ".join(result)
print(joined_string)
