# Write a Python program to create a class that represents a shape. Include  methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.
class shape:
    def area(self):
        pass
    def perimeter(self):
        pass
class circle(shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        print("area of circle is ", 3.14 * self.r * self.r)
    def perimeter(self):
        print("perimeter of a circle is ", 2 * 3.14 * self.r)
class square(shape):
    def __init__(self, s):
        self.s = s
    def area(self):
        print("area of square is ", self.s * self.s)
    def perimeter(self):
        print("perimeter of a square is ", 4 * self.s)
x = int(input("enter radius of a cicle - "))
z = int(input("enter side of a square  - "))
c = circle(x)
c.area()
c.perimeter()
s = square(z)
s.area()
s.perimeter() 
