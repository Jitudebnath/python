"""This program is related to Insertion sort"""


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr


# Taking input from the user
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

print("Original list:", numbers)
sorted_list = insertion_sort(numbers)
print("Sorted list:", sorted_list)
