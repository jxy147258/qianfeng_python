'''
1,把数据（属性，成员变量）和操作数据的方法（行为，成员方法）封装，就是对象，
2，把同类对象抽象出共性，就是类，
3，类中数据一般通过本类中方法类操作，
4，类通过接口和外界发生关系，对象之间通过消息通信
5，类的具体设计，三方面，类名，类属性，类行为（也叫方法/功能）
'''
#class 类名（父类列表），没有父类就写object，称为基类，超类
class Person(object): #类名
    name = ""         #类属性
    age = 0           #类属性
    height = 0        #类属性
    weight = 0        #类属性
    def run(self):
        print("run")
    def eat(self,food):
        print("eat"+food)