# Remove duplicate in an array


def remove_duplicate(nums):
    result = []
    for i in nums:
        if i not in result:
            result.append(i)

    return result


num = list(map(int, input("Enter the list of element:").split()))
print("Original list:", num)
print("without  duplicate:", remove_duplicate(num))
