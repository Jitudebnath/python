# Merge sort using python
def merge_arr(left, right):
    result = []
    i, j = 0, 0
    n = len(left)
    m = len(right)

    # Compare elements from both arrays
    while i < n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    while i < n:
        result.append(left[i])
        i += 1

    while j < m:
        result.append(right[j])
        j += 1

    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge_arr(left, right)


# Input
arr = list(map(int, input("Enter the values: ").split()))

# Correct function call
print("Sorted list:", merge_sort(arr))
