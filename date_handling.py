from datetime import datetime, date, time

current_date = datetime.now()
print(current_date)
print(current_date.year)
print(current_date.month)
print(current_date.day)
print(current_date.hour)
print(current_date.minute)
print(current_date.second)
print(current_date.microsecond)

print(datetime(2020, 1, 1))

print(datetime(2020, 1, 1).strftime("%Y. %B %d %H:%M:%S"))

print((datetime(2021, 1, 1) - datetime(2020, 1, 1)).days)

d = date(2020, 1, 1)
print(d)
t = time(12, 30, 45)
print(t)
print(datetime.combine(d, t))
