'''
GET:通过URL网站传递信息，可以直接在URL网址上添加要传递的信息
    把数据拼接到请求路径的后面传递给服务器，优点速度快，缺点是承载数据量小且不安全

POST:向服务器提交数据，是一种比较安全的数据传递方式
PUT:请求服务器存储一个资源，通常要制定存储的位置
DELETE：请求服务器删除一个资源
HEAD：请求获取对应的HTTP报头信息
OPTIONS：可以获取当前URL所支持的请求类型
'''


# GET方法示例
import  urllib.request

url1 = r"http://localhost:8080/"

respond1 = urllib.request.urlopen(url1)
data = respond1.read().decode("utf-8")
print(data)

