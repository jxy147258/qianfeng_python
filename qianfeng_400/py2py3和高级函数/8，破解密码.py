import itertools
import time

mylist1 = list(itertools.permutations([1,2,3,4],3))
print(mylist1)
print(len(mylist1))
# n中选m的可能，n!/(n-m)!


mylist12 = list(itertools.combinations([1,2,3,4,5],4))
print(mylist12)

newlist3 = list(itertools.product("0123456789",repeat=6)) # 循环6位，7位，8位，可以实现所有位数
print(len(newlist3))

myiter = ("".join(x) for x in itertools.product("0123456789",repeat=6))
while True:
    try:
        time.sleep(0.1)
        myStr = next(myiter)
        print(myStr)
    except StopIteration as e:
        break