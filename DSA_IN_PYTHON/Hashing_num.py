"""Hashing of numberes"""

n = [1, 2, 3, 4, 5, 10, 2, 3, 4, 5, 6, 7]
m = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Hash_list = [0] * 11
for num in n:
    Hash_list[num] += 1
for num in m:
    if num < 1 or num > 10:
        print(0)
    else:
        print(Hash_list[num])
