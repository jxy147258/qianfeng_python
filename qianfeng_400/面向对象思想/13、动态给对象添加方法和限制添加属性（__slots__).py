#MethodType(参数列表)，用于动态添加对象方法
#__slots__，用于限制动态添加对象属性的范围

from types import MethodType

class Person(object):
    # name = "per1" #类属性不能定义和__slots__中同名的属性，但是对象属性可以
    __slots__ = ("name","speak","age")
    def __init__(self,name):
        self.name = name



#动态添加对象方法
def say(self):
    print("my name is "+self.name)

per1 = Person("qwe")
per1.speak = MethodType(say, per1)
per1.speak()

#一个参考例子，也可以输出同样的内容
# per1.speak = say
# per1.speak(per1)

#限制添加对象属性的范围用__slots__ = (属性1，属性2)，age在范围里所以可以添加，height不在，所以报错
per1.age = 18
print(per1.age)

# per1.height = 190 # heigh不在__slots__定义的范围内，运行会报错
# print(per1.height)
