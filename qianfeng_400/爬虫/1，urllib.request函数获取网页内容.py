'''
1,response.geturl()
2,response.getcode()
3,urllib.request.unquote("带编码的url")，返回的是解码之后的正常url
'''

import urllib.request

url1 = r"http://www.baidu.com"

response1 = urllib.request.urlopen(url1)
# 读取文件全部内容，并赋值给一个字符串变量
print("read():",response1.read())
# 读取一行
print("readline():",response1.readline())
# 读取文件全部内容，并赋值给一个列表变量
print("readlines():",response1.readlines())
# 内容描述信息
print("info():",response1.info())
# 当前爬取的url
print("geturl()",response1.geturl())
# 爬取结果的状态码  
print("getcode()",response1.getcode())