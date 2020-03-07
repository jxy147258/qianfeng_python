import pymysql



# 链接数据库
conn = pymysql.connect("localhost","jixy2","123456","mysql")
#创建cursor对象
cursor = conn.cursor()


# sql语句
sql1 = '''CREATE TABLE IF NOT EXISTS `runoob_tbl`(
   `runoob_id` INT UNSIGNED AUTO_INCREMENT,
   `runoob_title` VARCHAR(100) NOT NULL,
   `runoob_author` VARCHAR(40) NOT NULL,
   `submission_date` DATE,
   PRIMARY KEY ( `runoob_id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8'''


# 用cursor对象执行sql语句
cursor.execute(sql1)

data = cursor.fetchone()
print(data)

cursor.close()
conn.close()


