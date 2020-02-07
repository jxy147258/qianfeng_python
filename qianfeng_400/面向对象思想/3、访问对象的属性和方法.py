class Person(object): #类名
    name = ""         #类属性
    age = 0           #类属性
    height = 0        #类属性
    weight = 0        #类属性
    def run(self):
        print("run")
    def eat(self,food):
        print("eat:"+food)
    def openDoor(self):
        print("我已经打开了冰箱门")
    def fillEle(self):
        print("我已经把大象装进了冰箱")
    def closeDoor(self):
        print("我已经关闭了冰箱们")

per1 = Person()
#访问属性
#取值：对象名.属性名
#存值：对象名.属性名 = 新值
per1.age = 18 # 可以使用类中原有的值也就是0，也可以重新赋值，也就是18
per1.name = "zhangsan"
print(per1.age,per1.name)

#访问方法
#格式：对象名.方法名（参数列表）
per1.openDoor()
per1.eat("apple")