# 晚间作业，人开枪射击子弹，子弹数减为0做提示
class Bulletbox(object):
    def __init__(self, count):
        self.bulletCount = count


class Gun(object):  # 类名
    def __init__(self, bulletBox):
        self.bulletBox = bulletBox

    def shoot(self):
        if self.bulletBox.bulletCount == 0:  # 程序执行时，此处的bulletcount调用的是Bulletbox类中的bulletCount
            print("没有子弹了")
        else:
            self.bulletBox.bulletCount -= 1
            print("剩余子弹：%d" % self.bulletBox.bulletCount)

class Person(object):
    def __init__(self, gun):
        self.gun = gun

    def fire(self):
        self.gun.shoot()

    def fillBullet(self, count):
        self.gun.bulletBox.bulletCount = count

# 弹夹
bulletbox1 = Bulletbox(5)

# 枪
gun1 = Gun(bulletbox1)

# 人
per1 = Person(gun1)

per1.fire()
per1.fire()
per1.fire()
per1.fire()
per1.fire()
per1.fire()
per1.fillBullet(5)
per1.fire()
per1.fire()
per1.fire()
per1.fire()
per1.fire()
per1.fire()
per1.fire()

'''
把对象当参数传入的理解：
类实例化一个对象之后，可以把对象赋值给一个变量，
而且变量又可以当参数传给函数，
那么对象就可以当参数传给函数
参考例子1：
class Animal():
    self.age = 0  # 类属性

    def Eat(self):  # 类方法
        print("觅食")
dog = Animal()  # 类的实例化，即对象
cat = Animal()  # 类的实例化，即对象
dog.Eat()  # 相当于Animal.Eat(dog)
参考例子2：
#将一个类的对象,封装到,另一个类中的方法中去

class Teacher:
    def __init__(self,tea_name,tea_age):
        self.teacher_name = tea_name
        self.teacher_age = tea_age
        self.salary = 2000  #老师的初始工资为2k
class Cource:
    def __init__(self,cour_name,cost,teacher):
        self.course_name = cour_name
        self.course_teacher = teacher  #这一句话是一个类的对象传进另一个类中的关键  *****
        self.course_cost = cost        #cost为课时费 每上一节课总的工资都要增加的
    def class_up(self):
        #course_teacher = T1,因为在下面创建Course类的对象时:C1 = Cource('生理课',30,T1),参数传递进来的
        self.course_teacher.salary += self.course_cost 

T1 = Teacher('李杰',24)  #创建类Teacher的对象 T1
T2 = Teacher('张昭',25)
T3 = Teacher('子龙',22)

C1 = Cource('生理课',30,T1)  #T1以一个对象的形式作为类Cource的参数 此时T1就等于Course类中的teacher  *****
print(C1.course_name)  #生理课
print(C1.course_teacher.teacher_name) #C1.course_teacher = T1; C1.course_teacher.teacher_name = T1.teacher_name
print(C1.course_teacher.teacher_age)  #C1.course_teacher.teacher_age = T1.teacher_age

print(C1.course_teacher.salary)  #上课前的工资
C1.class_up()  #上课
print(C1.course_teacher.salary)  #上课后的工资
'''


print("999")