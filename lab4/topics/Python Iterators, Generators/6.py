class vehicle:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")

class car(vehicle):
    pass

class boat(vehicle):
    def move(self):
        print("Sail!")

class plane(vehicle):
    def move(self):
        print("Fly!")

mycar = car("Ford", "Mustang")
myboat = boat("Ibiza", "Touring 20")
myplane = plane("Boeing", "747")

for x in (myboat, mycar, myplane):
    print(x.brand)
    print(x.model)
    x.move()