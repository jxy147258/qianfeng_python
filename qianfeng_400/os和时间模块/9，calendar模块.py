import calendar


print(calendar.month(2020,2))
#print(calendar.calendar(2020))

#判断闰年
print(calendar.isleap(2020))

#返回某个月的weekday的第一天，以及总天数
print(calendar.monthrange(2020,2))
print(calendar.monthrange(2020, 3))
print(calendar.monthrange(2020, 4))