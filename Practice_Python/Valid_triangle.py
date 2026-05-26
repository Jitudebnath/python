"""Check that triangle can form or not using sides"""


def is_triangle(a: int, b: int, c: int):
    if a + b > c and b + c > a and a + c > b:
        return "yes, you can form a valid triangle."
    else:
        return "No,you can't form a triangle."


a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

print(is_triangle(a, b, c))
