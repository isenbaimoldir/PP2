class getString:
    def __init__(self, mystring = ""):
        self.thisstring = input(mystring)

    def printstring(self):
        print(self.thisstring.upper())

x = getString()
x.printstring()