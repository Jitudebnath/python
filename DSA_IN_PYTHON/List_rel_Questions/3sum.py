# using python in find the 3 sum of a given list


def find3sum(arr):
    n = len(arr)
    my_set = set()
    for i in range(0, n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    temp = [arr[i], arr[j], arr[k]]
                    temp.sort()
                    my_set.add(tuple(temp))

    # Convert each tuple back to list
    return [list(ans) for ans in my_set]


# Input handling
arr = list(map(int, input("Enter numbers separated by space: ").split()))
print("Input array:", arr)

print("3-Sum triplets:", find3sum(arr))
