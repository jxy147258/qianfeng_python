'''
1,response.geturl()
2,response.getcode()
3,urllib.request.unquote("带编码的url")，返回的是解码之后的正常url
'''

import urllib.request as ur
import random

url1 = r"http://www.baidu.com"
'''
# 设置headers
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"
}
# 构造请求体
req = ur.Request(url1,headers=headers)

respond = ur.urlopen(req)
print(respond.read().decode("utf-8")) # 从网页上获取的是byte类型的，解码一下，变成字符串类型
'''

# 添加随机headers
headersList = ["Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36",
               "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Mobile Safari/537.36",
               "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"]
headerStr = random.choice(headersList)
req1 = ur.Request(url1)
req1.add_header("User-Agent",headerStr)
respond1 = ur.urlopen(req1)
# print(respond1.read().decode("utf-8"))
print(respond1.info())
