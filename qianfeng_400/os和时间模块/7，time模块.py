'''
时间表示形式
1，时间戳，从1970年1月1日0点0分0秒算起到当前为止的秒数
2，元组，9个值：年，月，日，时，分，秒，周，julian day，flag
3，格式化字符串。常用的是%y-%m-%d
        help(time)列出所有
        %Y  Year with century as a decimal number.
        %m  Month as a decimal number [01,12].
        %d  Day of the month as a decimal number [01,31].
        %H  Hour (24-hour clock) as a decimal number [00,23].
        %M  Minute as a decimal number [00,59].
        %S  Second as a decimal number [00,61].
        %z  Time zone offset from UTC.
        %a  Locale's abbreviated weekday name.
        %A  Locale's full weekday name.
        %b  Locale's abbreviated month name.
        %B  Locale's full month name.
        %c  Locale's appropriate date and time representation.
        %I  Hour (12-hour clock) as a decimal number [01,12].
        %p  Locale's equivalent of either AM or PM.
'''
import time


#时间戳，utc时间
t1 = time.time()
print("t1,UTC,timetrap:",t1)

#时间戳-->元组形式,UTC时间
t2 = time.gmtime()
print("t2,UTC,tumple:",t2)

#时间戳-->元组形式，local时间
t3 = time.localtime()
print("t3,Local,tumple:",t3)

#时间元组-->时间戳,t2、t3是将utc和local时间分别转成时间元组，那么相反方向也有两种
t4 = time.mktime(t3)
print("t4,From t3 local time,timetrap:",t4)
t5 = time.mktime(t2)
print("t5,From t2 UTC time,timetrap:",t5)

#时间戳-->字符串
t8 = time.ctime(t1)
print("t8,Local,string:",t8)

#时间元组-->字符串
t9 = time.strftime("%Y-%m-%d %H:%M:%S",t2)
print("UTC,string:",t9)

t6 = time.asctime(t2)
print("t6,From t2 UTC time,formated string:",t6)
t7 = time.asctime(t3)
print("t7,From t2 local time,formated string:",t7)
#字符串-->时间元组
t10 = time.strptime(t9,"%Y-%m-%d %H:%M:%S")
print("t10,utc,tumple",t10)


#程序等待一段时间
# for i in range(10):
#     time.sleep(2)
#     print(i)

#计时功能
y2 = time.clock()
sum = 0
for i in range(100):
    sum+=i
y1 = time.clock()
print(y1-y2)