import time, math

x, y = int(input()), int(input())

time.sleep(y / 1000)

print(f"square root of {x} after {y} mileseconds is " + str(math.sqrt(x)))