from datetime import datetime, timedelta

x = datetime.now()
y = x - timedelta(days = 1)
z = x + timedelta(days = 1)

print(x.strftime("%d"), y.strftime("%d"), z.strftime("%d"))