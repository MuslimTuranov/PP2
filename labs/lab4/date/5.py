import datetime

x = datetime.datetime.now() 

y = x + datetime.timedelta(days=100)

z = y.strftime('%A')

print(z)
