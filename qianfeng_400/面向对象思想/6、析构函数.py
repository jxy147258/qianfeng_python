#析构函数 __del__()，释放对象时自动调用

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

    def __del__(self):
        print(self.name,"这里是析构函数") #加上self.name就可以看出来是释放了哪个对象

per1 = Person("zhangsan",200,170,55)
#第一种释放对象的场景，假如以上语句是程序的最后一句，程序执行完这一句后对象会被自动销毁，也就自动调用析构函数

def myfunc1():
    per2 = Person("lisi",20,20,20)
    print(per1.age)

myfunc1()


#第二种释放对象的场景，是加上这一句，手工销毁对象
del per1 # 第一种场景是程序执行完毕自动释放对象并调用析构函数，
# 不管程序整体执行结束与否，这种场景是轮到这一句都会销毁对象
#而且，销毁后不能再访问
#print(per1.age) # 所以此句会报错

#第三种场景是，函数中定义的对象，函数执行完毕就释放对象并调用析构函数
