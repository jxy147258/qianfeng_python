import re


'''
例子1，字符串切割 
'''
str1 = "sunck      is a  good    man"
print(re.split(r" +",str1)) # r" +" 表示一个或多个空格，区别于的是split只能用指定的切割符去切割，如果空格数不规则就不能切割
# 运行结果：['sunck', 'is', 'a', 'good', 'man']

r'''
re.finditer
和findall一样，区别是返回一个迭代器
'''
str2 = r"sunck is a good man ! sunck is nice man ! sunck is a handsome man!"
d = re.finditer(r"(sunck)",str2)
while True:
    try:
        i = next(d)
        print(i)
    except StopIteration as e:
        break

r'''
sub(pattern, repl, string, count=0, flags=0)
subn(pattern, repl, string, count=0, flags=0)
功能：被pattern规则匹配的字符串，被repl替换掉，替换次数为count
pattern:正则规则
repl:指定要替换的字符粗汉
count：最多替换次数

两者区别，前者返回被替换的字符串，后者返回一个元组，元组第一个元素是被替换后的字符串，第二个元素是被替换的次数
'''
str3 = "sunck is a good good good man !"
print(re.sub(r"(good)","nice",str3,count=2))
print(re.subn(r"(good)","nice",str3,count=2))

r'''
分组
概念：除了判断是否匹配之外，正则表达式还有提取字串的功能，用（）表示的就是分组

'''
str4 = "010-52512345"
m = re.match(r"(\d{3})-(\d{8})",str4)
# 给分组起名字(?P<first>\d{3})
m = re.match(r"(?P<first>\d{3})-(?P<last>\d{8})",str4)
# 在匹配规则r""整体不加（），group（0）是原始字符串，group（1）010，group(2)是52512345，
# 加上（），后输出的结果中，group（0）是原始字符串，group（1）是整体字符串，group（2）是010，group(3)是52512345，
# print(m)
print("0",m.group(0))
print("1",m.group(1))
print("1",m.group("first"))
print("2",m.group(2))
# print("3",m.group(3))
print("groups",m.groups())

r'''
编译：当我们使用正则表示式时，re模块会干两件事
1，编译正则表示式，如果语法有错，会报错
2，用编译后的正则表达式去匹配对象
compile(pattern, flags=0)
'''
pat = r"^1(([3578]\d)|(47))\d{8}$"
print(re.match(pat,"13600000000"))
re_telphone = re.compile(pat)
print(re_telphone.match("13600000000"))

'''
1,函数汇总:re.match(),re.search(),re.findall(),re.finditer(),re.split(),re.sub(),re.subn()
2,规则经过编译之后，原来的re.XXX()函数参数中少了pattern参数

'''
