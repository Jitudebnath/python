"check number is a palindrome or not a palindrome"

num = int(input("Enter a number:"))
original = num
result = 0
while num > 0:
    last_digit = num % 10
    result = (result * 10) + last_digit
    num = num // 10

if result == original:
    print("Number is palindrome.")
else:
    print("Not a palindrome.")
