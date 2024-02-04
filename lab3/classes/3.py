class Shape:
    def __init__(self):
        pass
    def area(self):
        print(0)
class Rectangle(Shape):
    def __init__(self, length = "", width = ""):
        self.length = int(input(length))
        self.width = int(input(width))
    def area(self):
        print(self.length * self.width)

Rectangle().area()
Shape().area()

