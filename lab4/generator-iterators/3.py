class dev:
    def __init__(self, n):
        self.n = n
        self.start = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start < self.n:
            if x % 3 == 0 and x % 4 == 0:
                x = self.start
                yield x
                x += 1
        else:
            raise StopIteration
    
mydv = dev(46)
myiter = iter(mydv)

for x in myiter:
    print(x)