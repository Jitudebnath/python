"""ask a string from user ,Count how many
alphabets are there in that string"""

my_string = input("Enter a string :")

count = 0
for ch in my_string:
    if ch.isalpha():
        count = count + 1

print(count)
