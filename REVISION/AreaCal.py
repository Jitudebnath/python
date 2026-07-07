"""Calculate the area using python abstract method"""

from abc import ABC, abstractmethod


class Rectangle:
    def __init__(self, length: int, breadth: int):
        self.length = length
        self.breadth = breadth

    def area(self):
        print(self.length * self.breadth)

    def perimeter(self):
        print(2 * (self.length + self.breadth))


l = float(input("Enter the length : "))
b = float(input("Enter the breadth : "))

r = Rectangle(l, b)
r.area()
r.perimeter()
