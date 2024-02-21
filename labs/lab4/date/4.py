import datetime

date_format = '%Y-%m-%d %H:%M:%S'
date1_str = input()
date2_str = input()

date1 = datetime.datetime.strptime(date1_str, date_format)
date2 = datetime.datetime.strptime(date2_str, date_format)

x = date2 - date1

y = x.total_seconds()

print(y)
