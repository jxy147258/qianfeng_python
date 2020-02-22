'''
超过设置的超时时间后，就中断请求

'''


import urllib.request as ur
import random

url1 = r"http://www.baidu.com"
# 添加随机headers
headersList = ["Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36",
               "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Mobile Safari/537.36",
               "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"]
headerStr = random.choice(headersList)
req1 = ur.Request(url1)
req1.add_header("User-Agent",headerStr)
for i in range(1,100):
    try:
        respond1 = ur.urlopen(req1,timeout=1)
        print(len(respond1.read()))
    except:
        print("next url",i)
