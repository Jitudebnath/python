s = input("Enter a string: ")

# Hash list for lowercase English letters (a-z)
Hash_list = [0] * 26  # 26 slots for 26 letters

# Build frequency table
for ch in s:
    if "a" <= ch <= "z":  # ensure it's lowercase alphabet
        index = ord(ch) - ord("a")  # map 'a'->0, 'b'->1, ..., 'z'->25
        Hash_list[index] += 1

# Take queries from user
q = int(input("Enter number of queries: "))
for _ in range(q):
    ch = input("Enter character to query: ")
    if len(ch) == 1 and "a" <= ch <= "z":
        index = ord(ch) - ord("a")
        print(f"{ch}: {Hash_list[index]}")
    else:
        print(f"{ch}: 0")
