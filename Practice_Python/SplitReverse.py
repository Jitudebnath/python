"""Reverse word in a string """

s = input("Enter a sentence : ")
words = s.split()
words.reverse()
#using join just combine the reverse words 
result = " ".join(words)
print(result)