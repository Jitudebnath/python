"""Hashing using dict in oython programming language"""

m = list(map(int, input("Enter elements of list m separeted by space:").split()))

n = list(map(int, input("Enter elements of list n separeted by space:").split()))


hash_dict = {}

for num in m:
    hash_dict[num] = hash_dict.get(num, 0) + 1

for num in n:
    print(hash_dict.get(num, 0))
