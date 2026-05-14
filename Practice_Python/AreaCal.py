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


r = Rectangle(5, 4)
r.area()
r.perimeter()
