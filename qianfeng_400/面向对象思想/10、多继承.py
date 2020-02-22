class Father(object):
    def __init__(self,money):
        self.money = money
    def play(self):
        print("play")
    def func(self):
        print("func1")

class Mother(object):
    def __init__(self,faceValue):
        self.faceValue = faceValue
    def play(self):
        print("play")
    def eat(self):
        print("eat")
    def func(self):
        print("func2")

class Child(Father,Mother):
    def __init__(self,money,faceValue):
        Father.__init__(self,money)
        Mother.__init__(self,faceValue)

child1 = Child(300,100)
print(child1.money,child1.faceValue)