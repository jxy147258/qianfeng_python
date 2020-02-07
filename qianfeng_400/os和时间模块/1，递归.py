# 递归求和

def getSum(n):
    sum = 0
    for i in range(1, n+1):
        if i == 1:
            sum = 1
        else:
            sum +=getSum(n-1)
    return sum

print(getSum(5))
