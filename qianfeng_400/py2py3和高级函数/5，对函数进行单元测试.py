# 对函数，文档，模块进行测试
# 只涉及函数和文档测试，但是在函数测试时用了import命令，也就做了模块测试

import unittest
from myFuncAndModule import mySum
from myFuncAndModule import mySub

class UnitTest(unittest.TestCase):
    def setUp(self):
        print("测试开始。。")
    def tearDown(self):
        print("测试结束")
    def test_mySum(self):
        self.assertEqual(mySum(1,2),3,"加法有错")
    def test_mySub(self):
        self.assertEqual(mySub(1,2),-1,"减法有错")

if __name__ == "__main__":
    unittest.main()