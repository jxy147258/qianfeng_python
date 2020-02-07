'''
1，self代表类的实例，而非类
2，哪个对象调用方法，该self就代表那个对象
3，self.__class__ 代表类名
'''

class Person(object): #类名
    # name = ""         #类属性
    # age = 0           #类属性
    # height = 0        #类属性
    # weight = 0        #类属性
    #self.__class__代表的就是类名
    def run(self):
        print("run")
        print(self.__class__)
        p = self.__class__("tt",20,20,20)      # self.class相当于Person，也能创建对象
        print(p)
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
        #注意：self不是关键字，写成其他任何标识符其实也可以
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        #以上赋值操作后，原来定义变量就不要了，注释掉
    def say(self):
        # 哪个对象调用此函数，self就代表此对象，然后再取<self.属性>时就取此对象对应的属性，
        print("i am %s,i am %d years old"%(self.name,self.age))
        '''
                    +-------------------+     +--------------------+
                    | 栈区，存变量      |     |  堆存区，   存对象 |
                    --------------------+     +--------------------
              per1  |   0x100           |     |                    |
                    --------------------+     +--------------------
                    |                   |     | per1对象的属性     |  0x100
                    --------------------+     +                    +
                    |                   |     | 和方法             |
                    --------------------+     +--------------------
              per2  |  0x200            |     | per2对象的属性     |  0x200
                    --------------------+     +                    +
                    |                   |     | 和方法             |
                    +-------------------+     +--------------------+
        '''

#__init__()就是构造函数，在使用类实例化对象时自动调用
#以下就是类实例化对象时可以传参数的依据，因为有参数列表
# 实例化对象
#格式：对象名 = 类名(参数列表)

per1 = Person("zhangsan",20,170,55)
per1.say()#输出i am zhangsan,i am 20 years old
per2 = Person("lisi",30,180,60)
per2.say()#输出i am lisi,i am 30 years old
per2.run()



