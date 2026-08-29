"""ask a string from the user and count the uppercase
and lower case character in that string ."""

my_string = input("Enter a string :")

upper_count = 0
lower_count = 0

for ch in my_string:
    if ch.isupper():
        upper_count += 1
    elif ch.islower():
        lower_count += 1

print(f"There are {upper_count} upper case alphabet")

print(f"There are {lower_count} lower case alphabet")
