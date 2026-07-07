# use function for multiplication table of number


def multi_table(num):
    for i in range(1, 11):
        print(f"{num}*{i}={num*i}")


n = int(input("Enter a number:"))
print("-----Multiplication Table-----")
print(multi_table(n))
