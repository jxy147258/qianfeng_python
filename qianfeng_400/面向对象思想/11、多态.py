class Animal(object):
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(self.name+" 吃")


class Cat(Animal):
    def __init__(self,name):
        Animal.__init__(self,name)


class Dog(Animal):
    def __init__(self,name):
        Animal.__init__(self,name)

class Person(object):
    def feedAnimal(self,ani):
        ani.eat() # 人来喂，但是终归是动物来吃，所以是动物调用自己的eat()函数

cat1 = Cat("tom")
dog1 = Dog("jerry")
per1 = Person()
per1.feedAnimal(cat1)
per1.feedAnimal(dog1)