class Rectangle:
    def __init__(self, side1, side2):
        self.l = side1
        self.b = side2

    def area(self):
        print(self.l*self.b)

    def perimeter(self):
        print(2*(self.l+self.b))


class Square:

    def __init__(self, side):
        self.a = side

    def area(self):
        print(self.a**2)

    def perimeter(self):
        print(4*self.a)


square_obj = Square(int(input("Enter side of a square: ")))
square_obj.area()
square_obj.perimeter()
rectangle_obj = Rectangle(int(input("Enter length of a rectangle: ")),
                          int(input("Enter breath of a rectangle: ")))
rectangle_obj.area()
rectangle_obj.perimeter()
