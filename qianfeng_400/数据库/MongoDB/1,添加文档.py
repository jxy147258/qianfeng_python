from pymongo import MongoClient


# 连接服务器
conn = MongoClient("mongodb://192.168.0.9:27017/")


# 连接数据库
db = conn.runoob

# 获取集合
collection = db.runoob

# 添加文档
collection.insert([{"name":"houliu"},{"name":"mamam"}])

# 断开
conn.close()
