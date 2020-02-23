'''
1,response.geturl()
2,response.getcode()
3,urllib.request.unquote("带编码的url")，返回的是解码之后的正常url
'''

import urllib.request as ur

url1 = r"http://www.baidu.com"
path1 = r"F:\python_G\python_shell\qianfeng_400\爬虫\aa11.html"
ur.urlretrieve(url1,path1)
ur.urlcleanup()
