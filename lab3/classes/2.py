class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length = ""):
        self.length = int(input(length))
    def area(self):
        return self.length ** 2

area_of_square = Square()
print(area_of_square.area())

area_of_shape = Shape()
print(area_of_shape.area())