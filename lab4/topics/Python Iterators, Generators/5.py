class boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")

class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Drive!")

class plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Fly!")


mycar = car("Ford", "Mustang")
myboat = boat("Ibiza", "Touring 20")
myplane = plane("Boeing", "747")

for x in (myboat, mycar, myplane):
    x.move()