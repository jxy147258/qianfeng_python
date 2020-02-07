import  datetime


#获取当前时间
d1 = datetime.datetime.now()
print(d1)

#返回指定时间
d2 = datetime.datetime(1999,10,2,10,10,10,123456)
print(d2)

#时间转换成字符串
d3 = d1.strftime("%Y-%m-%d %X")
print(d3)

d4 = datetime.datetime.strptime(d3,"%Y-%m-%d %X")
print(d4)

#计算时间间隔
d5 = datetime.datetime(1999,10,2,10,10,10,123456)
d6 = datetime.datetime.now()
d7 = d6-d5
print(d7)
print(d7.days)
print(d7.seconds) #总时间差中，除天数之外，剩下的时分秒加起来的换算成秒