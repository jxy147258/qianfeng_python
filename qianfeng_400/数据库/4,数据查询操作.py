'''
fetchone(),获取下一个查询结果集，结果集是一个对象
fetchall(),获取全部的返回行
rowcount()，是一个只读属性，返回execute（）方法影响的行数


'''
import pymysql


# 链接数据库
conn = pymysql.connect("localhost", "jixy2", "123456", "mysql")
# 创建cursor对象
cursor = conn.cursor()


# sql语句
sql1 = "select now()"


# 用cursor对象执行sql语句
cursor.execute(sql1)

data = cursor.fetchone()
print(data)

cursor.close()
conn.close()



