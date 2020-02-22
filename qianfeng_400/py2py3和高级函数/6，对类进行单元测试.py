import unittest
from myClass import Person

class Test(unittest.TestCase):
    def test_init(self):
        super().__init__()
        p = Person("tom",20)
        self.assertEqual(p.name,"tom","name赋值错误")
        self.assertEqual(p.age,20,"age赋值错误")

    def test_getAge(self):
        p = Person("jerry",22)
        self.assertEqual(p.getAge(),22,"getAge方法有错误")

if __name__ == "__main__":
    unittest.main()