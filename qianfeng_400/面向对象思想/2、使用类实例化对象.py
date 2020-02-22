class Person(object): #类名
    name = ""         #类属性
    age = 0           #类属性
    height = 0        #类属性
    weight = 0        #类属性
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

#实例化对象
#格式：对象名 = 类名(参数列表)
#没有参数，小括号也不能省略
per1 = Person()
print(type(1))
per2 = Person()
print(per2)

#对象在堆区，变量在栈区