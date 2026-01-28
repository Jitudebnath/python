"""Create a list at least 10 numbers . Then create two separate
lists called 'odd' and 'Even'. put all the odd numbers from the original
list into 'odd'list and all even numbers to the 'Even' list."""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd = []
even = []

for i in my_list:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(f"The even list ={even}")
print(f"The odd list ={odd}")
