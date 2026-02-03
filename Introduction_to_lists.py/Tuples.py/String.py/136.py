"""COunt the number of space in a string"""

my_string = input("Enter a string :")

count = 0

for ch in my_string:
    if ch == " ":
        count += 1

print(count)
