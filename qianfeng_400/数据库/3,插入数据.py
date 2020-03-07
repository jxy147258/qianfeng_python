import pymysql



# 链接数据库
conn = pymysql.connect("localhost","jixy2","123456","mysql")
#创建cursor对象
cursor = conn.cursor()


# sql语句
sql1 = '''INSERT INTO runoob_tbl VALUES ('$runoob_title','$runoob_author','$submission_date')'''

try:
    cursor.execute(sql1)
    conn.commit()
except:
    # 如果提交失败，回滚到上一次数据
    conn.rollback()

cursor.close()
conn.close()


