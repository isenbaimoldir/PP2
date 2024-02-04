class Point:
    def __init__(self, x1 = 2, y1 = 4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x1
        self.y2 = y1

    def show(self):
        print(self.x1, self.y1)
    
    def move(self, x2 = 5, y2 = 4):
        self.x1 = x2
        self.y1 = y2
    
    def dist(self):
        print(int(((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5))

some_value = Point()
some_value.show()
some_value.move()
some_value.dist()