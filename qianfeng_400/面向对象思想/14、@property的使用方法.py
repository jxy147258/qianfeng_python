#一般情况下，对象属性，对外直接可以访问，
# 使用了限制访问__XX,就可以阻止直接访问private私有属性，
# 如果需要访问私有属性，可以定义set和get函数
#现在用#property解决访问私有属性的问题

class Person(object):
    def __init__(self,name,money):
        self.name = name
        self.__money = money

    #相当于get函数
    @property
    def money(self):
        return self.__money
    #相当于set函数
    @money.setter
    def money(self,money):
        if money < 0:
            money = 0
        self.__money = money

per1 = Person("张塞",10)
per1.money = -100
print(per1.name,per1.money)