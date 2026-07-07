# using python create a triangle

n = int(input("Enter a number: "))
for i in range(1, n + 1):  # start from 1 so the first row has 1 star
    for j in range(i):  # print i stars in each row
        print("*", end="")  # end="" prevents automatic newline
    print()  # move to the next line after each row
