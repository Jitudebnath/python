"""write a functions that accepts an integer and
prints the multiplications table"""


def multiplicaton_table(num):
    for i in range(1, 11):
        print(f"{num}*{i}={num*i}")


n = int(input("Enter a number:"))
print("Multiplicstion_table")
multiplicaton_table(n)
