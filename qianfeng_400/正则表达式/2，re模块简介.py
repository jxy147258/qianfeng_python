import re

r'''
re.match函数
原型：re.match(pattern,string,flags =0)
1、pattern:正则表达式
2、string:被检索的字符串
3、flags:标志位，用于控制正则表达式的匹配方式，可取的值及意义:
    re.S 是.匹配包括换行符在内的所有字符
    re.M 多行匹配，影响^和￥
    re.I 忽略大小写
    re.L 做本地户识别
    re.U 根据Unicode字符集解析字符，影响\w,\W,\b,\B
    re.X 以更灵活的格式理解正则表达式
4、功能:在字符串的起始位置匹配一个模式，如果不是起始位置，即使匹配成功的话，也返回None
5、特性:re.match("www","www.baidu.com").span())  返回匹配的下标

'''
print(re.match("www","www.baidu.com")) # 匹配成功
print(re.match("www","www.baidu.com").span()) # 返回匹配的下标
print(re.match("www","ww.baidu.com")) # 匹配不成功
print(re.match("www","baidu.www.com")) # 匹配成功的位置不是起始位置，所以算匹配失败
print(re.match("www","wwW.baidu.com")) # 大小写不匹配
print(re.match("www","wwW.baidu.com",flags=re.I)) # 忽略大小写后就能匹配成功
print("---------")

'''
re.search函数
原型：re.match(pattern,string,flags =0)
和re.match一样，区别：
从起始位置，以及其他任何位置只要能匹配到，就返回第一个匹配成功的下标
'''
print(re.search("sunck", "sunk is a goo man,good man is the sunck"))
print("+++++++++++")
'''
re.findall()函数
和re.match一样，区别：
返回所有匹配的结果，比如找"sunck"就把所有的sunck返回

'''
print(re.findall("sunck","sunckSunck", flags=re.I))