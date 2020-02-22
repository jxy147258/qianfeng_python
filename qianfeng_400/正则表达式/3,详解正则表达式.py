import re


print("------匹配单个字符和数字-----")
r'''
. 匹配除换行符意外的任意单个字符
[0123456789] []是字符集合，匹配方括号中所包含的任意一个字符
[0-9] 匹配任意一个数字
[a-z] 匹配任意一个小写字母
[A-Z] 匹配任意一个大写字母
[0-9a-zA-Z_] 匹配任意一个数字和字母和下划线
[^sunck] 匹配除了sunck这几个字母以外的所有字符，^称为脱字符
[^0-9] 匹配除了数字的其他任何字符
\d =[0-9]  匹配任意一个数字
\D =[^0-9] 匹配任意一个非数字字符
\w 匹配任意一个数字、字符和下划线，效果同[0-9a-zA-Z_]
\W 匹配非数字、字符和下划线，效果同[0-9a-zA-Z_]
\s 匹配任意的空白符（空格，换行，回车，换页，制表）效果通[ \f\n\r\r\t]
\S 匹配任意非的空白符（空格，换行，回车，换页，制表）效果通[^ \f\n\r\r\t]

'''
print(re.match(".", "1sunck is a good man !"))
# 运行结果<re.Match object; span=(0, 1), match='1'>
# 解释结果：match是从最开头匹配字符串，"."是匹配任意一个，所以结合起来就是匹配字符串最开头的一个字符


print(re.search("[0123456789]","sun4ck is 21666" ))
# 运行结果<re.Match object; span=(9, 10), match='6'>
# 解释结果：search是从整个字符串查找，并返回第一个匹配成功，[]是匹配一个字符，所以结合起来就是匹配整个字符串中第一个数字，
# 并且数字在[]中
# 再举一个例子
print(re.search("[sunck]","sunck is sunck is 666")) # <re.Match object; span=(0, 1), match='s'>
print(re.search("[sunck]","unck is sunck is 666"))  # <re.Match object; span=(0, 1), match='u'>
print(re.search("[sunck]","nck is sunck is 666"))   # <re.Match object; span=(0, 1), match='n'>
print(re.search("[sunck]","ck is sunck is 666"))    # <re.Match object; span=(0, 1), match='c'>



print("----------")
print(re.findall("[^0-9]","sunk is 666"))
print(re.findall("[0-9]","sunk is 666"))

print("===========")
print(re.findall(".","sunk i\ns 666")) # 不输出\n
print(re.findall(".","sunk i\ns 666",flags=re.S)) # 输出中有\n


print("------锚字符（边界字符）-----")
r'''
^ 行首匹配，和在[]里的^不是一个意思，^abc,判断是不是以abc开头
$ 行尾匹配，abc$,是判断是不是以abc结尾
\A 匹配字符串开始，它和^的区别是\A 只匹配整个字符串的开头，即使在re.M模式下也不会其他行的行首
\Z 匹配字符串结束，它和$的区别是\Z 只匹配整个字符串的结束，即使在re.M模式下也不会其他行的行尾
\b 匹配单个单词以某个字符结尾，er\b,就是以er结尾的单词，所谓的单词结尾就是单词后面是空格，
'''
print(re.search("^sunck","sunck is a good man "))
print(re.search("sunck$","sunck is a good man sunck"))
print(re.findall("^sunck","sunck is a good man sunck\nsunck is a nice man",re.M)) # 多行模式下，每一行的行首都会找到
print("123",re.findall(r"\Asunck","sunck is a good man sunck\nsunck is a nice man",re.M)) # 即使在re.M模式下也不会其他行的行首
print("123",re.findall("\Asunck","sunck is a good man sunck\nsunck is a nice man",re.M)) # 即使在re.M模式下也不会其他行的行首
print(re.findall("man$","sunck is a good man\nsunck is a nice man",re.M)) # 多行模式下，每一行的行尾都会找到
print(re.findall("man\Z","sunck is a good man\nsunck is a nice man",re.M)) # 即使在re.M模式下也不会其他行的行首



print(re.search(r"an\b","man is ")) # 即使在re.M模式下也不会其他行的行首



print("------匹配多个字符-----")

r'''
(xyz) xyz以整体出现
x? 匹配0个或1个x
x* 匹配0个或任意多个x
x+ 匹配至少一个，就是一个或多个
x{n} 匹配n个x，n个x作为一个整体返回
x{n，}匹配至少n个x
x{n，m}匹配至少n个x,最多m
x|y 匹配x或者y
'''

print(re.search(r"x?","xxxx")) # 非贪婪匹配
print(re.search(r"x*","xxxx")) # 贪婪匹配
print(re.findall(r"x?","xabx"))
print(re.findall(r"x+","xabx"))
print(re.findall(r"a{3}","aaabaaaaaa"))
print(re.findall(r"a{3,}","aaabaaaavaa"))


# 找出所有以sunck。。。man形式的语句
str1 = "sunck is a good man sunck is nice man sunck is very good man"
print(re.findall(r"^sunck.*man$",str1))


print("------特殊字符-----")
r'''
*?  +? (xyz)? 最小匹配，因为通常是尽可能多的匹配，可以使用这种解决贪婪匹配
'''
print(re.findall(r"//*.*?/*/",r"/* part1 */ /* part2 */")) # 非贪婪，找到一个就返回
print(re.findall(r"//*.*/*/",r"/* part1 */ /* part2 */"))  # 贪婪，找到最长的一个才返回


# 思考题，从字符串中找出以下几种信息
# 1，QQ号，规律，4位到10位，全数字
# 2，邮箱，@前是数字字母特殊字符都有可能，@后面是163.com
# 3，phone patern是r"^1(([3578]\d|(47)))\d{8}
# 4，user 6到12位
# 5，密码
# 6，ip
# 7，url