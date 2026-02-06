"""Convert two lists into a dictionary . Make two listen
on your own of same length,and convert them to dictonary"""

lst1 = ["python", "good", "done", "bye"]
lst2 = [34, "wow", "Jitu", 99]

result = {}

for i in range(0, len(lst1)):
    result[lst1[i]] = lst2[i]

print(result)
