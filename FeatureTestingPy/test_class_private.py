class Student(object):
    def __init__(self,name,age):
        self._name = name
        self._age = age
    def get_attribute(self):
        print("name:%s,age:%d"%(self._name,self._age))

s = Student('a',12)

s.get_attribute()
