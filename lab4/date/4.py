import datetime 

def difference(x, y):
    diff = y - x
    return diff.total_seconds()

x = datetime.datetime(2020, 1, 3)
y = datetime.datetime.now()

print(difference(x,y))