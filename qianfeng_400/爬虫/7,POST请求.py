import  urllib.request
import urllib.parse


url1 = "http://sunck.wang/form"
# 构建POST数据
data = {"username":"sunck","passwd":"666"}
postData = urllib.parse.urlencode(data).encode("utf-8") # POST数据要求是字节类型，不能是字符串
# 构建请求体
req = urllib.request.Request(url1,postData)

# 请求
response1 = urllib.request.urlopen(req)

print(response1.read().decode("utf-8"))

