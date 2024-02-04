class Shape:
    def __init__(self, tarea=0):
        self.area = tarea

    def calculate_area(self):
        return self.area

class Square(Shape):
    def __init__(self, length):
        super().__init__(length)

    def calculate_area(self):
        return self.area ** 2

# Create an instance of the Square class with a side length of 5
square_instance = Square(5)

# Call the calculate_area method on both the Shape and Square instances
print("Area of Shape:", Shape().calculate_area())          # Output: 0
print("Area of Square:", square_instance.calculate_area())  # Output: 25
