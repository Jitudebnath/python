# mutable/immutable Data type

a = [54, 23, 10, 99, -90]

print(a)
a.append(100)  # it will add the value at the end of the list
a.insert(3, "python")  # use index then use the value you want to insert
a[0] = 90  # This is updating the value in list
a.pop()  # by default it will delete the last value by index
a.remove(99)  # Remove by value
del a[1]  # Delete by index
a.clear()  # It will clear the list values but not the list
print(a)
