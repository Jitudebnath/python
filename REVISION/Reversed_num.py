#This work is all about reverse a number 
def reverse_number(num):
    reversed_num = 0   # Step 1: initialize
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10   # use num, not n
    return reversed_num   # return after loop finishes

# Example usage
num = int(input("Enter a number: "))
print("Original number:", num)
print("Reversed number:", reverse_number(num))
