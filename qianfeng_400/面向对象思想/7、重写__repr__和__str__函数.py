'''
__repr__()：是在cmd命令行中直接输入对象名，然后确定时调用
__str__():是在print(per1)时输出所有属性,适用于属性有很多，尤其是还要输出所有属性

'''

class Person(object): #类名
    # name = ""         #类属性
    # age = 0           #类属性
    # height = 0        #类属性
    # weight = 0        #类属性
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
    def __init__(self,name,age,height,weight):
        #关于self，类实例化一个对象时，self就是此对象，
        # 每一次创建不一样的对象self代表
        #不一样的对象，就是不一样的值
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        #以上赋值操作后，原来定义变量就不要了，注释掉
    def __str__(self):
        return "%s-%d-%d-%d"%(self.name,self.age,self.height,self.weight)

#__init__()就是构造函数，在使用类实例化对象时自动调用
#以下就是类实例化对象时可以传参数的依据，因为有参数列表
# 实例化对象
#格式：对象名 = 类名(参数列表)

per1 = Person("zhangsan",20,170,55)
print(per1)  #相当于调用print(per1.__str__())