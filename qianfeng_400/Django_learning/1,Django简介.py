'''
原型定义：
Model模型，管理数据，包括存取数据库
View视图，显示数据，
Control控制器，关联模型和视图,客户端请求发给controller，controlled去Model请求数据，Model把数据返回给Controller，
然后再交给View去展示，由view返回给客户端


Python中的定义：
Model，模型
Template，模板，相当于原型中View
View，视图，相当于Controller
url分发器




mysql相关：
更改root密码：
1,原始用户名密码存放目录：/etc/mysql/debian.cnf,
2,登陆之后更改root密码，update user set authentication_string=PASSWORD("147258Jxy") where user='root';
3,再执行update user set plugin="mysql_native_password";
4,刷新权限lush privileges;
5,重启服务，完成更改
增加远程访问：
update user set host='%' where user='root';
flush privileges;
'''

import pymysql
pymysql.connect("192.168.0.4", "root", "147258Jxy", "sunck")