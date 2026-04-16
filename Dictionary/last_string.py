# write a program to retrun the length of last word in a string
def length_Of_LastWord(s: str) -> int:
    # Step 1: Remove leading and trailing spaces
    s = s.strip()

    # Step 2: Split the string into words
    words = s.split()

    # Step 3: Return the length of the last word
    return len(words[-1])


# Taking input from the user
s = input("Enter a string: ")
print("Length of the last word:", length_Of_LastWord(s))
