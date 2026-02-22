"""check wether the string is a palindrome or not"""


def check_palindrome(n):
    if n == n[::-1]:
        return True
    else:
        return False


n = input("Enter a string:")
print(check_palindrome(n))
