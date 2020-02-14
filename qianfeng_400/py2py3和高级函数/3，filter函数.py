# filter（func，list），把传入的函数依次作用于序列上的每一个元素，根据返回的是True还是False,决定是否保留该元素



# 例子1，奇数偶数分开

def isOdd(num):
    if num%2 == 0:
        return True
    return False

print(list(filter(isOdd,[1,2,3,4,5,6,7,8,9])))


# 例子2，从列表中只拿出有用的信息
data  = [["姓名","年龄","爱好"],["张三","25","无"],["李四","26","钱"]]
def func1(v):
    v = str(v)
    if v == "无":
        return False
    return True

for line in data:
    print(list(filter(func1,line)))


