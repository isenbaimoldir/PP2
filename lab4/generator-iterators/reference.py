class mynumbers:
    def __init__(self, start, stop):
        self.start = int(start)
        self.stop = int(stop)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start < self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration
        

myclass = mynumbers(0, 20)
myiter = iter(myclass)

for x in myiter:
    print(x)