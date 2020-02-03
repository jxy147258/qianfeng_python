#时间之差

import datetime
d1 = datetime.datetime(2013, 8, 05,15,50)
d2 = datetime.datetime(2013, 8, 4,21,9,0,0)
print u'相差：%s天'%(d1-d2).days
#时区转换，当前系统所在时区+1
d = datetime.datetime.now()
d = d + datetime.timedelta(seconds=3600)
print d
print d.ctime()
