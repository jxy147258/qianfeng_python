from functools import  reduce
# map是把序列中每一个元素传给函数，做处理，然后返回一个新的序列
# 官方解释：将传入的序列中每一个元素依次作用于函数上，并把结果作为新的Iterator返回
# 格式map(func1,list1)
# 例子1，字符转数字
def func(chr):
    return {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}[chr]

resList1 = map(func,["1","2","3"])
# newList1 = map(int,["1","2","3"])
print(list(resList1))
# 例子2，数字转字符
resList2 = map(str,[1,2,3,4],)
print(list(resList2))


# reduce，函数接受序列中的前两个元素作为参数，进行处理，把处理结果和第三个元素作为两个参数传入再处理，作为新结果，依次类推
# 用法解释，reduce(func,[a,b,c,d])，相当于f(f(f(a,b),c),d)
# 例子1，求和，求阶乘
list1 = [1,2,3,4,5]
def mySum(x,y):
    return x + y

print(reduce(mySum,list1))
# 例子2，字符串转数字
def chr2int(str1):
    def fc(x,y):
        return x*10 +y
    def fs(chr):
        return {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}[chr]
    return reduce(fc,map(fs,list(str1)))
print(chr2int("19087"))

# 自己实现map函数
def myMap(func,originlist):
    resList = []
    for item in originlist:
        res = func(item)
        resList.append(res)
    return resList
list2 = ["1","2","3"]
print(myMap(func,list2))