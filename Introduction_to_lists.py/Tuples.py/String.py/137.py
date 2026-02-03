"""Ask a string from user.print the count of how many alphabets,digits,
spaces and symbols(everything else) are there in that string ."""

user_string = input("Enter a string: ")

# Initialize counters
alphabets = digits = spaces = symbols = 0

# Loop through each character in the string
for char in user_string:
    if char.isalpha():
        alphabets += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1
    else:
        symbols += 1

# Print the results
print("Alphabets:", alphabets)
print("Digits:", digits)
print("Spaces:", spaces)
print("Symbols:", symbols)
