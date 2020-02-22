class person(object):
    def __init__(self,name,age,money):
        self.name = name
        self.age = age
        self.__money = money
    def run(self):
        print("run")
    def getMoney(self):
        print(self.__money)
class student(person):
    def __init__(self,name,age,money,stuID):
        super(student,self).__init__(name,age,money) # name和age是继承来的
        self.stuID = stuID  #子类独有的属性
class worker(person):
    def __init__(self,name,age):
        self.name = name
        self.age = age


stu1 = student("tom",18,12345,112209107142)
print(stu1.name,stu1.age,stu1.stuID)
print(stu1.getMoney())
stu1.run()
work1 = worker(18,"wangwu")
print(work1.name,work1.age)