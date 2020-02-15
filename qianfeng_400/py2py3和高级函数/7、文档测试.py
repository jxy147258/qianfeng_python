# 提取注释中">>> "后面的代码进行执行和判断


import doctest


def mysum(x,y):
    '''
    这些中文都是没用的信息，本来应该是对函数的英语说明，奈何我英文不好，只能去他的。。
    以下才是有用的信息，注意：>>>后面必须有一个空格
    >>> print(mysum(1,2))
    3
    '''
    return x + y+1
print(mysum(1,2))
doctest.testmod()