import datetime
x = datetime.datetime.now()
print(x)

print(x.year)
print(x.strftime("%A")) #prints week days

print(x.strftime("%B")) #prints full month

print(x.strftime("%d")) #prints the  day
print(x.strftime("%w")) #prints weekday as a number
print(x.strftime("%m")) #prints months as a number
#%f	Microsecond 000000-999999	548513
#%z	UTC offset	+0100