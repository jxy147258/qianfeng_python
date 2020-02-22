#运算符重载就是+——*/等等运算符重新定义

class Person(object):
    def __init__(self,num):
        self.num = num
    def __add__(self, other):
        return Person(self.num+other.num)
    def  __str__(self):
        return "num = "+ str(self.num)

per1 = Person(1)
per2 = Person(2)
print(per1+per2)  #per1+per2 相当于per1.__add__(per2)
# 以上语句执行过程：生成per1时，per1.num是1，同理per2.num是2，
# 在__add__（）函数中形参self就是per1，other是per2，结合上一步的num，所以self.num+other.num=3
# 然后这个3作为参数传入到Person类中，这样就生成了一个新的对象，
# 这个新对象再调用__str__()就得到了3，但是为啥会自动执行__str__()???
print(per1.__add__(per2))
print(per1)
print(per2)