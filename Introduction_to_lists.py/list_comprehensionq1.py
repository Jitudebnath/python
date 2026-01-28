"""
write a list_comprehension problem .
"""

Start = int(input("Enter start nummber="))
End = int(input("Enter end number="))

my_list = [i for i in range(Start, End + 1) if i % 2 == 0 and i % 3 == 0]


print(my_list)
