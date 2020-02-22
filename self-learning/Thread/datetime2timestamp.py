# make string to datetime,then to timestamp

import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
    dt_now = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    utc_num = re.split(r'[-+:]', tz_str)[1]
    if tz_str[3] == '+':
        dt_now = dt_now-timedelta(hours=int(utc_num))
    else:
        dt_now = dt_now+timedelta(hours=int(utc_num))
    return dt_now.timestamp()

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
#assert t1 == 1433121030.0, t1
print(t1)
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
#assert t2 == 1433121030.0, t2
print(t2)
#print('ok')
