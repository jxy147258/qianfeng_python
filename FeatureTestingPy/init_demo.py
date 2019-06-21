# -*- coding: utf-8 -*-
"""
test init function 
"""

class Cat:
    """定义了一个Cat类"""

    #初始化对象
    def __init__(self, new_name, new_age):
        self.name = new_name
        self.age = new_age

    #方法
    def eat(self):
        print("猫在吃鱼....")

    def drink(self):
        print("猫正在喝kele.....")

    def introduce(self):
        print("的年龄是:%d")

#创建一个对象

#tom = Cat("n1",12)
#tom.eat()
#tom.drink()
#tom.name = "汤姆2"
#tom.age = 400
#tom.introduce()
#
#lanmao = Cat()
#lanmao.name = "蓝猫1"
#lanmao.age = 101
#lanmao.introduce()