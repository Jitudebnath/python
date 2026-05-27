# check user login data using python programming language


def login(n, p):
    correct_name = "jitu"
    correct_password = 1234
    if n == correct_name and p == correct_password:
        print("Login sucessful.")
    else:
        print("wrong Email or Password.")


n = input("Enter your Email:")
p = int(input("Enter your Password:"))
print(login(n, p))
