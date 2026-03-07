from array import *

arr = array("i", [])
n = int(input("Enter number of elements you want in your array :"))

for i in range(0, n):
    arr.append(int(input("Enter element value:")))

print("Your array is:\n")

for i in arr:
    print(i, end=" ")
