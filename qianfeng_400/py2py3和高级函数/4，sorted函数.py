list1 = [1,-9,2,8,-3,7,4,6]
list2 = sorted(list1,key=abs) # key接受函数来实现自定义排序规则
print(list1)
print(list2)

# 降序排列
list3 = sorted(list1,reverse=True)
print(list3)

# 按字符串长度排序
list4 = ["a111111","b22","c3"]
print(sorted(list4))
print(sorted(list4,key=len))

# 自己定义函数
def myLen(templist):
    return len(templist)
list6 = sorted(list4,key=myLen)
print(list6)
