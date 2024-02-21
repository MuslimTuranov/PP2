import datetime

x = datetime.datetime.now()

print("Yesterday was", x.day - 1, x.month, x.year)
print("Today is", x.day, x.month, x.year)
print("Tomorrow will be", x.day + 1, x.month, x.year)