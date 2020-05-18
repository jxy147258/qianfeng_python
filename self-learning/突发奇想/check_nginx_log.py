#!/bin/bash python
import os
import time


def check_stop(curLogPath="/home/jixy2/pycharm_projects/qianfeng_python-master/self-learning/突发奇想/1，九九乘法口诀表.py"):
    """
    检查nginx切换后，应用程序是否还有流量接入
    60秒内没有日志，则认为没有流量，返回true
    """
    print("当前时间是：", time.asctime(time.localtime(time.time())))
    print("当前log文件路径是：", curLogPath)
    newLogPath = str(input("如果log文件路径不正确，请输入正确的文件路径："))
    oldLogSize = os.path.getsize(curLogPath)
    print("当前log文件大小是：",  oldLogSize)

    time.sleep(5)
    newLogSize = os.path.getsize(curLogPath)
    print("当前Nginx的log文件大小是：", newLogSize)

    if oldLogSize == newLogSize:
        return True
    else:
        return False


a = check_stop()
print(a)
