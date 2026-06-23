"""Find out the longest odd string in a given number"""

def largest_odd(num_str):
    n = len(num_str)
    for i in range(n - 1, -1, -1):   # scan from right to left
        if int(num_str[i]) % 2 == 1: # check if digit is odd
            return num_str[:i+1]     # return prefix up to that digit
    return "" 

# Example
nums = input("Enter the number: ")
print(largest_odd(nums))
