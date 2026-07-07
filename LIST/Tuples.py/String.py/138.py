"""Write a program to reverse the order of words"""

my_string = input("Enter a value of string: ")

word = my_string.split()

word = word[::-1]

result = " ".join(i for i in word)

print(result)
