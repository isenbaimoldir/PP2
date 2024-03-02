class myevenn:
    def __init__(self, n):
        self.n = n
        self.start = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= self.n:
            x = self.start
            self.start += 2
            return x
        else:
            raise StopIteration

even = myevenn(int(input()))
myiter = iter(even)

for x in myiter:
    print(x, end = ' ')