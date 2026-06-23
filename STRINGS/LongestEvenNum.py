"""Return the longest even number"""

def longest_even(nums_str):
    n = len(nums_str)
    for i in range(n - 1, -1, -1):   
        if int(nums_str[i]) % 2 == 0:  
            return nums_str[:i+1]      # return prefix up to that digit
    return " "  

nums = input("Enter a number: ")
print(longest_even(nums))
