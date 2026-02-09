"""Introduction to exception handling"""

try:
    lst = [4, 5, 6, 7, 8, 92, 3, 5]

    print(lst[2])
    print(lst[89])
    print(lst[4])
    print(lst[5])
    print(lst[6])
except:
    print("some error occurs")
