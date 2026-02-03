"""Write a program in python that accepts a string and capitalize
the first letter of each word while converting all other letters to
lowercase"""

my_string = input("Enter a string :")

words = my_string.split()

result = " ".join(i.capitalize() for i in words)

print(result)
