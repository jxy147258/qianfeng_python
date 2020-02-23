r'''
概念：一种保存数据的格式
作用：可以保存本地的json文件，也可以即将json串进行传输，通常将json称为轻量级的传输方式
本质：是一个字符串
json文件组成：
{}   代表对象（字典）
[]   代表列表
：   代表键值对
，  分隔两个部分
'''


import json

jsonstr = '''{
"code": 0,
"msg": "",
"count": 2,
"data": [
{
"id": "154 工单",
"username": "Doe",
"city":"13585486456",
"sign": "center",
"classify": "aa",
"experience": "aa",
"score": "aa",
"wealth": "aa"
}, 
{
"id": "154",
"username": "oe",
"city": "13585456",
"sign": "ceter",
"classify": "a",
"experience": "a",
"score": "a",
"wealth": "a"
}
]
}'''

# 将json格式的字符串转为python数据类型的对象

jsonData = json.loads(jsonstr)
print(jsonData)
print(type(jsonData))
print(jsonData["data"]) # 已经转为了字典所以可以这么用


# 将python数据类型的对象转为json格式的字符串
dictStr = {
"code": 0,
"msg": "",
"count": 2,
"data": [
{
"id": "154 工单",
"username": "Doe",
"city":"13585486456",
"sign": "center",
"classify": "aa",
"experience": "aa",
"score": "aa",
"wealth": "aa"
},
{
"id": "154",
"username": "oe",
"city": "13585456",
"sign": "ceter",
"classify": "a",
"experience": "a",
"score": "a",
"wealth": "a"
}
]
}

jsonstr2 = json.dumps(dictStr)
print(jsonstr2)
print(type(jsonstr2))

# 读取本地json文件
jsonpath = r"/home/jixy2/pycharm_projects/qianfeng_python-master/qianfeng_400/爬虫/myjsontest.json"
with open(jsonpath,"rb") as f:
    data = json.load(f)
    print(data)
    print(type(data))

# 写入json文件
jsonstr3 = {
"code": 0,
"msg": "",
"count": 2,
"data": [
{
"id": "154 工单",
"username": "Doe",
"city":"13585486456",
"sign": "center",
"classify": "aa",
"experience": "aa",
"score": "aa",
"wealth": "aa"
}, 
{
"id": "154",
"username": "oe",
"city": "13585456",
"sign": "ceter",
"classify": "a",
"experience": "a",
"score": "a",
"wealth": "a"
}
]
}
jsonpath1 = r"/home/jixy2/pycharm_projects/qianfeng_python-master/qianfeng_400/爬虫/myjsontest1.json"
with open(jsonpath1,"w") as f:
    data1 = json.dump(jsonstr3,f)
    #1, 区别于dumps（）函数，dumps是只有一个参数，dump（）是两个参数
    #2,dump函数的传入的参数是字典