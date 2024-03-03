import math

def area(s, l):
    p = s*l
    a = l / ((2*math.tan(math.radians(180)/s)))
    return int((a*p)/2)

sides = int(input())
length = int(input())
print(area(sides, length))