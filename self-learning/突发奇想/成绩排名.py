# 输入成绩，成绩相同排名相同，后续的名词依次类推，比如90,90,90,89,89,89,76,那么排名是1,2,2,4
def Ranking(list1):

    for i in range(len(list1)):
        counter = 0
        if i == 0:
            print("第%d名成绩是：%d" % (i+1, list1[i]))
        if i >= 1:
            if list1[i-1] == list1[i]:
                counter += 1
            else:
                counter = 0
            if counter == 0:
                print("第%d名成绩是：%d" % (i+1, list1[i]))
            else:
                print("第%d名成绩是：%d" % (i+1-counter, list1[i]))


if __name__ == '__main__':
    originLi = [90, 90, 89, 89, 89, 89, 76, 76, 67]
    Ranking(originLi)
