import math

def area(h, f, s):
    return ((h+f)*h)/2

height = int(input())
first = int(input())
second = int(input())

print(area(height, first, second))