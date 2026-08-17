"""Remove the duplicate values and return the sorted array properly in a particular manner"""

# Take input from user
arr = list(map(int, input("Enter elements: ").split()))

# Hash set to store elements already seen
seen = set()
result = []

# Remove duplicates
for x in arr:
    if x not in seen:
        seen.add(x)
        result.append(x)

# Sort the result
result.sort()

print("Answer:", *result)