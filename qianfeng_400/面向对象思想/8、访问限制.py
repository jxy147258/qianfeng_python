'''
1，类中定义的属性以两个下划线开头为西游属性，外部不能访问
2，如果外部想访问，需要通过内部方法间接来操作和访问
3，也就是set函数和get函数来操作私有变量
4，如果变量名前后都有两个下划线，不是私有属性，
而是系统预先写好的，具有特殊意义
5，如果变量名前有一个下划线，类外可以直接访问，但是本意不想被访问
'''
class Person(object):
    def run(self):
        print("run")
    def eat(self,food):
        print("eat"+food)
    def openDoor(self):
        print("我已经打开了冰箱门")
    def fillEle(self):
        print("我已经把大象装进了冰箱")
    def closeDoor(self):
        print("我已经关闭了冰箱们")
    def __init__(self,name,age,height,weight,money):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.__money = money
    def getMoremoney(self,):
        self.__money += 99
        return self.__money
per1 = Person("zhangsan",20,170,55,10000)
print(per1.getMoremoney())

