"""Ask a string from user . Display the dictonary
where each key is a character and value is frequency of
character that comes in that string ."""

my_string = input("Enter a string :")

freq = {}

for ch in my_string:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1


print(freq)
