class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}\n{self.age}"

p1 = Person("John", 12)
print(p1)