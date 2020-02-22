'''由类名来调用的属性是类属性，__init__()中定义的是对象属性'''


class Person(object):
    name = "person"  # name是类属性，调用方法是Person.name
    def __init__(self, name):
        self.name = name  # self.name是对象属性，调用方法是对象名.name


#类属性和对象属性同名时，对象优先使用对象属性，没有对象属性时，使用类属性
#注意：类属性不要和对象属性同名，比如del了对象属性之后，仍然可以调用此同名属性，因为在类属性中还有
per1 = Person("tom")
print("per1 的name是 ",per1.name)
print("类属性，name的值是 ",Person.name)

