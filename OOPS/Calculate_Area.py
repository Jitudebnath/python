# Calculate the area of the Triangle and rectangle
class Shape:
    def find_area(self):
        print("Calculating Area...")


# Triangle class
class Triangle(Shape):
    def __init__(self):
        self.b = 0
        self.h = 0

    def read(self):
        print("-----Area of Triangle-----")
        self.b = float(input("Enter the base: "))
        self.h = float(input("Enter the height: "))

    def find_area(self):
        area = 0.5 * self.b * self.h
        print("Area of Triangle:", area)


# Rectangle class
class Rectangle(Shape):
    def __init__(self):
        self.length = 0
        self.breadth = 0

    def read(self):
        print("-----Area of Rectangle-----")
        self.length = float(input("Enter the length: "))
        self.breadth = float(input("Enter the breadth: "))

    def find_area(self):
        area = self.length * self.breadth
        print("Area of Rectangle:", area)


# Main program
if __name__ == "__main__":
    t = Triangle()
    t.read()
    t.find_area()

    r = Rectangle()
    r.read()
    r.find_area()
