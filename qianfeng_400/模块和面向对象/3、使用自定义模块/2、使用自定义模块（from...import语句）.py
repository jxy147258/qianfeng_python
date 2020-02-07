#只需要引入模块中的一部分，而不是全部用from。。。。import。import可以引入函数，也可以是类

from testing_import_module import myfunc1

myfunc1() # 此处是直接调用函数，区别于tim.myfunc1()
myfunc10() #myfunc10()函数没有引入，所以执行失败
