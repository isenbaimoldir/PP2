class mysquare:
    def __init__(self, n):
        self.n = n
        self.start = 1
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= self.n:
            x = self.start ** 2
            self.start += 1
            return x
        else:
            raise StopIteration
        
square = mysquare(4)
myiter = iter(square)

for x in myiter:
    print(x)